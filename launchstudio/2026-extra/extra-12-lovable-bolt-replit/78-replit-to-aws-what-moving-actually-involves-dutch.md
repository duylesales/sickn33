---
Titel: "Van Replit naar AWS: Wat Overstappen Werkelijk Inhoudt"
Trefwoorden: replit naar AWS, cloudmigratie, infrastructuur, containers, wanneer overstappen, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: SaaS Scale-Up
---

# Van Replit naar AWS: Wat Overstappen Werkelijk Inhoudt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Van Replit naar AWS: Wat Overstappen Werkelijk Inhoudt",
  "description": "Van een prototypingplatform naar een cloudaanbieder overstappen koopt controle en kost operationele verantwoordelijkheid. De redenen die het rechtvaardigen, het werk dat erbij komt kijken, de tussenopties, en de eerlijke doorlopende kosten.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-16",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/replit-to-aws-what-moving-actually-involves" }
}
</script>

Op een gegeven moment krijgt een oprichter die een product op een prototypingplatform draait te horen dat hij op een echte cloudaanbieder hoort te zitten. Het klinkt als volwassenheid, en soms is het de juiste stap.

Het is ook een ruil in plaats van een upgrade. U krijgt controle over waar dingen draaien, hoe ze zijn geconfigureerd en wat ze op schaal kosten. U neemt de verantwoordelijkheid voor dat alles op u — het netwerk, de certificaten, het schalen, het patchen, de monitoring en de onderdelen die op onhandige momenten breken.

Voor een product met één persoon en honderd klanten is die ruil vaak een slechte deal. Weten wanneer dat niet zo is, is waar dit hele artikel over gaat.

## De Redenen Die Het Rechtvaardigen

**Een contractuele of wettelijke eis.** De inkoop van een klant eist een specifieke regio, een genoemde certificering, of infrastructuur onder een overeenkomst die het platform niet biedt. Dit is de meest voorkomende echte reden, zoals het residentieartikel in deze reeks beschrijft, en ze komt meestal met omzet eraan vast.

**Een workload die het platform niet aankan.** Aanhoudende zware rekenkracht, gespecialiseerde hardware, grootschalige dataverwerking, of een netwerkopzet — een privéverbinding met de systemen van een klant — die een beheerd platform niet biedt.

**De economie op schaal.** Echt relevant boven een bepaald volume, en het omslagpunt ligt hoger dan oprichters aannemen. Daaronder is het platform goedkoper zodra uw tijd wordt meegeteld.

**Een bestaande voetafdruk.** Uw bedrijf draait al infrastructuur bij een aanbieder, met een team dat die beheert. Consolideren is redelijk.

## De Redenen Die Het Niet Zijn

**"Het is professioneler."** Klanten vragen waar data wordt opgeslagen en wat er gebeurt als het breekt. Geen van beide antwoorden vereist een bepaalde aanbieder.

**"We moeten misschien schalen."** De platforms schalen aanzienlijk verder dan de meeste producten ooit komen, en het migratiewerk is hetzelfde wanneer u het ook doet.

**"Een investeerder noemde het."** Vraag welk probleem het oplost. Vaak is de onderliggende zorg afhankelijkheid van één leverancier, en dat wordt aangepakt met overdraagbaarheid, niet met verhuizen.

**"We lopen steeds tegen limieten aan."** Soms echt. Vaak een verbindingslek, een ontbrekende index of een onbegrensde query, die allemaal met u meereizen en elders meer kosten.

## Waar het Werk Echt uit Bestaat

Uitgaande van een typisch Replit-product — een webapplicatie, een database, object storage, wat gepland werk — valt de migratie uiteen in vijf delen.

**De applicatie.** Gecontaineriseerd en gedraaid op een beheerde containerdienst. Dit is het eenvoudigste deel: een Dockerfile, een servicedefinitie, en een load balancer met een certificaat.

**De database.** Een beheerde Postgres-instance, met de data gemigreerd zoals beschreven in het database-artikel in deze reeks: dump, herstel, controle, met dubbel schrijven of een kort onderhoudsvenster afhankelijk van uw tolerantie.

**Opslag.** Objecten gekopieerd naar een bucket, waarbij uw applicatie URL's bij het lezen genereert in plaats van ze op te slaan — en daarom was het de moeite waard die beslissing vroeg te nemen.

**Gepland werk.** Geplande taken opnieuw ingericht met de eigen planner van de aanbieder, of als een kleine continu draaiende worker.

**Alles wat impliciet was.** Dit is het deel dat mensen verrast: netwerk, security groups, certificaten, DNS, logging, metrics, alerting, back-ups, opslag van geheimen, deploymentautomatisering, en toegangsbeheer voor wie het beheert. Het platform deed dit allemaal zonder dat erom werd gevraagd.

Voor een klein product twee tot vier weken werk, het meeste in die laatste categorie.

## De Doorlopende Kosten Die Niemand Begroot

De migratie is een project. Het beheer is permanent.

Iemand moet beveiligingsupdates toepassen, letten op verlopende certificaten, reageren als er 's nachts iets breekt, toegang beheren als mensen komen of gaan, de infrastructuurdefinities actueel houden, en de rekening begrijpen. Op een beheerd platform zit het meeste daarvan in de prijs.

Voor een solo-oprichter is dit de doorslaggevende overweging. Een uur per week aan infrastructuurwerk is zes werkdagen per jaar die niet aan het product worden besteed, en het eerste serieuze incident kost op één avond meer dan dat.

Migreert u, begroot het dan eerlijk: ofwel uw eigen tijd, ofwel een beheerde regeling met iemand die het voor u doet.

## De Tussenopties

Tussen een prototypingplatform en een volledige cloudaanbieder ligt een bereik dat past bij de meeste producten met een echte reden om te verhuizen.

**Een beheerd applicatieplatform** — Vercel, Netlify, Cloudflare, Render, Fly — dat u deployment vanuit een repository, regiokeuze, certificaten en schaling geeft, zonder het operationele oppervlak. Voor de meeste producten is dit de bestemming, niet AWS.

**Een beheerde database bij een aparte aanbieder**, die eisen rond dataresidentie oplost zonder te raken waar de applicatie draait.

**Eén beheerde dienst tegelijk.** Verhuis de database voor een residentie-eis; laat al het andere staan. De meeste contractuele eisen gaan over waar persoonsgegevens worden opgeslagen, niet over waar de applicatie wordt uitgevoerd.

Het instinct om alles tegelijk te verhuizen is meestal verkeerd, en de vraag bij elke voorgestelde migratie is aan welke specifieke eis ze voldoet — en of iets kleiners aan dezelfde eis voldoet.

## Bereid U Erop Voor Zonder Het te Doen

Er is een set wijzigingen die een toekomstige migratie goedkoop maakt, het product hoe dan ook verbetert, en een fractie kost van de tijd die de migratie zelf zou kosten.

**Alles in een repository, daarvandaan gedeployd.** Het platform draait uw code in plaats van haar te bewaren. Dit is het fundament en, zoals verschillende artikelen in deze reeks betogen, de moeite waard om op dag één te doen om heel andere redenen.

**Configuratie in omgevingsvariabelen.** Geen platformspecifieke waarden in code. Veranderen waar de database staat, wordt een variabele in plaats van een bewerking.

**Platformfuncties achter uw eigen grens.** Roept de applicatie overal uw eigen opslagmodule aan in plaats van de client van een specifieke aanbieder, dan raakt het wisselen van aanbieder één bestand.

**Standaardcomponenten.** Postgres in plaats van een eigen opslag. Object storage met een gangbare interface. Geplande taken die een endpoint aanroepen in plaats van af te hangen van een platformspecifiek mechanisme.

**Gedocumenteerde infrastructuur.** Een pagina met wat waar draait, welke diensten worden gebruikt, wat elk doet en waar de accounts staan. Wie een migratie uitvoert, begint hiermee, en zonder deze pagina is zijn eerste week ontdekkingswerk.

Doe deze vijf en een migratie wordt twee tot vier weken in plaats van een kwartaal. Nuttiger nog: u hebt haar waarschijnlijk nooit nodig — en ondertussen hebt u een product dat makkelijker over te dragen is, makkelijker te doorgronden, en niet afhankelijk van de blijvende goodwill van één leverancier.

## Vraag Het Eerst aan het Platform

Voordat u zich vastlegt op een verhuizing, vraag de aanbieder waar u nu zit of aan de eis kan worden voldaan waar u bent. Oprichters slaan dit verrassend consequent over, en het antwoord is vaak ja.

Regiokeuze, een abonnement met andere contractuele voorwaarden, een verwerkersovereenkomst met specifieke toezeggingen, een dedicated instance, of een complianceverklaring die u aan een klant kunt doorgeven — een aantal hiervan bestaat in hogere abonnementen en is niet zichtbaar op een prijspagina.

Een gesprek met het sales- of supportteam van een leverancier kost een half uur. Een migratie kost weken. De asymmetrie is groot genoeg dat het gesprek altijd eerst moet plaatsvinden, en het beëindigt de discussie vaak.

Twee dingen om klaar te hebben voor dat gesprek. De eis precies geformuleerd, met de woorden van de klant in plaats van een parafrase — "persoonsgegevens verwerkt en opgeslagen binnen Nederland" is een andere eis dan "EU-hosting", en de antwoorden verschillen. En de tijdlijn, omdat een aanbieder die er over zes maanden wel en over zes weken niet aan kan voldoen, u een ander antwoord heeft gegeven dan een simpel nee.

Is het antwoord echt nee, dan hebt u nu een gedocumenteerde reden voor de migratie, en dat is ook wat uw bestuur, uw adviseurs en uw eigen toekomstige zelf willen zien.

Bewaar wat ze u vertellen schriftelijk. Een toezegging over regio of certificering in een e-mail is wat u laat zien aan de klant wiens inkoop erom vroeg, en dat is aanzienlijk sneller dan zelf een verklaring regelen.

## Dit Inrichten

Voor een product met een echte reden om te verhuizen, is dit doorgaans twee tot vier weken: de eis specifiek geformuleerd en getoetst aan kleinere alternatieven, de bestemming gekozen — vaak een beheerd applicatieplatform in plaats van een kale cloudaanbieder, de applicatie gecontaineriseerd en gedeployd achter een load balancer met certificaten, de database gemigreerd naar een beheerde instance met controle, opslag gekopieerd met URL's die bij het lezen worden gegenereerd, gepland werk opnieuw ingericht, en daarna de impliciete laag bewust gebouwd: netwerk, logging, metrics, alerting, back-ups met een getest herstel, opslag van geheimen, deploymentautomatisering en administratief toegangsbeheer — met de doorlopende operationele kosten begroot als tijd of als beheerde regeling.

LaunchStudio voert deze migratie uit, en adviseert vaker een kleinere stap die aan dezelfde eis voldoet. Daarachter staat Manifera — elf jaar, 160+ projecten, infrastructuur voor klanten waaronder Vodafone, TNO en CFLW, vanuit Amsterdam, Singapore en Ho Chi Minh-stad.

[Vertel ons welke eis de verhuizing drijft](https://launchstudio.eu/nl/#contact) en wij vertellen u wat het kleinste is dat eraan voldoet.

## Echt voorbeeld

### Een Eis Die Eén Dienst Nodig Had, Niet Allemaal

Maarten Kolff bouwde Dossierbeheer op Replit: dossierbeheer voor jeugdzorgorganisaties, gebruikt door negen organisaties met samen zo'n 2.800 dossiers.

Een regionaal zorgsamenwerkingsverband bood een contract voor vier organisaties, op voorwaarde dat persoonsgegevens in Nederland werden opgeslagen, op infrastructuur onder een specifieke overeenkomst, met een genoemde certificering. Zijn bestuur en twee adviseurs waren het erover eens dat het antwoord een migratie naar AWS was.

De beoordeling haalde de eis en de aanname uit elkaar. De voorwaarde van het samenwerkingsverband ging over waar persoonsgegevens worden opgeslagen en verwerkt — de database en de dossierdocumenten. Ze zei niets over waar de applicatie wordt uitgevoerd, die geen data in rust bevat.

Negen werkdagen in plaats van een kwartaal: de database gemigreerd naar een beheerde Postgres-instance in een Nederlandse regio onder een overeenkomst die aan de certificeringseis voldoet, met een generale repetitie tegen een kopie en een overschakeling van 35 minuten op een zondag; dossierdocumenten verplaatst naar object storage in dezelfde regio, met URL's die bij het lezen worden gegenereerd zodat geen enkele opgeslagen verwijzing hoefde te worden herschreven; de applicatie op Replit gelaten, met functies die de nieuwe database en opslag aanroepen; een pagina met subverwerkers en een verklaring over de datalocatie gepubliceerd, zoals het residentieartikel in deze reeks aanbeveelt; back-ups in de regio ingericht met een getest herstel; en een gedocumenteerde beoordeling die laat zien waar elke categorie data nu staat.

**Resultaat:** aan de eis van het samenwerkingsverband werd voldaan en het contract werd getekend. Maartens infrastructuurkosten stegen van €95 naar €340 per maand. De volledige migratie die hem was aangeraden, werd geschat op zeven weken werk en ongeveer €900 per maand aan doorlopende kosten, en zou aan precies dezelfde eis hebben voldaan.

> *"Twee adviseurs zeiden me dat ik op AWS moest zitten. Het contract zei dat de gegevens van onze cliënten in Nederland moesten staan onder een specifieke overeenkomst. Dat is niet dezelfde zin, en het kostte een middag om dat vast te stellen."*
> — **Maarten Kolff, Oprichter, Dossierbeheer (Zwolle)**

**Kosten & Doorlooptijd:** €8.900 (analyse van de eis, gerepeteerde databasemigratie naar een beheerde instance in de regio, migratie van documentopslag, herconfiguratie van de applicatie, gepubliceerde documentatie over datalocatie, back-ups in de regio met getest herstel) — afgerond in 9 werkdagen.

## Veelgestelde vragen

### Wanneer is overstappen naar een cloudaanbieder gerechtvaardigd?

Bij een contractuele of wettelijke eis, een workload die het platform niet aankan, echte schaalvoordelen, of een bestaande voetafdruk die uw bedrijf al beheert. Niet voor professionaliteit of verwachte groei.

### Waar bestaat het werk eigenlijk uit?

De applicatie containeriseren, de database en opslag migreren, gepland werk opnieuw inrichten — en daarna alles wat het platform impliciet deed: netwerk, certificaten, logging, alerting, back-ups, geheimen, deployment en toegangsbeheer.

### Wat kost het daarna om te draaien?

Meer dan de factuur. Iemand moet patchen, monitoren, 's nachts reageren en toegang beheren. Voor een solo-oprichter is dat de doorslaggevende overweging, en het moet worden begroot als tijd of als beheerde regeling.

### Is er iets kleiners dat aan de eis voldoet?

Meestal wel. De meeste contractuele eisen gaan over waar persoonsgegevens worden opgeslagen, en dat lossen een beheerde database en opslag in de juiste regio op zonder de applicatie te verhuizen.

### Moet ik naar AWS of ergens anders heen?

Voor de meeste producten met een echte reden om te verhuizen geeft een beheerd applicatieplatform de controle die u nodig hebt zonder het operationele oppervlak. Een kale cloudaanbieder is juist wanneer de eis het echt vraagt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wanneer is migreren naar een cloudaanbieder gerechtvaardigd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Bij een contractuele of wettelijke eis, een workload die het platform niet aankan, echte schaalvoordelen, of een bestaande beheerde voetafdruk — niet voor professionaliteit."
      }
    },
    {
      "@type": "Question",
      "name": "Wat houdt een migratie naar AWS in?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De app containeriseren, database en opslag migreren, gepland werk opnieuw inrichten, plus netwerk, certificaten, logging, alerting, back-ups, geheimen en toegangsbeheer."
      }
    },
    {
      "@type": "Question",
      "name": "Wat zijn de doorlopende kosten van eigen infrastructuur?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Meer dan de rekening — patchen, monitoren, nachtelijke inzet en toegangsbeheer, die moeten worden begroot als tijd of ingekocht als beheerde dienst."
      }
    },
    {
      "@type": "Question",
      "name": "Is er een kleiner alternatief voor een volledige migratie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Meestal wel. De meeste eisen gaan over waar persoonsgegevens worden opgeslagen, en daaraan voldoen een beheerde database en opslag in de juiste regio."
      }
    },
    {
      "@type": "Question",
      "name": "AWS of een beheerd applicatieplatform?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor de meeste producten biedt een beheerd platform de benodigde controle zonder het operationele oppervlak; een kale cloudaanbieder alleen wanneer de eis het vraagt."
      }
    }
  ]
}
</script>
