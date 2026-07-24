---
Titel: "Waarom 'prototype-AI' en 'productie-AI' nooit één databaseschema mogen delen"
Trefwoorden: prototype ai, database schema separation, ai development environments, test data production data
Koperfase: Overweging
Doelgroep: Technische solo-oprichter
---
# Waarom 'prototype-AI' en 'productie-AI' nooit één databaseschema mogen delen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Waarom 'prototype-AI' en 'productie-AI' nooit één databaseschema mogen delen",
  "description": "Een technische uitleg over waarom een prototype ai-build en de productieversie ervan aparte databaseschema's nodig hebben, en wat er daadwerkelijk misgaat als test- en livegegevens er één delen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/prototype-production-never-share-schema" }
}
</script>

Een databaseschema is gewoon een blauwdruk — de tabellen, kolommen en relaties die bepalen hoe gegevens worden opgeslagen. Het klinkt als een detail dat te klein is om echte schade aan te richten. In de praktijk is of uw prototype-AI-build en uw productiesysteem één schema delen of twee aparte schema's gebruiken, een van de beslissingen met de meeste impact die een oprichter neemt — en het is bijna nooit een bewuste keuze. Het is meestal gewoon wat de AI-tool op dag één als standaard koos.

Hier is waarom die standaard meer betekent dan hij lijkt.

## Wat "een schema delen" eigenlijk betekent

Wanneer u een prototype bouwt met een AI-ontwikkeltool, zet de tool doorgaans één database en één schema op om alles vast te houden: uw testaccounts, uw voorbeeldrecords, en — zodra u echte gebruikers begint te onboarden — hun echte gegevens ook. Er is geen natuurlijk moment waarop de tool zegt "u zou dit nu waarschijnlijk moeten splitsen." Het blijft gewoon dezelfde tabellen gebruiken waarmee het begon, omdat dat het pad van de minste weerstand is.

Het risico is niet abstract. Het betekent dat een script dat is geschreven om testgegevens te resetten of te manipuleren, geen structurele barrière heeft die het bij echte gegevens weghoudt. Als het script "alle rijen in de customers-tabel" als doel heeft omdat dat simpeler is dan filteren op een omgevingsvlag, raakt het probleemloos rijen van echte klanten aan, omdat er voor het schema geen verschil is tussen de twee.

## Waarom dit een gangbare standaard is, geen zeldzame fout

AI-codeertools optimaliseren voor snel iets werkends. Het opzetten van aparte omgevingen — een werkelijk geïsoleerde testdatabase en een werkelijk geïsoleerde productiedatabase, idealiter met verschillende schema's of op zijn minst strikte scheiding tussen omgevingen — kost extra configuratie die de demo niet beter laat werken. Het betaalt zich pas later uit, als de twee anders gebruikt gaan worden. Omdat de feedbackloop van de tool "werkt dit nu" is, is scheiding tussen omgevingen precies het soort investering die hij uit zichzelf geen reden heeft om te doen.

Dat betekent dat de verantwoordelijkheid voor deze splitsing volledig bij de oprichter ligt, of bij wie het project ook beoordeelt — en als niemand het aankaart, zet de standaard (één gedeeld schema) zich gewoon stilletjes voort tot in productie.

## Wat er misgaat zonder scheiding

Drie faalmodi komen keer op keer voor:

**Testscripts die livegegevens raken.** Een migratie-, opschonings- of seedingscript geschreven tegen "de database" zonder onderscheid tussen omgevingen, draait tegen welke database er op dat moment ook geconfigureerd is — inclusief productie, als dat toevallig is aangesloten.

**Schemawijzigingen die livegegevens stilletjes breken.** Een structurele wijziging gemaakt om een nieuwe prototypefeature mogelijk te maken — een kolom hernoemen, een gegevenstype wijzigen — past zich toe op dezelfde tabellen die echte klantrecords bevatten, zonder aparte staging-stap om problemen eerst op te vangen.

**Test- en echte gegevens die door elkaar lopen in rapportage of analyse.** Zelfs zonder een destructief incident maken gedeelde schema's het gemakkelijk voor testaccounts, voorbeeldtransacties of placeholderrecords om vermengd te raken met echte gebruiksgegevens, wat stilletjes alles vertekent dat erop gebouwd is.

## De oplossing: scheiding van omgevingen als een eersteklas beslissing

De technische oplossing is eenvoudig — aparte databases (of op zijn minst duidelijk gepartitioneerde schema's) voor test en productie, met inloggegevens en verbindingsstrings die het structureel lastig maken om per ongeluk een testoperatie op livegegevens te richten. Het moeilijkere deel is inzien dat dit bewust moet gebeuren, want geen enkele AI-ontwikkeltool zal het als ontbrekend markeren. Het lijkt gewoon alsof alles werkt, tot het moment dat een script dat voor testgegevens bedoeld was, ergens draait waar het niet zou moeten.

## Ambers migratiescript

Amber Schouten, een oprichter in Winterswijk, bouwde VoorraadKoppel — een tool voor voorraadsynchronisatie — met Cursor. Haar testgegevens en echte productiegegevens leefden in precies hetzelfde databaseschema, zonder scheiding tussen de twee. Een routinematig migratiescript, geschreven en getest tegen voorbeeldvoorraadrecords, werd opnieuw uitgevoerd zodra VoorraadKoppel echte klanten had aangesloten — en omdat het schema geen onderscheid maakte tussen test- en liverijen, corrumpeerde het script live klantvoorraadrecords samen met de testgegevens die het eigenlijk had moeten raken.

Niets aan het script zelf was ongebruikelijk. Het deed precies waarvoor het geschreven was. Het probleem was dat "waarvoor het geschreven was" geen grens had die het bij productie weghield, omdat die grens nooit gebouwd was.

Onze technici in Singapore, samenwerkend met collega's in Amsterdam en Ho Chi Minh-stad, behandelen scheiding van omgevingen als een van de standaardcontroles bij elk door AI gebouwd project voordat het live gaat — omdat het onzichtbaar is tot het moment dat het dat niet meer is. LaunchStudio brengt Manifera's enterprise-grade engineering, verfijnd over meer dan 160 opgeleverde projecten, naar precies dit soort infrastructuurreview. U kunt [zien wat een review voor databasescheiding en verharding zou kosten](https://launchstudio.eu/en/#calculator) voor uw eigen project.

## Echt voorbeeld

### Een AI-native oprichter in actie: één migratiescript, geen grens om het tegen te houden

Amber Schouten had maandenlang aan VoorraadKoppel gesleuteld, waarbij ze voorraadsynchronisatielogica testte tegen voorbeeldgegevens die ze had opgebouwd in Cursor. Toen echte klanten hun voorraadsystemen begonnen te koppelen, bleef diezelfde database groeien — echte records in dezelfde tabellen als haar oorspronkelijke testgegevens, omdat niets in de opzet de twee ooit had gescheiden.

Toen Amber moest aanpassen hoe voorraadaantallen werden bijgehouden, draaide ze een migratiescript dat ze eerder succesvol had gebruikt tijdens het testen. Het werkte precies zoals ontworpen — het werkte elke rij bij die aan de criteria voldeed. Het probleem was dat "elke rij" nu ook live klantvoorraadaantallen omvatte, naast de testgegevens waarvoor het script oorspronkelijk was geschreven. Bij verschillende klanten werden voorraadniveaus stilletjes gewijzigd voordat Amber de discrepantie opmerkte tijdens een routinecontrole.

De technici van LaunchStudio bouwden VoorraadKoppels datalaag opnieuw op met een werkelijk gescheiden testomgeving, herstelden de getroffen records vanuit beschikbare back-ups, en voegden waarborgen toe zodat toekomstige scripts niet meer zonder een expliciete, bewuste overschrijving tegen productie konden draaien.

**Resultaat:** VoorraadKoppel draait nu test en productie op volledig gescheiden infrastructuur, en Amber heeft een gedocumenteerd proces voor elke toekomstige migratie die goedkeuring vereist voordat livegegevens worden aangeraakt.

> *"Ik wist niet eens dat de twee iets deelden. Ik dacht er gewoon aan als 'de database'."*
> — **Amber Schouten, oprichter, VoorraadKoppel (Winterswijk)**

**Kosten en tijdlijn:** € 1.250 (scheiding van omgevingen, gegevensherstel en implementatie waarborgen) — voltooid in 9 werkdagen.

---

## Veelgestelde vragen

### Wat is het verschil tussen een gedeeld schema en gescheiden omgevingen?

Een gedeeld schema betekent dat test- en productiegegevens in dezelfde tabellen leven, zonder structurele grens ertussen. Gescheiden omgevingen gebruiken aparte databases of duidelijk gepartitioneerde schema's, zodat een operatie gericht op de ene niet per ongeluk de andere kan bereiken.

### Waarom zetten AI-ontwikkeltools deze scheiding niet automatisch op?

Scheiding van omgevingen voegt configuratieoverhead toe die niet beïnvloedt of een prototype werkt in een demo, dus tools die geoptimaliseerd zijn voor snelle, zichtbare resultaten hebben weinig ingebouwde reden om dit standaard op te nemen.

### Hoe kan een oprichter nagaan of hun project dit probleem nu heeft?

Een snelle manier om te controleren is vragen of testgegevens en echte gebruikersgegevens zijn opgeslagen in dezelfde database met dezelfde inloggegevens. Als het antwoord ja is, of onduidelijk, is een review de moeite waard voordat u een script draait dat gegevens op schaal wijzigt.

### Controleert het team van Manifera specifiek op dit probleem tijdens een review?

Ja. Scheiding van omgevingen is een van de standaard infrastructuurcontroles die de technici van Manifera, in Amsterdam, Singapore en Ho Chi Minh-stad, uitvoeren op elk door AI gebouwd project voordat ze het klaar verklaren voor productieverkeer.

### Kan deze scheiding worden toegevoegd nadat een product al echte gebruikers heeft?

Ja, al vereist het zorgvuldigheid, omdat bestaande gegevens correct gesorteerd en gemigreerd moeten worden in plaats van willekeurig gesplitst. Het is een afgebakend project, geen volledige herbouw, wanneer het wordt uitgevoerd door iemand die bekend is met het bestaande schema.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "What's the difference between a shared schema and separate environments?", "acceptedAnswer": { "@type": "Answer", "text": "A shared schema means test and production data live in the same tables with no structural boundary between them. Separate environments use distinct databases or clearly partitioned schemas, so an operation aimed at one cannot accidentally reach the other." } },
    { "@type": "Question", "name": "Why don't AI development tools set up this separation automatically?", "acceptedAnswer": { "@type": "Answer", "text": "Environment separation adds configuration overhead that doesn't affect whether a prototype works in a demo, so tools optimized for fast, visible results have little built-in reason to include it by default." } },
    { "@type": "Question", "name": "How can a founder tell if their project has this problem right now?", "acceptedAnswer": { "@type": "Answer", "text": "A quick way to check is asking whether test data and real user data are stored in the same database with the same connection credentials. If the answer is yes, or unclear, it's worth a review before running any script that modifies data at scale." } },
    { "@type": "Question", "name": "Does Manifera's team check for this specific issue during a review?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. Environment separation is one of the standard infrastructure checks Manifera's engineers, across Amsterdam, Singapore, and Ho Chi Minh City, run on any AI-built project before recommending it's ready for production traffic." } },
    { "@type": "Question", "name": "Can this kind of separation be added after a product already has real users?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, though it requires care, since existing data needs to be sorted and migrated correctly rather than simply split arbitrarily. It's a contained project, not a full rebuild, when handled by someone familiar with the existing schema." } }
  ]
}
</script>
