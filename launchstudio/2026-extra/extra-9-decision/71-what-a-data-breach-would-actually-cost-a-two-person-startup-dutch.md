---
Titel: "Wat een datalek daadwerkelijk kost voor een tweepersoons startup"
Trefwoorden: kosten datalek startup, AVG meldplicht datalek 72 uur, beveiligingsincident kleine SaaS kosten, datalek mkb, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: SaaS-Oprichter Scale-Up
---

# Wat een datalek daadwerkelijk kost voor een tweepersoons startup

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wat een datalek daadwerkelijk kost voor een tweepersoons startup",
  "description": "Oprichters die zoeken naar 'kosten van een datalek' vinden enterprise-bedragen in de miljoenen die niet op hen slaan. Dit artikel ontleedt de reële kostenposten — forensisch onderzoek, meldplicht, klantverloop, verloren deals en toezichthouders — op de schaal van een tweepersoons SaaS-bedrijf.",
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
  "datePublished": "2027-01-04",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/what-a-data-breach-would-actually-cost-a-two-person-startup"
  }
}
</script>

€ 4,45 miljoen. Dat is het bedrag dat steevast bovenaan staat in de eerste drie zoekresultaten voor "gemiddelde kosten van een datalek", overgenomen uit het jaarlijkse rapport van IBM en herhaald op duizenden landingspagina's van cybersecurity-aanbieders. Dit gebeurt zonder de ene cruciale contextuele zin die er werkelijk toe doet: dat cijfer is een gemiddelde van datalekken bij multinationals met duizenden werknemers, eigen juridische afdelingen en enterprise-klantcontracten met torenhoge boeteclausules. Een tweepersoons SaaS-onderneming met 3.000 gebruikersrecords en één parttime freelancer gaat nooit van zijn leven ergens € 4,45 miljoen voor betalen. Het citeren van dat getal tegenover een oprichter die beslist hoeveel hij aan beveiliging moet uitgeven, is niet informatief — het werkt averechts. Het veroorzaakt óf blinde paniek óf, veel vaker, totale ontkenning: omdat het bedrag zo overduidelijk irrelevant is voor een bedrijf van deze schaal, ronden oprichters het mentaal af naar "dit geldt niet voor mij" en stoppen ze helemaal met nadenken over het risico. Beide reacties gaan voorbij aan de kernvraag: wat zou een datalek *u*, specifiek op uw schaal, daadwerkelijk kosten — en is dat bedrag substantieel genoeg om nu preventief geld aan uit te geven vóórdat het misgaat?

## De 72-uursklok die niemand goed uitlegt

Onder Artikel 33 van de AVG (Algemene Verordening Gegevensbescherming / GDPR) heeft u, zodra u ontdekt dat persoonsgegevens waarvoor u verwerkingsverantwoordelijke bent zijn gecompromitteerd — ongeautoriseerd ingezien, gestolen, gewijzigd of ontoegankelijk gemaakt —, exact 72 uur de tijd om een melding te doen bij de toezichthouder (de Autoriteit Persoonsgegevens in Nederland, of de bevoegde autoriteit in de EU-lidstaat waar u bent gevestigd), tenzij aannemelijk is dat het incident geen risico oplevert voor de betrokkenen. Die 72 uur is géén termijn om het hele incident volledig te onderzoeken en op te lossen; het is de termijn om een eerste officiële melding te doen met wat u op dat moment weet, met de mogelijkheid dit later gefaseerd aan te vullen. De initiële melding stelt echter harde eisen aan de inhoud: de aard van de inbreuk, bij benadering het aantal getroffen personen en records, een contactpunt voor opvolging, de waarschijnlijke gevolgen en de maatregelen die u heeft genomen of voorstelt te nemen. De meeste kleine startups ontdekken om 02:00 uur 's nachts op dag één van een incident dat ze zelfs het tweede punt — "bij benadering hoeveel records" — niet kunnen invullen. Ze weten eenvoudigweg niet precies welke persoonsgegevens ze bewaren, waar deze staan opgeslagen, of in welke van hun drie databases en externe cloudtools de gegevens van een specifieke klant zich bevinden. Dát kennishiaat, niet het datalek zelf, verandert een beheersbaar incident in een chaotische crisis. Voorbereid zijn op de 72-uursklok vereist vooraf: een data-inventarisatie van één pagina met welke data u verzamelt en waar deze staat, een aangewezen contactpersoon (al bent u dat zelf) en een vast meldingssjabloon dat u snel kunt invullen in plaats van onder acute stress vanaf nul te moeten opstellen.

## Forensisch onderzoek: de eerste echte factuur

De eerste concrete factuur waar de meeste kleine softwarebedrijven na het ontdekken van een lek mee te maken krijgen, is het achterhalen van wat er daadwerkelijk is gebeurd: welke systemen zijn benaderd, welke data is geëxfiltreerd, bevindt de aanvaller zich nog steeds in het netwerk, en wanneer begon de inbreuk? Dit is forensisch onderzoek, en dat is geen werk dat een solo-oprichter of een tweekoppig team geloofwaardig zelf kan uitvoeren. Enerzijds omdat het specialistische vakkennis vereist, anderzijds omdat de stelling "de persoon die mogelijk de configuratiefout maakte, heeft zelf het onderzoek geleid" geen stand houdt tegenover een toezichthouder of veeleisende zakelijke klanten die achteraf vragen stellen. Een freelance incident-response consultant in West-Europa factureert doorgaans tussen de € 900 en € 2.000 per dag. Een afgebakend datalek op de schaal van een vroege SaaS-applicatie — een openbare database-tabel, een gelekte API-sleutel of een verkeerd geconfigureerde cloud storage bucket — vergt gewoonlijk twee tot vijf dagen gericht forensisch werk om de scope vast te stellen, af te dichten en formeel te documenteren. Dat brengt een realistische factuur voor forensisch onderzoek bij een klein incident op circa € 2.000 tot € 8.000. Dat is geen astronomisch enterprise-bedrag van honderdduizenden euro's, maar wel een forse, onvoorziene kostenpost waarvoor u vooraf een reservering moet kunnen maken. Het plan "we zoeken wel iemand als het zover is" kost u immers 24 tot 48 uur kostbare tijd waarin u naarstig zoekt naar een beschikbare specialist terwijl de 72-uursklok doortikt.

## Meldplicht: meer arbeidsuren dan factuurbedrag

Het informeren van getroffen gebruikers brengt zelden grote directe out-of-pocket uitgaven met zich mee — een e-mail sturen kost niets. Het kost echter een enorme hoeveelheid uren van de oprichter, op exact het moment dat een tweepersoonsbedrijf geen enkel uur kan missen. Het opstellen van een juridisch sluitende verklaring die informeert zonder onnodige paniek te zaaien, het inrichten van een speciaal kanaal voor vragen (een speciale inbox, een tijdelijke FAQ-pagina of telefonische opvang) en het daadwerkelijk beantwoorden van verontruste gebruikers gedurende de daaropvolgende één tot twee weken kost realistisch 15 tot 30 uur aan oprichterstijd. Gewaardeerd tegen een bescheiden ondernemersuurtarief van € 60 per uur betekent dat € 900 tot € 1.800 aan productiviteit die niet naar productontwikkeling, verkoop of marketing gaat, precies in de week waarin de startup zich geen stilstand kan veroorloven. Wanneer de inbreuk waarschijnlijk een hoog risico inhoudt voor de rechten en vrijheden van betrokkenen, verplicht Artikel 34 van de AVG u bovendien om elke getroffen persoon individueel direct te informeren — een tweede meldingsplicht met strikte formele vereisten.

## Klantverloop: de kostenpost die niet op een factuur staat

Er wordt geen formele factuur uitgereikt voor klantverloop (churn), en dat is precies de reden waarom oprichters dit effect structureel onderschatten wanneer ze de financiële risico's van een datalek afwegen. Onafhankelijk onderzoek naar beveiligingsincidenten wijst consistent uit dat een substantieel deel van de getroffen klanten — veelgenoemde percentages liggen tussen een kwart en een derde — stopt met het gebruik van een dienst nadat ze bericht hebben gekregen dat hun gegevens bij een incident betrokken waren, zelfs wanneer de respons van het bedrijf snel, professioneel en transparant was. Voor een tweepersoons SaaS-onderneming met bijvoorbeeld 40 betalende B2B-klanten à € 80 per maand is het verliezen van acht klanten (20%) door een datalek geen detail: het betekent dat er maandelijks direct € 640 aan terugkerende omzet verdwijnt, oftewel bijna € 7.700 in het daaropvolgende jaar. In tegenstelling tot een eenmalige factuur voor forensisch onderzoek is klantverloop een blijvende deuk in uw omzetlijn en een directe aanslag op uw financiële runway, die juist het zwaarst toeslaat onder de meest betrokken en kritische klanten.

## Verloren enterprise-deals: het onzichtbare slachtoffer

De allergrootste schadepost bij een datalek voor een kleine B2B-softwareonderneming is doorgaans de verkoopdeal die opeens geruisloos stilvalt zonder dat iemand u expliciet vertelt waarom. Het openbaar moeten melden van een datalek duikt immers maanden later onvermijdelijk op tijdens de security-audits van potentiële zakelijke klanten. Vrijwel elke enterprise-beveiligingsvragenlijst vraagt tegenwoordig expliciet of uw organisatie in de afgelopen 12 tot 24 maanden een beveiligingsincident heeft doorgemaakt. Een contract met een corporate klant ter waarde van € 25.000 tot € 60.000 aan jaarlijkse contractwaarde (ACV) wordt in zo'n situatie zelden formeel afgewezen; het traject vertraagt simpelweg, uw interne pleitbezorger wordt terughoudend en de inkoopafdeling legt de lat ineens onhaalbaar hoog. Voor een kleine startup waar één of twee enterprise-klanten 30% tot 50% van de totale jaaromzet uitmaken, overstijgt deze ene onzichtbare schadefactor alle andere kostenposten bij elkaar. Omdat dit in de administratie verschijnt als "de deal ging helaas niet door" en niet als "het datalek kostte ons veertigduizend euro", leggen oprichters zelden het verband.

## Toezichthouders: wat er werkelijk gebeurt, niet de sensationele boete

De maximale boetes onder de AVG — tot € 20 miljoen of 4% van de wereldwijde jaaromzet — halen voortdurend het nieuws, maar zijn in de praktijk vrijwel nooit van toepassing op startende bedrijven van deze omvang. Wat bij een kleine onderneming die tijdig meldt, volledig meewerkt en aantoont dat zij redelijke beveiligingsmaatregelen had getroffen veel eerder gebeurt, is een schriftelijke waarschuwing, het verzoek om een plan van aanpak voor herstelmaatregelen of in ernstigere gevallen een formele berisping. Dit zijn administratieve procedures die vooral tijd en juridisch advies kosten (doorgaans enkele honderden tot een paar duizend euro aan advocaatkosten om correct en formeel te reageren) in plaats van een bedrijfsslopende boete. Toezichthouders zoals de Autoriteit Persoonsgegevens wegen eerdere inspanningen zwaar mee: een partij die geen data-overzicht had, geen incidentenprocedure kende en basisbeveiliging verwaarloosde, wordt fundamenteel anders behandeld dan een startup die binnen 72 uur melding deed, exact kon aantonen wat er gebeurde en vooraf aantoonbare basisbeveiliging had ingeregeld. Het boeterisico bestaat, maar de operationele en commerciële gevolgen zijn voor een startup aanzienlijk groter.

## De optelsom: een realistisch bedrag, geen schrikbeeld

Tellen we de kosten bij elkaar op voor een afgebakend datalek bij een tweepersoons SaaS-onderneming met enkele duizenden gebruikers en enkele grotere deals in de pipeline: forensisch onderzoek € 2.000 tot € 8.000, communicatie en support € 900 tot € 1.800 aan eigen uren, juridisch advies voor de toezichthouder € 500 tot € 2.500, direct klantverloop in het eerste jaar tussen de € 3.000 en € 8.000, en één vertraagde of verloren enterprise-deal ter waarde van € 10.000 tot € 60.000. Dat resulteert in een realistische totale schadelast van circa € 15.000 tot € 75.000 voor een relatief klein, beheerst incident. Dat is geen 4,45 miljoen euro, maar het is een enorm bedrag dat voor een beginnende startup fataal kan zijn — en het is vele malen hoger dan de kosten van het preventieve programmeerwerk dat het lek had voorkomen. Dat is de feitelijke afweging die u moet maken: een grondige security-audit, professionele authenticatie, versleutelde dataopslag en een eenvoudig incidentenprotocol kosten slechts een fractie van de onderkant van die schadepost. Beveiliging is geen kostenpost die u eindeloos voor u uit kunt schuiven, het is een zakelijke verzekering.

De engineers van [Manifera hebben meer dan 160 softwareprojecten opgeleverd](https://www.manifera.com/about-us/), en diezelfde industriestandaarden — strikte toegangscontrole, encryptie in rust en transit, en afhankelijkhedenscans — past LaunchStudio toe op door AI gegenereerde prototypes vóórdat ze live gaan, zonder de frontend die u heeft gebouwd te verstoren. Het voorkomen van een incident is vrijwel altijd vele malen goedkoper dan de schadeafhandeling achteraf.

[Beschrijf uw huidige technische inrichting en wij vertellen u binnen één werkdag welke kwetsbaarheden daadwerkelijk openstaan](https://launchstudio.eu/nl/#contact) — de meeste oprichters zijn verrast over hoe concreet en snel oplosbaar de lijst met beveiligingspunten blijkt te zijn.

## Echt voorbeeld

### De 'near-miss' van een tweepersoonsteam: De storage bucket die negen dagen openstond

Bram Voskuijlen en zijn medeoprichter runden Ledgerlytics, een compacte SaaS-tool voor factuurreconciliatie voor freelance boekhouders, gebouwd met behulp van Bolt en gehost op een combinatie van Supabase en Vercel. Tijdens een routinematige beveiligingscontrole die Bram initieerde na het lezen over een datalek bij een concurrent, ontdekte een externe auditor dat een cloud storage bucket met geüploade klantfacturen — pdf-bestanden met namen, IBAN's en btw-nummers van circa 1.100 eindklanten van de aangesloten boekhouders — sinds de aanmaak negen dagen eerder op openbare leestoegang (`public read`) had gestaan. Dit was een overblijfsel van een standaardconfiguratie uit Bolt die niemand handmatig had gecontroleerd.

Er was in de toegangslogbestanden geen bewijs van ongeautoriseerde downloads van buitenaf, maar "geen bewijs" is juridisch niet gelijk aan "geen risico". Onder de AVG geldt de verplichting om te beoordelen en zo nodig te melden immers zodra data onbeschermd toegankelijk is geweest. Brams team liet met spoed een forensische verificatie uitvoeren om te bevestigen dat de logbestanden integer waren en diende binnen het 72-uursvenster een voorlopige melding in bij de Autoriteit Persoonsgegevens, gecombineerd met een gerichte notificatie aan de kleine groep eindgebruikers van wie volledige bankgegevens zichtbaar waren geweest.

**Resultaat:** De toezichthouder sloot het dossier af met een schriftelijke ontvangstbevestiging zonder sancties of vervolgonderzoek, dankzij de proactieve melding en de directe technische sanering. Ledgerlytics verloor nul betalende klanten, maar Bram berekende dat de audit, de juridische bijstand en twee dagen stilgelegd ontwikkelwerk het bedrijf circa € 4.800 hadden gekost aan directe uitgaven en ondernemersuren — een bedrag dat hij nu bewaart als referentie voor wat "preventie" in harde euro's waard is.

> *"Ik had dat krantenkopbedrag van 4 miljoen euro wel tien keer gelezen en het zette me nooit aan tot actie. Maar een echte factuur van € 4.800 voor iets dat veel erger had kunnen aflopen — dát zorgde ervoor dat een audit van opslagrechten een vast onderdeel van onze maandelijkse routine werd."*
> — **Bram Voskuijlen, Medeoprichter, Ledgerlytics**

---

## Veelgestelde Vragen

### Moet ik de toezichthouder echt informeren bij een datalek dat minder dan honderd mensen treft?

Jazeker, dat is heel goed mogelijk. De meldplicht onder de AVG wordt getriggerd door het risico voor de rechten en vrijheden van betrokken personen, niet door het absolute aantal getroffenen. Een klein datalek met gevoelige financiële gegevens of medische data moet vrijwel altijd worden gemeld. Alleen wanneer een risico redelijkerwijs is uitgesloten kan melding achterwege blijven, maar dat vereist een gedegen juridische afweging.

### Wat is het allergoedkoopste dat een tweepersoons startup kan doen om het risico op een datalek te verlagen?

Stel een data-inventarisatie van één A4'tje op: welke persoonsgegevens verzamelt u, waar worden ze exact opgeslagen en wie heeft er toegang toe? Het kost u slechts één middag werk, en het is hét document dat een chaotische 72-uurscrisis verandert in een gestructureerde checklist wanneer er zich daadwerkelijk een incident voordoet.

### Dekt een cyberverzekering de kosten die in dit artikel worden beschreven?

Slechts een gedeelte. Forensisch onderzoek en externe juridische bijstand worden doorgaans gedekt, evenals directe notificatiekosten. Klantverloop (churn) en misgelopen contracten worden vrijwel nooit vergoed, omdat dit gevolgschade betreft. Controleer daarnaast specifiek de polisvoorwaarden rond bestuurlijke boetes, aangezien die vaak zijn uitgesloten.

### Waarin verschilt dit van wat de beveiligingsdiensten van LaunchStudio al afdekken?

De Launch Ready- en Launch & Grow-pakketten van LaunchStudio richten zich op de preventieve kant: encryptie, toegangsbeveiliging, autorisatie en audit van softwareconfiguraties om te voorkomen dat er überhaupt een inbreuk ontstaat. Dit artikel brengt in kaart welk financieel risico u accepteert als u die preventieve stappen overslaat of uitstelt.

### Vanaf welke bedrijfsgrootte wordt die statistiek over de 'gemiddelde kosten van een datalek' daadwerkelijk relevant?

Die miljoenenstatistieken zijn pas representatief voor organisaties met complexe IT-infrastructuren over meerdere vestigingen, omvangrijke compliance-afdelingen en tienduizenden klanten — organisaties met tientallen engineers en zware contractuele aansprakelijkheden. Dat is een volstrekt ander risicoprofiel dan dat van een startende software-onderneming.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik de toezichthouder echt informeren bij een datalek dat minder dan honderd mensen treft?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Jazeker, dat is mogelijk. De meldplicht onder de AVG hangt af van het risico voor de rechten van betrokkenen, niet van het aantal personen. Een incident met gevoelige financiële gegevens vereist vrijwel altijd een melding."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het allergoedkoopste dat een tweepersoons startup kan doen om het risico op een datalek te verlagen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Stel een data-inventarisatie van één A4 op waarin staat welke gegevens u bewaart, waar ze staan en wie toegang heeft. Het kost één middag en voorkomt paniek tijdens de 72-uurs meldtermijn."
      }
    },
    {
      "@type": "Question",
      "name": "Dekt een cyberverzekering de kosten die in dit artikel worden beschreven?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Slechts ten dele. Forensisch onderzoek en juridische bijstand worden vaak gedekt, maar gevolgschade zoals klantverloop en misgelopen enterprise-contracten worden vrijwel nooit vergoed."
      }
    },
    {
      "@type": "Question",
      "name": "Waarin verschilt dit van wat de beveiligingsdiensten van LaunchStudio al afdekken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LaunchStudio richt zich op preventieve maatregelen — encryptie, autorisatie, configuratie-audits — om datalekken te voorkomen. Dit artikel berekent de kosten wanneer die preventie wordt nagelaten."
      }
    },
    {
      "@type": "Question",
      "name": "Vanaf welke bedrijfsgrootte wordt die statistiek over de 'gemiddelde kosten van een datalek' daadwerkelijk relevant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Pas bij grote ondernemingen met tientallen engineers, complexe IT-landschappen en dedicated complianceteams; voor een startende SaaS-startup met twee personen is dat bedrag niet representatief."
      }
    }
  ]
}
</script>
