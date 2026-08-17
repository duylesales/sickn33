---
Titel: "Wat AI in databaseontwerp verkeerd doet voor multi-tenant apps"
Trefwoorden: ai in database, ai database, ai native, ai deployment
Koperfase: Besluit
Doelgroep: Technische Solo-oprichter / Indie Hacker
---

# Wat AI in databaseontwerp verkeerd doet voor multi-tenant apps

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wat AI in databaseontwerp verkeerd doet voor multi-tenant apps",
  "description": "Een vergelijking van hoe AI-tools doorgaans databases ontwerpen voor multi-tenant apps versus hoe ze ontworpen zouden moeten worden, en wat AI in databasewerk daadwerkelijk goed moet doen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-08-13",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/what-ai-in-database-design-gets-wrong-for" }
}
</script>

"Oprichters bouwen tegenwoordig snel prototypes met AI. De uitdaging die overblijft, is de architectuur en beveiliging die nodig zijn om die producten verder te brengen — precies daar tellen onze elf jaar ervaring," is ongeveer hoe Herre Roelevink, CEO van LaunchStudio en oprichter van Manifera, het patroon beschrijft dat hij herhaaldelijk ziet. Nergens komt dat patroon voorspelbaarder naar boven dan in AI in databaseontwerp voor multi-tenant apps — het specifieke geval waarin de gegevens van meer dan één betalende klant in hetzelfde systeem moeten leven zonder elkaar ooit te raken.

Het is de moeite waard om rechtstreeks te vergelijken wat een AI-tool standaard produceert tegenover wat een goed ontworpen multi-tenant database daadwerkelijk nodig heeft, want het verschil is niet subtiel zodra u weet waar u moet kijken, en het is precies het soort gat dat goedkoop is om vroeg te repareren en duur om te repareren nadat echte klantgegevens zich erbovenop hebben opgestapeld.

Deze specifieke vergelijking telt meer voor databaseontwerp dan voor bijna elk ander deel van een door AI gegenereerde app, omdat een databaseschema ongewoon duur is om achteraf te wijzigen vergeleken met een frontend-component of een API-route. Frontendcode wordt voortdurend geregenereerd en aangepast door normale iteratie met een AI-tool. Een databaseschema, zodra echte klantgegevens zich erin hebben opgestapeld, verzet zich tegen diezelfde nonchalante iteratie — het later correct wijzigen betekent live gegevens migreren, niet slechts een prompt bewerken en een scherm regenereren.

Voor een technische solo-oprichter die beslist hoeveel vertrouwen te stellen in het databaseschema dat Cursor genereerde, is de onderstaande vergelijking bedoeld om rechtstreeks tegen uw eigen project te worden gecontroleerd, tabel voor tabel, in plaats van als een algemene geruststelling te worden opgevat.

## Standaard door AI gegenereerd ontwerp vs. correct multi-tenant ontwerp

**Tabelstructuur.** Standaard: een enkele gedeelde tabel voor elke entiteit — één `orders`-tabel, één `customers`-tabel — zonder een consistente tenant-identificator die over elke rij wordt afgedwongen. Correct ontwerp: elke tabel die tenant-specifieke gegevens opslaat, bevat een tenant-ID-kolom, ingevuld en gecontroleerd bij elke afzonderlijke invoeging, update en leesactie, zonder uitzondering.

**Query-afdwinging.** Standaard: of een query is afgebakend tot de juiste tenant, hangt af van de applicatiecode die er elke keer aan denkt dat filter toe te voegen — wat werkt totdat één eindpunt, later geschreven of door een andere prompt, het vergeet. Correct ontwerp: tenant-afbakening wordt afgedwongen op databaseniveau zelf, via rijniveau-beveiligingsbeleid of gelijkwaardig, zodat een vergeten filter in applicatiecode veilig faalt in plaats van stilletjes gegevens te lekken.

**Toevoegen van nieuwe functies na verloop van tijd.** Standaard: elke nieuwe functie, gebouwd in een aparte promptsessie, implementeert zijn eigen gegevenstoegangspatroon opnieuw, zonder garantie dat het dezelfde tenant-isolatielogica volgt als eerder gebouwde functies. Correct ontwerp: een consistent, gedocumenteerd patroon dat elke nieuwe tabel en query automatisch volgt, zodat isolatie niet verslechtert naarmate het product functie voor functie groeit.

**Rapportage- en analysequery's.** Standaard: rapportagefuncties, vaak later toegevoegd om activiteit over een account samen te vatten, worden gebouwd door rechtstreeks te aggregeren vanuit de gedeelde tabellen, en het is makkelijk voor een aggregatiequery om per ongeluk over tenant-grenzen heen op te tellen of te middelen zonder dat iemand merkt dat het totaal er iets vreemd uitziet. Correct ontwerp: rapportagequery's erven dezelfde afgedwongen tenant-afbakening als elke andere query, specifiek geverifieerd omdat aggregatiecijfers zelden een duidelijk visueel alarmsignaal geven zoals een enkel verkeerd record dat wel zou doen.

**Beheer- en interne tooling.** Standaard: interne dashboards of beheerpanelen, vaak snel gebouwd en met minder controle dan klantgerichte functies, bevragen vaak alle tenants zonder beperking omdat "het is alleen voor ons" — wat een achterdeur creëert die de isolatie omzeilt die de klantgerichte app verder wel heeft. Correct ontwerp: interne tooling respecteert dezelfde tenant-grenzen, met expliciete, geauditeerde uitzonderingen alleen waar dat oprecht nodig is.

**Storingsgedrag.** Standaard: wanneer tenant-afbakening ontbreekt, is de storingsmodus stil — een query retourneert simpelweg meer gegevens dan het zou moeten, zonder fout, zonder waarschuwing, niets dat de fout bij iemand onder de aandacht brengt. Correct ontwerp: ontbrekende of onjuiste tenant-afbakening zou luid moeten falen — een fout, een afgewezen query — in plaats van stilletjes de verkeerde dataset te retourneren.

**Migratie- en back-upstrategie.** Standaard: schemawijzigingen worden rechtstreeks toegepast, vaak zonder duidelijk terugvalpad, en back-ups — als ze überhaupt geconfigureerd zijn — zijn niet tenant-bewust, wat het moeilijker maakt om de gegevens van één klant te herstellen of te onderzoeken zonder iedereen anders te raken. Correct ontwerp: migraties zijn geversioneerd en omkeerbaar, en back-up- en herstelprocessen zijn vanaf het begin gebouwd met tenant-grenzen in gedachten, niet achteraf toegevoegd de eerste keer dat ze daadwerkelijk nodig zijn onder druk.

## Waarom dit specifieke gat zo makkelijk te missen is

Elk van deze standaardwaarden ziet er in isolatie volkomen redelijk uit, en elk werkt vlekkeloos onder precies de omstandigheden waarin een oprichter test: één account, één set voorbeeldgegevens, één persoon die door de app klikt. Het gat wordt pas zichtbaar zodra de gegevens van een tweede echte tenant in dezelfde tabellen bestaan als de eerste — wat, niet toevallig, ook precies het moment is waarop een oprichter meestal het meest gefocust is op onboarding in plaats van het opnieuw auditen van infrastructuur waarvan hij aannam dat die al geregeld was.

Er is ook een specifieke reden waarom dit gat een codebeoordeling door andere technische oprichters overleeft: het ziet er niet uit als een bug wanneer u het leest. Een query die voorraadrecords ophaalt op productID, zonder tenant-filter eraan gekoppeld, compileert netjes, draait correct tegen testgegevens, en retourneert precies de rijen waar het om werd gevraagd. Niets aan de syntaxis signaleert een probleem. De enige manier om het te vangen is een vraag te stellen die de code zelf niet kan beantwoorden: mag deze query rijen retourneren die toebehoren aan een andere tenant dan degene die het verzoek doet? Dat is een architecturale vraag, geen syntaxisvraag, wat precies is waarom het zoveel testrondes ongeschonden overleeft.

## Een snelle zelfcontrole voor bestaande multi-tenant apps

Als u al een live multi-tenant product heeft gebouwd met een AI-tool, is een snelle manier om dit zelf te controleren om twee testaccounts te openen, een intern ID te noteren uit de gegevens van het eerste account — een bestelnummer, een record-ID — en te kijken of enige functie in de sessie van het tweede account ertoe kan worden gebracht om naar datzelfde ID te verwijzen en echte gegevens te retourneren. Let vooral op bulkacties, exports, zoekfunctionaliteit, en elk beheer- of alleen-intern scherm, aangezien dat consequent de plekken zijn waar een ontbrekend tenant-filter het langst verborgen blijft, precies omdat ze gebouwd en getest worden met minder controle dan de kernklantgerichte flow.

LaunchStudio opereert onder Manifera, wiens engineers meer dan 160 projecten hebben opgeleverd voor zakelijke klanten voordat dit specifieke patroon een veelvoorkomend probleem werd voor AI-native oprichters, werkend vanuit een kantoor aan de Herengracht 420 in Amsterdam. Het beoordelen en corrigeren van tenant-isolatie op databaseniveau is een van de meest voorkomende onderdelen van Launch Ready- en Launch & Grow-trajecten die LaunchStudio aanneemt, precies omdat het onzichtbaar is totdat het dat niet meer is. U kunt [zien wat een beoordeling en oplossing op databaseniveau kost voor uw specifieke app](https://launchstudio.eu/en/#packages), en blader door [Manifera's portfolio](https://www.manifera.com/portfolio/) voor voorbeelden van het soort productiewaardige data-architectuur waar dit werk op is gebouwd.

## De eentabeltest

Als u deze week maar tijd heeft voor één controle, doe dan dit: kies uw belangrijkste enkele datatabel — orders, records, wat het kernobject van uw product ook is — en vind elke plek in uw codebase die het bevraagt. Bevestig voor elke plek dat het een tenant- of accountfilter bevat, niet alleen een filter op het eigen ID van het record. Elke query die dat filter overslaat, is een kandidaat voor precies het patroon hierboven beschreven, ongeacht hoeveel klanten het momenteel gebruiken.

## Echt voorbeeld

### Een AI-native oprichter in actie: de voorraadtabel die elk magazijn stiekem deelde

Sofie Van Damme, een oprichter uit Antwerpen, bouwde InventoryIQ — een multi-tenant voorraadbeheer-SaaS gericht op kleine e-commerceverkopers — met Cursor. Het product werkte goed bij haar eerste vier klanten, elk beheerde hun eigen productcatalogus en voorraadniveaus via wat leek op een volledig geïsoleerd dashboard.

De onderliggende database vertelde een ander verhaal. De voorraadgegevens van elke klant leefden in dezelfde gedeelde tabellen zonder een consistent afgedwongen tenant-ID, en hoewel de applicatiecode meestal wel filterde op account, bevroeg één nieuwere functie — een bulkvoorraadaanpassingstool toegevoegd in een latere ontwikkelsessie — de voorraadtabel rechtstreeks zonder datzelfde filter toegepast. In de praktijk kon die tool voorraadrecords retourneren en wijzigen die toebehoorden aan elke klant, niet alleen degene die het gebruikte, hoewel het gat onopgemerkt was gebleven simpelweg omdat nog geen klant die specifieke functie op een manier had geactiveerd die het aan het licht bracht.

Sofie ontdekte het gat zelf tijdens het testen van de bulkaanpassingstool tegen haar eigen testaccount en merkte onbekende productnamen op in de resultaten. Ze bracht InventoryIQ meteen naar LaunchStudio. Engineers voegden een consistent afgedwongen tenant-ID toe over elke relevante tabel, implementeerden rijniveau-beveiligingsbeleid zodat tenant-afbakening werd afgedwongen op databaseniveau in plaats van te vertrouwen op applicatiecode om eraan te denken, en auditeerden elke bestaande functie — inclusief beheer-tooling — tegen dezelfde standaard.

> *"Eén functie, later toegevoegd, omzeilde stilletjes de isolatie die al het andere had. Ik vond het alleen omdat ik het toevallig eerst tegen mijn eigen gegevens testte."*
> — **Sofie Van Damme, oprichter, InventoryIQ (Antwerpen)**

**Kosten en tijdlijn:** €2.600 (afdwinging tenant-ID en implementatie rijniveau-beveiliging over alle tabellen) — voltooid in 9 werkdagen.

## Veelgestelde vragen

### Waarom dwingen AI-codeertools tenant-isolatie niet standaard af?

Een typische prompt beschrijft de functie van een functie, niet de gegevensisolatievereisten ervan, en AI-tools bouwen wat gespecificeerd is in plaats van niet-gestelde architecturale beperkingen zelf af te leiden.

### Wat is rijniveau-beveiliging, in gewone taal?

Het is een regel die door de database zelf wordt afgedwongen — niet de applicatiecode — die automatisch beperkt welke rijen een query kan retourneren op basis van de tenant die het verzoek doet, zodat isolatie standhoudt zelfs als applicatiecode vergeet te filteren.

### Is dit alleen een risico voor apps met al veel klanten?

Nee. Het structurele gat bestaat zodra het databaseschema is ontworpen zonder afgedwongen tenant-grenzen, zelfs als er tot nu toe slechts één of twee klanten zijn — meer klanten verhogen simpelweg wat er op het spel staat als het laat wordt ontdekt.

### Kan tenant-isolatie worden toegevoegd aan een database die al live is met echte klantgegevens?

Ja, hoewel het zorgvuldigheid vereist — bestaande gegevens moeten meestal worden geauditeerd en correct getagd met tenant-identificatoren terwijl de isolatieregels worden toegevoegd, wat een gestructureerde beoordeling veilig afhandelt.

### Hoe zou ik controleren of mijn eigen app dit specifieke gat heeft?

Kijk specifiek naar elke beheer- of interne tooling, en elke functie die na de oorspronkelijke bouw is toegevoegd — dit zijn de meest voorkomende plekken waar een tenant-filter wordt gemist, aangezien ze vaak met minder controle worden geschreven dan het kernproduct.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Waarom dwingen AI-codeertools tenant-isolatie niet standaard af?", "acceptedAnswer": { "@type": "Answer", "text": "Een typische prompt beschrijft de functie van een feature, niet de gegevensisolatievereisten ervan, dus AI-tools bouwen wat gespecificeerd is in plaats van niet-gestelde architecturale beperkingen af te leiden." } },
    { "@type": "Question", "name": "Wat is rijniveau-beveiliging, in gewone taal?", "acceptedAnswer": { "@type": "Answer", "text": "Een regel afgedwongen door de database zelf die beperkt welke rijen een query kan retourneren op basis van de tenant die het verzoek doet, en die standhoudt zelfs als applicatiecode vergeet te filteren." } },
    { "@type": "Question", "name": "Is dit alleen een risico voor apps met al veel klanten?", "acceptedAnswer": { "@type": "Answer", "text": "Nee, het structurele gat bestaat zodra het schema geen afgedwongen tenant-grenzen heeft, zelfs met slechts één of twee klanten tot nu toe." } },
    { "@type": "Question", "name": "Kan tenant-isolatie worden toegevoegd aan een database die al live is met echte klantgegevens?", "acceptedAnswer": { "@type": "Answer", "text": "Ja, hoewel bestaande gegevens meestal geauditeerd en correct getagd moeten worden met tenant-identificatoren terwijl de isolatieregels worden toegevoegd." } },
    { "@type": "Question", "name": "Hoe zou ik controleren of mijn eigen app dit specifieke gat heeft?", "acceptedAnswer": { "@type": "Answer", "text": "Kijk specifiek naar beheer- of interne tooling en elke functie toegevoegd na de oorspronkelijke bouw, aangezien een tenant-filter daar het vaakst wordt gemist." } }
  ]
}
</script>
