---
Titel: "Lovable Supabase: Waar Bedrijfslogica Daadwerkelijk Thuishoort"
Trefwoorden: lovable supabase, database functies, triggers, constraints, supabase security, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-oprichters / Indie Hackers
---

# Lovable Supabase: Waar Bedrijfslogica Daadwerkelijk Thuishoort

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Waar Bedrijfslogica Daadwerkelijk Thuishoort",
  "description": "Regels die alleen in de browser worden afgedwongen zijn vrijblijvende suggesties. Wat er in de database hoort als constraints, functies en triggers, wat in server-side code thuishoort en wat beslist nooit een trigger mag zijn.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-02",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/92-lovable-supabase-where-business-logic-belongs" }
}
</script>

Er is een fundamentele regel waarvan jouw softwareproduct afhankelijk is. Een reservering mag nooit overlappen met een andere boeking. Het totaalbedrag op een factuur moet exact gelijk zijn aan de som van de factuurregels. Een korting mag de totale orderwaarde niet overschrijden. Een bestelling behoort toe aan precies één klantaccount.

Waar bevindt die regel zich in je codebase? Bij een applicatie gebouwd met AI luidt het antwoord vrijwel altijd: in het frontend-scherm waar de gebruiker de gegevens invoert. Dat betekent dat het geen wet is, maar een beleefde suggestie - keurig afgedwongen voor wie via de officiële knoppen klikt, maar volledig afwezig voor iedereen die direct een API-aanroep doet, en onvindbaar voor elk ander datapad binnen je systeem.

Waar een bedrijfsregel leeft is geen theoretische discussie tussen programmeurs. Het bepaalt of je klantdata integer blijft naarmate je bedrijf groeit.

## Vier plekken waar een regel kan leven

**1. In de browser.** Directe feedback, uitstekend voor de gebruikerservaring, maar biedt nul komma nul beveiliging. Alles wat de client afdwingt, kan door een kwaadwillende of een script worden overgeslagen.

**2. In server-side code.** Echte handhaving voor alle verkeer dat netjes via die specifieke API-route loopt. De zwakte is dat software in de loop der tijd meerdere datastromen krijgt: de webapp, een externe API, een nachtelijke cron-job, een Excel-import en een admin-dashboard. Een regel die in één route is geschreven, ontbreekt gegarandeerd in de andere routes.

**3. In de database als een constraint (randvoorwaarde).** Wordt afgedwongen ongeacht hoe de data de database binnenkomt. Kan niet worden omzeild, kan niet worden vergeten, en geldt evengoed voor je eigen ad-hoc beheer-scripts als voor betalende klanten.

**4. In de database als een functie of database-trigger.** Voor complexe regels die meer logica vereisen dan een eenvoudige constraint kan uitdrukken.

Het leidende principe dat vrijwel elk vraagstuk oplost: **hoe dichter een regel bij de data leeft, hoe moeilijker hij te schenden is**. Plaats regels die permanent waar moeten blijven daar waar ze altijd gelden (de database), en plaats al het andere daar waar het het makkelijkst te lezen en testen is (applicatiecode).

## Wat áltijd een database constraint moet zijn

Deze controles kosten de database vrijwel geen rekenkracht en voorkomen complete categorieën aan datacorruptie:

**Verplichte velden gedefinieerd als `NOT NULL`.** Een order zonder gekoppelde klant moet technisch onmogelijk zijn, niet slechts ongebruikelijk.

**Foreign keys (referentiële integriteit).** Een rij die verwijst naar een andere tabel moet gegarandeerd verwijzen naar een record dat daadwerkelijk bestaat. Door AI gegenereerde databaseschema's laten foreign keys opvallend vaak weg; zo ontstaan de mysterieuze 'weesrecords' (orphans) die niemand kan verklaren.

**Uniciteit (Unique constraints) waar het telt.** Eén lidmaatschap per persoon per organisatie, één uniek e-mailadres per account. In de database afgedwongen is dit een harde garantie; in applicatiecode afgedwongen is het wachten op een race condition zodra twee gebruikers gelijktijdig op verzenden klikken.

**Check constraints voor waardebereiken.** Een bestelaantal groter dan nul, een btw-percentage tussen 0 en 100, een einddatum die ná de startdatum ligt. Eén regel SQL per tabel.

**Logische standaarden en timestamps,** automatisch gegenereerd door PostgreSQL (`now()`), in plaats van te hopen dat de frontend-client een betrouwbare systeemtijd meestuurt.

Wanneer je deze regels toevoegt aan een bestaande database, zal de eerste migratiepoging geheid falen. De database zal records ontdekken die de regels nu al schenden. En dat is exact de winst: die foutmeldingen vormen de inventarisatie van de verborgen dataproblemen die je vandaag al hebt.

## Waar functies en triggers hun waarde bewijzen

Sommige regels zijn te complex voor een statische constraint. Een select aantal hoort daadwerkelijk thuis in de database als triggers en stored procedures:

**Gegarandeerde audit trails.** Een database-trigger die elke wijziging automatisch wegschrijft naar een alleen-lezen loggingtabel kan door geen enkele nieuwe ontwikkelaar of API-route worden vergeten - precies de eigenschap die een wettelijk auditspoor vereist.

**Afgeleide waarden die nooit mogen afwijken.** Een gecachet factuurtotaal, een zoekvector of een geaggregeerde teller. Een trigger die deze consistent houdt is betrouwbaarder dan hopen dat elke update-query in de applicatiecode eraan denkt om de teller handmatig op te hogen.

**Atomaire bewerkingen met meerdere stappen.** Een saldo overboeken tussen twee accounts, een plaats toekennen uit een beperkte capaciteit, of een opeenvolgend factuurnummer zonder gaten toewijzen. Een PostgreSQL-functie die draait binnen één database-transactie is hiervoor het enige juiste instrument; in applicatiecode leidt dit onherroepelijk tot overboekingen.

**Voorkomen van overlappende periodes.** Kamerreserveringen, dienstroosters of machineplanningen. PostgreSQL beschikt over geavanceerde `EXCLUDE USING gist`-constraints die overlappende tijdvakken wiskundig uitsluiten - iets wat in gewone applicatiecode nagenoeg onmogelijk waterdicht te bouwen is.

## Wat beslist géén trigger moet zijn

Een noodzakelijk tegenwicht, want doorslaan in database-triggers leidt tot een operationeel moeras:

**Alles wat een externe API of netwerkdienst aanroept.** Een trigger die een e-mail verstuurt of een betaal-API aanroept laat je complete database wachten op een extern systeem. Een netwerkfout bij de mailserver laat dan de gehele database-transactie crashen, waardoor de gebruiker zijn formulier niet eens kan opslaan.

**Commercieel bedrijfsbeleid dat per kwartaal verandert.** Prijsstaffels, tijdelijke kortingsacties en loyaliteitsregels veranderen continu en horen thuis in overzichtelijke, testbare applicatiecode.

**Lange berekeningen.** Triggers moeten binnen milliseconden klaar zijn. Trage triggers maken elke schrijfoperatie in je database tergend langzaam, inclusief bewerkingen die niets met de regel te maken hebben.

**Complexe kettingreacties.** Triggers die op hun beurt weer andere triggers afvuren worden onmogelijk te doorgronden en maken foutopsporing tot een nachtmerrie. Twee niveaus diep is doorgaans al één niveau te veel.

De vuistregel: **gebruik de database voor invarianten** - zaken die over de data zelf permanent waar moeten zijn. **Gebruik applicatiecode voor beleid** - regels die gelden omdat het management dat dit kwartaal heeft afgesproken.

## Waarom gegenereerde software dit stelselmatig fout doet

Dit gebeurt niet per toeval, maar door de manier waarop AI-tools werken.

Een generatieve tool bouwt een interface om aan een specifieke prompt te voldoen. Validatie in die interface is direct zichtbaar, reageert interactief en bewijst aan de gebruiker dat de feature werkt. Constraints in de database zijn onzichtbaar, vereisen een formele databasemigratie en veranderen visueel niets aan de gedemonstreerde feature. De AI bouwt ze dus simpelweg niet, tenzij je er expliciet om vraagt.

Het resultaat is een database vol met permissieve kolommen (`nullable`), waarbij regels verspreid liggen over schermen die toevallig als eerste werden geprompt, en drie schermen dezelfde regel subtiel anders valideren. De oplossing is expliciet instrueren: *"voeg een foreign key toe"*, *"maak deze kolom not-null"*, *"dwing deze uniciteit af via een database constraint"*. AI-modellen voeren dit uitmuntend uit wanneer je erom vraagt, maar zullen het nooit uit zichzelf voorstellen.

## Migreren van schermvalidatie naar echte database-afspraken

Het structureel versterken van een actieve applicatie met bestaande data verloopt via een vaste route:

Schrijf de bedrijfsregels op in gewone mensentaal. Voer voor elke regel een SQL-query uit om te controleren hoeveel bestaande rijen de regel schenden - dit getal is steevast hoger dan verwacht. Bepaal hoe de vervuilde data gecorrigeerd moet worden (soms in overleg met de klant). Corrigeer de data, voeg de constraint toe en verwijder de overbodige, gedupliceerde validatielogica uit je schermen. Behoud de frontend-validatie puur voor snelle feedback naar de gebruiker, maar vertrouw er nooit meer op als beveiligingslaag.

Begin altijd bij de regels met de hoogste bedrijfswaarde: alles wat geld raakt, eigendomsrechten van tenants en uniciteit.

## Het schema vastleggen waar je het kunt zien

Nog één cruciaal punt, want hier gaat het in productie vaak mis:

Constraints, functies en triggers die je handmatig aanmaakt via het Supabase-dashboard bestaan uitsluitend in die ene specifieke database. Je Git-repository heeft er geen weet van, verschillende omgevingen groeien uit elkaar en een herstelactie vanuit een back-up levert een database op mét data maar zónder je bedrijfsregels. Bewaar alle database-aanpassingen als genummerde SQL-migratiebestanden in je repository. Dit maakt wijzigingen inzichtelijk en traceerbaar via code reviews.

## De zojuist toegevoegde regels doelbewust testen

Een constraint die je nog nooit opzettelijk hebt proberen te breken, is louter een aanname. Vijftien minuten doelbewust wangedrag verandert een aanname in een bewezen zekerheid:

**Probeer elke regel rechtstreeks te schenden.** Niet via de schermen van je app, maar via de Supabase SQL Editor of via een API-aanroep met je publieke anon-key. Probeer een order aan te maken zonder klant-ID. Voeg een tweede lidmaatschap toe voor dezelfde gebruiker. Voer een negatief factuurbedrag in. Elke poging moet direct door de database worden afgewezen met een duidelijke foutcode; slaagt er één, dan is de regel niet actief.

**Controleer hoe je applicatie reageert op een databasefout.** Vang de specifieke constraint-fouten op in je frontend en vertaal ze naar begrijpelijke zinnen voor de gebruiker: *"Dit e-mailadres is al in gebruik"*, in plaats van een cryptische PostgreSQL-error die interne tabelnamen lekt.

**Test gelijktijdigheid (concurrency).** Open twee verschillende browsers en claim exact op hetzelfde moment de allerlaatste beschikbare plek. Validatie in de browser faalt bij gelijktijdigheid; een database-transactie slaagt gegarandeerd.

## De datalaag zichzelf laten handhaven

Voor een bestaand product is dit een overzichtelijk traject: bedrijfsregels inventariseren, dataviolaties opsporen en herstellen, constraints en foreign keys activeren, atomaire functies inrichten voor capaciteitsberekeningen, audit trails borgen via triggers en de complete datastructuur vastleggen in Git-migraties.

LaunchStudio voert dit werk uit in samenhang met het autorisatiemodel (RLS), omdat beide direct in PostgreSQL leven en bij AI-applicaties meestal gelijktijdig ontbreken. De engineers zijn afkomstig van Manifera: elf jaar ervaring met enterprise PostgreSQL-architecturen voor klanten zoals Vodafone, TNO en CFLW vanuit Amsterdam Herengracht 420 en Ho Chi Minhstad.

[Deel de regels van jouw product met ons](https://launchstudio.eu/nl/#contact) voor een technisch assessment binnen één werkdag, of bekijk onze [pakketten](https://launchstudio.eu/nl/#packages).

## Echt voorbeeld

### Elf onkostendeclaraties dubbel uitbetaald

Carola Mudde bouwde met Lovable het platform Declaratie: een declaratieverwerkingssysteem voor twee kleinere gemeenten, een woningstichting en vier culturele instellingen in de regio Sittard en Geleen, goed voor circa 1.400 declaraties per maand.

Alle bedrijfsregels stonden in het invoerscherm van de webapp. Een declaratie mocht niet hoger zijn dan € 500 zonder goedkeuring van een leidinggevende, een aankoopbon was verplicht boven € 50, en een declaratie kon slechts één keer worden ingediend. Alle drie de controles werden uitgevoerd in de browser.

Drie problemen dienden zich gelijktijdig aan. Een financieel medewerker bij een gemeente gebruikte een door Carola gebouwde Excel-importfunctie voor bulk-invoer. Die import liep niet via de webpagina en controleerde dus niets - 60 declaraties werden zonder aankoopbon geïmporteerd. Een dubbelklik op de verzendknop bij een trage internetverbinding leidde ertoe dat elf declaraties dubbel in het systeem belandden, waarvan er acht daadwerkelijk dubbel werden uitbetaald vóórdat de accountantscontrole plaatsvond. En een stagiair ontdekte dat het bedrag na formele goedkeuring nog kon worden gewijzigd via een directe API-call, omdat de statuscontrole uitsluitend in de gebruikersinterface zat; twee declaraties waren na goedkeuring aangepast.

De database bevatte geen enkele constraint: geen foreign keys, geen unieke sleutels, en elke kolom accepteerde `NULL`.

In negen werkdagen werd de datalaag definitief dichtgetimmerd: de regels werden formeel vastgelegd in overleg met de zeven organisaties; een analyse bracht 214 rijen aan het licht die regels schonden, waaronder 31 declaraties zonder geldige koepelorganisatie; de vervuilde records werden gecorrigeerd; `NOT NULL`- en foreign key-constraints werden toegevoegd op elf tabellen; een unieke constraint op de combinatie van medewerker, datum, bedrag en omschrijving sloot dubbele indieningen definitief uit; check constraints bewaakten de bedragen en een trigger forceerde de aanwezigheid van een bijlage ongeacht de invoerroute; de goedkeuringsstatus werd onveranderbaar gemaakt na accordering via een trigger met een gekoppelde audit-tabel; de Excel-importmodule werd herschreven om exact dezelfde databaseregels te doorlopen; en alle wijzigingen werden vastgelegd in SQL-migraties.

De acht onterechte betalingen werden in de twee maanden daarna verrekend. De gemanipuleerde declaratie werd intern door de betreffende organisatie afgehandeld.

**Resultaat:** Nul dubbele of ongeoorloofde declaraties in de veertien maanden daarna, en het geautomatiseerde auditspoor is inmiddels het standaarddocument dat de accountant van de gemeente bij elke jaarrekening opvraagt.

> *"Mijn bedrijfsregels waren geprogrammeerd in één scherm, terwijl er drie routes waren waarlangs data het systeem binnenkwam. Eén daarvan was een importfunctie die ik zelf had gebouwd."*
> - **Carola Mudde, Oprichter, Declaratie (Sittard)**

**Kosten & Doorlooptijd:** € 4.900 (definitie bedrijfsregels, dataherstel 214 rijen, foreign keys en constraints, uniciteits- en onveranderbaarheidstriggers, audit trail, importmodule herschrijven, migraties) - opgeleverd in 9 werkdagen.

## Veelgestelde vragen

### Waarom is validatie in de browser onvoldoende voor bedrijfszekerheid?

Omdat controles aan de voorkant door iedereen omzeild kunnen worden, en omdat software altijd alternatieve datastromen krijgt: externe API-koppelingen, batch-imports, achtergrondtaken en beheer-omgevingen. Een regel die alleen in een invoerscherm staat, ontbreekt in al die andere routes.

### Welke regels moeten áltijd als database constraint worden ingericht?

Verplichte velden als `NOT NULL`, foreign keys om relaties te garanderen, uniciteitsregels voor e-mails en lidmaatschappen, check constraints voor getals- en datumbereiken, en automatische databasestimestamps. Elk kost één regel SQL en voorkomt structurele datacorruptie.

### Wanneer is een database-trigger het juiste instrument?

Voor waterdichte audit trails die niet vergeten mogen worden, berekende totalen die nooit uit de pas mogen lopen, atomaire transacties (zoals het toewijzen van schaarse voorraad), en wiskundige overlap-preventie bij kamer- of personeelsplanningen.

### Wat hoort beslist níét thuis in een database-trigger?

Aanroepen naar externe webhooks of mailservers, veranderlijk commercieel kortingsbeleid, trage dataverwerkingen en ingewikkelde kettingen van triggers die elkaar beïnvloeden. Gebruik de database voor harde data-invarianten en applicatiecode voor beleid.

### Hoe voeg ik constraints toe aan een database die al vol met klantdata zit?

Verwacht dat de eerste migratie faalt doordat bestaande data de nieuwe regels schendt - die foutenlijst is exact het startpunt. Inventariseer de overtredingen, corrigeer de historische data in overleg met je gebruikers, activeer vervolgens de constraint en saneer daarna overbodige frontend-code.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom is validatie in de browser onvoldoende voor bedrijfszekerheid?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Frontend-validatie kan worden omzeild en ontbreekt bij alternatieve invoerroutes zoals API's, Excel-imports en achtergrondtaken."
      }
    },
    {
      "@type": "Question",
      "name": "Welke regels moeten áltijd als database constraint worden ingericht?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "NOT NULL op verplichte velden, foreign keys, uniciteitsregels, check constraints op bedragen en datums, en server-gegenereerde timestamps."
      }
    },
    {
      "@type": "Question",
      "name": "Wanneer is een database-trigger het juiste instrument?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor audit trails, afgeleide totalen die synchroon moeten blijven, atomaire capaciteitstoewijzingen en overlap-preventie bij roosters."
      }
    },
    {
      "@type": "Question",
      "name": "Wat hoort beslist níét thuis in een database-trigger?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Externe API-calls, mailverkeer, continu veranderend prijsbeleid, langdurige taken en cascades van triggers."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voeg ik constraints toe aan een database die al vol met klantdata zit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Spoor schendingen op via SQL, saneer de data met klanten, activeer de constraint en verwijder gedupliceerde schermvalidaties."
      }
    }
  ]
}
</script>
