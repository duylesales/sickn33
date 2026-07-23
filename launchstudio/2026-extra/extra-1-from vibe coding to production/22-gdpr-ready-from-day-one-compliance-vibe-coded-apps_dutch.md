---
Titel: "AVG-klaar Vanaf Dag Eén: Compliance Voor Vibe-gecodeerde Apps"
Trefwoorden: van vibe coding naar productie, ai privacy issues, ai data security, ai secure, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Founder (niet-technisch)
---

# AVG-klaar Vanaf Dag Eén: Compliance Voor Vibe-gecodeerde Apps

AVG-naleving wordt door de meeste founders mentaal ondergebracht bij "juridisch papierwerk" — een privacybeleid om te publiceren, een cookiebanner om toe te voegen, een vakje ergens. Meerdere van de substantiële kernvereisten zijn eigenlijk architecturaal: beslissingen over hoe jouw database gestructureerd is en hoe de logica van jouw applicatie persoonsgegevens afhandelt, gemaakt tijdens het bouwen, die betekenisvol duurder worden om achteraf toe te voegen naarmate een product langer live is met echte geaccumuleerde data.

## Waarom "Later Toevoegen" Een Duurder Plan Is Dan Het Klinkt

Een privacybeleid kan oprecht achteraf geschreven of bijgewerkt worden met minimale wrijving. Dataarchitectuur kan niet zo makkelijk gewijzigd worden zodra echte gebruikersdata al binnen een specifieke structuur bestaat — een databaseschema gebouwd zonder een schone manier om daadwerkelijk de data van een specifieke gebruiker te verwijderen (een echte AVG-vereiste, geen papierwerk) kan significante herstructurering vereisen om achteraf toe te voegen zodra duizenden echte records bestaan over meerdere gerelateerde tabellen, vergeleken met die mogelijkheid vanaf de allereerste tabeldefinitie in het schema ontwerpen.

## Het Recht Op Vergetelheid, Als Architecturale Vereiste

De AVG's "recht om vergeten te worden" vereist dat wanneer een gebruiker verwijdering verzoekt, je hun persoonsgegevens daadwerkelijk kunt verwijderen — volledig, inclusief uit back-ups binnen een redelijke termijn, en uit elke plek waar het gedupliceerd of afgeleid werd. AI-gegenereerde databaseschema's houden vaak helemaal geen rekening met deze vereiste, aangezien een prompt die "gebruikersprofielen en hun activiteit opslaan" beschrijft natuurlijk een structuur produceert geoptimaliseerd voor het opslaan en bevragen van data, geen die ontworpen is met schone verwijderingspaden over elke tabel die naar een gegeven gebruiker zou kunnen verwijzen, inclusief data gedupliceerd in logs, caches, of analysesystemen.

## Dataminimalisatie: Een Beslissing Gemaakt Elke Keer Een Veld Toegevoegd Wordt

De AVG's principe van dataminimalisatie — alleen verzamelen wat daadwerkelijk noodzakelijk is voor jouw gestelde doel — wordt incrementeel geschonden, één veld tegelijk, wanneer een founder een AI-tool vraagt om "ook [aanvullend veld] te verzamelen terwijl we toch bezig zijn" zonder een specifieke, geformuleerde reden gekoppeld aan de daadwerkelijke functie van het product. Dit accumuleert onzichtbaar, aangezien geen enkel aanvullend veld significant aanvoelt, tot een dataaudit een database onthult die aanzienlijk meer persoonsgegevens verzamelt dan het product oprecht nodig heeft om te functioneren.

## Dataresidentie: Waar Jouw Data Daadwerkelijk Leeft, Niet Waar Je Aanneemt Dat Het Leeft

Veel AI-codeertools hebben standaard hosting- en databaseproviders met infrastructuur buiten de EU tenzij een founder specifiek anders configureert — een beslissing impliciet gemaakt via de standaardinstellingen van een tool, niet via enige doelbewuste keuze door de founder, die zich mogelijk niet eens bewust is dat de instelling bestaat of wat het impliceert voor dataresidentieverplichtingen specifiek relevant voor EU-persoonsgegevens.

## Verwerkersovereenkomsten: De Over Het Hoofd Geziene Leveranciersdimensie

Elke externe dienst die persoonsgegevens namens jou verwerkt — jouw hostingprovider, jouw e-maildienst, jouw AI-model-API als je er persoonsgegevens naar stuurt — heeft een passende verwerkersovereenkomst nodig, en moet zelf adequate waarborgen bieden voor die verwerking. Dit is een leveranciersselectie- en configuratiekwestie, niet iets dat de gegenereerde applicatiecode van een AI-codeertool überhaupt aanpakt, aangezien het bestaat op het niveau van welke diensten je koos en hoe je jouw relatie ermee configureerde, niet in de code zelf.

## Waarom Achteraf Toevoegen Progressief Duurder Wordt

Elk van deze dimensies deelt een specifiek patroon: hoe eerder je ze aanpakt, hoe dichter de kosten bij nul liggen, omdat je simpelweg een andere initiële beslissing neemt in plaats van bestaande data te migreren of een bestaand systeem te herstructureren met echte, live records afhankelijk van de huidige structuur. De kostencurve is niet lineair — het versnelt specifiek zodra echte gebruikersdata accumuleert binnen welke structuur ook oorspronkelijk gekozen werd, aangezien de vereiste migratie groeit met het volume en de complexiteit van wat al bestaat.

## Wat Dit Vanaf Het Begin Inbouwen Daadwerkelijk Inhoudt

Concreet: jouw databaseschema ontwerpen met verwijderingspaden vanaf het begin overwogen, niet achteraf toegevoegd; datacollectie bewust beperken tot wat specifiek gerechtvaardigd is door de functie van jouw product; doelbewust EU-gebaseerde infrastructuur selecteren waar vereist, in plaats van de standaardinstelling van een tool te accepteren; en bevestigen dat verwerkersovereenkomsten bestaan met elke relevante leverancier voordat echte persoonsgegevens erdoorheen beginnen te stromen.

[LaunchStudio](https://launchstudio.eu/en/) bouwt AVG-bewuste architectuur standaard in bij elke opdracht, en behandelt deze als de dag-één-architecturale beslissingen die ze daadwerkelijk zijn in plaats van post-lancering-papierwerk, gesteund door Manifera's compliance-bewuste engineeringcultuur gevormd door klanten zoals TNO.

[Bouw compliance in voordat de data van jouw eerste echte gebruiker bestaat](https://launchstudio.eu/en/#calculator) — dit is betekenisvol goedkoper voordat echte data accumuleert dan erna.

## Echt voorbeeld

### Een AI-native founder in actie: verwijdering achteraf toevoegen aan een schema nooit ervoor ontworpen

Marloes, een voormalig maatschappelijk werker die founder werd in Nijmegen, bouwde ZorgNotities, een AI-tool die kleine thuiszorgorganisaties hielp cliëntenzorgnotities en familiecommunicatie te beheren, met Bolt, groeiend naar twaalf zorgorganisaties en enkele honderden cliëntrecords over het eerste jaar zonder ooit specifiek te ontwerpen voor de AVG-verwijderingsvereisten, aangezien haar oorspronkelijke focus tijdens het bouwen volledig lag op de kernfunctionaliteit van de tool voor notities en communicatie.

Toen een familie volledige verwijdering van de records van hun familielid verzocht onder het AVG-recht op vergetelheid, ontdekte Marloes dat ZorgNotities' databaseschema geen schone manier had om de data van een specifieke cliënt volledig te verwijderen — zorgnotities verwezen naar cliënt-ID's over verschillende gerelateerde tabellen, sommige data was gedupliceerd naar een aparte analysesamenvattingstabel voor organisatorische rapportage, en back-ups behielden volledige historische kopieën zonder eenvoudig mechanisme om selectief de records van één cliënt eruit te zuiveren.

**Resultaat:** LaunchStudio herstructureerde ZorgNotities' dataarchitectuur om oprechte, complete verwijdering over elke tabel en back-upretentiebeleid te ondersteunen, een aanzienlijk groter en duurder project dan dezelfde mogelijkheid in het originele schema bouwen zou zijn geweest, gezien de noodzaak om enkele honderden bestaande records te migreren naar de nieuwe structuur zonder de twaalf organisaties die het product actief gebruikten te verstoren.

> *"Als ik om correcte verwijderingsafhandeling had gevraagd toen de database leeg was, zou het een kleine ontwerpbeslissing zijn geweest. Erom vragen na een jaar echte cliëntdata over een tiental organisaties maakte er een oprecht migratieproject van. De vereiste veranderde niet — mijn kosten om eraan te voldoen wel, volledig vanwege wanneer ik het aanpakte."*
> — **Marloes Hendrickx, Founder, ZorgNotities (Nijmegen)**

**Kosten & tijdlijn:** €3.400 (dataarchitectuurherstructurering en -migratie) — voltooid in 12 werkdagen.

---

## Veelgestelde vragen

### Als mijn app momenteel geen EU-persoonsgegevens verwerkt, zijn deze architecturale overwegingen dan nog steeds op mij van toepassing?

Niet onmiddellijk, hoewel als EU-expansie zelfs een plausibele toekomstige richting is, verwijderingspaden en minimalisatiediscipline vanaf het begin inbouwen nu weinig kost en de exacte achteraf-toevoegkosten vermijdt die Marloes later ervoer, zodra echte data geaccumuleerd is binnen welke structuur ook oorspronkelijk gekozen werd.

### Hoeveel duurder is het achteraf toevoegen van verwijderingsmogelijkheid doorgaans, vergeleken met er vanaf het begin voor ontwerpen?

Het varieert naar hoeveel data geaccumuleerd is en hoeveel gerelateerde tabellen en gedupliceerde kopieën bestaan tegen de tijd dat achteraf toevoegen plaatsvindt, maar zoals Marloes' casus illustreert, is het verschil tussen "een ontwerpbeslissing in een lege database" en "een migratieproject over live, actief gebruikte data" vaak substantieel, direct groeiend met tijd en gebruik.

### Lost het gebruiken van een EU-gebaseerde hostingprovider dataresidentiezorgen automatisch op?

Het lost de specifieke dimensie op van waar data fysiek opgeslagen is, wat een betekenisvolle en vaak primaire zorg is, hoewel volledige compliance ook afhangt van jouw verwerkersovereenkomsten met elke betrokken leverancier en jouw daadwerkelijke datahanteringspraktijken, niet locatie alleen.

### Is dataminimalisatie iets waarvoor een AI-codeertool theoretisch geïnstrueerd zou kunnen worden om het automatisch af te dwingen?

Niet betrouwbaar — minimalisatie vereist oordeel over wat daadwerkelijk noodzakelijk is voor de functie van jouw specifieke product, een bepaling waarvoor de tool geen onafhankelijke basis heeft; het hangt volledig af van een founder of reviewer die doelbewust elk dataveld evalueert tegen oprechte noodzaak, niet iets dat een prompt kan delegeren.

### Hoe identificeert LaunchStudio doorgaans welke AVG-gerelateerde architecturale overwegingen van toepassing zijn op een specifiek prototype?

Via hetzelfde soort afgebakende audit elders in deze serie behandeld, onderzoekend welke persoonsgegevens jouw specifieke product daadwerkelijk verzamelt, opslaat en verwerkt, en tegen welke specifieke vereisten dat dataprofiel triggert, in plaats van een generieke compliancechecklist uniform toe te passen op elke opdracht.
