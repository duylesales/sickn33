---
Titel: "Lovable Betalingen: Marktplaatsuitbetalingen en Wie het Geld Vasthoudt"
Trefwoorden: lovable betalingen, marktplaatsuitbetalingen, gesplitste betalingen, gekoppelde accounts, escrow, aansprakelijkheid platform, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Lovable Betalingen: Marktplaatsuitbetalingen en Wie het Geld Vasthoudt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Betalingen: Marktplaatsuitbetalingen en Wie het Geld Vasthoudt",
  "description": "Tweezijdige producten innen geld voor iemand anders, wat verandert wat uw app moet doen en waarvoor u juridisch verantwoordelijk bent. Gekoppelde accounts, timing van uitbetalingen, terugbetalingen tussen twee partijen, en het model dat u moet vermijden.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-payments-marketplace-payouts-and-who-holds-the-money" }
}
</script>

Er is een versie van dit product die een weekend met Lovable voor u bouwt, en die werkt. Klanten betalen op de zakelijke rekening van uw bedrijf. Aan het eind van de maand opent u een spreadsheet, rekent u uit wat elke aanbieder verdiende, trekt u uw commissie eraf en maakt u de overboekingen zelf.

Het werkt bij elf aanbieders. Bij veertig is het een dag per maand. Bij honderd is het een parttimebaan met een complianceprobleem eraan vast, want het in bewaring nemen van andermans geld en het later doorgeven is in de Europese Unie een gereguleerde activiteit, en "ik heb een kleine marktplaats gebouwd" is geen vrijstelling waar iemand van heeft gehoord.

Het alternatief is niet ingewikkelder om te bouwen. Het is alleen anders, en het kiezen voordat u aanbieders hebt is veel goedkoper dan achteraf omzetten.

## Het Model Dat U Moet Vermijden

Geld erin, geld eruit, vanaf uw eigen rekening, heet optreden als betalingstussenpersoon, en het is de opzet die het probleem veroorzaakt.

Er komen drie dingen bij. Het regelgevingsrisico van het aanhouden van gelden van anderen, waar in Nederland en de bredere EU een vergunningsstelsel aan vastzit. Een boekhoudkundig beeld waarin het bruto transactievolume door uw omzet loopt, waardoor uw bedrijf veel groter lijkt dan het is en uw fiscale positie een stuk interessanter wordt dan u wilt. En operationeel risico dat volledig van u is: als een aanbieder betwist wat hem is betaald, is het bewijs uw spreadsheet.

Er is één smal geval waarin het prima is — u bent werkelijk de verkoper, de aanbieder is uw onderaannemer, en u neemt de commerciële verantwoordelijkheid voor de levering. Dat is geen marktplaats. Dat is een bedrijf met leveranciers, en het moet als zodanig worden ingericht en beschreven.

## Gekoppelde Accounts, en Wat Ze Veranderen

De standaardstructuur is dat elke aanbieder een eigen account heeft bij de betaalprovider, gekoppeld aan uw platform. De klant betaalt; de provider splitst de betaling op het moment van inning; uw commissie komt bij u terecht en de rest bij de aanbieder. Het geld staat nooit op uw bankrekening.

Dat verandert uw bouw op vier specifieke punten.

**Onboarding wordt een echte functie.** Elke aanbieder doorloopt identiteitsverificatie bij de provider — naam, adres, bankgegevens, en voor bedrijven de eigendomsstructuur. Uw app moet ze erdoorheen leiden, vertellen wat er nog ontbreekt, en weigeren ze iets te laten aanbieden totdat ze zijn goedgekeurd. Dit kost aanbieders dagen, geen minuten, en elke marktplaats onderschat het.

**Uitbetalingen hebben een timing.** Gelden worden doorgaans een periode vastgehouden voordat ze de aanbieder bereiken, en elke provider doet dat anders. Aanbieders vinden dit veel belangrijker dan u verwacht — kasstroom is de reden dat kleine bedrijven zich bij marktplaatsen aansluiten en de reden dat ze vertrekken. Toon het schema in hun dashboard in plaats van de vraag veertig keer per e-mail te beantwoorden.

**Terugbetalingen worden een probleem met drie partijen.** Als een klant wordt terugbetaald nadat de aanbieder al is uitbetaald, moet het geld ergens vandaan komen. Bepaal het vooraf: van de volgende uitbetaling van de aanbieder, van zijn saldo, of van u. Implementeer het dan, want het alternatief is per geval onderhandelen terwijl een klant wacht.

**Uw commissie is uw omzet, niet de transactie.** Modelleer dit correct vanaf de eerste verkoop. Uw jaarrekening moet de commissie als omzet tonen en de rest als doorstroming, wat zowel juist is als veel makkelijker uit te leggen aan een accountant of een investeerder later.

## Wat Uw Database Moet Bevatten

Wat de provider ook doet, uw applicatie heeft een eigen grootboek nodig, en dat is het deel dat door AI gegenereerde marktplaatscode volledig weglaat.

Voor elke transactie: het brutobedrag, de commissie, het aandeel van de aanbieder, eventuele btw aan beide kanten, de referentie van de provider, de status, en de uitbetaling waartoe ze uiteindelijk behoort. Voor elke aanbieder: verificatiestatus, wat er is uitbetaald, wat er openstaat, en wat er wordt vastgehouden.

Dit grootboek is wat u in staat stelt de vraag van een aanbieder over een betaling uit maart te beantwoorden, het jaaroverzicht te maken dat hij nodig heeft voor zijn eigen boekhouding, en het geval te ontdekken waarin de registratie van de provider en die van u van elkaar afwijken — wat gebeurt, meestal omdat een terugbetaling of geschil ergens werd verwerkt waar uw code niet keek.

Stem het maandelijks af met het rapport van de provider. Automatisch als het kan, met het oog als het moet, maar doe het: een marktplaats waarvan het grootboek stilletjes van de werkelijkheid is afgeweken, is achteraf erg moeilijk te herstellen.

## Btw in een Transactie met Drie Partijen

Vraag hierover advies, want het antwoord hangt af van wat u werkelijk verkoopt en aan wie.

In grote lijnen: uw commissie is een dienst die u aan de aanbieder levert, met een eigen btw-behandeling op basis van waar hij zit en of hij een bedrijf is. Het onderliggende product of de onderliggende dienst wordt door de aanbieder aan de klant geleverd, met een eigen behandeling die doorgaans niet aan u is om te bepalen.

Twee praktische gevolgen voor uw bouw. U geeft facturen uit in twee richtingen — uw commissiefactuur aan de aanbieder, en vaak de factuur van de aanbieder aan de klant namens hem, wat een legitieme regeling is die self-billing heet en zijn instemming vereist. En uw app moet de btw-status van elke aanbieder kennen, want een marktplaats van particulieren en een van geregistreerde bedrijven werken niet op dezelfde manier.

## Vertrouwen en Veiligheid Komen Eerder Dan U Denkt

Elke marktplaats krijgt uiteindelijk een versie van dezelfde middag: een aanbieder die niet leverde, een klant die zegt niet te hebben gekregen waarvoor hij betaalde, en een platform in het midden zonder proces.

U hebt drie dingen nodig vóórdat het gebeurt, niet tijdens. Een manier om een uitbetaling vast te houden — de mogelijkheid om de afrekening van een aanbieder te pauzeren terwijl iets wordt onderzocht, wat achteraf bijna onmogelijk is toe te voegen omdat het geld dan al is verplaatst. Een geschreven verklaring van waar het platform wel en niet verantwoordelijk voor is, in uw voorwaarden, zodat het gesprek vanuit een gedeeld uitgangspunt begint. En een registratie van wat er is afgesproken: de boeking, de berichtenreeks, de annulering, de tijdstempels. Marktplaatsen die communicatie buiten het platform laten plaatsvinden, verliezen het vermogen om over wat dan ook te oordelen.

Opschorting verdient een ontworpen proces, geen geïmproviseerd proces. Een opgeschorte aanbieder moet geen nieuwe boekingen meer ontvangen, toegang houden tot zijn lopende verplichtingen en zijn eigen gegevens, en een duidelijke route naar een oplossing hebben. Een account volledig verwijderen midden in een geschil verandert een slechte week in een advocatenbrief.

Niets hiervan hoeft uitgebreid te zijn bij 30 aanbieders. Het moet alleen bestaan.

## De Rapportages Waar Aanbieders om Zullen Vragen

De vragen komen in een voorspelbare volgorde, en ze goed beantwoorden is een retentiefunctie in plaats van een administratieve last.

In de eerste maand: wat heb ik verdiend, en wanneer komt het binnen? In het eerste kwartaal: welke van mijn aanbiedingen leveren echt geld op? Aan het eind van het jaar: wat geef ik mijn accountant?

De laatste is degene die kleine marktplaatsen verwaarlozen, en de vraag die het meest bepaalt of aanbieders blijven. Een jaaroverzicht — bruto-inkomsten, ingehouden commissie, netto uitbetaald, per maand, met de btw-behandeling vermeld — kost u een middag en bespaart elke aanbieder een avond. Voor een platform waarvan de aanbieders eenmanszaken zijn, is dat een echte reden om u te verkiezen boven het alternatief.

## Eén Providerbeslissing Die U Vroeg Moet Nemen

Niet elke betaalprovider ondersteunt gekoppelde accounts in elk land, en marktplaatsen ontdekken dat op het slechtst denkbare moment — wanneer een aanbieder in België of Duitsland niet kan worden aangesloten.

Controleer drie dingen voordat u zich vastlegt. In welke landen uw aanbieders gevestigd mogen zijn, welke rechtsvormen worden ondersteund (eenmanszaken en eenpersoons-bv's vormen het merendeel van de meeste Nederlandse marktplaatsen en worden anders behandeld dan grotere bv's), en of de betaalmethoden die uw klanten verwachten — iDEAL voorop — werken met gesplitste betalingen in plaats van alleen met directe afschrijvingen.

De antwoorden verschillen per provider en veranderen in de loop van de tijd, dus controleer ze in de actuele documentatie in plaats van in een vergelijkingsartikel. Tien minuten controleren tegen uw werkelijke aanbieders voorkomt de migratie die u anders in maand acht wordt opgedrongen.

## Dit Inrichten

Voor een marktplaats kost dit doorgaans twee tot drie weken in plaats van dagen: een provider gekozen op ondersteuning van gekoppelde accounts in uw markten, onboarding van aanbieders met verificatie gevolgd tot afronding, aanbiedingen pas zichtbaar na geverifieerde status, gesplitste betalingen bij inning met automatisch ingehouden commissie, een transactiegrootboek in uw eigen database, uitbetalingsschema's zichtbaar voor aanbieders, beleid voor terugbetalingen tussen drie partijen bepaald en geïmplementeerd, geschillenafhandeling, self-billing of commissiefacturatie met de juiste btw-behandeling, overzichten voor aanbieders, en maandelijkse afstemming met de provider.

LaunchStudio heeft dit type product herhaaldelijk gebouwd, en de faalwijzen zijn steeds dezelfde. Achter het werk staat Manifera — elf jaar, 120+ engineers, en platformwerk voor klanten als Vodafone, TNO en CFLW, met Europees klantcontact vanaf de Herengracht 420 in Amsterdam.

[Beschrijf uw marktplaats](https://launchstudio.eu/nl/#contact) voordat u de eerste betaling ontvangt — dit is het deel dat later echt duur is om te veranderen.

## Echt voorbeeld

### De Spreadsheet Die een Risico Werd

Pleun Maasland bouwde Atelierplek in Lovable: een platform waar zelfstandige keramisten en grafici ateliertijd en ovenplekken huren bij werkplaatsen in de Randstad. Klanten betalen per sessie; werkplaatsen ontvangen het bedrag minus 12 procent commissie.

Haar eerste versie deed het voor de hand liggende. Betalingen gingen naar de rekening van Atelierplek, en op de vijfde van elke maand rekende ze uit wat elk van de 34 werkplaatsen tegoed had en betaalde ze met de hand uit. Het kostte haar het grootste deel van een dag en was twee keer fout gegaan.

In dezelfde maand kwamen er twee dingen. Een werkplaats vroeg waarom een sessie uit januari nooit in een uitbetaling was verschenen, en het antwoord reconstrueren uit bankafschriften en haar boekingstabel kostte een avond. En haar accountant vertelde haar dat €287.000 aan brutoboekingen in haar omzet stond, wat haar btw-positie veranderde, haar deed lijken op een bedrijf dat meerdere keren groter was dan het werkelijk was, en de vraag opriep of ze dat geld überhaupt mocht aanhouden.

Elf werkdagen: migratie naar gekoppelde accounts, waarbij alle 34 bestaande werkplaatsen via identiteitsverificatie werden aangesloten en aanbiedingen werden geblokkeerd tot goedkeuring; betalingen gesplitst bij inning, zodat de commissie bij Atelierplek binnenkomt en het sessiebedrag direct naar de werkplaats gaat; een transactiegrootboek dat voor elke boeking bruto, commissie, aandeel van de werkplaats, btw en uitbetalingsreferentie vastlegt; uitbetalingsschema's zichtbaar in het dashboard van elke werkplaats; een terugbetalingsbeleid voor annuleringen na uitbetaling, verrekend met de volgende afrekening van de werkplaats met hun instemming in de voorwaarden; self-billing-facturen aan klanten namens werkplaatsen, met een aparte maandelijkse commissiefactuur aan elke werkplaats; jaaroverzichten voor hun eigen boekhouding; en een maandelijkse afstemmingstaak die het grootboek vergelijkt met het rapport van de provider.

**Resultaat:** de handmatige uitbetalingsdag verdween, de omzet in de jaarrekening daalde naar de commissie die Pleun werkelijk verdient, en de vergunningsvraag was van tafel omdat het platform niemands geld meer aanhoudt. In veertien maanden heeft de afstemmingstaak drie verschillen gesignaleerd, allemaal terugbetalingen die buiten de applicatie waren verwerkt, en elk werd in dezelfde week opgelost in plaats van aan het eind van het jaar.

> *"Een dag per maand kon ik mee leven. Ontdekken dat €287.000 van andermans geld door mijn zakelijke rekening was gegaan, was het deel waar ik niet mee kon leven."*
> — **Pleun Maasland, Oprichter, Atelierplek (Haarlem)**

**Kosten & Doorlooptijd:** €7.400 (migratie naar gekoppelde accounts, onboarding van aanbieders met verificatiecontrole, gesplitste betalingen, transactiegrootboek, inzicht in uitbetalingen, terugbetalingen tussen drie partijen, self-billing en commissiefacturatie, overzichten, maandelijkse afstemming) — afgerond in 11 werkdagen.

## Veelgestelde vragen

### Kan ik niet gewoon betalingen innen en aanbieders zelf uitbetalen?

Technisch kan het, en het creëert regelgevingsrisico rond het aanhouden van andermans gelden, blaast uw omzet op met geld dat niet van u is, en laat geschillen met aanbieders rusten op uw spreadsheet. Gekoppelde accounts voorkomen alle drie.

### Hoe lang duurt de onboarding van aanbieders?

Dagen in plaats van minuten, omdat identiteits- en bankverificatie via de provider lopen en soms documenten vereisen. Bouw het als een gevolgd proces met duidelijke status, en laat een aanbieder niets aanbieden voordat het is afgerond.

### Wie betaalt een terugbetaling nadat de aanbieder al is uitbetaald?

Degene die in uw voorwaarden staat, bepaald voordat het gebeurt. Gangbare opties zijn verrekenen met de volgende uitbetaling van de aanbieder of een doorlopend saldo aanhouden. Het onbepaald laten betekent onderhandelen met een aanbieder terwijl een klant wacht.

### Is mijn omzet de transactie of de commissie?

De commissie. Het vanaf de eerste verkoop zo modelleren houdt uw jaarrekening juist en voorkomt een onprettig gesprek met uw accountant over bruto transactievolume in uw omzet.

### Heb ik een eigen transactiegrootboek nodig als de provider er een heeft?

Ja. U moet vragen van aanbieders kunnen beantwoorden, overzichten kunnen maken, en kunnen ontdekken wanneer uw registratie en die van de provider van elkaar afwijken — wat gebeurt, meestal via terugbetalingen of geschillen die buiten uw applicatie zijn verwerkt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan ik marktplaatsbetalingen innen en aanbieders zelf uitbetalen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Technisch wel, maar het creëert regelgevingsrisico rond het aanhouden van andermans gelden, blaast de omzet op met geld dat niet van u is, en laat geschillen rusten op een spreadsheet."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt de onboarding van aanbieders op een marktplaats?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dagen, omdat identiteits- en bankverificatie via de provider lopen en vaak documenten vereisen. Volg het als proces en maak aanbiedingen pas zichtbaar na afronding."
      }
    },
    {
      "@type": "Question",
      "name": "Wie betaalt een terugbetaling nadat de aanbieder is uitbetaald?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Degene die uw voorwaarden noemen — meestal verrekend met de volgende uitbetaling van de aanbieder of een doorlopend saldo. Bepaal het voordat het gebeurt, niet tijdens."
      }
    },
    {
      "@type": "Question",
      "name": "Is de omzet van een marktplaats de transactie of de commissie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De commissie. Modelleer het zo vanaf de eerste verkoop, zodat uw jaarrekening laat zien wat het bedrijf werkelijk verdient."
      }
    },
    {
      "@type": "Question",
      "name": "Heb ik een eigen grootboek nodig als de betaalprovider er een heeft?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja — voor vragen van aanbieders, jaaroverzichten, en het ontdekken van verschillen tussen uw registratie en die van de provider na terugbetalingen of geschillen."
      }
    }
  ]
}
</script>
