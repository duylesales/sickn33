---
Titel: "AI-Appbeveiliging: Back-ups Die een Aanvaller Niet Kan Verwijderen"
Trefwoorden: ai-appbeveiliging, back-ups, ransomware, onveranderbare opslag, hersteltests, point-in-time recovery, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische solo-oprichter / Indie hacker
---

# AI-Appbeveiliging: Back-ups Die een Aanvaller Niet Kan Verwijderen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-Appbeveiliging: Back-ups Die een Aanvaller Niet Kan Verwijderen",
  "description": "Een back-up die bereikbaar is met de inloggegevens waarmee uw applicatie draait, is geen back-up tegen een compromittering. Gescheiden beheer, onveranderbaarheid, wat u naast de database moet meenemen, en bewijzen dat een herstel werkt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-24",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-app-security-backups-an-attacker-cannot-delete" }
}
</script>

De meeste oprichters denken bij back-ups aan ongelukken: een slechte migratie, een verkeerde verwijdering, een hardwarestoring. Die zijn echt, en de automatische back-ups van het platform vangen ze meestal goed op.

Er is een tweede scenario dat de automatische opzet niet opvangt, en het is inmiddels de vaakste oorzaak van catastrofaal dataverlies bij kleine bedrijven. Iemand krijgt uw inloggegevens in handen. Hij neemt niet alleen de data mee — hij verwijdert haar, en daarna verwijdert hij de back-ups, omdat hetzelfde account waarmee uw product draait bij beide kan.

Het onderscheid is eenvoudig te formuleren. Een back-up die kan worden vernietigd door wie uw applicatie compromitteert, is een back-up tegen fouten, niet tegen aanvallen.

## Gescheiden Beheer, Niet Alleen Gescheiden Opslag

De eigenschap die ertoe doet, is niet de locatie. Het is wie haar kan verwijderen.

Een kopie in een andere regio van hetzelfde account, te verwijderen met dezelfde inloggegevens, is bescherming tegen een regionale storing en verder niets. Een kopie in een apart account of bij een andere provider, met eigen inloggegevens die uw applicatie niet heeft, is bescherming tegen compromittering.

Voor een klein product is dit niet ingewikkeld: een geplande export naar opslag in een ander account, waarbij de schrijfsleutel objecten kan aanmaken maar niet kan verwijderen of overschrijven. De applicatie kan aan het archief toevoegen en verder niets.

Die eigenschap van alleen schrijven is de hele truc, en ze is bij elke grote objectopslagdienst beschikbaar als rechtenbeleid.

## Onveranderbaarheid Maakt Het Zeker

Nog een stap verder, en het waard voor alles waarvan u niet zou kunnen herstellen: object lock, of iets vergelijkbaars, dat verwijdering voor een vastgestelde bewaartermijn voorkomt, ongeacht de rechten.

Staat het aan, dan kan een back-up die vandaag wordt geschreven dertig dagen lang door niemand worden verwijderd — niet door een aanvaller met volledige inloggegevens, niet door een verkeerd script, niet door u. Dat is af en toe onhandig, en precies de bedoeling.

Combineer de twee ideeën met een bewaarregel die dagelijkse kopieën een maand bewaart, wekelijkse een kwartaal, en maandelijkse een jaar, en u hebt een opzet die zowel een compromittering overleeft als het tragere probleem van corruptie die pas weken later wordt opgemerkt.

## Maak Meer Back-ups dan Alleen de Database

De database is waar de aandacht naartoe gaat, en ze is niet het hele product. Vier andere dingen doen ertoe.

**Geüploade bestanden.** Voor veel producten zijn de documenten waardevoller dan de rijen, en objectopslag heeft vaak helemaal geen automatische back-up — een verwijderd object is gewoon weg.

**Configuratie.** Omgevingsvariabelen, providerinstellingen, DNS-records, webhook-endpoints, geplande taken. Niet groot, en het verschil tussen een herstel van uren en een van dagen.

**Het schema, in een vorm die u kunt toepassen.** Uw migratiebestanden in een repository, en daarom horen ze daar.

**De lijst van waar uw product van afhangt**, zodat een herbouw niet begint met een inventarisatie.

Schrijf dit op als herstelplan. Wie onder druk een herstel uitvoert — heel goed mogelijk uzelf, moe — moet instructies volgen in plaats van zich dingen te herinneren.

## Een Back-up Die U Niet Hebt Teruggezet Is een Hypothese

De meest voorkomende bevinding wanneer een herstel voor het eerst wordt geprobeerd, is dat het niet werkt: de export was onvolledig, het formaat is onleesbaar, een vereiste extensie ontbreekt, het bestand is sinds maart nul bytes omdat er een sleutel veranderde en niets het controleerde.

Test het dus. Zet terug naar een kladomgeving, laat de applicatie ertegen draaien, controleer dat recente records bestaan en dat bestanden waarnaar de database verwijst er werkelijk zijn. Meet de tijd van het geheel.

Twee keer per jaar is voor de meeste producten genoeg, plus één keer na elke grote wijziging in uw infrastructuur. Schrijf de datum en de duur op. Dat getal — hoe lang een volledig herstel duurt — is degene waar uw zakelijke klanten naar vragen, en degene die niemand kan beantwoorden zonder het te hebben gedaan.

## Ken Uw Twee Getallen

Twee vragen bepalen wat uw opzet moet bereiken, en ze beantwoorden verandert back-ups van een vaag goed voornemen in een specificatie.

**Hoeveel data kunt u zich veroorloven te verliezen?** Draaien back-ups elke nacht, dan is het antwoord tot een dag. Voor een product waarin klanten een dag werk in uw applicatie doen, is dat meestal te veel, en point-in-time recovery — beschikbaar op de meeste beheerde databaseplannen — brengt het terug tot minuten.

**Hoe lang kunt u plat liggen?** Een herstel van een kleine database kost minuten; een herstel inclusief het reconstrueren van configuratie en het opnieuw uploaden van bestanden kan een dag kosten. Moet het antwoord twee uur zijn, dan bepaalt dat wat u vooraf voorbereidt.

Geen van beide getallen hoeft indrukwekkend te zijn. Het moet bekend zijn, genoemd, en consistent met wat u klanten vertelt.

## Back-ups Zijn Ook Persoonsgegevens

Een archief van uw database is een kopie van alles wat uw klanten u gaven, en het erft elke verplichting die het origineel heeft.

Drie gevolgen waar oprichters op onhandige momenten tegenaan lopen.

**Versleuteling.** Back-ups moeten versleuteld zijn in opslag en tijdens transport, wat de meeste diensten standaard doen — maar controleer het in plaats van het aan te nemen, vooral bij exports die u zelf naar een bucket schreef. De sleutel mag niet naast de data staan.

**Toegang.** Wie een back-up kan lezen, kan elk record in uw product lezen, zonder een van de controles die uw applicatie afdwingt. Die toegangslijst moet korter zijn dan uw lijst voor productietoegang, en ze moet worden beoordeeld.

**Verwijdering.** Oefent een klant zijn recht op verwijdering uit, dan blijft zijn data in back-ups staan. Het geaccepteerde standpunt is dat back-ups haar voor een vastgestelde bewaartermijn mogen bevatten, mits u haar niet in productie terugzet zonder de verwijdering opnieuw toe te passen, en mits de termijn is genoemd. Wat niet verdedigbaar is, is onbeperkt bewaren zonder beleid — en dat is wat een bucket met exports van drie jaar terug in feite is.

Schrijf dus de bewaarregel op en dwing haar automatisch af, leg vast wat uw herstelprocedure doet met verwijderverzoeken, en noem de bewaartermijn van back-ups in uw privacydocumentatie. Het is een korte alinea, en het is het verschil tussen een weloverwogen standpunt en een vergissing.

## De Mislukkingen Die Back-ups Niet Dekken

Twee scenario's verslaan een verder goede opzet, en beide zijn even nadenken waard omdat de oplossing goedkoop is.

**Corruptie die u niet opmerkt.** Een fout schrijft drie weken lang verkeerde waarden. Elke nachtelijke back-up bewaart de verkeerde waarden getrouw, en tegen de tijd dat iemand het opmerkt, is de laatste schone kopie buiten de bewaartermijn gevallen. Dat is het argument voor een maandelijkse kopie die een jaar wordt bewaard: niet omdat u verwacht data van elf maanden oud nodig te hebben, maar omdat het moment van ontdekking soms ver ligt van het moment van schade.

**Verwijdering die doorwerkt.** Een cascadeverwijdering haalt de records van een klant weg samen met alles wat ernaar verwijst, en de back-up die een uur later wordt gemaakt, legt het resultaat vast. Point-in-time recovery helpt hier waar een nachtelijke momentopname dat niet doet, en dat is de belangrijkste reden om het aan te zetten.

Beide pleiten voor dezelfde gewoonte: houd het vermogen om verder terug te gaan dan nodig voelt, en kunnen één tabel of één account terugzetten in plaats van alleen de hele database. Een volledig herstel om de records van één klant terug te krijgen, betekent het werk van iedereen anders sinds de back-up weggooien, wat zelden een acceptabele ruil is en precies de positie waarin oprichters terechtkomen als het enige beschikbare middel alles-of-niets is.

Eén keer een gedeeltelijk herstel oefenen — één tabel, naar een kladdatabase, en dan de rijen terugkopiëren — kost een uur en verandert het ergste soort incident in een gewone reparatie.

## Dit Inrichten

Voor een bestaand product kost dit doorgaans één dag: platformback-ups bevestigd en hun bewaartermijn begrepen, een onafhankelijke kopie geschreven naar opslag in een apart account met een schrijfsleutel zonder verwijderrecht die uw applicatie niet heeft, object lock of vergelijkbare onveranderbaarheid met een bewaarschema van dagelijkse, wekelijkse en maandelijkse kopieën, geüploade bestanden meegenomen in de back-up, configuratie en DNS vastgelegd, migraties in de repository, een geschreven herstelplan, een geplande hersteltest met de duur vastgelegd, monitoring die meldt wanneer een back-up uitblijft of onverwacht klein is, en doelen voor herstelpunt en hersteltijd genoemd.

LaunchStudio richt dit in als onderdeel van productieklaar maken en voert de hersteltests uit binnen de managed regeling van €49 per maand. De engineers zijn van Manifera — elf jaar, 160+ projecten, en herstelprocedures voor klanten als Vodafone, TNO en CFLW.

[Vraag ons wanneer u voor het laatst een back-up hebt teruggezet](https://launchstudio.eu/nl/#contact). Het antwoord is meestal nooit, en dat is de bevinding.

## Echt voorbeeld

### De Back-ups Stonden in Hetzelfde Account

Youri Landman bouwde Praktijkdossier in Lovable: cliëntdossiers en sessienotities voor psychologen- en coachingpraktijken, 64 behandelaars met zo'n 3.200 cliënten.

Een behandelaar hergebruikte een wachtwoord dat in een ongerelateerd datalek voorkwam. De aanvaller logde in, vond het praktijkbeheer, en — omdat Youri praktijkbeheerders een exportfunctie met brede databasetoegang had gegeven — haalde een aanzienlijke hoeveelheid data op voordat hij records in de hele praktijk verwijderde.

Zoveel was te herstellen. Wat de avond lang maakte, was dat Youri's enige extra back-up een nachtelijke export was die naar een bucket in hetzelfde cloudaccount als de applicatie werd geschreven, met dezelfde inloggegevens, met een lifecycleregel en zonder bescherming. Ze was in dit geval niet verwijderd, maar ze was bereikbaar, en een iets grondigere aanvaller had haar weggehaald.

Het herstel zelf duurde vervolgens elf uur, omdat de export de database bevatte en verder niets. Bijlagen bij sessienotities — het gevoeligste en minst vervangbare deel van het product — stonden in een opslagbucket waarvan nooit een back-up was gemaakt, en 340 ervan waren weg.

Drie werkdagen: een onafhankelijke back-up naar een account bij een andere provider met een schrijfsleutel zonder verwijderrecht die de applicatie niet heeft; object lock met 35 dagen onveranderbaarheid en een bewaarschema van dagelijks voor een maand, wekelijks voor een kwartaal en maandelijks voor een jaar; geüploade sessiebijlagen meegenomen, waarvan nooit een back-up was gemaakt; point-in-time recovery ingeschakeld op de database, waardoor het mogelijke verlies terugging van 24 uur naar vijf minuten; configuratie, DNS en webhook-endpoints vastgelegd in de repository; een geschreven herstelplan met genummerde stappen; een hersteltest uitgevoerd en getimed op 47 minuten voor het volledige product; monitoring die meldt als een back-up uitblijft of meer dan 20 procent kleiner is dan de vorige; de exportfunctie ingeperkt zodat praktijkbeheerders alleen hun eigen praktijk kunnen exporteren in plaats van breed te bevragen; en tweestapsverificatie verplicht gesteld voor beheerdersaccounts.

**Resultaat:** 340 bijlagen waren niet te herstellen en de betrokken cliënten werden geïnformeerd, wat Youri de slechtste professionele ervaring van zijn leven noemt. De opzet sindsdien had het voorkomen: een reconstructie van elf uur werd een herstel van 47 minuten, en de back-ups staan nu op een plek waar zijn eigen inloggegevens niet bij kunnen.

> *"Ik had back-ups. Ik had ze in hetzelfde account, met dezelfde sleutels, en ik had er nooit één teruggezet. Wat ik eigenlijk had, was een bestand waarvan ik hoopte dat het nuttig was."*
> — **Youri Landman, Oprichter, Praktijkdossier (Utrecht)**

**Kosten & Doorlooptijd:** €3.300 (onafhankelijke onveranderbare back-up met schrijfsleutel zonder verwijderrecht, bewaarschema, back-up van bestanden, point-in-time recovery, vastleggen van configuratie, herstelplan, getimede hersteltest, monitoring van back-ups, inperken van export, tweestapsverificatie voor beheerders) — afgerond in 3 werkdagen.

## Veelgestelde vragen

### Zijn de automatische back-ups van mijn platform genoeg?

Voor ongelukken meestal wel. Voor een compromittering niet — kunnen de inloggegevens waarmee uw applicatie draait ook de back-ups verwijderen, dan neemt een aanvaller die de ene neemt ook de andere.

### Wat maakt een back-up veilig voor een aanvaller?

Gescheiden beheer: een ander account met een sleutel die kan schrijven maar niet kan verwijderen of overschrijven, bij voorkeur met object lock, zodat verwijderen tijdens de bewaartermijn onmogelijk is.

### Wat wordt vergeten bij back-ups?

Geüploade bestanden, die vaak helemaal geen automatische back-up hebben, plus configuratie, DNS-records, webhook-endpoints en geplande taken. De database alleen levert zelden een werkend product op.

### Hoe vaak moet ik een herstel testen?

Twee keer per jaar en na elke wijziging in de infrastructuur. Leg de duur vast — dat getal is waar klanten naar vragen en wat u niet kunt schatten zonder het te doen.

### Wat zijn doelen voor herstelpunt en hersteltijd?

Hoeveel data u zich kunt veroorloven te verliezen, en hoe lang u plat kunt liggen. Nachtelijke back-ups betekenen tot een dag verlies; point-in-time recovery brengt dat terug tot minuten.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Zijn automatische platformback-ups voldoende?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor ongelukken wel; voor een compromittering niet. Kunnen de inloggegevens van uw applicatie de back-ups verwijderen, dan kan een aanvaller die ze heeft beide verwijderen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat maakt een back-up bestand tegen een aanvaller?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Gescheiden beheer — een ander account, een schrijfsleutel die uw applicatie niet heeft, en object lock die verwijderen tijdens de bewaartermijn voorkomt."
      }
    },
    {
      "@type": "Question",
      "name": "Wat wordt meestal weggelaten uit back-ups?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Geüploade bestanden, die vaak helemaal geen back-up hebben, plus configuratie, DNS, webhook-endpoints en geplande taken."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe vaak moet een herstel worden getest?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Twee keer per jaar en na wijzigingen in de infrastructuur, met de duur vastgelegd — dat getal is waar klanten naar vragen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat zijn doelen voor herstelpunt en hersteltijd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hoeveel data u kunt verliezen en hoe lang u plat kunt liggen. Nachtelijke back-ups riskeren een dag; point-in-time recovery brengt het terug tot minuten."
      }
    }
  ]
}
</script>
