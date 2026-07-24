---
Titel: "Waarom 'Beveiliging' voor u iets anders betekent dan voor uw AI-codeertool"
Trefwoorden: ai secure, ai generated code security, authorization vs authentication, ai app security gaps
Koperfase: Bewustzijn
Doelgroep: AI-Native oprichter (niet-technisch)
---
# Waarom 'Beveiliging' voor u iets anders betekent dan voor uw AI-codeertool

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Waarom 'Beveiliging' voor u iets anders betekent dan voor uw AI-codeertool",
  "description": "Oprichters en AI-codeertools gebruiken het woord 'veilig' om twee volledig verschillende dingen te bedoelen. Dit is de kloof die door AI gebouwde apps kwetsbaar maakt, en hoe u die dicht.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/security-means-different-things" }
}
</script>

Vraag een oprichter wat "veilig" betekent en u hoort meestal iets over een hangslotpictogram, een groene URL-balk, misschien een inlogscherm. Stel een AI-codeertool dezelfde vraag en functioneel luidt het antwoord: de code is gecompileerd, het verzoek gaf een 200 terug, er is niets vastgelopen. Beide partijen denken dat ze het over hetzelfde hebben. Dat is niet zo. Die mismatch is stilletjes verantwoordelijk voor een groot deel van de kwetsbaarheden die op dit moment in door AI gegenereerde apps zitten, en bijna niemand merkt het op totdat het te laat is.

Dit is geen kritiek op de tools. Lovable, Bolt, Cursor en v0 zijn buitengewoon goed in het omzetten van een beschrijving naar werkende software. Maar "werkend" en "veilig" zijn verschillende eigenschappen, en een AI-model dat is getraind om aan uw prompt te voldoen, heeft geen zelfstandig begrip van wie wel en niet mag zien wat. Het bouwt wat u hebt gevraagd. Als u vroeg om een dashboard waarin gebruikers hun eigen gegevens zien, bouwt het een dashboard. Of de server daadwerkelijk controleert dat de gegevens toebehoren aan de persoon die erom vraagt, is een aparte vraag die de tool nooit gedwongen werd te beantwoorden.

## Het hangslot is niet het punt

De meeste niet-technische oprichters stellen beveiliging gelijk aan versleuteling tijdens verzending — HTTPS, dat kleine hangslotpictogram in de browser. En eerlijk gezegd, dat is belangrijk: het voorkomt dat iemand op hetzelfde wifi-netwerk van het koffietentje uw verkeer kan lezen. Maar het zegt niets over wat er gebeurt zodra een verzoek uw server bereikt. HTTPS beschermt de leiding. Het controleert op geen enkele manier of de persoon die het verzoek verstuurt, dat specifieke stukje data eigenlijk wel mag opvragen.

Dat tweede probleem heeft een naam: autorisatie. Het verschilt van authenticatie, wat alleen bevestigt *wie* iemand is (u bent ingelogd, hier is uw sessie). Autorisatie stelt bij elke afzonderlijke gegevensaanvraag een moeilijkere vraag: *mag deze specifieke ingelogde persoon dit specifieke record zien?* AI-codeertools zijn behoorlijk goed in authenticatie — inlogstromen zijn veelvoorkomende, goed gedocumenteerde patronen. Bij autorisatie gaat het mis, omdat de tool daarvoor de eigendomsregels van uw datamodel moet begrijpen, en die worden standaard meestal helemaal niet afgedwongen op databaseniveau.

## Twee verschillende definities van 'klaar'

Wanneer u een AI-tool vertelt "zorg dat dit veilig is", hoort deze een instructie om dingen toe te voegen zoals wachtwoordhashing, HTTPS-omleidingen, misschien een inlogpoort. Het hoort niet automatisch "zorg ervoor dat Gebruiker A nooit de records van Gebruiker B kan ophalen door een getal in de URL te veranderen." Die tweede eis moet expliciet, doordacht en getest worden — meestal met controles op rijniveau die worden afgedwongen op de server of in de database zelf, niet alleen verborgen door een frontend die simpelweg geen 'bekijken'-knop toont.

Dit is de kern van de mismatch. U denkt in termen van *uitkomsten* — niemand zou gegevens moeten zien die niet van hem of haar zijn. De tool denkt in termen van *instructies* — heb ik het letterlijke verzoek uitgevoerd. Totdat u expliciet vraagt om autorisatiecontroles aan de serverzijde voor elk gegevenstoegangspad, zullen de meeste door AI gegenereerde backends deze niet hebben, omdat niets in een typische prompt die beperking afdwingt.

LaunchStudio wordt mogelijk gemaakt door Manifera, een softwareontwikkelingsbedrijf met meer dan 11 jaar ervaring in productie-engineering, en onze technici vanuit Amsterdam zien deze exacte kloof in bijna elke door AI gegenereerde codebase die we beoordelen — een volledig werkend product met een gegevenstoegangsgat waar niemand een naam voor had bedacht. Als u een tweede paar ogen wilt voordat u er op de harde manier achter komt, kunt u [uw project beschrijven via ons proces](https://launchstudio.eu/en/#process) en dan vertellen wij u eerlijk wat er ontbreekt. Voor de onderliggende technische normen waaraan wij elke beoordeling toetsen, zie hoe [Manifera softwareontwikkeling op maat benadert](https://www.manifera.com/services/custom-software-development/).

## Echt voorbeeld

### Een AI-native oprichter in actie: het hangslot was niet het probleem

Mila Verstappen, een oprichter uit Arnhem, bouwde "KlantWacht" — een wachtrijbeheer-SaaS voor kleine dienstverlenende bedrijven — met Lovable. Ze had haar huiswerk gedaan: de app gebruikte overal HTTPS, had een goed inlogscherm, en wachtwoorden werden gehasht. Volgens elke definitie die ze had geleerd te controleren, was KlantWacht veilig. Ze lanceerde de app met vertrouwen naar haar eerste paar pilotklanten.

Wat ze niet had gecontroleerd — omdat niets in het bouwproces dit had gesignaleerd — was wat er gebeurde na het inloggen. Elk klantaccount kon de wachtrijgegevens van elk ander klantaccount opvragen, simpelweg door een ID in het verzoek te veranderen. Er was geen controle aan de serverzijde die bevestigde dat de opgevraagde wachtrij daadwerkelijk toebehoorde aan het ingelogde bedrijf. De frontend *toonde* standaard alleen uw eigen wachtrij, maar de backend gaf gewoon die van iedereen prijs als er direct om werd gevraagd. Het was geen geavanceerde aanval. Het was een ontbrekende 'if'-instructie.

De kloof kwam aan het licht toen een van haar pilotklanten, uit nieuwsgierigheid rondkijkend, de live wachtrij van een ander bedrijf opmerkte in een netwerkverzoek. Mila bracht het project naar LaunchStudio. Onze technici voegden autorisatiecontroles aan de serverzijde toe voor elk gegevenseindpunt, waarbij elk verzoek werd gekoppeld aan de eigen records van het geauthenticeerde account op databaseniveau in plaats van te vertrouwen op de frontend om te verbergen wat helemaal niet opgevraagd zou mogen worden, en doorzochten de rest van het schema op hetzelfde ontbrekende patroon.

**Resultaat:** KlantWacht handhaaft nu eigendomscontroles bij elke query, geverifieerd met geautomatiseerde tests die precies de cross-account toegang proberen die eerder werkte.

> *"Ik dacht dat ik alles goed had gedaan omdat ik de vakjes had aangevinkt die ik kende. Ik wist niet dat er vakjes waren waar ik nog nooit van had gehoord."*
> — **Mila Verstappen, oprichter, KlantWacht (Arnhem)**

**Kosten en tijdlijn:** € 950 (autorisatieaudit en fix voor alle eindpunten) — voltooid in 4 werkdagen.

---

## Veelgestelde vragen

### Betekent HTTPS dat mijn door AI gebouwde app veilig is?

Nee. HTTPS beschermt gegevens tijdens de overdracht tussen de browser en uw server, maar zegt niets over of uw server correct controleert wie welke gegevens mag benaderen zodra een verzoek binnenkomt.

### Waarom voegen AI-codeertools niet automatisch autorisatiecontroles toe?

Omdat een prompt zoals "bouw een dashboard" niet expliciet vraagt om eigendomscontroles per record, en de tool geen zelfstandig oordeel heeft over de toegangsregels van uw datamodel, tenzij u die specificeert.

### Wat is het verschil tussen authenticatie en autorisatie?

Authenticatie bevestigt wie een gebruiker is (deze is ingelogd). Autorisatie bevestigt wat die specifieke gebruiker mag zien of doen, wat bij elke afzonderlijke gegevensaanvraag gecontroleerd moet worden.

### Hoe zou ik weten of mijn app dit soort gat heeft?

De technici van Manifera, waaronder het in Amsterdam gevestigde team, beoordelen door AI gegenereerde codebases specifiek op ontbrekende eigendomscontroles aan de serverzijde — het is een van de eerste dingen waar een beveiligingsbeoordeling naar zoekt, omdat de frontend alleen nooit kan bewijzen dat de backend veilig is.

### Kan dit worden opgelost zonder mijn app opnieuw te bouwen?

Ja. Autorisatiegaten worden meestal opgelost op de backend- en databaselaag zonder uw bestaande frontend aan te raken, wat precies het soort productie-hardening werk is waarin LaunchStudio zich specialiseert.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Does HTTPS mean my AI-built app is secure?", "acceptedAnswer": { "@type": "Answer", "text": "No. HTTPS protects data in transit but says nothing about whether the server checks who is allowed to access which data once a request arrives." } },
    { "@type": "Question", "name": "Why don't AI coding tools add authorization checks automatically?", "acceptedAnswer": { "@type": "Answer", "text": "A typical prompt doesn't explicitly request per-record ownership checks, and the tool has no independent judgment about a data model's access rules unless told." } },
    { "@type": "Question", "name": "What's the difference between authentication and authorization?", "acceptedAnswer": { "@type": "Answer", "text": "Authentication confirms who a user is. Authorization confirms what that specific user is allowed to see or do on every data request." } },
    { "@type": "Question", "name": "How would I know if my app has this kind of gap?", "acceptedAnswer": { "@type": "Answer", "text": "A security review by engineers experienced with AI-generated code, like Manifera's Amsterdam-based team, specifically checks for missing server-side ownership checks." } },
    { "@type": "Question", "name": "Can this be fixed without rebuilding my app?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. Authorization gaps are typically fixed at the backend and database layer without touching the existing frontend." } }
  ]
}
</script>
