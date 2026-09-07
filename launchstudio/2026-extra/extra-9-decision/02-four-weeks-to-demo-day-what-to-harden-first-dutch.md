---
Titel: "Vier Weken tot Demo Day: Wat Eerst Hardenen en Wat Uitstellen"
Trefwoorden: voorbereiding demo day, hardening sprint van vier weken, productiegereedheid sprint, accelerator demo day, MVP triage vóór lancering, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: SaaS-Oprichter Scale-Up
---

# Vier Weken tot Demo Day: Wat Eerst Hardenen en Wat Uitstellen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Vier Weken tot Demo Day: Wat Eerst Hardenen en Wat Uitstellen",
  "description": "Een week-tot-week triageplan voor scale-up oprichters met een vaste demodag en een prototype dat nog niet productierijp is. Behandelt wat absoluut gedicht moet worden voordat vreemden het product aanraken, en welke zeven categorieën veilig kunnen wachten tot na de pitch.",
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
  "datePublished": "2027-01-07",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/four-weeks-to-demo-day-what-to-harden-first"
  }
}
</script>

Achtentwintig dagen. Niet "ongeveer een maand" — achtentwintig dagen, waarvan er pakweg negentien werkdagen zijn, en waarvan er misschien veertien overeind blijven na investeerdersgesprekken, pitchdeck-revisies en de drie verplichte afspraken die uw programmacoördinator alvast heeft ingepland. Dat is het daadwerkelijke budget waarmee u moet triageren, en de eerste fout die de meeste oprichters maken, is plannen op basis van de kalendermaand in plaats van die veertien dagen.

De tweede fout is fundamenteler: Demo Day behandelen als een deadline voor *features*. Dat is het niet. Demo Day is het allereerste moment waarop uw product gelijktijdig wordt gebruikt door mensen die het niet zelf hebben gebouwd, die niet voorzichtig zijn, en die in een aantal gevallen actief nieuwsgierig zijn naar wat er gebeurt als ze op plekken klikken waar ze niet horen te zijn. Het is een deadline voor hardening verpakt in het jasje van een productdeadline, en de triage ziet er totaal anders uit zodra u het zo bekijkt.

## Wat Demo Day Daadwerkelijk Test

Uw eigen demonstratie op het podium is ingestudeerd en veilig. Het echte risico schuilt in de negentig seconden nadat de QR-code op het scherm verschijnt en het uur volgend op de pitch. Dat is het moment waarop tussen de veertig en driehonderd mensen gelijktijdig uw product openen via een overbelast wifi-netwerk, zich aanmelden met wegwerpadressen en functies testen in een volgorde die u zelf nog nooit heeft geprobeerd.

Drie zaken bezwijken in dat tijdsbestek met een voorspelbare regelmaat. Ten eerste, **concurrency**: een prototype dat nooit meer dan vier gelijktijdige sessies heeft gekend, krijgt er ineens tweehonderd te verwerken. De connection pool van een starter-tier Postgres-database — vaak begrensd tussen de 15 en 60 directe verbindingen — raakt verzadigd, waardoor het product niet simpelweg vertraagt, maar hard crasht met serverfouten. Ten tweede, **de aanmeldstroom**: elke flow die uw gebruikers normaal gesproken pas *na* de registratie bereiken, wordt nu direct doorlopen door iemand die zojuist een nieuw account heeft aangemaakt, in een datastatus die uw handmatig aangemaakte testaccounts nooit hebben gehad. Ten derde, **de isolatiegrens**: wanneer honderden accounts binnen tien minuten worden aangemaakt, is de kans dat twee gebruikers elkaars gegevens zien niet langer theoretisch, maar statistisch onvermijdelijk.

Let op wat er níét op dit lijstje staat. Niemand op Demo Day maalt erom dat uw onboarding drie stappen telt in plaats van twee, of dat een leeg dashboard er visueel wat kaal uitziet. Het verschil tussen een demo die investeerders overtuigt en een demo die verandert in een pijnlijk incident dat u aan uw lead investor moet uitleggen, is vrijwel volledig infrastructureel van aard.

## De Triageregel: Repareer Wat Een Vreemde Kan Bereiken

Hier is het filter dat de komende vier weken behapbaar maakt. **Rangschik elk openstaand actiepunt op basis van de vraag of een onbekende, die normaal of licht afwijkend gedrag vertoont, het binnen tien minuten na de eerste aanmelding kan bereiken.**

Alles wat binnen die zone valt, is werk voor week één. Alles daarbuiten — de beheerdersinterface die alleen uzelf gebruikt, het rapportagescherm achter een betaald abonnement dat niemand op Demo Day bezit, de tweede API-integratie — is uitstelbaar, ongeacht hoe luid het in uw hoofd roept om aandacht.

Deze regel druist vaak in tegen het gevoel van een oprichter, omdat de punten die het hardst knagen meestal de zichtbare, half afgewerkte visuele elementen zijn. De kwesties die een Demo Day echter fataal verstoren, zijn onzichtbaar en voelen voor de oprichter al als "klaar". Pas de regel mechanisch toe en het herordent uw prioriteitenlijst binnen een uur.

## Week 1 — De Audit en Twee Onontkoombare Besluiten

Besteed de eerste drie dagen uitsluitend aan het inventariseren van wat u daadwerkelijk in handen heeft, zonder direct code aan te passen. Een grondige review op codeniveau van een AI-gegenereerde codebase — of deze nu uit Lovable, Bolt, Cursor of een mix daarvan stamt — brengt steevast dezelfde categorieën naar boven: autorisatie die enkel via frontend-routing wordt afgedwongen maar ontbreekt op de API, databasepolicies die ontbreken of geconfigureerd zijn als een overkoepelende `true`-conditie, beheer-sleutels die naar de browser lekken, betalingswebhooks die zonder handtekeningverificatie worden verwerkt, het ontbreken van rate limiting, en een databaseschema zonder tenant-kolom op tabellen die daar straks afhankelijk van zijn.

De werkelijke meerwaarde van deze audit is niet de lijst met bevindingen. Het zijn de twee principiële keuzes die direct moeten worden gemaakt.

**Besluit één: is er sprake van een fundamentele architectuurfout?** Als de review aantoont dat uw datamodel geen enkel concept kent van welke organisatie eigenaar is van een rij, dan voert u geen hardening-sprint van vier weken uit; dan staat u voor een volledige schemamigratie, en die past simpelweg niet naast alle andere taken. Het enige verstandige antwoord is dan om Demo Day te beperken tot een gecontroleerde single-tenant demo-omgeving en de migratie in te plannen voor ná het evenement. Proberen een databaseschema te migreren in week drie van een vierweekse sprint is het klassieke recept om op Demo Day te staan met een half gemigreerde database zonder werkend rollback-plan.

**Besluit twee: waarop gaat u demonstreren?** Op de live productieomgeving met echte registraties, of in een afgeschermde staging-omgeving met vooraf klaargezette testaccounts? Beide keuzes zijn volkomen legitiem. Wat echter fataal is, is op de dag zelf ontdekken dat u het ene bedoelde, maar het andere heeft voorbereid. Hak deze knoop door in week één, want dit bepaalt of weken twee tot en met vier draaien om het beveiligen van een openbaar platform of om het robuust maken van een gecontroleerde omgeving.

## Week 2 — De Scheiding Tussen Gebruikers

Als u in vier weken slechts één ding grondig kunt aanpakken, kies dan voor dit onderdeel. Week twee staat volledig in het teken van toegangscontrole, en dit omvat drie lagen die door oprichters dikwijls op één hoop worden gegooid.

**Authenticatie** — bewijzen wie iemand is — is doorgaans de laag die AI-tools redelijk goed implementeren, omdat diensten zoals Supabase Auth, Auth0, Clerk of NextAuth het zware werk doen. Controleer desondanks de fundamenten: verlopen sessies correct, worden tokens niet opgeslagen op plekken waar kwaadwillende scripts ze kunnen uitlezen, en lekt de wachtwoord-herstelfunctie niet of een e-mailadres al in de database voorkomt?

**Autorisatie** — bepalen wat een specifieke gebruiker mag doen — is het punt waar prototypes structureel falen. De test bestaat niet uit het doorklikken in de frontend. De echte test is het uitvoeren van een geauthenticeerde API-aanroep voor een object dat van uzelf is, het ID daarin wijzigen naar een object dat toebehoort aan een ander account, en de aanroep opnieuw versturen. Als het antwoord data oplevert, heeft u een ernstig datalek te pakken. Doe dit voor elk type entiteit: dossiers, uploads, exports, facturen en webhooks.

**Isolatie** — de scheiding structureel verankeren in plaats van via losse voorwaarden in applicatiecode — is de enige duurzame oplossing. Row-Level Security (RLS) policies in PostgreSQL, afgestemd op de geauthenticeerde gebruiker of diens organisatie, dwingen de regels af op databaseniveau in plaats van in backend-code die u bij een volgende update per ongeluk kunt vergeten. Het kost meer tijd in week twee, maar bespaart u ontelbare risico's in elke week daarna.

Reserveer de volledige week hiervoor. Toegangscontrole die op een vrije namiddag even snel wordt "geregeld", is toegangscontrole die alleen werkt voor de routes waar u op dat moment toevallig aan dacht.

## Week 3 — Betalingen, E-mail en Foutafhandeling

Week drie is gereserveerd voor de paden die alleen worden geactiveerd wanneer er iets heel goed of juist heel slecht gaat — en die daardoor het minst getest worden.

Als u live betalingen accepteert tijdens Demo Day, of direct in de dagen erna, moet de integratie aan vier harde eisen voldoen: cryptografische verificatie van webhook-handtekeningen tegen uw geheim, zodat niemand een valse `checkout.session.completed` kan versturen om zichzelf gratis toegang te verschaffen; idempotentietesten, zodat wanneer Stripe of Mollie een webhook opnieuw verzendt (wat gegarandeerd gebeurt) er geen dubbel abonnement wordt geactiveerd; een abonnementsstatus die expliciet in uw eigen database leeft in plaats van afgeleid te worden van het laatste binnengekomen event; en een heldere afhandeling van mislukte incasso's die voorkomt dat een gebruiker stilletjes voor altijd gratis toegang behoudt.

Transactionele e-mail is het andere cruciale onderdeel van week drie, en het is de stille sluipmoordenaar van conversie op demodagen. Verzenden vanaf een domein zonder correcte SPF-, DKIM- en DMARC-records zorgt ervoor dat verificatiemails bij een aanzienlijk deel van de ontvangers direct in de spambox belanden. Op een Demo Day is een verificatiemail die twintig minuten te laat arriveert een e-mail die aankomt nadat de geïnteresseerde het tabblad al lang heeft gesloten. Configureer de DNS-records, verstuur via een gespecialiseerde provider (zoals Postmark, Resend of SendGrid) en test de aflevering expliciet naar Gmail, Outlook en minimaal één zakelijk bedrijfsdomein, aangezien die filters elk volstrekt anders reageren.

Besteed vervolgens een halve dag aan **foutafhandeling**. Wat ziet de bezoeker wanneer een externe API-koppeling time-out vertoont? Laat een mislukte bestandsupload een zwevende record achter in de database? En toont uw foutpagina een volledige stacktrace waarin het adres van uw databasehost zichtbaar is? Niets hiervan oogt glamoureus, maar het is exact wat een vreemde als eerste te zien krijgt zodra er iets hapert.

## Week 4 — Codefreeze, Generieke Repetitie en Monitoring

Week vier bevat géén nieuwe functionele ontwikkelingen. Dat is geen vrijblijvend advies; dat is het absolute bestaansrecht van week vier.

**Hanteer een strikte feature-freeze vanaf dag één van deze week.** Vrijwel elk Demo Day-debacle met een technische oorzaak is terug te herleiden naar een ogenschijnlijk onschuldige aanpassing die binnen 72 uur vóór de pitch naar productie werd gepusht — meestal een kleine cosmetische tweak waarvan men dacht dat die "onmogelijk iets stuk kon maken".

**Oefen onder reële belasting.** Geen theoretische loadtest met software, maar een gecoördineerde praktijktest. Vraag twintig bekenden om binnen hetzelfde tijdsbestek van drie minuten gelijktijdig een account aan te maken en het product te gebruiken, bij voorkeur via hun smartphone op 4G/5G. U leert hier meer van dan van welke geautomatiseerde tool dan ook, en u ontdekt het ruim op tijd om de limiet van uw connection pool te verhogen, een connection pooler (zoals PgBouncer of Supabase Pooler) tussen te schakelen, of een synchrone e-mailverzending naar een achtergrondwachtrij te migreren.

**Monitor wat u niet met het blote oog kunt volgen.** Zorg voor storingsnotificaties (via Sentry) die rechtstreeks binnenkomen op uw telefoon, een uptime-check die specifiek het registratie-endpoint test in plaats van alleen de homepagina, en logs die u tijdens het evenement helder kunt uitlezen. De fout die u zoekt is er een die u om 14:02 opmerkt en om 14:20 heeft opgelost, niet een probleem waar een investeerder u drie dagen later tijdens een vervolggesprek op moet wijzen.

**Leg het rollback-protocol vast op papier.** Eén A4-tje: hoe de deployment teruggedraaid moet worden, wie beschikt over de beheerdersinlog, en wat de exacte procedure is om een databaseback-up te herstellen. Onder invloed van adrenaline herinnert niemand zich de juiste commando's.

## Wat U Veilig Kunt Uitstellen

Zeven zaken die dringend aanvoelen, maar dat binnen een tijdsbestek van vier weken beslist niet zijn: een formele penetratietest; voorbereidingen op SOC 2 of ISO 27001; multi-regio redundantie; een complete analytische en attributie-infrastructuur; prestatie-optimalisatie voor dataverkeer dat u nog niet heeft; het toevoegen van een tweede of derde betaalmethode; en het beheerdersdashboard dat u al weken voor uzelf wilt bouwen.

Elk van deze punten heeft een legitiem moment. Geen van die momenten is nu. De eerlijke manier om uit te stellen, is door elk punt te koppelen aan een meetbare trigger — bijvoorbeeld: "pentest zodra de eerste enterprise-klant daarom vraagt", "SOC 2 zodra een contract boven de € 25k hiervan afhangt" — zodat uitstel een weloverwogen strategische keuze is in plaats van stilzwijgende struisvogelpolitiek.

## Wat Te Doen Als U Slechts Twee Weken Heeft

Omdat veel oprichters dit lezen met nog maar veertien dagen op de klok, volgt hier de gecomprimeerde aanpak:
- **Dagen 1 t/m 3:** Audit, en accepteer direct de structurele uitkomst daarvan.
- **Dagen 4 t/m 9:** Uitsluitend autorisatie op de API-laag, niets anders.
- **Dagen 10 t/m 11:** E-mail deliverability en de top drie foutafhandelingspaden.
- **Dag 12:** Harde codefreeze.
- **Dagen 13 en 14:** Praktijktest met twintig echte gebruikers en inrichten van monitoring.

Bij een deadline van twee weken kiest u er expliciet voor om betalingen uit te stellen. Gebruik op Demo Day een wachtlijst, handmatige facturen of een eenvoudige Stripe Payment Link. Niemand in het publiek zal het ontbreken van een geautomatiseerde checkout kwalijk nemen; een haperende betaling of dubbele incasso op het podium daarentegen vergeeft niemand.

Achter LaunchStudio staat het team van Manifera met meer dan 120 ervaren software-engineers. Hun [portfolio aan opgeleverde productiesystemen](https://www.manifera.com/portfolio/) is precies de reden waarom een tijdsbestek van vier weken een helder afbakeningsgesprek is in plaats van een gok: onze vaste-prijs trajecten van 1 tot 3 weken zijn exact ontworpen voor dit type harde deadlines.

Vier weken is ruim voldoende voor een waterdichte gebruikersscheiding, een betrouwbare geldstroom en een geslaagde generale repetitie — het is niet genoeg voor alles, en de oprichters die slagen op Demo Day zijn zij die doelbewust keuzes durfden te maken. [Plan een introductiegesprek van 15 minuten](https://launchstudio.eu/nl/#contact) en u sluit af met een concrete planning van wat haalbaar is in uw resterende veertien werkdagen.

## Echt voorbeeld

### Een Scale-Up Oprichter in Actie: De Freeze in Week Drie Die de Pitch Redde

Joris Bakhuizen, oprichter van Stagelijn, een SaaS-platform voor dienstenplanning in de horeca, naderde de Demo Day van een bekende Amsterdamse accelerator met een in Bolt gebouwd prototype, vier betalende pilotlocaties en nog precies 26 dagen op de klok. Zijn oorspronkelijke plan was om alle vier de weken te besteden aan een exportfunctie voor salarisadministraties waar een investeerder terloops naar had gevraagd.

De technische audit in week één gooide dat plan radicaal om. De API van Stagelijn bleek elk gewenst dienstenrooster op te halen op basis van ID, zonder ooit te valideren of het opvragende account wel hoorde bij de betreffende horecalocatie. In de gebruikersinterface was dit onzichtbaar, maar voor iedereen die simpelweg een getal in de URL aanpaste, lag alle concurrentiegevoelige personeelsdata direct open. Met vier pilotlocaties was dit een sluimerend risico; met tweehonderd nieuwsgierige Demo Day-bezoekers zou dit een acuut datalek worden. De salarisexport daarentegen was een functie die niemand in de zaal tijdens de presentatie zou aanklikken.

Weken twee en drie werden volledig besteed aan autorisatie op locatieniveau via Row-Level Security in Postgres, het configureren van SPF- en DKIM-records zodat activatiemails niet langer in de spambox van Outlook belandden, en het implementeren van een achtergrondwachtrij voor het verzenden van e-mails, wat voorheen de databaseverbinding acht seconden lang per registratie blokkeerde. Week vier kende een strikte codefreeze en een stresstest met 22 oprichters uit andere accelerator-cohorten die gelijktijdig een account aanmaakten. Dit bracht een database-plafond aan het licht bij circa veertig gelijktijdige sessies, wat twee dagen vóór de pitch direct werd opgelost door het tussenplaatsen van een connection pooler.

**Resultaat:** 214 vlekkeloze aanmeldingen in de eerste anderhalf uur na de pitch van Stagelijn, nul systeemfouten, nul datalekken tussen locaties en twee concrete vervolggesprekken voor een term sheet. De export voor salarisadministraties werd vijf weken later rustig gebouwd, toen een daadwerkelijke klant erom vroeg.

> *"Ik stond op het punt mijn laatste maand te verdoen aan het bouwen van een functie voor één enkele persoon in de zaal. In plaats daarvan heb ik geïnvesteerd in het fundament dat tweehonderd mensen tegelijk gingen aanraken."*
> — **Joris Bakhuizen, Oprichter Stagelijn (Amsterdam)**

**Kosten & Doorlooptijd:** € 4.200 (Launch & Grow Pakket, autorisatie, e-mail deliverability en concurrency hardening) — opgeleverd in 15 werkdagen.

---

## Veelgestelde Vragen

### Moet ik demonstreren op live productie of in een afgeschermde staging-omgeving?

Beide keuzes zijn prima verdedigbaar, maar beslis dit direct in week één, omdat het alle vervolgstappen beïnvloedt. Een afgeschermde omgeving met voorgeprogrammeerde testdata elimineert concurrency- en registratierisico's volledig, ten koste van het niet direct kunnen registreren van geïnteresseerden in de zaal — wat voor veel pitches een zeer verstandige afweging is.

### Kan een hardening-sprint van vier weken ook een databaseschemamigratie omvatten?

Vrijwel nooit zonder grote risico's. Een migratie die eigenaarschap of multi-tenancy raakt, vereist een eigen ontwikkeltraject met een uitvoerig getest rollback-mechanisme. Het proberen tussen te schuiven naast reguliere hardening is de voornaamste reden waarom oprichters op Demo Day stranden met een half gemigreerde database waar ze niet meer uitkomen.

### Hoe weet ik zeker of mijn applicatie tweehonderd gelijktijdige aanmeldingen aankan?

Door het fysiek te testen in plaats van er theoretisch over na te denken. Twintig echte mensen die zich binnen drie minuten aanmelden via mobiel internet leggen knelpunten in connection pooling, synchrone e-mailprocessen en rate limits veel sneller en realistischer bloot dan welke schatting ook, en het geeft u direct de tijd om het op te lossen.

### Is het acceptabel om een demonstratie te geven zonder werkende betaalfunctie?

Jazeker, en bij een doorlooptijd van vier weken of minder is het vaak zelfs de slimste keuze. Een betaallink, handmatige factuur of wachtlijst valt een publiek niet op, terwijl een webhook-fout die iemand tijdens uw pitch per ongeluk dubbel belast direct fataal is voor uw geloofwaardigheid.

### Wat moet ik doen met auditbevindingen die ik niet op tijd kan oplossen?

Noteer elk punt zorgvuldig inclusief de concrete drempelwaarde die actie vereist — zoals een gebruikersaantal, contractwaarde of compliancenorm — en deel dit overzicht transparant met potentiële investeerders. Een oprichter die zijn resterende technische schuld exact kan benoemen en prioriteren, maakt een aanzienlijk professionelere indruk dan iemand die beweert dat er geen enkel probleem is.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik demonstreren op live productie of in een afgeschermde staging-omgeving?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Beide opties zijn legitiem, maar beslis in week één. Een afgeschermde omgeving met klaargezette accounts sluit concurrency- en aanmeldrisico's uit, maar vangt geen live registraties op in de zaal."
      }
    },
    {
      "@type": "Question",
      "name": "Kan een hardening-sprint van vier weken ook een databaseschemamigratie omvatten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vrijwel nooit veilig. Een migratie rondom eigenaarschap of multi-tenancy vereist een apart venster met geteste rollbacks; forceren leidt vaak tot een half gemigreerde database op de demodag zelf."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe weet ik zeker of mijn applicatie tweehonderd gelijktijdige aanmeldingen aankan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Oefen met echte mensen. Laat twintig personen tegelijk via mobiele data binnen drie minuten registreren; dit legt connection-pool plafonds en blokkerende processen direct bloot."
      }
    },
    {
      "@type": "Question",
      "name": "Is het acceptabel om een demonstratie te geven zonder werkende betaalfunctie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, en bij vier weken tijd vaak de betere keuze. Een betaallink of facturatie op afspraak valt niet negatief op, terwijl een webhook-fout tijdens een live pitch direct pijnlijk zichtbaar is."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet ik doen met auditbevindingen die ik niet op tijd kan oplossen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Documenteer ze met duidelijke actietriggers (gebruikersaantallen of omzetdrempels) en deel dit transparant met investeerders. Precieze kennis van technische schuld getuigt van senioriteit."
      }
    }
  ]
}
</script>
