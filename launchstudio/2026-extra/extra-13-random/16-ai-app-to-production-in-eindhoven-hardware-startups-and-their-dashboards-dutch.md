---
Titel: "Van AI-app naar productie in Eindhoven: Hardware-startups en hun dashboards"
Trefwoorden: ai-app naar productie, ai app productie eindhoven, iot dashboard beveiliging, hardware startup web app, cursor, device api keys, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-oprichter / Indie Hacker
---

# Van AI-app naar productie in Eindhoven: Hardware-startups en hun dashboards

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Van AI-app naar productie in Eindhoven: Hardware-startups en hun dashboards",
  "description": "Hardware- en deeptech-oprichters in de regio Eindhoven ontwikkelen hun fysieke apparaten uiterst zorgvuldig, maar bouwen het bijbehorende webdashboard vaak haastig met AI. Dit artikel behandelt wat er verandert wanneer die AI-app naar productie gaat: apparaat-identiteit, datainname op schaal, tijdreeksdata en firmware-compatibiliteit.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-16",
  "inLanguage": "nl-NL",
  "contentLocation": { "@type": "Place", "name": "Eindhoven, Nederland" },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-app-to-production-in-eindhoven-hardware-startups-and-their-dashboards" }
}
</script>

In de Brainportregio krijgt de hardware de engineeringaandacht die ze verdient. Sensoren worden gekalibreerd, behuizingen getest, firmware gereviewd. Dan wordt, vaak in de laatste weken vóór een pilot, het dashboard voor de klant in een paar avonden in Cursor gebouwd — omdat het "maar het webgedeelte" is. Bij het naar productie brengen van die AI-app ontdekken veel Eindhovense hardware-startups dat het webgedeelte juist de plek is waar de data van hun klanten, en de inloggegevens van hun apparaten, werkelijk leven.

Dit artikel is voor technische oprichters rond Eindhoven — op de High Tech Campus, Strijp-S of bij een van de spin-offs van de universiteit — van wie het apparaat degelijk is en het dashboard door AI gebouwd.

## Waarom Hardwaredashboards een Ander Soort Webapp Zijn

Een typische SaaS-app ontvangt verzoeken van mensen. Een hardwaredashboard ontvangt voortdurend verzoeken van apparaten, en af en toe van mensen. Dat verandert bijna alles aan productierijpheid:

- **Het apparaat is ook een gebruiker.** Het heeft een identiteit, inloggegevens en rechten nodig — en in tegenstelling tot een mens kan het zijn wachtwoord niet herstellen.
- **Data komt voortdurend binnen.** Een paar honderd apparaten die elke minuut rapporteren, leveren per dag meer schrijfacties op dan de meeste SaaS-apps in een maand zien.
- **De data is een tijdreeks.** Query's vragen om bereiken en aggregaten ("gemiddelde luchtvochtigheid per uur vorige week"), en gewone tabellen gaan daar op schaal slecht mee om.
- **Fouten zijn fysiek.** Een dashboard dat commando's naar apparaten kan sturen — een klep openen, een instelwaarde veranderen — maakt van een fout in toegangsbeheer een veiligheidsprobleem.

AI-codeertools weten hier niets van tenzij je het ze vertelt, en zelfs dan leveren ze de meest gangbare patronen voor webapps op, die uitgaan van menselijke gebruikers.

## Identiteit van Apparaten: Het Meest Voorkomende Gat

Het patroon dat LaunchStudio het vaakst vindt in AI-gebouwde hardwaredashboards: elk apparaat gebruikt dezelfde API-sleutel, vaak vastgecodeerd in de firmware, en het endpoint voor binnenkomende data vertrouwt elke `device_id` die het verzoek bevat.

De gevolgen zijn ernstig. Iedereen die de sleutel uit één apparaat haalt — of uit het bestand van een firmware-update — kan als elk apparaat data sturen, voor elke klant. En de sleutel kan niet worden ingetrokken zonder elk apparaat in het veld bij te werken.

Het productiepatroon is inloggegevens per apparaat: elk apparaat krijgt bij het in gebruik nemen een eigen token of certificaat, de server leidt de identiteit van het apparaat af uit de inloggegevens in plaats van uit de body van het verzoek, en een gecompromitteerd apparaat kan afzonderlijk worden ingetrokken. Bij opzetten op basis van MQTT horen de toegangslijsten van de broker elk apparaat te beperken tot zijn eigen topics.

## Binnenkomende Data Die de Vloot Overleeft

AI-gegenereerde endpoints voor binnenkomende data schrijven elke meting meestal rechtstreeks naar de hoofddatabase, één rij per verzoek. Met twintig apparaten in een pilot gaat dat prima. Met tweeduizend apparaten die elke dertig seconden rapporteren, zijn dat meer dan vijf miljoen inserts per dag in dezelfde database die je dashboard bevraagt.

Wat productie nodig heeft:

- **Bundelen en bufferen.** Apparaten of een gateway sturen metingen in batches; de server zet ze in een wachtrij en schrijft ze in bulk weg.
- **Idempotentie.** Apparaten proberen het opnieuw wanneer de verbinding wegvalt. Elke meting heeft een unieke identificator nodig, zodat herhalingen geen duplicaten opleveren.
- **Tegendruk.** Is de server traag, dan moet die apparaten vertellen te wachten, niet stilletjes data laten vallen.
- **Tijd van het apparaat, gecontroleerd door de server.** Apparaten met een verkeerde klok leveren metingen uit 1970 of volgend jaar; de server hoort die te markeren.

## Tijdreeksdata Zonder Tijdreekspijn

Standaard Postgres-tabellen gaan tot op zekere hoogte acceptabel om met tijdreeksdata, en daarna worden dashboards stroperig traag. Opties die het beheersbaar houden, zijn de extensie TimescaleDB, partitioneren op tijd, en vooraf berekende samenvattingen (aggregaten per uur en per dag), zodat grafieken geen ruwe metingen hoeven te doorzoeken. Bewaartermijnen doen er ook toe: beslis hoe lang ruwe metingen worden bewaard voordat alleen aggregaten overblijven.

## Klanten Mogen Alleen Hun Eigen Apparaten Zien

B2B-klanten van hardware — kassen, fabrieken, woningcorporaties — verwachten strikte scheiding. Een AI-gebouwd dashboard filtert apparaten vaak per klant in de interface, terwijl de API de data van elk apparaat teruggeeft als erom wordt gevraagd. Scheiding tussen tenants moet op de server worden afgedwongen, bij voorkeur in de database met row level security gekoppeld aan de organisatie van de klant, en moet net zo goed gelden voor endpoints voor commando's.

## Commando's Vragen Meer Zorg dan Data

Kan je dashboard commando's naar apparaten sturen, behandel dat pad dan als het gevoeligste deel van het systeem: rolcontroles (niet elke gebruiker bij een klant mag instelwaarden veranderen), bevestiging bij ingrijpende acties, een auditlog van wie wat wanneer stuurde, en limieten op waarden zodat een tikfout een verwarming niet naar een onveilige temperatuur kan sturen.

## Firmware en Backend: Twee Releasecycli in de Pas Houden

Hardware-startups hebben twee releasecycli die in heel verschillende tempo's bewegen. Het dashboard kan dagelijks worden bijgewerkt; firmware op duizenden apparaten in het veld wordt zelden, voorzichtig en soms nooit bijgewerkt. Een AI-app voor een apparaatproduct naar productie brengen betekent dat de backend jarenlang met oude firmware moet kunnen omgaan.

Praktische regels:

- **Geef elke apparaat-API een versie.** Apparaten sturen bij elk verzoek een firmwareversie mee; de backend blijft oudere versies ondersteunen totdat ze bewust worden uitgefaseerd.
- **Hernoem of verwijder nooit velden die apparaten sturen** zonder overgangsperiode. Voeg nieuwe velden toe naast de oude.
- **Laat apparaten configuratie ophalen.** Apparaten vragen de backend om configuratie in plaats van dat die naar hen wordt gestuurd, zodat wijzigingen geleidelijk kunnen worden uitgerold en teruggedraaid.
- **Rol firmware gefaseerd uit.** Werk 5% van de apparaten bij, let op foutpercentages en connectiviteit, en ga dan verder.

AI-gegenereerde backendcode houdt hier zelden rekening mee, omdat in een demo elk apparaat de firmware draait die het dashboard verwacht.

## Beveiligingsnormen die Hardwareklanten Noemen

B2B-klanten van hardware verwijzen bij inkoop steeds vaker naar formele normen. Degene die Eindhovense oprichters het vaakst tegenkomen:

| Norm of regelgeving | Reikwijdte | Wat het betekent voor de webkant |
| --- | --- | --- |
| ETSI EN 303 645 | Beveiligingsbasis voor IoT voor consumenten | Geen standaardwachtwoorden, een updatemechanisme, beveiligde communicatie |
| IEC 62443 | Industriële automatisering en besturingssystemen | Zones, toegangsbeheer, veilige ontwikkelpraktijken |
| EU Cyber Resilience Act | Producten met digitale elementen die in de EU worden verkocht | Omgaan met kwetsbaarheden, beveiligingsupdates, documentatie gedurende de levensduur van het product |
| ISO 27001 | Beheer van informatiebeveiliging | Organisatorische maatregelen; vaak gevraagd aan de leverancier |

Vooral de Cyber Resilience Act zal veel verbonden producten raken die in de EU worden verkocht naarmate de verplichtingen ingaan, inclusief plichten om kwetsbaarheden af te handelen en te melden en beveiligingsupdates te leveren. De backend en het dashboard horen bij dat plaatje, omdat daar inloggegevens van apparaten, updates en klantdata samenkomen.

## Eigendom van en Toegang tot Data voor Klanten

Industriële klanten willen vaak hun data: ruwe metingen geëxporteerd naar hun eigen systemen, API's voor hun datateams, bewaartermijnen die zij bepalen. Plan op API's voor klanten met sleutels en scopes per klant, rate limits, auditlogs van toegang en duidelijke contractuele afspraken over wie eigenaar is van de data en wat er aan het einde van het contract gebeurt. Vroeg een export en API bouwen voorkomt ook de losse verzoeken om CSV-bestanden die anders elke week engineeringtijd kosten.

## De Vloot Bewaken, Niet Alleen de Server

Uptimebewaking van de server is niet genoeg voor een apparaatproduct. Je moet ook weten wanneer apparaten stil worden: een sensor die stopt met rapporteren, kan kapot, offline of gecompromitteerd zijn. Nuttige signalen zijn het aantal apparaten dat per uur rapporteert tegenover het verwachte aantal, apparaten met ongebruikelijke berichtfrequenties (te veel of te weinig), de verdeling van firmwareversies, en de vertraging tussen het tijdstip van een meting en de aankomst ervan. Meldingen hierop vangen problemen op die een klant anders als eerste zou ontdekken — meestal op het moment dat een kas oververhit raakt of een machine stopt.

## Van Pilot naar Uitrol: Een Checklist

Bevestig, voordat je van een pilot opschaalt naar een uitrol bij een hele klant:

1. Inloggegevens per apparaat met intrekking zijn ingericht.
2. De verwerking van binnenkomende data kan in een loadtest tien keer het pilotvolume aan.
3. Opslag voor tijdreeksen heeft bewaartermijnen en samenvattingen ingesteld.
4. Scheiding tussen tenants wordt afgedwongen en is getest.
5. Commando's hebben rolcontroles, bevestiging, limieten en auditlogs.
6. Firmware- en backendversies zijn compatibel over minstens twee releases.
7. Bewaking van de vloot geeft meldingen bij stille apparaten.
8. Een beveiligingsoverzicht ligt klaar voor het IT-team van de klant.

Dit is de lijst die de engineers van klanten tijdens een besluit over uitrol doorlopen, vaak precies in deze volgorde.

## Apparaatdata en de AVG

Apparaatdata is niet automatisch anoniem. Metingen uit een kas zijn meestal bedrijfsdata, maar data van een slimme huissensor, een wearable of een voertuig kan laten zien wanneer iemand thuis is, hoe die zich verplaatst of hoe die leeft — en dat maakt het persoonsgegevens. Breng in kaart welke datastromen betrekking hebben op herkenbare personen, pas dataminimalisatie toe (aggregeer waar ruwe data niet nodig is), stel per stroom bewaartermijnen vast en documenteer de rechtsgrond. Bij B2B-producten treden klanten vaak op als verwerkingsverantwoordelijke en jij als verwerker, wat een verwerkersovereenkomst vereist en een duidelijke lijst met subverwerkers, inclusief cloud- en tijdreeksdiensten. Dit vroeg goed regelen, voorkomt ongemakkelijke gesprekken wanneer de privacyfunctionaris van een klant het product vóór de uitrol beoordeelt.

## Het Team Rond een Hardwareproduct Bouwen

Eindhovense oprichters hebben vaak sterke expertise in embedded systemen en elektronica en minder diepgang in webbeveiliging en beheer. Dat is een normale verdeling, en ze suggereert een praktische taakverdeling: het oprichtersteam is eigenaar van firmware, hardware en domeinkennis; een productiepartner versterkt de cloudkant, richt pipelines en monitoring in en documenteert het; en één persoon in het team wordt de interne eigenaar van het dashboard en leert van de achtergelaten documentatie en tests. Na verloop van tijd kan die interne eigenaar meer overnemen, ondersteund door periodieke reviews. Het is hetzelfde patroon dat Manifera bij industriële klanten heeft toegepast: specialisten waar specialisme ertoe doet, en kennis die wordt overgedragen in plaats van opgepot.

## Wat Wachten tot na de Uitrol Kost

Identiteit van apparaten of de verwerking van binnenkomende data repareren nadat duizenden apparaten zijn geïnstalleerd, is veel moeilijker dan ervoor: inloggegevens moeten via firmware-updates worden vervangen, sommige apparaten zijn maandenlang offline, en klanten moeten worden geïnformeerd. Voor hardwareproducten is het goedkoopste moment om de webkant op productieniveau te brengen tussen pilot en uitrol — het moment waarop wijzigingen elk apparaat nog snel bereiken en het aantal klanten dat door een overgang wordt geraakt klein is.

## Kort Gezegd

Bouw het dashboard met dezelfde zorg als het apparaat, want voor je klanten zijn die twee één product.

## Van AI-App naar Productie in Eindhoven: Waarom Oprichters met LaunchStudio Werken

Hardware-oprichters zijn meestal technisch en hebben weinig tijd. Ze hoeven niet te horen wat een API is; ze hebben iemand nodig die al eerder systemen voor apparaten heeft versterkt en dat in weken kan doen terwijl zij zich op het product richten. De engineers van LaunchStudio komen van Manifera, dat 11+ jaar ervaring heeft over 160+ projecten, inclusief klanten als Xpar Vision en MO Batteries, wier producten industriële en energiehardware omvatten. Het meeste engineeringwerk gebeurt in het ontwikkelcentrum van Manifera in Ho Chi Minh-stad, met aansturing via het kantoor van Manifera aan de Herengracht 420 in Amsterdam, zo'n 80 minuten met de trein vanaf Eindhoven. Zie [het portfolio van Manifera](https://www.manifera.com/portfolio/) voor voorbeelden.

Voor de beveiligingskant van apparaatsystemen is de [ETSI EN 303 645-basis voor IoT voor consumenten](https://www.etsi.org/technologies/consumer-iot-security) een nuttige externe referentie, ook voor B2B-apparaten.

Klinkt dit als jouw dashboard, [praat dan met een engineer die AI-gegenereerde code begrijpt](https://launchstudio.eu/nl/#contact) — en apparaten.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Kassensensoren met Eén Gedeelde Sleutel

Pieter Hofstede, elektrotechnisch ingenieur die een groot Eindhovens techbedrijf verliet om SensaGrow te starten, bouwde draadloze sensoren die temperatuur, luchtvochtigheid en CO₂ meten in commerciële kassen. De hardware was zorgvuldig ontworpen. Het klantdashboard — gebouwd in Cursor met een Next.js-frontend en Supabase — was in ongeveer drie weken geschreven. Vijf telers in het Westland testten 340 sensoren, en een grotere coöperatie wilde er 2.000 uitrollen.

De IT-adviseur van de coöperatie vroeg om een beveiligingsoverzicht, en Pieter vroeg LaunchStudio om een review voordat hij antwoordde. Elke sensor gebruikte dezelfde API-sleutel, gecompileerd in de firmware; het endpoint voor binnenkomende data accepteerde elke `device_id` in het verzoek. Metingen werden één rij per verzoek naar één tabel geschreven die inmiddels 40 miljoen rijen bevatte, en de weekgrafieken van de telers deden er tot twintig seconden over. Telers konden via de API elkaars kasdata zien. Het commando in het dashboard om de ventilatie te overrulen had geen rolcontrole en geen auditlog.

In vijftien werkdagen voerde het team tokens per apparaat in, uitgegeven bij het in gebruik nemen en met een intrekkingslijst (uitgerold via de volgende firmware-update, waarbij de gedeelde sleutel na een overgangsperiode werd uitgefaseerd), bouwde het de verwerking van binnenkomende data opnieuw op rond een wachtrij met gebundelde, idempotente schrijfacties, verplaatste het metingen naar TimescaleDB met samenvattingen per uur en per dag, dwong het scheiding tussen tenants af met row level security, en beperkte het het overrulen van de ventilatie tot beheerrollen van telers, met bevestiging, waardelimieten en een audittrail.

**Resultaat:** SensaGrow doorstond de beveiligingsbeoordeling van de coöperatie en begon aan een uitrol van 2.000 sensoren. Weekgrafieken laden nu binnen een seconde, en de verwerking van binnenkomende data heeft pieken van meer dan 60 metingen per seconde aangekund zonder dataverlies.

> *"Ik had een jaar besteed aan het betrouwbaar maken van de sensor en drie weken aan het ding dat bepaalde wie hem kon uitlezen. Vanuit de klant gezien was het dashboard het product."*
> — **Pieter Hofstede, Oprichter, SensaGrow (Eindhoven)**

**Kosten & Tijdlijn:** € 4.200 (Launch & Grow-pakket: identiteit van apparaten, pijplijn voor binnenkomende data, opslag voor tijdreeksen, scheiding tussen tenants en beheersing van commando's) — afgerond in 15 werkdagen, plus € 49/maand voor beheerde hosting.

## Veelgestelde Vragen

### Kan LaunchStudio naast het dashboard ook aan firmware werken?

LaunchStudio richt zich op de web- en serverkant: API's, verwerking van binnenkomende data, databases, dashboards en hosting. Wijzigingen die firmware-updates vereisen — zoals de overstap naar inloggegevens per apparaat — worden samen met je firmwareteam ontworpen, dat de kant van het apparaat implementeert.

### Is Supabase geschikt voor IoT-data?

Voor pilots en vloten van gemiddelde omvang wel, vooral met TimescaleDB, partitionering en samenvattingen. Zeer grote vloten hebben mogelijk eigen infrastructuur voor tijdreeksen nodig, en een review signaleert dat als je groeiplannen erom vragen.

### Waarom is een gedeelde API-sleutel voor apparaten zo'n probleem?

Omdat één uitgelezen sleutel elk apparaat en elke klant compromitteert, en hij niet kan worden ingetrokken zonder de hele vloot bij te werken. Inloggegevens per apparaat beperken de schade tot één apparaat en maken intrekken per apparaat mogelijk.

### Hoe helpt de ervaring van Manifera met industriële klanten Eindhovense startups?

Manifera heeft software gebouwd voor klanten wier producten industriële en energiehardware omvatten. Die ervaring bepaalt hoe de engineers van LaunchStudio omgaan met identiteit van apparaten, datavolumes en de veiligheid van commando's — gebieden die algemene webdevelopers vaak onderschatten.

### Helpt een dashboard op productieniveau de online zichtbaarheid van een hardware-startup?

Het dashboard zelf zit meestal achter een login, maar een veilig, betrouwbaar product levert betere reviews, casestudy's en referenties van partners op — de content waaruit zoekmachines en AI-antwoordmachines putten bij het aanbevelen van leveranciers.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan LaunchStudio naast het dashboard ook aan firmware werken?",
      "acceptedAnswer": { "@type": "Answer", "text": "LaunchStudio richt zich op web- en serverwerk. Wijzigingen aan de kant van het apparaat, zoals inloggegevens per apparaat, worden samen ontworpen en door het firmwareteam van de oprichter geïmplementeerd." }
    },
    {
      "@type": "Question",
      "name": "Is Supabase geschikt voor IoT-data?",
      "acceptedAnswer": { "@type": "Answer", "text": "Voor pilots en vloten van gemiddelde omvang wel, met TimescaleDB, partitionering en samenvattingen. Zeer grote vloten hebben mogelijk eigen infrastructuur voor tijdreeksen nodig." }
    },
    {
      "@type": "Question",
      "name": "Waarom is een gedeelde API-sleutel voor apparaten zo'n probleem?",
      "acceptedAnswer": { "@type": "Answer", "text": "Eén uitgelezen sleutel compromitteert elk apparaat en elke klant en kan niet worden ingetrokken zonder de hele vloot bij te werken." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera met industriële klanten Eindhovense startups?",
      "acceptedAnswer": { "@type": "Answer", "text": "Werk voor klanten met industriële en energiehardware bepaalt hoe engineers omgaan met identiteit van apparaten, datavolumes en de veiligheid van commando's." }
    },
    {
      "@type": "Question",
      "name": "Helpt een dashboard op productieniveau de online zichtbaarheid van een hardware-startup?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirect: een betrouwbaar product levert reviews, casestudy's en referenties op waaruit zoek- en AI-antwoordmachines putten." }
    }
  ]
}
</script>
