---
Titel: "Wat 'Van Vibe Coding Naar Productie' Eigenlijk Betekent"
Trefwoorden: van vibe coding naar productie, ai coding, ai native, build ai, LaunchStudio, Manifera
Koperfase: Bewustzijn
Doelgroep: AI-Native Founder (niet-technisch)
---

# Wat "Van Vibe Coding Naar Productie" Eigenlijk Betekent

"Het is eigenlijk al klaar, ik hoef het alleen nog te lanceren." Bijna elke founder die met Lovable, Bolt of Cursor een prototype heeft vibe-coded, zegt wel een variant van deze zin — en bijna iedereen ontdekt dat de weg van vibe coding naar productie een aparte engineeringfase is, geen formaliteit die je er na het bouwen nog even bij plakt. Na genoeg AI-gegenereerde codebases te hebben bekeken om het patroon met bijna mechanische consistentie te zien terugkeren, is het de moeite waard om precies uit te leggen waarom "het werkt" en "het is klaar" antwoorden zijn op twee verschillende vragen, en waarom dat verschil structureel is, niet cosmetisch.

## Twee Verschillende Activiteiten Met Dezelfde Naam

Vibe coding — in gewone taal beschrijven wat je wilt en een AI-tool werkende software zien genereren — is oprecht opmerkelijk goed in het produceren van iets dat er binnen enkele uren uitziet en functioneert als een echt product. Productiegereedheid is een aparte discipline: die software veilig maken om bloot te stellen aan echte gebruikers, echte betalingen en echte data, onder omstandigheden die je zelf niet had voorzien. Dit zijn geen twee punten op dezelfde lijn waarbij het ene gewoon doorloopt in het andere. Het ene is geoptimaliseerd voor snelheid van creatie binnen een smalle, door de ontwikkelaar gecontroleerde context. Het andere is geoptimaliseerd voor veerkracht onder omstandigheden die je niet controleert — vijandige input, gelijktijdige toegang, gedeeltelijke storingen van systemen waarvan je afhankelijk bent. Deze twee door elkaar halen is de meest voorkomende fout die AI-native founders maken, en het is een begrijpelijke fout, want niets aan een soepele demo geeft aan dat het twee verschillende dingen zijn.

## Het Vertrouwensgrens-probleem, Correct Uitgelegd

Hier is het concept dat de meeste uitleg van deze kloof volledig overslaat, en het is precies het concept dat ertoe doet: elke applicatie heeft een vertrouwensgrens — de lijn die "dingen die ik controleer" scheidt van "dingen die ik niet controleer." Jouw frontend, hoe goed gebouwd ook, staat aan de verkeerde kant van die lijn zodra je app live gaat, omdat een browser fundamenteel iets is dat de eindgebruiker controleert, niet jij. Alles wat alleen in de frontend wordt afgedwongen — validatie, permissiecontroles, businessregels — is een suggestie, geen garantie, want een voldoende nieuwsgierige gebruiker kan developer tools openen, de netwerkverzoeken van je frontend onderscheppen, en diezelfde verzoeken direct versturen, met welke aanpassingen dan ook. AI-codeertools bouwen standaard snel door de frontend en backend te behandelen als één doorlopend, coöperatief systeem, omdat dat precies de aanname is die een demo binnen enkele minuten laat werken. Productiegereedheidswerk is in wezen het proces van die grens correct opnieuw trekken: elke regel die er daadwerkelijk toe doet — wie wat mag zien, wie wat mag doen, welke data geldig is — verplaatsen naar de kant van de lijn die je daadwerkelijk controleert, namelijk de server.

## Waarom De Kloof Onzichtbaar Is Tot Hij Dat Niet Meer Is

Een vibe-gecodeerd prototype kan elke test doorstaan die een founder zelf uitvoert — doorklikken door de aanmeldflow, de kernfunctie testen, het aan vrienden laten zien — terwijl het nog steeds hardgecodeerde API-sleutels in de codebase bevat, authenticatiecontroles die alleen in de frontend bestaan, en geen enkele gestructureerde afhandeling voor wat er gebeurt als een externe dienst een time-out geeft. Geen van deze gaten toont zich in een demo, omdat een demo per definitie is: jij die je eigen product precies gebruikt zoals bedoeld, op je eigen machine, met je eigen data. Ze tonen zich allemaal in de eerste week dat echte gebruikers — die zich gedragen op manieren die je niet had voorzien, op netwerken die je niet controleert, soms met kwaadwillige bedoelingen — de app voor het eerst gebruiken.

## De Vorm Van De Kloof, In Kaart Gebracht Naar Waar Engineers Daadwerkelijk Kijken

Van vibe coding naar productie gaan betekent doorgaans het aanpakken van een consistente set dimensies, en ervaren engineeringteams controleren ze in een vrij voorspelbare volgorde omdat die volgorde ruwweg de impactstraal volgt. Geheimen en credentials die hardgecodeerd waren in plaats van opgeslagen in omgevingsconfiguratie komen eerst, omdat een gelekte sleutel geautomatiseerd, op schaal, binnen enkele minuten na blootstelling misbruikt kan worden door wie hem ook vindt. Authenticatie en autorisatie die op API-niveau afgedwongen moeten worden — niet enkel verstopt achter een inlogscherm — komen daarna, omdat dit de grens is die bepaalt of "ingelogd" ook "toegestaan" betekent, bij elk afzonderlijk verzoek, niet alleen het eerste. Gestructureerde foutafhandeling voor aanroepen naar externe diensten volgt, aangezien AI-gegenereerde code risicovolle operaties doorgaans in één brede catch-all wikkelt in plaats van een time-out te onderscheiden van een validatiefout van een storing. Een lichte maar doelgericht opgezette teststructuur, en basale observability zodat problemen op een dashboard verschijnen in plaats van in de inbox van een klant, maken de lijst compleet. Niets hiervan vereist het herbouwen van wat je hebt gebouwd. Het vereist het verharden ervan, ongeveer in deze volgorde, tegen precies de faalmodi die een demo nooit triggert.

## Waarom Dit Geen Herbouw Is — En Waarom Founders Dat Denken

De instinctieve angst, zodra een founder de kloof begrijpt, is dat het dichten ervan betekent dat je opnieuw moet beginnen. Dat is niet zo, en begrijpen waarom vereist het scheiden van twee dingen die AI-gegenereerde code de neiging heeft door elkaar te laten lopen: wat je product *doet* (de frontend, de AI-logica, de gebruikerservaring die je hebt ontworpen en getest) en wat dat product *betrouwbaar op schaal* maakt (de infrastructuurlaag die eronder en eromheen zit). De frontend die je hebt ontworpen verandert niet. De AI-logica die je hebt afgesteld verandert niet. Wat verandert is onzichtbaar voor een gebruiker die normaal door je app klikt — het wordt alleen zichtbaar voor iemand die aan de randen test, en dat is precies waar reëel gebruik uiteindelijk terechtkomt.

[LaunchStudio](https://launchstudio.eu/en/) bestaat specifiek voor deze fase — een werkend AI-gegenereerd prototype van vibe coding naar productie brengen zonder de frontend aan te raken die je al hebt gebouwd, gesteund door Manifera's engineeringteam en hun 11+ jaar ervaring met het verharden van software voor precies deze realistische omstandigheden.

[Beschrijf wat je hebt gebouwd en waar je vastzit](https://launchstudio.eu/en/#contact) — de meeste founders staan dichter bij productie dan ze denken, ze hebben alleen de specifieke kloof nog niet in kaart gebracht.

## Echt voorbeeld

### Een AI-native founder in actie: de kloof ontdekken voordat die haar een klant kostte

Sanne, fysiotherapeut die wellnessondernemer werd in Zutphen, bouwde HerstelPlan, een AI-tool die gepersonaliseerde herstel-oefenschema's genereerde voor fysiotherapiepatiënten op basis van hun blessuretype en voortgangsnotities, met Lovable. Ze beschouwde HerstelPlan als vrijwel af — de demo werkte foutloos voor de twaalf patiënten aan wie ze het persoonlijk had laten zien, ieder ingelogd, elk hun eigen schema zag, en verder niets, precies zoals bedoeld.

Een lokale fysiotherapiepraktijk toonde interesse om HerstelPlan te gebruiken voor hun patiëntenbestand, en hun praktijkmanager stelde een routinematige inkoopvraag: "Hoe wordt patiëntdata beveiligd, en wie heeft er toegang toe?" Sanne besefte dat ze het antwoord oprecht niet wist — ze had nooit geverifieerd of HerstelPlans data-toegangscontroles ergens anders bestonden dan in de interface die ze had ontworpen, omdat niets in haar eigen testen haar ooit had gedwongen verder dan die interface te kijken.

Sanne bracht HerstelPlan naar LaunchStudio specifiek om die onzekerheid te dichten voordat het haar de opdracht van de praktijk zou kosten. De audit van het Manifera-team bevestigde dat haar instinct terecht nerveus was: authenticatie bestond alleen in de frontend, wat betekende dat een gemiddeld technische persoon patiëntendossiers kon benaderen door de onderliggende API direct aan te roepen met een ander patiënt-ID, waardoor het inlogscherm — en de vertrouwensgrens die het geacht werd af te dwingen — volledig werd omzeild.

**Resultaat:** LaunchStudio implementeerde correcte server-side authenticatie en rolgebaseerde toegangscontrole, geverifieerd tegen de API in plaats van de interface, vóór Sannes vervolggesprek met de praktijk — waardoor ze de beveiligingsvraag met specifieke details kon beantwoorden in plaats van onzekerheid, en de opdracht won.

> *"Ik dacht dat 'klaar' betekende dat het werkte wanneer ik erdoorheen klikte. Ik wist niet dat 'klaar' en 'productieklaar' verschillende vragen waren totdat iemand me een vraag stelde die ik niet kon beantwoorden."*
> — **Sanne Bakker, Founder, HerstelPlan (Zutphen)**

**Kosten & tijdlijn:** €2.100 (Launch Ready Pakket, beveiliging en toegangscontrole) — live in 9 werkdagen.

---

## Veelgestelde vragen

### Als mijn prototype perfect werkt in elke test die ik zelf uitvoer, waarom zou het dan niet productieklaar zijn?

Omdat je eigen testen het bedoelde pad door de interface beoefenen — de kant van de vertrouwensgrens die jij controleert — terwijl productiegereedheid gaat over wat er aan de andere kant gebeurt: directe API-aanroepen, misvormde input, gelijktijdige gebruikers, en randgevallen die een enkele founder die handmatig test structureel onwaarschijnlijk ooit zal triggeren, zoals Sannes casus illustreert. De demo en het aanvalsoppervlak zijn simpelweg niet hetzelfde terrein.

### Hoe weet ik of mijn specifieke prototype een gat heeft zoals dat van Sanne, zonder te wachten tot een klant het vraagt?

Een gestructureerde audit die specifiek de API-laag direct test — je eigen interface omzeilend zoals een echte kwaadwillende of een nieuwsgierige technische gebruiker zou doen — is de betrouwbare manier om erachter te komen, in plaats van te wachten op een externe trigger zoals een verloren deal, een supportticket, of een incident. LaunchStudio's initiële scopinggesprek brengt doorgaans precies dit soort gat naar boven voordat het een van beide wordt.

### Betekent "van vibe coding naar productie" dezelfde checklist voor elk type app?

De algemene dimensies — geheimen, authenticatie, foutafhandeling, testen, observability — zijn breed toepasbaar omdat ze hetzelfde vertrouwensgrensprobleem weerspiegelen ongeacht wat je app doet. Het specifieke risico en de prioriteitsvolgorde verschuiven afhankelijk van welke data je app verwerkt: een tool die gezondheidsdata verwerkt, zoals die van Sanne, rechtvaardigt meer urgentie specifiek op toegangscontrole, terwijl een app zonder gevoelige data maar met zware externe API-afhankelijkheid mogelijk foutafhandeling eerst prioriteert.

### Is dit gat specifiek voor één AI-codeertool, of geldt het over Lovable, Bolt, Cursor en andere?

Het geldt breed over AI-codeertools, aangezien ze allemaal geoptimaliseerd zijn om snel functionele, demo-klare output te genereren door frontend en backend standaard als één coöperatief systeem te behandelen — wat precies is wat een prompt-naar-app-workflow in eerste instantie magisch laat aanvoelen. Het gat is een categoriekenmerk van hoe deze tools ontworpen zijn om te werken, geen fout specifiek voor de implementatie van één tool.

### Hoe lang duurt het doorgaans om dit gat te dichten zodra het geïdentificeerd is?

Voor de meeste prototypes met één product sluit LaunchStudio's Launch Ready-pakket de kernproblemen binnen één tot drie weken tegen een vaste prijs, hoewel de exacte tijdlijn afhangt van welke specifieke dimensies — geheimen, authenticatie, betalingen, hosting — werk nodig hebben, en hoe diep die problemen daadwerkelijk zitten zodra een engineer de codebase daadwerkelijk opent, wat precies is wat het initiële scopinggesprek is ontworpen om vast te stellen voordat er enige toezegging wordt gedaan.
