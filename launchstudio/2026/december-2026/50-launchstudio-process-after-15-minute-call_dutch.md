---
Titel: "Het LaunchStudio Proces: Wat Gebeurt Er Na Uw Gesprek van 15 Minuten?"
Trefwoorden: ai development, ai deployment, build app with ai, ai app dev, LaunchStudio, Manifera
Koperfase: Beslissing
Doelpersona: AI-Native Oprichter (Niet-Technisch)
---

# Het LaunchStudio Proces: Wat Gebeurt Er Na Uw Gesprek van 15 Minuten?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Het LaunchStudio Proces: Wat Gebeurt Er Na Uw Gesprek van 15 Minuten?",
  "description": "Een concrete, transparante toelichting van wat er exact gebeurt vanaf het moment dat een oprichter het kennismakingsgesprek van LaunchStudio boekt tot aan een live, productieklaar product.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-12-31",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/launchstudio-process-after-15-minute-call"
  }
}
</script>

De onzekerheid over *"wat gebeurt er eigenlijk precies als ik dit inplan?"* houdt meer oprichters tegen dan de prijs zelf. Onzekerheid over het proces, niet de prijs, is vaak de werkelijke reden waarom een twijfelende oprichter aarzelt om dat eerste gesprek te boeken. Dit is een concrete, stapsgewijze toelichting van wat er precies gebeurt nadat u dat doet.

## Stap 1: Het Kennismakingsgesprek van 15 Minuten

U beschrijft uw product, wat u al heeft gebouwd (doorgaans met Lovable, Bolt, Cursor of v0) en wat u wilt bereiken — een lanceerdeadline, een specifieke zorg zoals beveiliging, of algemene begeleiding om het product productieklaar te maken. Er is geen technische achtergrond vereist; het gesprek is zo gestructureerd dat oprichters hun situatie in gewone mensentaal kunnen toelichten, waarna het team van LaunchStudio dat aan hun kant vertaalt naar een technische scope.

## Stap 2: Codebase-Review en Scoping

Na afloop van het gesprek inspecteert het team de werkelijke codebase van uw prototype om te beoordelen wat er al staat, wat er nog ontbreekt ten opzichte van de 7-lagen productiestack (frontend, AI/modellaag, authenticatie, database, betalingen, hosting, monitoring) en welke specifieke werkzaamheden nodig zijn om de hiaten voor uw specifieke product en doelen te dichten.

## Stap 3: Vaste Offerte en Tijdslijn

U ontvangt een specifieke, gespecificeerde offerte — geen vage bandbreedte — samen met een bindende tijdslijn, doorgaans één tot drie weken afhankelijk van de scope. Dit is het moment waarop u beslist of u wilt doorgaan; het eerste gesprek en de scoping-analyse scheppen geen enkele verplichting.

## Stap 4: Kickoff en Ontwikkeling

Zodra u de offerte goedkeurt, begint het engineeringteam van Manifera met het werk. Uw visuele frontend-ontwerp wordt behouden als vast startpunt (zoals behandeld in onze eerdere richtlijnen voor frontend-behoud), waarbij het team de ontbrekende infrastructuurlagen eromheen bouwt — authenticatie, databasebeveiliging, betalingen en hostingconfiguratie.

## Stap 5: Voortgangscommunicatie

Gedurende de ontwikkeling ontvangt u regelmatige updates over de voortgang — geen radiostilte tot een plotseling bericht dat "het klaar is". Voor oprichters met harde externe deadlines (een lanceerevenement, een toezegging aan een klant) wordt de voortgangscommunicatie afgestemd op die urgentie.

## Stap 6: Testen en Beoordeling

Vóór de definitieve oplevering test het team kritieke flows (registratie, kernfunctionaliteit, betalingsverwerking) en voert bij privacygevoelige projecten de cross-account isolatietests uit die worden behandeld in onze richtlijnen voor multi-tenant architecturen. U wordt uitgenodigd om het live, gedeployde product zelf te inspecteren voordat het traject als voltooid wordt beschouwd.

## Stap 7: Livegang en Nazorg

Uw product gaat live op uw eigen domein, onder uw eigen accounts, met volledig behoud van uw eigendom over de code. Afhankelijk van uw pakket loopt 48-uurs ondersteuning na de lancering (Launch Ready) of doorlopende prioriteitsondersteuning met beheerde hosting (Launch & Grow, €49/maand) daarna door.

## Wat Er Zeker NIET Gebeurt

Geen herontwerp van uw interface zonder uitdrukkelijk overleg. Geen verrassingen met open eindes en uurtarieven, zoals beschreven in onze richtlijnen voor vaste prijzen. Geen druk om aanvullende diensten aan te schaffen die uw specifieke project niet nodig heeft — het doel is een afgebakende, eerlijke samenwerking, niet het maximaliseren van declarabele uren.

[Boek uw gesprek van 15 minuten](https://launchstudio.eu/en/#contact) — de eerste, geheel vrijblijvende stap in dit transparante proces.

## Achter Stap 2: Hoe de 7-Lagen Gap-Analyse Daadwerkelijk Werkt

Oprichters willen natuurlijk weten wat er daadwerkelijk gebeurt tijdens de codebase-review, aangezien dit de stap is die zowel de offerte als de daaropvolgende planning bepaalt. De inspectie is geen oppervlakkige technische scan — het zijn zeven gerichte controles, elk gekoppeld aan één productielaag, die elk een specifiek oordeel (geslaagd, afgekeurd of gedeeltelijk) opleveren in plaats van een vaag algemeen gevoel.

**Wat er per laag wordt gecontroleerd:**
1. **Frontend** — is de interface stabiel, of breekt deze bij situaties die de AI-tool nooit heeft getest (lege data, foutstatussen, trage verbindingen)? Deze laag passeert meestal grotendeels ongewijzigd, omdat oprichters hier de meeste iteratietijd aan hebben besteed in hun AI-tool.
2. **AI/Modellaag** — wordt de modelaanroep veilig gedaan vanuit een server-route, of is de API-sleutel zichtbaar aan de client-side? Is er een fallback als de AI-provider een time-out geeft of ongeldige data terugstuurt?
3. **Authenticatie** — is er een echt sessie- en wachtwoordhashing-systeem aanwezig, of is "inloggen" puur cosmetisch waarbij een naam in local storage wordt opgeslagen zonder verificatie?
4. **Database** — is er daadwerkelijke isolatie op rijniveau (Row Level Security) tussen gebruikers, of stelt het schema technisch elke ingelogde gebruiker in staat om data van anderen op te vragen?
5. **Betalingen** — is er een betaalprovider-koppeling (Mollie of Stripe) en handelt deze mislukte betalingen, restituties en abonnementswijzigingen correct af?
6. **Hosting** — is de huidige deployment stabiel onder gelijktijdige gebruikersbelasting, of is deze alleen door de oprichter solo getest?
7. **Monitoring** — krijgt het team een melding als het product uitvalt of fouten genereert, of ontdekt de oprichter dit pas via een boze e-mail van een klant?

Elke laag krijgt een specifieke notitie in het scoping-document — geen vaag "moet naar gekeken worden", maar de exacte constatering, zoals *"geen row-level security policies ingesteld op de tabel boekingen"* — omdat vage bevindingen leiden tot vage offertes, en dat is precies wat oprichters willen vermijden.

**Waarom dit leidt tot een vaste offerte in plaats van een bandbreedte:** doordat de bevinding per laag specifiek is, kunnen de benodigde engineering-uren om elk gat te dichten met reëel vertrouwen worden gecalculeerd, in plaats van marges in te bouwen voor onzekerheid. Een oprichter wiens authenticatie Supabase Auth al correct gebruikt, krijgt een lagere offertecomponent voor die laag dan een oprichter bij wie "inloggen" cosmetisch blijkt te zijn — de review bepaalt direct het bedrag.

Dit is ook waarom de codebase-review plaatsvindt vóór de offerte: een vaste prijs afgeven zonder eerst de 7 lagen te inspecteren zou puur gokwerk zijn. Het is de technische reden waarom de offerte in Stap 3 gespecificeerd kan worden, en waarom twee oprichters met vergelijkbaar klinkende producten toch verschillende offertes kunnen ontvangen zodra hun echte codebases zijn onderzocht.

**Wat oprichters vooraf kunnen doen om deze stap te versnellen:** zorg dat de live URL van uw prototype en, indien mogelijk, leestoegang tot de codebase (een GitHub-link of export uit Lovable, Bolt, Cursor of v0) klaarliggen. U hoeft zelf geen technische samenvatting te schrijven — het benoemen van de hiaten is precies waar onze review voor dient — maar directe toegang tot de code maakt van Stap 2 een snelle en feitelijke inspectie.

## Echt voorbeeld

### Een AI-native oprichter in actie: Alle stappen doorlopen van start tot finish

Puck, coördinator van kinderactiviteiten in Culemborg, bouwde met v0 SpeelAgenda: een AI-tool die leeftijdsgeschikte lokale uitjes en activiteiten voorstelde aan ouders op basis van de interesses van hun kinderen. Ze had wekenlang geaarzeld voordat ze het kennismakingsgesprek met LaunchStudio boekte, puur omdat ze niet wist wat er zou gebeuren — zou ze onder druk worden gezet voor een dure aankoop, zou haar ontwerp zonder overleg worden aangepast, en was de planning wel betrouwbaar?

Pucks gesprek van 15 minuten behandelde haar prototype, haar doel om vóór het nieuwe schooljaar te lanceren en haar specifieke zorg over het behoud van haar ontwerp. De daaropvolgende codebase-review identificeerde de concrete gaten: geen echte authenticatie, geen mogelijkheid om het geplande maandelijkse bedrag af te rekenen en een database zonder betrouwbare scheiding tussen ouderaccounts. Ze ontving een vaste offerte van €2.250 met een doorlooptijd van 11 werkdagen — zonder verkoopdruk of onnodige extra's.

Puck keurde de offerte goed, waarna de ontwikkeling startte met wekelijkse voortgangsupdates met het oog op haar schooljaar-deadline. Vóór oplevering verifieerde Puck zelf dat twee afzonderlijke ouder-testaccounts elkaars kindgegevens niet konden zien. SpeelAgenda lanceerde op haar eigen domein, in haar eigen accounts, met haar oorspronkelijke v0-ontwerp volledig intact.

**Resultaat:** SpeelAgenda ging drie dagen vóór Pucks schooljaar-deadline live, waarbij het hele proces exact verliep zoals besproken tijdens het eerste gesprek — waarmee alle eerdere twijfels werden weggenomen.

> *"Ik had het boeken van het gesprek een maand uitgesteld omdat ik niet wist waar ik aan begon. Elke stap verliep exact zoals vooraf beschreven — geen verrassingen, geen verkoopdruk en geen enkele wijziging aan mijn ontwerp waar ik niet eerst akkoord op had gegeven."*  
> — **Puck Willems, Oprichter SpeelAgenda (Culemborg)**

**Kosten & tijdlijn:** €2.250 (Launch Ready Pakket) — binnen 11 werkdagen live opgeleverd.

---

## Veelgestelde vragen

### Zit er enige verplichting of kosten verbonden aan het eerste gesprek van 15 minuten?
Nee. Het gesprek is gratis en verplicht u tot niets — het is specifiek bedoeld om u inzicht te geven in uw opties en een heldere scope te schetsen voordat u besluit over een betaald traject.

### Hoe lang duurt de codebase-review en het opstellen van de offerte doorgaans na het gesprek?
Dit hangt af van de complexiteit, maar oprichters ontvangen hun gespecificeerde vaste offerte doorgaans binnen enkele werkdagen na de intake, zodra het team de code grondig heeft geanalyseerd.

### Wat als ik het tijdens het ontwikkelproces ergens niet mee eens ben, zoals een voorgestelde technische keuze?
Dankzij directe en regelmatige communicatie kunnen vragen en opmerkingen direct worden besproken en bijgestuurd, in plaats van pas bij de eindoplevering.

### Kan ik de scope nog aanpassen nadat de vaste offerte is goedgekeurd?
Ja. Zoals behandeld in onze richtlijnen voor vaste prijzen worden wijzigingen altijd transparant vooraf besproken en vastgelegd, inclusief eventuele aanpassingen in prijs of tijdslijn.

### Verschilt het proces tussen de pakketten Launch Ready en Launch & Grow?
Het kernproces (gesprek, scoping, offerte, ontwikkeling, testen, livegang) is voor beide pakketten identiek. Het verschil zit in de inhoud van de scope: Launch & Grow voegt betalingsverwerking, beheerde hosting en doorlopend maandelijks beheer toe aan de basis-hardening van Launch Ready.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Zit er enige verplichting of kosten verbonden aan het gesprek van 15 minuten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Het gesprek is volledig kosteloos en vrijblijvend, bedoeld om uw opties helder in kaart te brengen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt de codebase-review en het opstellen van de offerte?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Oprichters ontvangen hun gespecificeerde vaste offerte doorgaans binnen enkele werkdagen na het gesprek."
      }
    },
    {
      "@type": "Question",
      "name": "Wat als ik het tijdens de bouw niet eens ben met een technische keuze?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Door directe voortgangscommunicatie worden eventuele opmerkingen direct tijdens het proces besproken en afgestemd."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik de scope nog aanpassen na akkoord op de offerte?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, eventuele scope-uitbreidingen worden altijd vooraf transparant besproken en schriftelijk overeengekomen."
      }
    },
    {
      "@type": "Question",
      "name": "Verschilt het proces tussen Launch Ready en Launch & Grow?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het 7-stappenproces is gelijk; Launch & Grow voegt betalingskoppeling, managed hosting en maandelijks beheer toe."
      }
    }
  ]
}
</script>
