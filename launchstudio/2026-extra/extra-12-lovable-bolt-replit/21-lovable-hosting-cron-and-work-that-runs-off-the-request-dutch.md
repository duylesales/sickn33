---
Titel: "Lovable Hosting: Cron en Werk Dat Buiten het Verzoek Draait"
Trefwoorden: lovable hosting, cronjobs, geplande taken, pg_cron, taakmonitoring, heartbeat-meldingen, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Lovable Hosting: Cron en Werk Dat Buiten het Verzoek Draait

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting: Cron en Werk Dat Buiten het Verzoek Draait",
  "description": "Gepland werk in een door AI gebouwde app faalt stil, omdat er niets verschijnt als er niets draait. Waar u cron laat draaien, waarom tijdzones herinneringen breken, en de heartbeat die u vertelt dat het is gestopt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-hosting-cron-and-work-that-runs-off-the-request" }
}
</script>

Elke mislukking in een product kondigt zichzelf aan, behalve deze. Een kapotte pagina geeft een foutmelding. Een mislukte betaling levert een klacht op. Een geplande taak die stopt met draaien, levert helemaal niets op - geen fout, geen melding, geen supportticket - omdat wat ze had moeten maken gewoon niet verschijnt, en niemand mist iets wat hij nooit heeft gezien.

Herinneringen gaan niet meer de deur uit. De nachtelijke export komt niet meer binnen. Abonnementen worden niet meer gecontroleerd. En de mediane tijd tot ontdekking wordt, in de producten die wij hebben bekeken, in weken gemeten.

De techniek hier is triviaal. De discipline niet, en die komt neer op één idee: er moet iets klagen als de taak niet draait.

## Waar Gepland Werk Kan Draaien

Vier opties, en voor een Lovable- en Supabase-product dekken de eerste twee bijna alles.

**De eigen planner van Supabase** voert volgens schema SQL uit of roept een functie aan, binnen de database, zonder extra dienst. Ideaal voor dataonderhoud, opruimen, verversen van aggregaties en werk in de rij zetten.

**De cron van uw hostingplatform**, die volgens schema een endpoint in uw applicatie aanroept. Ideaal wanneer het werk de code van uw applicatie nodig heeft - e-mails versturen, providers aanroepen, documenten genereren.

**Een externe planningsdienst** die een URL aanroept, met als voordeel dat hij onafhankelijk is van uw platform en u vertelt wanneer een aanroep mislukt.

**Een langlopende worker** op een kleine server, wat alleen het juiste antwoord is wanneer het volume dat rechtvaardigt.

Wat u ook kiest, één regel geldt: de geplande taak moet werk in de rij zetten in plaats van het uit te voeren. Een schema dat taken aanmaakt, is snel, kan niet met zichzelf overlappen, en laat een registratie achter. Een schema dat vier minuten bezig is met e-mails versturen, wordt uiteindelijk halverwege afgekapt door een time-out van het platform, nadat een onbekend deel ervan is verstuurd.

## Bescherm het Endpoint

Cron die werkt door een URL aan te roepen, creëert een URL die iedereen kan aanroepen.

Verstuurt dat endpoint facturen, dan kan een buitenstaander die het vindt ze herhaaldelijk versturen. Herberekent het saldi, dan kan hij het duizend keer uitvoeren. En URL's worden gevonden - in logs, in de browsergeschiedenis, in een repository, door scannen.

De bescherming is een gedeeld geheim in een header, gecontroleerd voordat er iets gebeurt, waarbij het verzoek anders wordt geweigerd. Cronmechanismen van het platform leveren er vaak een; doet het uwe dat niet, verzin er dan een. Het zijn drie regels code, en het alternatief is een endpoint met echte macht en zonder deur.

Maak de taak, nu u er toch bent, idempotent om dezelfde reden als elk achtergrondwerk: een nieuwe poging, een dubbele aanroep of een per ongeluk handmatige aanroep mag niet van iets twee exemplaren opleveren.

## Tijdzones Breken Juist Herinneringen

Schema's draaien in UTC tenzij anders aangegeven, en Nederland loopt afhankelijk van het seizoen één of twee uur voor.

Een taak die is ingesteld op 08:00 gaat in de zomer om 09:00 Nederlandse tijd de deur uit en in de winter om 10:00, wat voor een herinnering die zegt "uw afspraak is om negen uur" het verschil is tussen nuttig en nutteloos. Twee keer per jaar, op een zondag in maart en oktober, verschuift elk schema in uw product een uur ten opzichte van uw klanten.

Twee gewoontes vangen het op. Plan bewust in UTC en reken om, in plaats van te hopen dat de standaard van het platform bij uw gebruikers past. En draai voor alles waarbij het lokale uur ertoe doet - herinneringen, dagelijkse samenvattingen, meldingen tijdens kantooruren - de taak vaker dan nodig en bepaal binnen de taak welke ontvangers aan de beurt zijn, op basis van hun eigen tijdzone.

De tweede gewoonte is wat een product laat werken voor een klant in een ander land zonder tweede implementatie, en het kost niets om haar vroeg over te nemen.

## Overlap, Time-outs en de Taak Die Langer Duurt dan Haar Interval

Een taak die elke vijf minuten is gepland en zes minuten gaat duren, draait uiteindelijk twee keer tegelijk, en de mislukking die volgt hangt af van wat ze doet - dubbele e-mails, dubbel getelde rijen, een deadlock.

Voorkom het met een lock die de taak aan het begin neemt en aan het eind vrijgeeft, zodat een tweede aanroep hem ziet en stopt. In Postgres is dit één aanroep van een advisory lock; in applicatiecode is het een rij in een tabel.

Time-outs verdienen dezelfde aandacht. Door het platform aangeroepen cron-endpoints hebben meestal een harde limiet van seconden tot een paar minuten. Een taak die meegroeit met uw data, overschrijdt die limiet op een dag, stil, midden in haar werk. In de rij zetten in plaats van uitvoeren lost dit per definitie op, en daarom is het de aanbeveling.

## De Heartbeat Die Stilte Hoorbaar Maakt

Dit is het deel om te bouwen, ook als u verder niets bouwt.

Elke geplande taak legt vast dat ze draaide en of ze slaagde. Eén controle, die zelf volgens schema draait, kijkt naar die registraties en slaat alarm als iets wat werd verwacht niet binnen de termijn is gebeurd.

De omkering doet ertoe: u slaat geen alarm bij mislukking, die zou u toch zien. U slaat alarm bij afwezigheid, en dat is de faalwijze die werkelijk voorkomt.

Een tabel met de taaknaam, de laatste geslaagde run en een verwacht interval is genoeg. Dat geldt ook voor een externe monitoringdienst waarbij elke taak een unieke URL aanroept wanneer ze klaar is en de dienst u waarschuwt als een aanroep uitblijft - met als voordeel dat het nog werkt als uw hele platform plat ligt, en gratis is bij de volumes die een klein product nodig heeft.

## Schrijf Op Wat Er Draait

Niemand kan beoordelen wat hij niet kan zien, en gepland werk is van nature onzichtbaar: niets in de interface van uw applicatie noemt het.

Een bestand in de repository met elke taak, het schema, wat ze doet, wat ze raakt en wat er moet gebeuren als ze faalt, is tien minuten schrijfwerk dat zichzelf terugbetaalt de eerste keer dat iemand anders uw product moet begrijpen - of de eerste keer dat u er na een maand aan iets anders naar terugkeert.

Dezelfde lijst maakt een jaarlijkse review mogelijk. Taken stapelen zich op: een opruimtaak voor een tabel die niet meer bestaat, een samenvattingsmail die niemand leest, een synchronisatie met een dienst die u niet meer gebruikt. Elke taak draait voor altijd, verbruikt middelen en faalt af en toe, totdat iemand er bewust naar kijkt.

## Maak Elke Taak met de Hand Uitvoerbaar

Een geplande taak die alleen door haar schema kan worden gestart, is een taak die u niet kunt onderzoeken, testen of herstellen.

Geef elke taak een manier om op verzoek te draaien - een beheeractie, een commando, een beveiligd endpoint dat u kunt aanroepen - met twee parameters die het ondersteunen waard zijn. Een proefrun die meldt wat ze zou doen zonder het te doen, waarmee u een wijziging veilig controleert. En een datum of periode, zodat een taak die dinsdag miste voor dinsdag kan worden uitgevoerd in plaats van voor vandaag.

Die tweede parameter is wat een gemist tijdvak verandert van een incident in een taak. De herinneringstaak die op de 14e faalde, kan voor de 14e worden uitgevoerd; het rapport dat vorige maand niet werd gegenereerd, kan voor vorige maand worden gegenereerd. Zonder dat is het enige herstel wachten op morgen en het gat accepteren, wat precies is wat er in de meeste kleine producten gebeurt omdat niemand het alternatief bouwde.

De verwante gewoonte: laat taken werken over een genoemde periode in plaats van over "nu". Een taak die vraagt om records die sinds de laatste geslaagde run zijn aangemaakt, is bestand tegen te laat komen, tegen overgeslagen worden, en tegen twee keer draaien. Een taak die vraagt om records die vandaag zijn aangemaakt, verliest alles op het moment dat ze vandaag niet draait - precies de dag dat ze robuust had moeten zijn.

Nog een reden om het te bouwen: het eerste wat iemand doet wanneer een geplande taak zich misdraagt, is proberen het te reproduceren, en een taak die alleen om vier uur 's nachts draait, is een taak die u om vier uur 's nachts debugt. Een handmatige trigger verandert dat in een gewone middag werk.

## Dit Inrichten

Voor een bestaand product kost dit doorgaans een halve tot een hele dag: elke geplande taak geïnventariseerd, elk omgezet naar werk in de rij zetten in plaats van uitvoeren, endpoints beschermd met een gedeeld geheim en idempotent gemaakt, schema's ingesteld in UTC met werk op lokaal uur aangestuurd door de tijdzone van de ontvanger, overlap voorkomen met locks, een runregistratie geschreven door elke taak, een melding op afwezigheid met verwachte intervallen, externe heartbeatmonitoring voor de kritieke taken, en de hele set gedocumenteerd in de repository.

LaunchStudio richt dit in als onderdeel van productieklaar maken, en binnen de managed regeling van €49 per maand komen de heartbeatmeldingen bij ons binnen in plaats van bij u. De engineers zijn van Manifera - elf jaar, 160+ projecten, vanaf de Herengracht 420 in Amsterdam en Ho Chi Minh-stad.

[Vraag ons wanneer uw nachtelijke taak voor het laatst draaide](https://launchstudio.eu/nl/#contact). De meeste oprichters kunnen het niet beantwoorden.

## Echt voorbeeld

### Elf Dagen Ontbrekende Herinneringen

Casper IJsselstein bouwde Afspraakherinnering met Lovable: afspraakherinneringen voor tandarts- en orthodontiepraktijken, de avond ervoor verstuurd per e-mail en sms, gebruikt door 38 praktijken met samen zo'n 1.900 afspraken per week.

De herinneringstaak draaide elke nacht op de cron van zijn hostingplatform. In maart veranderde een deploy een afhankelijkheid, de taak begon op haar eerste regel te falen, en het platform registreerde een mislukte aanroep in een logboek waar niemand naar keek.

Elf dagen later belde een praktijkmanager in Bergen op Zoom om te vragen of de herinneringen waren uitgezet, omdat hun no-showpercentage ongeveer was verdubbeld. Over 38 praktijken waren dat zo'n 3.000 herinneringen die nooit werden verstuurd en, volgens de eigen schattingen van de praktijken, meer dan 200 gemiste afspraken.

Twee werkdagen: de herinneringstaak omgezet van het werk zelf doen naar één taak per praktijk in de rij zetten, zodat een mislukking één praktijk raakt in plaats van alle, en een time-out de run niet halverwege kan afbreken; het cron-endpoint beschermd met een gedeeld geheim, nadat het eerder aanroepbaar was geweest voor iedereen die het pad kende; planning omgezet naar elk uur, met de tijdzone van de ontvanger en de openingstijden van de praktijk beoordeeld binnen de taak, ter vervanging van één UTC-run die sinds de klokwissel een uur te laat ging; een advisory lock om overlap te voorkomen; een runregistratie door elke taak; een melding op afwezigheid die afgaat wanneer de herinneringsrun niet binnen 26 uur succesvol is afgerond; externe heartbeatmonitoring zodat de melding ook werkt als het platform dat niet doet; en een document met alle zes geplande taken, waaruit bleek dat er twee al maanden niets nuttigs deden.

**Resultaat:** de faalwijze wordt nu binnen uren opgemerkt in plaats van weken. In het jaar daarna ging de afwezigheidsmelding drie keer af - twee keer bij echte mislukkingen die dezelfde ochtend werden opgevangen, één keer bij een platformincident - en geen enkele praktijk heeft een gat ontdekt voordat Casper dat deed.

> *"Het faalde elf nachten lang en mijn product zag er de hele tijd volkomen gezond uit. Op geen enkel scherm was iets kapot. Wat ontbrak, was iets wat niemand ziet."*
> - **Casper IJsselstein, Oprichter, Afspraakherinnering (Roosendaal)**

**Kosten & Doorlooptijd:** €2.100 (omzetten van taken naar wachtrijtaken, authenticatie van endpoints, tijdzonebewuste planning, locks tegen overlap, runregistraties, meldingen op afwezigheid met externe heartbeat, documentatie en opruimen van taken) - afgerond in 2 werkdagen.

## Veelgestelde vragen

### Waarom falen geplande taken zonder dat iemand het merkt?

Omdat hun succes iets oplevert en hun mislukking niets. Er bereikt geen fout een gebruiker, dus het enige signaal is afwezigheid - en daarom moet de melding op afwezigheid zitten in plaats van op mislukking.

### Moet een cronjob het werk doen of het in de rij zetten?

In de rij zetten. Een schema dat in de rij zet, is in milliseconden klaar, kan niet overlappen, laat een registratie achter en is immuun voor time-outs van het platform die lange runs anders halveren.

### Hoe voorkom ik dat vreemden mijn cron-endpoint aanroepen?

Vereis een gedeeld geheim in een header en weiger al het andere voordat er werk wordt gedaan. Een gepland endpoint is een URL met echte macht, en die wordt uiteindelijk gevonden.

### Waarom gaan mijn herinneringen in de winter een uur te laat?

Schema's draaien in UTC en Nederland schuift tussen één en twee uur voor. Draai de taak vaker en bepaal binnen de taak wie aan de beurt is, op basis van de lokale tijd van elke ontvanger.

### Wat is de minimale monitoring die het waard is?

Een registratie van de laatste geslaagde run van elke taak en een melding wanneer er een niet binnen de verwachte termijn is afgerond. Een externe heartbeatdienst dekt daarnaast het geval dat uw eigen platform plat ligt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom falen geplande taken onopgemerkt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Mislukking levert niets op in plaats van een foutmelding, dus niemand ziet het. Meld op afwezigheid - een taak die niet heeft gedraaid - in plaats van op mislukking."
      }
    },
    {
      "@type": "Question",
      "name": "Moet een cronjob het werk uitvoeren of in de rij zetten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In de rij zetten. Het schema is direct klaar, kan niet met zichzelf overlappen, laat een registratie achter, en is immuun voor time-outs van het platform."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe bescherm ik een cron-endpoint?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vereis een gedeeld geheim in een header en weiger al het andere voordat er werk wordt gedaan. De URL wordt uiteindelijk ontdekt."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom verschuiven geplande herinneringen in de winter een uur?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Schema's draaien in UTC terwijl Nederland tussen één en twee uur voor loopt. Draai vaker en selecteer ontvangers op hun eigen lokale tijd."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de minimale monitoring voor gepland werk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een registratie van de laatste geslaagde run per taak plus een melding wanneer er een haar termijn mist, bij voorkeur met een externe heartbeat die platformstoringen overleeft."
      }
    }
  ]
}
</script>
