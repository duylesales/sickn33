---
Titel: "Case Study: Binnen 3 Weken SOC 2-conform voor een Multi-Tenant AI-platform"
Keywords: SOC 2, Multi-Tenant AI Platform, SOC 2 Compliance, AI SaaS Security, LaunchStudio, Manifera
Buyer Stage: Decision
---

# Case Study: Binnen 3 Weken SOC 2-conform voor een Multi-Tenant AI-platform

Een getekend enterprise-contract met een SOC 2-clausule in de leveranciersovereenkomst is óf het beste nieuws dat een founder dat kwartaal krijgt, óf het moment waarop een deal maandenlang stil komt te liggen. Het verschil heeft meestal niets te maken met het product zelf, maar alles met de vraag of de onderliggende infrastructuur ooit met een audit in gedachten is gebouwd. Dit is de case study van Dorian Kessler, oprichter van Ledgerly, een multi-tenant AI-boekhoudplatform gebouwd met **Bolt** dat kleine accountantskantoren bediende die de boeken van meerdere klanten beheerden via één gedeeld inlogsysteem — en wat er gebeurde toen een middelgroot accountantsnetwerk hem vertelde dat een getekend contract afhankelijk was van het binnen 30 dagen afronden van een SOC 2 Type I-audit door Ledgerly. Hieronder leest u precies waar een SOC 2-audit op controleert bij een multi-tenant AI-platform, waarom Ledgerly's architectuur die audit bijna niet doorstond, en hoe een engineeringsprint van drie weken een vastgelopen zescijferig contract omzette in een getekende deal.

## Een Contract Afhankelijk van een Compliance-raamwerk Waar Niemand op Had Gepland

Ledgerly groeide zoals de meeste AI-native B2B SaaS-producten dat doen: Dorian, een voormalig accountant zonder formele technische achtergrond, bouwde het kernproduct in vier maanden met Bolt, waarbij hij een LLM-gedreven engine voor het categoriseren van transacties bovenop een vrij standaard multi-tenant Supabase-backend legde. Individuele accountantskantoren meldden zich aan, elk met tientallen eigen klantboeken binnen de gedeelde infrastructuur van Ledgerly — één platform, meerdere tenants, waarbij de data van elke tenant onzichtbaar hoorde te blijven voor elke andere tenant. Het werkte goed genoeg dat een accountantsnetwerk met 40 vestigingen een pilot startte, en na drie maanden met sterke resultaten stuurde hun inkoopteam een term sheet voor een jaarcontract ter waarde van ongeveer €140.000 — afhankelijk van het slagen van Ledgerly voor een SOC 2 Type I-audit binnen 30 dagen, een standaardvereiste voor elke leverancier die financiële data op die schaal verwerkt.

Dorian had wel eens van SOC 2 gehoord, zoals de meeste founders: als een compliance-raamwerk dat terloops door andere founders werd genoemd, vaag geassocieerd met "enterprise-gereedheid", maar nooit iets wat hij technisch in detail had hoeven begrijpen. Nu had hij 30 dagen om het volledig te doorgronden, of het contract kwijt te raken.

## Wat een SOC 2-audit Daadwerkelijk Vereist voor een Multi-Tenant AI-platform

SOC 2 is geen enkele checklist — het is een audit tegen vijf mogelijke Trust Services Criteria (beveiliging, beschikbaarheid, verwerkingsintegriteit, vertrouwelijkheid en privacy), en de meeste SaaS-leveranciers streven op zijn minst naar het beveiligingscriterium, soms gecombineerd met beschikbaarheid en vertrouwelijkheid voor platforms die gevoelige multi-tenant data verwerken. Een SOC 2 Type I-audit beoordeelt of de juiste controles op één specifiek moment zijn ontworpen en aanwezig; een Type II-audit, die meestal later volgt, beoordeelt of die controles gedurende een periode van maanden effectief hebben gefunctioneerd. Ledgerly had eerst Type I nodig, en zelfs die smallere lat legde ernstige tekortkomingen bloot.

Voor een multi-tenant AI-platform specifiek onderzoekt een auditor een consistente set technische controles, en Ledgerly's bestaande, met Bolt gebouwde infrastructuur had voor bijna geen enkele daarvan een echt antwoord:

- **Logische tenant-isolatie.** De audit vereiste bewijs dat de klantdata van het ene accountantskantoor nooit — zelfs niet per ongeluk — kon worden opgevraagd door gebruikers van een ander kantoor. Ledgerly's Supabase-tabellen hadden Row Level Security wel gedefinieerd in het schema, maar inconsistent afgedwongen — sommige tabellen beperkten query's tot de geauthenticeerde tenant, andere vertrouwden volledig op de applicatielaag om resultaten te filteren, wat betekende dat een bug in de frontend-code — en niet een garantie op databaseniveau — het enige was dat de grootboeken van het ene kantoor scheidde van die van het andere.

- **Toegangscontrole en least privilege.** De audit vereiste gedocumenteerde rolgebaseerde toegangscontrole, waaruit bleek dat interne medewerkers van Ledgerly en platformbeheerders alleen toegang hadden tot de data die hun rol vereiste, met gelogde wijzigingen in toegang. Ledgerly had één beheerdersrol met onbeperkte databasetoegang, door Dorian en zijn ene contractor onderling gebruikt.

- **Change management.** De audit vereiste bewijs dat codewijzigingen aan productie werden beoordeeld en bijgehouden vóór implementatie, en niet rechtstreeks vanaf een lokale machine werden gepusht. Dorian had gedurende de gehele geschiedenis van het platform rechtstreeks vanaf zijn eigen laptop naar productie gedeployed, zonder pull request-beoordelingsproces en zonder deploymentlog.

- **Encryptie tijdens transport en in rust.** De audit vereiste bevestiging dat data zowel tijdens transport als in opslag versleuteld was, inclusief back-ups. Ledgerly's live verbindingen waren TLS-versleuteld, maar geautomatiseerde databasebackups werden onversleuteld opgeslagen in de standaardopslag van de cloudprovider.

- **Beheer van leveranciers en sub-processors.** De audit vereiste een gedocumenteerde lijst van elke externe dienst die klantdata raakte — de LLM-provider, de hostingprovider, de e-maildienst — samen met bewijs dat deze leveranciers zelf aan een basisbeveiligingsstandaard voldeden. Zo'n lijst bestond niet.

- **Incidentrespons en monitoring.** De audit vereiste een gedocumenteerd incidentresponsplan en bewijs van actieve monitoring op beveiligingsgebeurtenissen. Ledgerly had geen foutopsporing, geen beveiligingsmeldingen en geen schriftelijk responsplan.

- **Beveiligingspraktijken van medewerkers.** De audit vereiste bewijs van basale beveiligingshygiëne voor iedereen met systeemtoegang — unieke inloggegevens, multi-factor authenticatie op bevoorrechte accounts en offboarding-procedures. Noch Dorian, noch zijn contractor gebruikte MFA op de productiedatabaseconsole.

Zeven categorieën, en Ledgerly had voor precies nul daarvan een auditklaar antwoord, ondanks dat het product zelf betrouwbaar werkte voor elke klant die het gebruikte.

## Waarom AI-native Multi-Tenant Platforms Standaard Moeite Hebben met SOC 2

De kloof waar Ledgerly voor stond is structureel, geen weerspiegeling van slordig engineeringwerk. Bolt is, net als andere AI-builders, geoptimaliseerd om een werkend multi-tenant product snel live te krijgen — en Ledgerly's kerncategoriseringsengine en tenant-gerichte dashboards waren daarvoor oprecht solide. Maar "elke tenant ziet bij normaal gebruik alleen zijn eigen data" en "de data van elke tenant is aantoonbaar, controleerbaar geïsoleerd, zelfs onder vijandige of onbedoelde omstandigheden" zijn verschillende technische lat-hoogtes, en de tweede is precies wat SOC 2 test. Row Level Security-beleid dat wel in het schema bestaat maar niet consistent wordt afgedwongen, deploymentworkflows zonder beoordelingspoort, en de volledige afwezigheid van een gedocumenteerde incidentrespons zijn terugkerende bevindingen bij vrijwel elk door een AI-builder gegenereerd multi-tenant platform dat wij hebben voorbereid op een SOC 2-audit — omdat niets daarvan nodig is om het product te laten werken in een demo of zelfs in vroeg klantgebruik, en het pas urgent wordt zodra het inkoopteam van een enterprise-koper met naam en toenaam om het auditrapport vraagt.

## De Sprint van Drie Weken: Ledgerly Auditklaar Maken

Met 30 dagen op de klok en een getekende term sheet op het spel, schakelde Dorian LaunchStudio in onder het **Enterprise Hardening**-pakket, direct afgestemd op het beveiligingscriterium van SOC 2 en de specifieke hiaten die een multi-tenant AI-platform moest dichten. Het engineeringteam werkte tegen Ledgerly's bestaande, met Bolt gebouwde frontend, zonder de interface te veranderen die elke klant al had leren kennen.

Row Level Security werd herschreven en consistent afgedwongen over elke tabel met tenant-data, gekoppeld aan een `firm_id`-claim ingebed in elke geauthenticeerde sessie, met vijandige testquery's uitgevoerd tegen elke tabel om te bevestigen dat cross-tenant toegang op databaseniveau werd geweigerd, en niet slechts door applicatiecode werd gefilterd. Rolgebaseerde toegangscontrole werd geïmplementeerd voor interne Ledgerly-medewerkers, ter vervanging van de ene gedeelde beheerdersinlog door individueel gescopeerde accounts en een gelogde geschiedenis van toegangswijzigingen. Er werd een correcte change-managementworkflow ingesteld op GitHub, die pull request-beoordeling vereiste voordat iets productie bereikte, met elke deployment automatisch gelogd. Geautomatiseerde back-ups werden opnieuw geconfigureerd om te versleutelen met AES-256 in rust. Er werd een gedocumenteerde inventaris van sub-processors samengesteld, die de LLM-provider, hostingprovider en e-maildienst omvatte, elk getoetst aan basisbeveiligingsverplichtingen. Sentry werd geïnstalleerd voor het monitoren van fouten en beveiligingsgebeurtenissen, wat een gedocumenteerd incidentresponsplan voedde dat het team samen met Dorian opstelde, met daarin detectie, beheersing en een tijdlijn voor klantmelding. En multi-factor authenticatie werd afgedwongen op elk account met toegang tot de productiedatabase.

## De Auditdag: Wat er Veranderde

Dorians SOC 2 Type I-audit, uitgevoerd door een onafhankelijke externe auditor 19 werkdagen na de start van de sprint, slaagde zonder uitzonderingen op het beveiligingscriterium — het inkoopteam van het accountantsnetwerk ontving het rapport vijf dagen vóór de deadline van 30 dagen. De herziening van de RLS werd op zichzelf iets dat het eigen IT-team van het netwerk specifiek testte tijdens hun eigen due diligence, waarbij ze cross-tenant querypogingen uitvoerden die niets opleverden, precies zoals het rapport beweerde.

De bredere les geldt voor elk AI-native multi-tenant platform op weg naar een enterprise-koper, financiële dienstverlener of zorginstelling: SOC 2 is geen document dat je schrijft, het is een beschrijving van controles die ofwel bestaan in je infrastructuur, ofwel niet. De producten die onder deadlinedruk slagen, zijn de producten waarbij de onderliggende architectuur — tenant-isolatie afgedwongen op databaseniveau, niet op applicatieniveau; deploymentwijzigingen beoordeeld, niet rechtstreeks naar productie gepusht; incidenten gepland, niet geïmproviseerd — snel genoeg werd hersteld om waar te zijn voordat de auditor arriveerde, en niet slechts als waar werd beschreven in een beleidsdocument dat niemand kon verifiëren.

## Belangrijkste Inzichten

- Een SOC 2-audit voor een multi-tenant AI-platform controleert een consistente set technische controles: logische tenant-isolatie, rolgebaseerde toegangscontrole, change management, encryptie in rust en tijdens transport, sub-processor-documentatie, incidentrespons en beveiligingspraktijken van medewerkers — en AI-builder-scaffolds dekken standaard zelden meer dan één of twee daarvan.

- Row Level Security die wel in het schema bestaat maar niet consistent wordt afgedwongen over elke tenant-gescopeerde tabel is de meest voorkomende bevinding bij een multi-tenant SOC 2-audit, omdat het betekent dat isolatie op databaseniveau afhankelijk is van correct gedrag van applicatiecode in plaats van structureel gegarandeerd te zijn.

- Een ontbrekend change-managementproces — rechtstreeks naar productie deployen zonder pull request-beoordeling of een deploymentlog — is een bijna automatische auditbevinding, omdat auditors bewijs nodig hebben dat codewijzigingen zijn beoordeeld voordat ze productie bereikten, niet slechts een bewering dat dit zo was.

- Een gedocumenteerd incidentresponsplan en sub-processor-inventaris zijn vrijwel universele SOC 2-vereisten die geen enkele AI-builder automatisch genereert, maar ze kunnen worden geschreven en ingesteld binnen een gerichte meerwekense sprint naast de technische correcties.

- Het slagen voor een SOC 2-audit onder deadlinedruk vereist geen herbouw van een multi-tenant platform. LaunchStudio verhardde Ledgerly's tenant-isolatie, toegangscontroles en monitoring volledig onder de bestaande, met Bolt gebouwde frontend, zodat de beoordelaars van het accountantsnetwerk hetzelfde product bekeken dat ze al hadden gepilot.

## Laat een SOC 2-deadline Uw Enterprise-contract Niet Vastlopen

Als uw multi-tenant AI-platform op weg is naar een SOC 2-audit volgens het tijdschema van een klant, dan bepaalt precies de kloof tussen "het product werkt voor elke tenant" en "tenant-isolatie is aantoonbaar voor een onafhankelijke auditor" of het contract wordt gesloten.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 en geleid door Oprichter & Managing Director **Herre Roelevink**. Zoals Roelevink het verwoordt: *"We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot wasdom te brengen. Wij hebben elf jaar ervaring in precies dat vakgebied."* Door "Nederlands management te combineren met Vietnamees meesterschap", onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420), een Aziatische hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minh-stad, Vietnam** (Pho Quang Street), met enterprise-klanten waaronder Vodafone en TNO. Via LaunchStudio verharden senior engineeringteams uw bestaande multi-tenant AI-platform tegen precies de controles die een SOC 2-audit toetst — tenant-isolatie, toegangscontrole, change management, encryptie, incidentrespons — binnen 1 tot 3 weken, zonder een volledige rebuild. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact) of bekijk hoe het [maatwerk software-ontwikkelteam van Manifera](https://www.manifera.com/services/custom-software-development/) compliance-gerichte hardening aanpakt voor AI-native platforms.

## Echt Voorbeeld

### Een AI-native Founder in Actie: Een Klok van 30 Dagen op een Contract van €140.000

Dorian Kessler, oprichter van Ledgerly, een multi-tenant AI-boekhoudplatform gebouwd met **Bolt**, had 30 dagen om te slagen voor een SOC 2 Type I-audit nadat een accountantsnetwerk met 40 vestigingen dit als voorwaarde stelde voor een getekend jaarcontract ter waarde van ongeveer €140.000. Een eerste beoordeling toonde Row Level Security die inconsistent werd afgedwongen over tenant-tabellen, één gedeelde beheerdersinlog met onbeperkte databasetoegang, geen change-managementproces, onversleutelde back-ups, geen gedocumenteerde lijst van sub-processors en geen incidentresponsplan.

Dorian schakelde LaunchStudio's Enterprise Hardening-pakket in voor een sprint van drie weken tegen Ledgerly's bestaande, met Bolt gebouwde frontend. Het engineeringteam herschreef en handhaafde RLS-beleid gekoppeld aan een `firm_id`-claim over elke tenant-tabel, verving de gedeelde beheerdersinlog door individueel gescopeerde, MFA-afgedwongen accounts, stelde een op GitHub gebaseerde change-managementworkflow in die pull request-beoordeling vereiste, versleutelde geautomatiseerde back-ups met AES-256, stelde een gedocumenteerde inventaris van sub-processors samen, installeerde Sentry voor het monitoren van beveiligingsgebeurtenissen, en schreef samen met Dorian een formeel incidentresponsplan.

**Resultaat:** Ledgerly slaagde voor de SOC 2 Type I-audit zonder uitzonderingen op het beveiligingscriterium, vijf dagen vóór de deadline van 30 dagen, en Dorian tekende het jaarcontract van het accountantsnetwerk ter waarde van ongeveer €140.000 aan terugkerende omzet.

**Kosten & Doorlooptijd:** €6.400 (Enterprise Hardening Pakket) — auditklaar in 19 werkdagen.

---

---

---
## Veelgestelde Vragen

### Wat controleert een SOC 2-audit specifiek voor een multi-tenant AI-platform?

Een auditor beoordeelt controles waaronder logische tenant-isolatie (of de data van de ene tenant onder welke omstandigheden dan ook kan worden opgevraagd door een andere), rolgebaseerde toegangscontrole voor intern personeel, gedocumenteerd change management voor productiedeployments, encryptie in rust en tijdens transport, een sub-processor-inventaris voor externe leveranciers die klantdata raken, een gedocumenteerd incidentresponsplan en basale beveiligingspraktijken van medewerkers zoals MFA. De meeste AI-builder-scaffolds van tools zoals Bolt, Lovable of Cursor dekken standaard geen van deze.

### Waarom is Row Level Security zo belangrijk voor een SOC 2-audit?

Omdat het bepaalt of tenant-isolatie een structurele garantie op databaseniveau is, of slechts een gedrag dat de applicatiecode onder normale omstandigheden toevallig produceert. Als RLS wel in het schema bestaat maar niet op elke tenant-gescopeerde tabel wordt afgedwongen, zal een auditor dit doorgaans markeren, omdat een bug of onoplettendheid in de applicatielaag — en niet een databaseregel — het enige is dat cross-tenant datatoegang voorkomt.

### Hoe lang duurt het om een multi-tenant AI-platform voor te bereiden op SOC 2?

Voor een gerichte Type I-audit zoals die van Ledgerly — tenant-isolatie, toegangscontrole, change management, encryptie, sub-processor-documentatie en incidentrespons — is een sprint van drie weken (ongeveer 19 werkdagen) realistisch, mits het werk zich richt op de specifieke controles die de audit daadwerkelijk beoordeelt, in plaats van een algemene beveiligingsoverhaul.

### Vereist het slagen voor een SOC 2-audit het herbouwen van een door een AI-builder gegenereerd platform?

Nee. SOC 2-correctiewerk vindt plaats op het niveau van database, toegangscontrole, deployment en monitoring — onder de productinterface die een founder bouwde met Bolt, Lovable of Cursor. Het werk van LaunchStudio bij Ledgerly liet het bestaande, tenant-gerichte dashboard onaangeroerd, wat praktisch van belang was omdat de klant die de audit beoordeelde precies die interface al had gepilot.

### Wat is het verschil tussen SOC 2 Type I en Type II, en welke heb ik als eerste nodig?

Type I beoordeelt of de juiste controles op één specifiek moment zijn ontworpen en aanwezig — in wezen een momentopname. Type II beoordeelt of diezelfde controles gedurende een periode van maanden — meestal zes tot twaalf — effectief hebben gefunctioneerd. De meeste enterprise-contracten vereisen eerst Type I als initieel bewijs van gereedheid, waarbij Type II later volgt naarmate de relatie volwassener wordt en de controles een trackrecord hebben opgebouwd om tegen te auditen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat controleert een SOC 2-audit specifiek voor een multi-tenant AI-platform?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een auditor beoordeelt controles waaronder logische tenant-isolatie (of de data van de ene tenant onder welke omstandigheden dan ook kan worden opgevraagd door een andere), rolgebaseerde toegangscontrole voor intern personeel, gedocumenteerd change management voor productiedeployments, encryptie in rust en tijdens transport, een sub-processor-inventaris voor externe leveranciers die klantdata raken, een gedocumenteerd incidentresponsplan en basale beveiligingspraktijken van medewerkers zoals MFA. De meeste AI-builder-scaffolds van tools zoals Bolt, Lovable of Cursor dekken standaard geen van deze."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom is Row Level Security zo belangrijk voor een SOC 2-audit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat het bepaalt of tenant-isolatie een structurele garantie op databaseniveau is, of slechts een gedrag dat de applicatiecode onder normale omstandigheden toevallig produceert. Als RLS wel in het schema bestaat maar niet op elke tenant-gescopeerde tabel wordt afgedwongen, zal een auditor dit doorgaans markeren, omdat een bug of onoplettendheid in de applicatielaag — en niet een databaseregel — het enige is dat cross-tenant datatoegang voorkomt."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt het om een multi-tenant AI-platform voor te bereiden op SOC 2?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor een gerichte Type I-audit zoals die van Ledgerly — tenant-isolatie, toegangscontrole, change management, encryptie, sub-processor-documentatie en incidentrespons — is een sprint van drie weken (ongeveer 19 werkdagen) realistisch, mits het werk zich richt op de specifieke controles die de audit daadwerkelijk beoordeelt, in plaats van een algemene beveiligingsoverhaul."
      }
    },
    {
      "@type": "Question",
      "name": "Vereist het slagen voor een SOC 2-audit het herbouwen van een door een AI-builder gegenereerd platform?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. SOC 2-correctiewerk vindt plaats op het niveau van database, toegangscontrole, deployment en monitoring — onder de productinterface die een founder bouwde met Bolt, Lovable of Cursor. Het werk van LaunchStudio bij Ledgerly liet het bestaande, tenant-gerichte dashboard onaangeroerd, wat praktisch van belang was omdat de klant die de audit beoordeelde precies die interface al had gepilot."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het verschil tussen SOC 2 Type I en Type II, en welke heb ik als eerste nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Type I beoordeelt of de juiste controles op één specifiek moment zijn ontworpen en aanwezig — in wezen een momentopname. Type II beoordeelt of diezelfde controles gedurende een periode van maanden — meestal zes tot twaalf — effectief hebben gefunctioneerd. De meeste enterprise-contracten vereisen eerst Type I als initieel bewijs van gereedheid, waarbij Type II later volgt naarmate de relatie volwassener wordt en de controles een trackrecord hebben opgebouwd om tegen te auditen."
      }
    }
  ]
}
</script>
