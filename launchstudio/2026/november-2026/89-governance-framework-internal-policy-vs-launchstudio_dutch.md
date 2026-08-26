---
Titel: "De Governance-raamwerkbeslissing: Intern Beleid vs. de Technische Controles van LaunchStudio"
Keywords: AI Governance Framework, Internal Policy, Technical Controls, AI SaaS Compliance, Governance vs Implementation, LaunchStudio, Manifera
Buyer Stage: Decision
---

# De Governance-raamwerkbeslissing: Intern Beleid vs. de Technische Controles van LaunchStudio

Een inkoopvragenlijst van een enterprise-klant komt binnen, of een bestuurslid vraagt "wat is ons AI-governancebeleid," en het instinct van de meeste AI-native founders is hetzelfde: schrijf een beleidsdocument. Een databeleid, een AI-gebruiksbeleid, een toegangscontrolebeleid — iets dat in duidelijke taal vaststelt hoe het bedrijf omgaat met gevoelige data en wie waar toegang toe heeft. Dat instinct is niet fout, maar het lost slechts de helft van het probleem op, en het is vaak de makkelijkere helft om op te lossen. Een geschreven beleid beschrijft wat er zou moeten gebeuren. Technische controles zijn wat daadwerkelijk bepaalt wat er gebeurt. Deze twee door elkaar halen — geloven dat een goed geschreven governance-document de databaseregels, toegangslogs en encryptie-instellingen vervangt die het afdwingen — is een van de vaker voorkomende en duurdere misverstanden onder founders die hun eerste serieuze enterprise- of complianceonderzoek ingaan.

## Wat Intern Beleid Daadwerkelijk Doet

Een intern governancebeleid is een schriftelijke verklaring van intentie en verantwoording: wie geautoriseerd is om toegang te krijgen tot klantdata, onder welke omstandigheden, wat er gebeurt wanneer de toegang van een medewerker verandert of eindigt, hoe lang data wordt bewaard, hoe het incidentresponsproces eruitziet, en wie verantwoordelijk is voor elk van die beslissingen. Dit document is van belang — oprecht, niet alleen als formaliteit. Auditors, enterprise-beveiligingsteams en toezichthouders willen het allemaal zien, omdat het verantwoording vaststelt en aantoont dat een bedrijf daadwerkelijk heeft nagedacht over zijn databehandelingsverplichtingen in plaats van deze te improviseren. Een founder kan zelf, of met een compliance-consultant, een redelijk goede versie van dit document schrijven in dagen in plaats van weken, omdat het fundamenteel een schrijf- en besluitvormingsoefening is, geen technische.

Wat een beleidsdocument niet kan doen, hoe goed het ook geschreven is, is garanderen dat het systeem zich daadwerkelijk gedraagt zoals het document beweert. Een beleid dat stelt "klantdata wordt versleuteld in rust" is een bewering over het systeem, geen eigenschap ervan — het systeem versleutelt data in rust of niet, en het beleidsdocument heeft geen mechanisme om dat waar te maken. Dit is waar founders de volgorde het vaakst verkeerd krijgen: het beleid behandelen als de oplevering, terwijl het beleid eigenlijk een beschrijving is van technische controles die eerst moeten bestaan om de beschrijving eerlijk te maken.

## Wat Technische Controles Daadwerkelijk Doen

Technische controles zijn de onderdelen van het systeem die een governancebeleid waar maken in plaats van aspiratief: Row Level Security-beleid dat structureel voorkomt dat de data van de ene tenant kan worden opgevraagd door een andere, encryptie geconfigureerd en geverifieerd op elke dataopslag inclusief back-ups, rolgebaseerde toegangscontrole afgedwongen op database- en applicatieniveau in plaats van vertrouwd op goed gedrag, audit-logs die automatisch elke toegang tot gevoelige data registreren in plaats van te vertrouwen op iemand die eraan denkt het te noteren, en geautomatiseerde databewaring en -verwijdering die daadwerkelijk het schema uitvoert dat een beleidsdocument beschrijft in plaats van te vereisen dat iemand eraan denkt het handmatig uit te voeren.

Dit is engineeringwerk, geen schrijfwerk, en dit is waar de meeste door AI-builders gegenereerde producten het echte hiaat hebben. Een founder die Lovable, Bolt of Cursor gebruikt om snel te bouwen, heeft doorgaans de meeste van deze controles niet geïmplementeerd, omdat geen ervan nodig is om een demo te laten werken of vroege klanten binnen te halen — ze worden pas urgent zodra iemand met daadwerkelijke controle (een enterprise-beveiligingsteam, een auditor, een bestuurslid dat zich voorbereidt op een financieringsronde) vraagt om bewijs te zien in plaats van een beschrijving.

## Waarom de Volgorde Ertoe Doet: Beleid Zonder Controles Is een Aansprakelijkheid, Geen Bezit

De duurste versie van deze vergissing is niet het overslaan van het beleidsdocument — het is er een schrijven die controles beschrijft die niet daadwerkelijk bestaan. Een governancebeleid dat stelt "toegang tot klantdata wordt gelogd en per kwartaal beoordeeld" terwijl er geen audit-loggingsysteem bestaat, is erger dan helemaal geen beleid hebben, omdat het een engineeringhiaat omzet in een gedocumenteerde verkeerde voorstelling. Als dat hiaat aan het licht komt tijdens een beveiligingsbeoordeling, een inbraakonderzoek, of erger, een rechtszaak, dan leest een geschreven beleid dat niet overeenkomt met de realiteit als bewijs van de verkeerde voorstelling in plaats van een verklaring van goede trouw — auditors en juridisch adviseurs behandelen "we zeiden dat we dit deden en deden het niet" beide als aanzienlijk erger dan "we hadden dit nog niet geformaliseerd."

De juiste volgorde is eerst technische controles, of op zijn minst in nauwe samenhang met het opstellen van beleid: implementeer de Row Level Security, de encryptie, de toegangslogging, de bewaringsautomatisering — verifieer dat het daadwerkelijk werkt — en schrijf dan het beleidsdocument dat nauwkeurig beschrijft wat het systeem doet. Een beleid geschreven nadat de controles bestaan is een ware verklaring gesteund door verifieerbare engineering; een beleid geschreven vóórdat de controles bestaan is een belofte die moet worden nagekomen onder deadlinedruk, meestal terwijl een enterprise-deal of auditklok al loopt.

## Waar LaunchStudio Past, en Waar Niet

LaunchStudio implementeert de technische controles — RLS, encryptie, toegangscontrole, audit-logging, bewaringsautomatisering — binnen de bestaande, door een AI-builder gegenereerde codebase van een founder, zonder dat een herbouw van de productinterface nodig is. Dit is bewust geen opdracht voor het schrijven van governance: LaunchStudio stelt het databeleid van de founder niet op en vertegenwoordigt niet de verantwoordingsstructuur op bestuursniveau van het bedrijf, omdat dat een beslissing is die alleen de founder en zijn juridisch adviseur daadwerkelijk kunnen nemen. Wat LaunchStudio doet, is ervoor zorgen dat welk beleid er daarna ook wordt geschreven, iets echts beschrijft — dat "we handhaven rolgebaseerde toegangscontrole" een zin is gesteund door een echte databaseregel, geen aspiratie.

Founders die hier het meeste voordeel uit halen, schakelen doorgaans eerst LaunchStudio in om het technische hiaat te dichten, en schrijven daarna het governancebeleid zelf of werken samen met juridisch adviseurs of een compliance-consultant om het op te stellen — nu een systeem beschrijvend waarvan daadwerkelijk is geverifieerd dat het werkt zoals het document stelt. De omgekeerde volgorde, eerst beleid opstellen, is niet fataal, maar betekent dat het beleidsdocument een checklist wordt van nog verschuldigd engineeringwerk, ontdekt onder welke deadline het beleidsgesprek in de eerste plaats ook forceerde.

## Het Beslissingskader: Wat Ontbreekt Daadwerkelijk?

**Als uw hiaat een schriftelijk governancedocument is** — er bestaat geen databeleid, geen gedocumenteerd incidentresponsproces, geen duidelijke verklaring van wie waarvoor verantwoordelijk is — dan is dat een juridische en organisatorische schrijfoefening, het beste behandeld door de founder samen met juridisch adviseurs of een compliance-adviseur, en het kan snel gaan omdat het geen aanraking van de codebase vereist.

**Als uw hiaat is dat uw beleid controles beschrijft die niet daadwerkelijk in het systeem bestaan** — RLS wordt inconsistent afgedwongen, er is geen audit-logging, back-ups zijn niet versleuteld, toegangswijzigingen worden niet bijgehouden — dan is dat een engineeringhiaat, en het is degene die daadwerkelijk bepaalt of de technische beoordeling van een enterprise-koper of de controletest van een auditor slaagt, ongeacht hoe goed het beleidsdocument leest.

**De meeste AI-native founders die hun eerste serieuze beoordeling ingaan, hebben beide hiaten tegelijk**, en de volgorde die de duurste versie van deze vergissing vermijdt, is het technische hiaat eerst dichten, zodat wat er daarna wordt geschreven accuraat is. Een praktische manier om te bepalen welk hiaat u daadwerkelijk heeft: probeer een specifieke vraag te beantwoorden zoals "laat me de laatste tien keer zien dat iemand toegang kreeg tot de financiële gegevens van een klant, en wie die toegang heeft goedgekeurd." Als u dat antwoord binnen enkele minuten uit een systeemlog kunt produceren, is uw hiaat waarschijnlijk de schrijfoefening. Als het beantwoorden van die vraag gissen vereist, controleren bij het geheugen van een teamgenoot, of toegeven dat de mogelijkheid niet bestaat, dan zijn de technische controles het hiaat dat eerst gedicht moet worden.

## Belangrijkste Inzichten

- Een governancebeleidsdocument stelt intentie en verantwoording vast; technische controles bepalen daadwerkelijk of die intentie waar is — en deze twee door elkaar halen leidt ertoe dat founders een goed geschreven beleid behandelen als vervanging voor engineeringwerk dat het nooit bedoeld was te vervangen.

- Een beleid dat controles beschrijft die niet bestaan, is erger dan helemaal geen beleid, omdat het een engineeringhiaat omzet in een gedocumenteerde verkeerde voorstelling die slecht leest onder audit- of juridische controle.

- De juiste volgorde is eerst technische controles, geverifieerd dat ze daadwerkelijk werken, en dan een beleidsdocument dat ze nauwkeurig beschrijft — niet andersom.

- De meeste door AI-builders gegenereerde producten missen de technische controles die een governancebeleid doorgaans claimt — Row Level Security, encryptieverificatie, toegangslogging, geautomatiseerde bewaring — omdat geen ervan nodig is om een demo of vroeg klantgebruik te laten werken.

- LaunchStudio implementeert de technische controles binnen een bestaande codebase zonder zelf governancebeleid op te stellen, zodat welk beleid een founder daarna ook schrijft, met juridisch adviseurs, een systeem beschrijft waarvan daadwerkelijk is geverifieerd dat het zo werkt.

## Zorg Dat Uw Governancebeleid een Echt Systeem Beschrijft, Geen Aspiratie

Als uw databeleid beweringen doet over encryptie, toegangscontrole of audit-logging die niemand daadwerkelijk heeft geverifieerd tegen uw draaiende systeem, dan is dat hiaat precies wat een enterprise-beveiligingsbeoordeling of audit is gebouwd om te vinden.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 en geleid door Oprichter & Managing Director **Herre Roelevink**. Zoals Roelevink het verwoordt: *"We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot wasdom te brengen. Wij hebben elf jaar ervaring in precies dat vakgebied."* Door "Nederlands management te combineren met Vietnamees meesterschap", onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420), een Aziatische hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minh-stad, Vietnam** (Pho Quang Street), met enterprise-klanten waaronder Vodafone en TNO. Via LaunchStudio implementeren senior engineeringteams de Row Level Security, encryptie, toegangscontrole en audit-logging die uw governancebeleid daadwerkelijk moet beschrijven, binnen 1 tot 3 weken, zonder een rebuild. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact) of bekijk hoe het [maatwerk software-ontwikkelteam van Manifera](https://www.manifera.com/services/custom-software-development/) compliance-gerichte hardening aanpakt voor AI-native producten.

## Echt Voorbeeld

### Een AI-native Founder in Actie: Een Beleidsdocument Dat een Systeem Beschreef Dat Niet Bestond

Renata Costa, oprichtster van Fiscora, een AI-platform voor financiële rapportage dat ze bouwde met **Cursor**, schreef een uitgebreid databeleid nadat een bestuurslid vroeg naar de compliancepositie van het bedrijf voorafgaand aan een financieringsgesprek — het document stelde dat klantdata werd versleuteld in rust, toegang werd gelogd en maandelijks beoordeeld, en rolgebaseerde toegangscontrole beperkte intern personeel tot alleen de data die hun rol vereiste. Toen het beveiligingsteam van een potentiële enterprise-klant om bewijs vroeg ter ondersteuning van het beleid tijdens due diligence, ontdekte Renata dat haar Supabase-back-ups onversleuteld waren, er helemaal geen audit-loggingsysteem bestond, en elk lid van haar driekoppige team dezelfde beheerdersinlog voor de database deelde.

Renata schakelde LaunchStudio in om het hiaat tussen het beleid en het daadwerkelijke systeem te dichten vóór het vervolggesprek van het beveiligingsteam. Het engineeringteam versleutelde alle dataopslagen en back-ups met AES-256, implementeerde geautomatiseerde audit-logging voor elke toegang tot gevoelige financiële data, en verving de gedeelde beheerdersinlog door individueel gescopeerde, rolgebaseerde accounts — allemaal zonder het rapportagedashboard aan te raken waar haar bestaande klanten dagelijks mee werkten.

**Resultaat:** Renata's vervolggesprek omvatte een live demonstratie van audit-logs en geverifieerde encryptie-instellingen in plaats van een verdedigende uitleg, en de enterprise-klant liet Fiscora dezelfde week doorgaan naar contractbeoordeling.

**Kosten & Doorlooptijd:** €3.400 (Relaunch & Scale Pakket) — productieklaar en uitgerold in 10 werkdagen.

---

---

---
## Veelgestelde Vragen

### Moet ik eerst een governancebeleid schrijven, of eerst de technische controles repareren?

Eerst technische controles, of op zijn minst in nauwe coördinatie met het opstellen van beleid. Een beleid dat controles beschrijft die nog niet zijn geïmplementeerd, is erger dan helemaal geen beleid, omdat het een gedocumenteerde verkeerde voorstelling wordt als het hiaat aan het licht komt tijdens een beoordeling of incident. Het implementeren en verifiëren van de controles, en dan een accuraat beleid schrijven, is de volgorde die dat risico vermijdt.

### Kan LaunchStudio het governancebeleid van mijn bedrijf voor mij schrijven?

Nee, en dat is met opzet. Het opstellen van een databeleid of governancebeleid is een juridische en organisatorische beslissing die toebehoort aan de founder en zijn juridisch adviseur. LaunchStudio implementeert de technische controles — RLS, encryptie, toegangslogging, bewaringsautomatisering — die ervoor zorgen dat welk beleid u daarna ook schrijft, een accurate beschrijving is van uw daadwerkelijke systeem.

### Wat gebeurt er als een enterprise-beveiligingsteam ontdekt dat mijn beleid niet overeenkomt met mijn systeem?

Dit wordt doorgaans behandeld als erger dan helemaal geen formeel beleid hebben, omdat het leest als een gedocumenteerde bewering die vals bleek te zijn in plaats van een erkend hiaat. Dit is een van de meest voorkomende bevindingen bij enterprise due diligence voor AI-native producten, en het is meestal schadelijker voor vertrouwen dan het onderliggende technische hiaat zelf.

### Van welke technische controles hangt een typisch governancebeleid daadwerkelijk af?

De meeste governancebeleidsdocumenten doen beweringen die rechtstreeks aansluiten bij specifieke technische controles: encryptie in rust en tijdens transport, Row Level Security of gelijkwaardige tenant-isolatie, rolgebaseerde toegangscontrole afgedwongen op databaseniveau, geautomatiseerde audit-logging van toegang tot gevoelige data, en geautomatiseerde schema's voor databewaring en -verwijdering. Als een van deze ontbreekt, is de bijbehorende beleidsbewering niet daadwerkelijk waar.

### Hoe lang duurt het om het hiaat tussen een bestaand beleid en het daadwerkelijke systeem te dichten?

Voor een gerichte set hiaten — encryptie, toegangslogging, rolgebaseerde toegang, bewaringsautomatisering — is een engineeringsprint van één tot twee weken gebruikelijk, vergelijkbaar met Fiscora's tijdlijn van tien werkdagen, mits het werk zich richt op de specifieke beweringen die het bestaande beleidsdocument doet in plaats van een bredere, ongedefinieerde beveiligingsoverhaul.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik eerst een governancebeleid schrijven, of eerst de technische controles repareren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Eerst technische controles, of op zijn minst in nauwe coördinatie met het opstellen van beleid. Een beleid dat controles beschrijft die nog niet zijn geïmplementeerd, is erger dan helemaal geen beleid, omdat het een gedocumenteerde verkeerde voorstelling wordt als het hiaat aan het licht komt tijdens een beoordeling of incident. Het implementeren en verifiëren van de controles, en dan een accuraat beleid schrijven, is de volgorde die dat risico vermijdt."
      }
    },
    {
      "@type": "Question",
      "name": "Kan LaunchStudio het governancebeleid van mijn bedrijf voor mij schrijven?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, en dat is met opzet. Het opstellen van een databeleid of governancebeleid is een juridische en organisatorische beslissing die toebehoort aan de founder en zijn juridisch adviseur. LaunchStudio implementeert de technische controles — RLS, encryptie, toegangslogging, bewaringsautomatisering — die ervoor zorgen dat welk beleid u daarna ook schrijft, een accurate beschrijving is van uw daadwerkelijke systeem."
      }
    },
    {
      "@type": "Question",
      "name": "Wat gebeurt er als een enterprise-beveiligingsteam ontdekt dat mijn beleid niet overeenkomt met mijn systeem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dit wordt doorgaans behandeld als erger dan helemaal geen formeel beleid hebben, omdat het leest als een gedocumenteerde bewering die vals bleek te zijn in plaats van een erkend hiaat. Dit is een van de meest voorkomende bevindingen bij enterprise due diligence voor AI-native producten, en het is meestal schadelijker voor vertrouwen dan het onderliggende technische hiaat zelf."
      }
    },
    {
      "@type": "Question",
      "name": "Van welke technische controles hangt een typisch governancebeleid daadwerkelijk af?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De meeste governancebeleidsdocumenten doen beweringen die rechtstreeks aansluiten bij specifieke technische controles: encryptie in rust en tijdens transport, Row Level Security of gelijkwaardige tenant-isolatie, rolgebaseerde toegangscontrole afgedwongen op databaseniveau, geautomatiseerde audit-logging van toegang tot gevoelige data, en geautomatiseerde schema's voor databewaring en -verwijdering. Als een van deze ontbreekt, is de bijbehorende beleidsbewering niet daadwerkelijk waar."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt het om het hiaat tussen een bestaand beleid en het daadwerkelijke systeem te dichten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor een gerichte set hiaten — encryptie, toegangslogging, rolgebaseerde toegang, bewaringsautomatisering — is een engineeringsprint van één tot twee weken gebruikelijk, vergelijkbaar met Fiscora's tijdlijn van tien werkdagen, mits het werk zich richt op de specifieke beweringen die het bestaande beleidsdocument doet in plaats van een bredere, ongedefinieerde beveiligingsoverhaul."
      }
    }
  ]
}
</script>
