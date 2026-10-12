---
Titel: "Lovable Hosting en Uptime: Wat een SLA je daadwerkelijk verplicht"
Trefwoorden: lovable hosting, ai app security, service level agreement saas, uptime meting, onderhoudsvenster planning, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Lovable Hosting en Uptime: Wat een SLA je daadwerkelijk verplicht

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting en Uptime: Wat een SLA je daadwerkelijk verplicht",
  "description": "Een zakelijke klant vraagt om 99,9% uptime. Wat dat percentage in minuten betekent, waarom externe afhankelijkheden je belofte begrenzen, hoe je eerlijk meet en wat je kunt bieden in plaats van een onhoudbare toezegging.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-30",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-hosting-uptime-and-what-an-sla-commits-you-to" }
}
</script>

De eis duikt vroeg of laat op in een conceptcontract, meestal van de eerste zakelijke klant die groot genoeg is om een formele inkoopprocedure te hanteren: *leverancier garandeert een beschikbaarheid van 99,9%*.

Veel oprichters zetten zonder blikken of blozen hun handtekening. Het is immers slechts één regel tussen veertig andere juridische bepalingen, het percentage klinkt als iets wat een professionele applicatie vanzelfsprekend hoort te halen, en ertegenin gaan voelt als het toegeven van technische zwakte. Maar wat je zojuist hebt ondertekend, is een meetbare juridische verplichting met gekoppelde boetes of ontbindingsrechten, op infrastructuur die je zelf niet beheert, gemeten op een wijze die niemand contractueel heeft vastgelegd.

Dat betekent niet dat je zo'n eis direct moet afwijzen. Het betekent dat je exact moet begrijpen wat dat getal in de praktijk inhoudt vóórdat je tekent, en dat je weet welk professioneel alternatief je kunt aanbieden als 99,9% technisch niet haalbaar is.

## Wat een Service Level Agreement (SLA) daadwerkelijk inhoudt

Een SLA bestaat uit twee onlosmakelijke delen, en het tweede deel is waar het om draait:

**Een beschikbaarheidstoezegging.** De dienst is gedurende een vastgesteld percentage van de tijd operationeel, gemeten volgens een overeengekomen meetmethode over een specifieke tijdsperiode (meestal per kalendermaand).

**Een compensatieregeling (remedy).** Wat de klant ontvangt als je die toezegging niet nakomt — doorgaans service credits (korting op de volgende factuur), in sommige gevallen het recht om het contract direct te ontbinden, en in slecht opgestelde contracten zelfs open claims voor gevolgschade.

Een overeenkomst met een percentage maar zónder omschreven sanctie is vaag in jouw voordeel totdat er een conflict ontstaat — waarna het in niemands voordeel vaag blijkt te zijn. Maar een overeenkomst waarin direct ontbindingsrecht is gekoppeld aan een cijfer dat je nog nooit proactief hebt gemonitord, is een enorm bedrijfsrisico dat je hebt geaccepteerd zonder daar een risicopremie voor te rekenen.

## Wat percentages betekenen in keiharde minuten

De percentages lijken op papier sprekend op elkaar, maar de realiteit is totaal anders:

**99% staat ongeveer 7 uur downtime per maand toe.** Zeer comfortabel en realistisch haalbaar voor vrijwel elk klein B2B SaaS-product.

**99,5% staat circa 3,5 uur downtime per maand toe.**

**99,9% — "three nines" — staat slechts circa 43 minuten downtime per maand toe.** Eén mislukte software-update, één tijdelijke storing bij je hostingprovider of een herstart van je database verbruikt dit budget al volledig.

**99,95% staat slechts ongeveer 22 minuten downtime per maand toe.** Dit vereist serieuze redundancy: geautomatiseerde failover, continue gezondheidscontroles en multi-region opzet.

**99,99% staat circa 4 minuten downtime per maand toe.** Dit is simpelweg onmogelijk voor een applicatie die draait in één datacenterregio met één database en een solo-oprichter met één telefoon.

Oprichters kiezen blindelings voor 99,9% omdat ze dat getal overal zien staan bij enterprise partijen. Maar voor een applicatie die door één persoon wordt beheerd op managed cloud-infrastructuur, is 99% of 99,5% eerlijk en realistisch. En een eerlijke toezegging die je waarmaakt, is commercieel honderd keer sterker dan een belofte die je in het tweede kwartaal al verbreekt.

## Jouw keten van afhankelijkheden begrenst je belofte

De rekenkundige wet die founders stelselmatig vergeten: beschikbaarheid telt niet op, maar vermenigvuldigt zich omlaag door je gehele technische keten.

Jouw webapplicatie is afhankelijk van je hostingplatform, je beheerde database, je authenticatieprovider, je betalingsprovider (zoals Stripe of Mollie) en je DNS-provider. Als elk van deze externe diensten op papier een uptime van 99,9% behaalt, is de gecombineerde beschikbaarheid van een systeem dat álle vijf nodig heeft om te functioneren wiskundig aanzienlijk lager dan die 99,9%.

Je kunt onmogelijk meer garanderen dan je zwakste toeleverancier levert, en je hebt nul invloed op hun servers. Bestudeer de officiële SLA's van je hosting- en databaseproviders vóórdat je toezeggingen doet aan klanten, en kijk vooral goed naar wat zij in hun eigen kleine lettertjes uitsluiten.

Daarom sluit een professioneel geformuleerde uptime-garantie altijd storingen bij derden, gepland onderhoud en problemen in de netwerken of browsers van de klant expliciet uit.

## Uptime eerlijk en objectief meten

Een contractuele belofte zonder vastgelegde meetmethode is een gegarandeerde ruzie zodra er iets hapert.

**Van waaruit meet je?** Gebruik een externe monitoringdienst die van buitenaf jouw URL bevraagt, niet een intern script op je eigen server dat over zichzelf rapporteert.

**Hoe vaak meet je?** Een controle om de zestig seconden levert een heel ander resultaat op dan een ping om de vijf minuten.

**Wat telt formeel als 'downtime'?** Telt alleen een volledige time-out mee, of ook een HTTP-respons die er vijftien seconden over doet? Een 500-foutpagina, of ook een pagina die wel laadt maar waarvan een belangrijk formulier faalt?

**Over welke periode?** Gangbaar is per kalendermaand, waarbij de teller aan het begin van elke maand weer op nul begint.

Voor een klein SaaS-product is het antwoord eenvoudig: installeer één betrouwbare externe uptime-monitor die elke minuut test, en gebruik de publieke statusgeschiedenis als het officiële bewijsstuk. Richt dit in vóórdat je ook maar één contract ondertekent. Een belofte die je niet kunt aantonen met data, kun je juridisch niet verdedigen — en je hebt die data voor je eigen gemoedsrust sowieso nodig.

## Wat je een klant kunt bieden in plaats van loze percentages

Een zakelijke klant die om 99,9% vraagt, zoekt meestal naar zekerheid en professionaliteit, niet per se naar die exacte formule. Meerdere alternatieven bieden die zekerheid veel eerlijker:

**Een realistisch percentage dat je daadwerkelijk haalt,** helder onderbouwd. 99,5% met een geverifieerd meetrapport straalt autoriteit en deskundigheid uit; 99,9% zonder enig meetinstrument oogt als het invullen van een loterijbriefje.

**Een reactietijdgarantie in plaats van een uptime-percentage.** "We reageren tijdens kantooruren binnen twee uur en starten direct met onderzoek bij incidenten die de beschikbaarheid raken." Dit is vaak exact wat de klant écht wil, en dit ligt wél binnen jouw directe controle.

**Duidelijke communicatieafspraken.** Een vast contactpersoon, een actuele statuspagina tijdens een storing en een heldere schriftelijke evaluatie (post-mortem) na afloop.

**Transparantie over je cloud-infrastructuur.** Noem expliciet welke providers je gebruikt en wat hún officiële SLA's zijn. Dat wekt oneindig veel meer vertrouwen dan een los cijfer.

**Geverifieerde herstelgaranties (RPO/RTO).** Hoe vaak er back-ups worden gemaakt en hoe snel een complete herstelprocedure (restore) verloopt, ondersteund door cijfers uit daadwerkelijke proeven.

Tijdens inkoopgesprekken wint een leverancier die bescheiden, bewezen garanties biedt het steevast van partijen die schermen met indrukwekkende getallen waar niets achter zit.

## Onderhoudsvensters (Maintenance Windows)

Als je een beschikbaarheidspercentage afspreekt, moet je gelijktijdig gepland onderhoud contractueel regelen. Anders telt elke software-update rechtstreeks mee als downtime.

Standaardpraktijk: een overeengekomen onderhoudsvenster — bijvoorbeeld op zondagochtend of buiten kantooruren — dat minimaal 48 uur van tevoren wordt aangekondigd, en waarbij werkzaamheden niet meetellen voor het uptime-percentage. Voor moderne webapplicaties is het nog beter om je deployment-proces zo in te richten dat er 'zero-downtime deployments' plaatsvinden, waardoor deze vraag überhaupt niet meer ter sprake hoeft te komen.

## Wat je doet als je de SLA toch een keer mist

Vroeg of laat gebeurt het onvermijdelijke: er treedt een flinke storing op. Wat je reputatie redt, is hoe je handelt:

Informeer de klant proactief vóórdat zij jou bellen. Lever direct de objectieve metingen van je monitoringtool aan. Keer de afgesproken vergoeding of creditfactuur direct uit zónder dat de klant daarom hoeft te smeken; een proactief verleende creditfactuur kost je een fractie van de goodwill die verloren gaat als je erover gaat discussiëren. Schrijf een beknopt verslag over wat er misging en welke preventieve maatregel je hebt genomen. En verwerk het incident eerlijk in je eigen statistieken in plaats van het stilzwijgend te wissen.

Klanten vergeven een technische storing moeiteloos. Wat ze nooit vergeven, is de ontdekking dat hun leverancier over zijn eigen uptime-cijfers heeft gelogen.

## Bouwen aan een betrouwbaarheid die je kunt waarmaken

Als je daadwerkelijk een hoge beschikbaarheid wilt leveren, is de benodigde techniek bekend: software-updates uitvoeren zonder downtime, een database met geautomatiseerde failover, geavanceerde health checks die functionele fouten signaleren in plaats van alleen een ping beantwoorden, directe alarmering via SMS of pushbericht bij uitval, een geteste rollback-procedure met één druk op de knop, en bereikbaarheid buiten kantooruren.

Elk van deze voorzieningen kost tijd en geld. De juiste vraag is dan ook niet hoe hoog het percentage kan worden, maar welke maatregelen bedrijfseconomisch gerechtvaardigd zijn voor jouw specifieke klantenbestand. Voor de meeste Nederlandse B2B-producten ligt de lat ruim onder de magische "vier negens".

## De technische fundamenten onder je beloftes leggen

Een contractuele garantie is slechts zoveel waard als de operationele techniek die eronder ligt. Daarom hoort deze discussie thuis bij je DevOps-inrichting en niet puur op de juridische afdeling.

LaunchStudio bouwt die solide basislaag: externe 24/7 uptime-monitoring met directe alerting naar een mens, gecentraliseerde foutopsporing (error tracking), een deployment-pipeline met een staging-omgeving en rollback met één commando zodat updates geen uitval veroorzaken, periodiek geteste back-ups met een gemeten hersteltijd, en een compleet infrastructuurdossier waarmee je elke inkoopvragenlijst direct met feiten beantwoordt. Met managed hosting vanaf €49 per maand kijkt er altijd iemand mee die de notificatie opvangt.

De gebruikersinterface die je in Lovable hebt gebouwd blijft onaangeroerd. De technische realisatie ligt in handen van Manifera: elf jaar ervaring in het beheren van bedrijfskritische softwaresystemen voor opdrachtgevers als Vodafone, TNO en CFLW, vanuit Amsterdam en Ho Chi Minhstad.

[Beschrijf je project](https://launchstudio.eu/nl/#contact) en we rekenen exact voor welke beschikbaarheid je eerlijk en veilig kunt garanderen, meestal binnen één werkdag, of bekijk direct de inhoud van onze [pakketten](https://launchstudio.eu/nl/#packages).

## Wat er naast het percentage in je contract hoort te staan

Het percentage eist alle aandacht op, maar de omliggende clausules bepalen wat het juridisch en financieel écht betekent. Vijf bepalingen die je zwart-op-wit geregeld wilt hebben:

**De uitsluitingen (force majeure en derden).** Gepland onderhoud binnen afgesproken vensters, storingen veroorzaakt door het eigen netwerk of de systemen van de klant, en uitval bij kritieke toeleveranciers buiten jouw controle. Dit is volstrekt gebruikelijk en redelijk.

**De exacte meetmethode.** Welke specifieke monitoringdienst meet, met welk interval, wat de definitie is van onbeschikbaarheid, en hoe de klant inzage krijgt. Zonder dit is elk percentage een bron van toekomstige conflicten.

**Een gemaximeerde compensatie (capped remedy).** Service credits die evenredig zijn aan de uitvalduur, met een hard maximum — bijvoorbeeld maximaal 20% of 50% van het maandbedrag. Onbeperkte aansprakelijkheid voor omzetschade door uitval is een risico dat een startup simpelweg niet kan dragen.

**Een hersteltermijn vóór ontbinding (cure period).** Mocht je de norm een maand niet halen, dan hoort een redelijk contract jou eerst een termijn van dertig dagen te geven om de oorzaak structureel te verhelpen alvorens de klant mag opzeggen.

**Afstemming op je eigen leveranciersvoorwaarden.** Als je de klant toezeggingen doet die jouw hostingprovider jou niet biedt, benoem dit dan expliciet of pas het getal aan. Meer beloven dan je zelf gegarandeerd krijgt, is het stilzwijgend absorberen van andermans risico.

Voor een klein softwarebedrijf vereist dit geen dure advocaten. Het vergt simpelweg dat je de SLA-clausule zorgvuldig leest en vraagt om vier of vijf standaard aanpassingen. Professionele inkoopafdelingen gaan hier vrijwel altijd direct mee akkoord: een leverancier die onderhandelt over een realistische SLA, is immers een leverancier die serieus van plan is zijn afspraken na te komen.

## Echt voorbeeld

### Een getekend contract met een getal dat niemand controleerde

Ruud Bosman runde Inspectiepunt, een softwaretool voor inspectierapporten in de bouw gebouwd in Lovable en gebruikt door zeven inspectiebureaus rondom Deventer. Zijn grootste klant, een regionale woningcorporatie, nam een beschikbaarheidseis van 99,9% op in een tweejarig contract. Ruud tekende zonder aarzelen.

Vier maanden later vroeg de corporatie om het officiële uptime-rapport over het afgelopen kwartaal. Ruud had echter geen enkel monitoringsysteem actief en kon niets overleggen.

Het reconstrueren van de uptime bleek pijnlijker dan het ontbreken van de rapportage. Aan de hand van foutenlogboeken en e-mails ontdekte hij minstens twee forse storingen: een mislukte software-release die anderhalf uur had geduurd en een database-verbindingsfout gedurende een weekend. Samen overschreden deze twee incidenten het toegestane downtime-budget voor het gehele jaar al ruimschoots.

Het herstel vergde vier werkdagen: externe uptime-monitoring met pings om de minuut en directe SMS-alarmering naar zijn telefoon; geavanceerde error tracking; een CI/CD deployment-pipeline met staging en automatische rollback zodat releases geen storingen meer veroorzaakten; een geverifieerde database-herstelprocedure geklokt op 26 minuten; en een overzichtelijk document met de uptime-garanties van zijn cloudleveranciers naast zijn eigen gemeten prestaties.

Vervolgens ging hij het gesprek aan dat hij eerder had vermeden. Hij stelde voor het contract te wijzigen naar 99,5%, extern gemeten volgens een vastgelegde methode, inclusief een reactietijdgarantie en een onderhoudsvenster — en legde eerlijk uit waarom 99,9% technisch onhaalbaar was voor een applicatie in één cloudregio gerund door een solist.

**Resultaat:** de woningcorporatie accepteerde de contractwijziging zonder enig bezwaar. De inkoopmanager gaf achteraf aan dat een transparant gemeten 99,5% met duidelijke procedures veel meer zekerheid bood dan een loze 99,9% op papier.

> *"Ik had getekend voor een getal omdat het zo professioneel stond in een contract. Maar als ze me hadden gevraagd of ik het had gehaald of met een factor tien had overschreden, had ik geen flauw idee gehad."*
> — **Ruud Bosman, Oprichter, Inspectiepunt (Deventer)**

**Kosten & Doorlooptijd:** € 1.900 (monitoring en alerting, deployment-pipeline met rollback, gemeten back-upherstel en uptime-documentatie) — afgerond in 4 werkdagen.

## Veelgestelde vragen

### Wat staat een uptime-garantie van 99,9% in de praktijk toe?

Circa 43 minuten downtime per maand. Eén mislukte software-update of een tijdelijke storing bij je clouddienst verbruikt dit budget al volledig, waardoor dit een riskante toezegging is voor een applicatie die door één persoon wordt beheerd in één datacenterregio.

### Kan ik een hogere beschikbaarheid beloven dan mijn hostingprovider garandeert?

Nee. Beschikbaarheid telt cumulatief omlaag door je gehele technische keten — hosting, database, login, betalingen en DNS. Je maximale uptime ligt wiskundig altijd onder die van je minst betrouwbare externe toeleverancier.

### Hoe hoort uptime formeel te worden gemeten in een SaaS-overeenkomst?

Via een onafhankelijke externe monitoringdienst die met vaste tussenpozen van buitenaf controleert, met een eenduidige definitie van wat onbeschikbaarheid inhoudt en gemeten over een kalendermaand. Zonder deze afspraken is een SLA juridisch niet controleerbaar.

### Wat kan ik aanbieden als ik geen 99,9% uptime kan garanderen?

Bied een realistisch percentage dat je wél haalt (zoals 99% of 99,5%), gekoppeld aan een reactietijdgarantie, duidelijke incidentcommunicatie, inzicht in de back-uphersteltijd en transparantie over de garanties van je cloudproviders. Zakelijke inkopers waarderen bewezen haalbaarheid meer dan loze beloftes.

### Wat moet ik doen als ik de afgesproken uptime-norm toch een keer mis?

Licht de klant direct zelf in vóórdat zij aan de bel trekken, verstrek de objectieve meetgegevens, pas de overeengekomen creditfactuur direct toe zonder discussie en lever een beknopt verslag met verbetermaatregelen. Storingen worden door zakelijke klanten geaccepteerd; onjuiste rapportages niet.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat staat een uptime-garantie van 99,9% in de praktijk toe?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Circa 43 minuten downtime per maand. Eén mislukte software-update of provider-storing verbruikt dit al volledig, waardoor het riskant is voor een applicatie beheerd door één persoon."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik een hogere beschikbaarheid beloven dan mijn hostingprovider garandeert?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Beschikbaarheid telt wiskundig omlaag door de keten van hosting, database, authenticatie, betalingen en DNS. Je plafond ligt altijd onder je zwakste schakel."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe hoort uptime formeel te worden gemeten in een SaaS-overeenkomst?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Via een onafhankelijke externe monitoringdienst met vaste intervallen, een duidelijke definitie van downtime en een maandelijkse meetperiode. Anders is de SLA niet te verifiëren."
      }
    },
    {
      "@type": "Question",
      "name": "Wat kan ik aanbieden als ik geen 99,9% uptime kan garanderen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een haalbaar percentage zoals 99,5%, een reactietijdgarantie, transparante incidentcommunicatie, gemeten hersteltijden en inzicht in de SLA's van je cloudproviders."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet ik doen als ik de afgesproken uptime-norm toch een keer mis?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Licht de klant proactief in, deel de meetrapporten, pas de creditering ongevraagd toe en deel een kort verbeterverslag. Eerlijkheid behoudt het vertrouwen."
      }
    }
  ]
}
</script>
