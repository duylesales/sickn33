---
Titel: "Cursor en Documentatie: Een Codebase Uitlegbaar Houden"
Trefwoorden: cursor documentatie, README, architectuurbeslissingen, overdracht, AI-leesbare documentatie, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Cursor en Documentatie: Een Codebase Uitlegbaar Houden

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cursor en Documentatie: Een Codebase Uitlegbaar Houden",
  "description": "In een product dat grotendeels door tools is geschreven, is documentatie het enige overzicht van waarom iets is zoals het is. De vier documenten die het hebben waard zijn, geschreven voor zowel de volgende persoon als de volgende AI-sessie.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-29",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/cursor-and-documentation-keeping-a-codebase-explainable" }
}
</script>

In een codebase die met de hand is geschreven, draagt de code een deel van haar eigen uitleg. Wie een functie schreef, koos haar structuur om een reden, en zelfs zonder commentaar weerspiegelt de vorm een bedoeling.

Gegenereerde code heeft dat niet. Ze weerspiegelt een patroon dat statistisch passend was, en de reden waarom uw product iets op een bepaalde manier doet, bestaat alleen in een gesprek dat inmiddels is gesloten.

Dat maakt documentatie hier waardevoller, en ze heeft een tweede publiek dat ze eerder niet had: de tool die volgende maand wordt gevraagd deze code te wijzigen, leest de repository, en wat hij daar vindt, bepaalt de kwaliteit van wat hij oplevert.

## Vier Documenten, Niets Meer

**Een README** die beantwoordt hoe u dit ding draait: wat het is, wat het nodig heeft, de commando's om het in te richten en te starten, en waar de omgevingen zijn. Geschreven voor iemand die het project nooit heeft gezien, en daar hoort u ook bij na vier maanden aan iets anders.

**Een afsprakenbestand** — het bestand dat deze reeks steeds aanbeveelt — dat patronen, naamgeving, gekozen bibliotheken, de regels die niet gebroken mogen worden en de woordenschat van het product beschrijft. Gelezen door mensen en door assistenten.

**Een beslissingenlogboek.** Een lijst met keuzes en waarom, met datums. Waarom Supabase in plaats van een database die u zelf draait. Waarom betalingen via één aanbieder lopen. Waarom facturen onveranderlijk zijn. Drie zinnen per stuk.

**Een operationele pagina.** Wat er volgens schema draait, wat u doet als er iets breekt, waar de back-ups staan en hoe u er een terugzet, wie u bij elke aanbieder kunt bereiken. Dit is het document waarvoor u dankbaar zult zijn om zeven uur op een zondagochtend.

Vier bestanden, misschien zes pagina's in totaal. Meer dan dat wordt niet bijgehouden.

## Schrijf Op Waarom, Niet Wat

De code zegt wat ze doet. Documentatie die dat herhaalt, is een tweede kopie die gelijk moet blijven, en die blijft niet gelijk.

Wat de code niet kan zeggen, is waarom. Waarom deze aanpak in plaats van de voor de hand liggende. Waarom deze limiet 50 is en niet 100. Waarom deze ogenschijnlijk overbodige controle bestaat — omdat de import van een klant in maart duplicaten opleverde en dit dat voorkomt.

Die laatste categorie is het waardevolste wat u kunt opschrijven, omdat dat precies is wat bij een toekomstige opschoning wordt verwijderd, door mens of machine. Een commentaar dat zegt "dit lijkt overbodig; het voorkomt de dubbele rijen beschreven in beslissing 14" is een commentaar dat een incident bespaart.

## Het Beslissingenlogboek Is het Waardevolste Document

Het is ook het document dat niemand schrijft, omdat de redenering op het moment van de beslissing vanzelfsprekend en blijvend voelt.

Zes maanden later is ze geen van beide. De vraag "waarom doet ons product het zo" komt van een nieuwe developer, van een klant, van een investeerder, of van uzelf, en het eerlijke antwoord is meestal dat niemand het nog weet.

Houd het belachelijk licht, anders gebeurt het niet. Een bestand, een gedateerde regel, drie zinnen: wat werd besloten, wat de alternatieven waren, waarom deze. Geschreven op het moment zelf, niet achteraf.

De regels die er het meest toe doen: alles wat u koos tegen een voor de hand liggend alternatief in, alles waarover u anders opnieuw de discussie zou voeren, en alles wat een toekomstige lezer zonder de context als een fout zou beschouwen.

## Schrijf Het Zo Dat de Tools Het Kunnen Gebruiken

Dit is het deel dat specifiek is voor deze manier van bouwen, en het verandert hoe goede documentatie eruitziet.

Assistenten lezen de repository. Documentatie die regels duidelijk formuleert, korte voorbeelden geeft en een consistente woordenschat gebruikt, verbetert meetbaar wat ze genereren. Documentatie die uitweidt, of die ergens anders in een wiki staat, doet helemaal niets.

Drie praktische gevolgen. Houd het in de repository, als platte tekst, naast de code. Formuleer regels als regels — "elk endpoint moet de organisatie van de aanroeper controleren" in plaats van een alinea over het belang van autorisatie. En neem van elk patroon een kort voorbeeld op, omdat een model voorbeelden veel betrouwbaarder imiteert dan dat het proza volgt.

Dezelfde eigenschappen maken het beter voor mensen, wat handig is, en het betekent dat de documentatie één keer voor beide doelgroepen wordt geschreven in plaats van twee keer.

## Genereer de Saaie Delen, Schrijf de Rest

Een assistent is goed in het maken van documentatie die structuur beschrijft: wat deze module bevat, wat deze functie aanneemt en teruggeeft, wat deze endpoints zijn. Dat is echt nuttig en vervelend om te schrijven.

Hij kan het waarom niet schrijven, omdat het waarom nooit in de code stond. Een model vragen uw beslissingen te documenteren, levert plausibele redeneringen op die niet de uwe waren, en dat is erger dan een leeg bestand — het is een zelfverzekerd verslag van iets dat niet is gebeurd.

Dus: genereer het referentiemateriaal, schrijf de beslissingen zelf. Drie zinnen op het moment van de beslissing, het enige moment waarop de redenering beschikbaar is.

## De Documentatie Die Uw Klanten Nodig Hebben

Alles hierboven is intern. Een product heeft ook documentatie nodig die naar buiten is gericht, en voor een klein B2B-product doet die meer werk dan oprichters verwachten.

Drie onderdelen, in volgorde van waarde.

**Aan de slag.** De kortste weg van een nieuw account naar datgene waarvoor uw product bestaat. Geen rondleiding langs elke functie — één volgorde, met de beslissingen die iemand bij elke stap moet nemen. Dit vermindert het supportvolume meer dan welke andere pagina ook, en het is de pagina die de meeste producten niet hebben.

**Antwoorden op de vragen die mensen stellen.** Rechtstreeks uit uw supportinbox, in de woorden die klanten gebruiken. Zoals de SEO-artikelen in deze reeks opmerken, dienen deze ook als content die de juiste bezoekers trekt.

**Een naslag voor wat mensen instellen.** Integratie-instellingen, rechten, importformaten, de velden in een export. Droog, specifiek en geraadpleegd in plaats van gelezen.

Twee eigenschappen doen er meer toe dan volledigheid. Het moet actueel zijn, omdat documentatie die een vorige versie van de interface beschrijft erger is dan geen. En het moet ergens staan waar een klant het kan vinden zonder te vragen — openbaar, doorzoekbaar, gelinkt vanuit het product op de plek waar elk ding wordt gedaan.

Voor een product met een handvol klanten kan dit vijf pagina's zijn. De toets of het genoeg is, is eenvoudig: als een klant iets vraagt, is er dan een pagina die u kunt sturen? Is het antwoord meestal nee, dan kost het schrijven van die pagina na het beantwoorden vijftien minuten, en hoeft de vraag nooit meer te worden beantwoord.

## Documentatie als Overdrachtsbezit

Er komt uiteindelijk een moment waarop iemand anders dan u aan het product moet werken: een freelancer, een werknemer, de technische beoordelaar van een overnemer, of een partner die het onderhoudt terwijl u iets anders doet.

Wat die persoon ontvangt, bepaalt of de overgang een week of een kwartaal duurt, en het verschil zit bijna volledig in deze documenten in plaats van in de code.

Met deze documenten kan een competente developer binnen een dag productief zijn: hij weet hoe het draait, wat de afspraken zijn, waarom de ongebruikelijke beslissingen werden genomen, en wat er gebeurt als er 's nachts iets breekt.

Zonder deze documenten besteedt dezelfde persoon twee weken aan het lezen van code om af te leiden wat een pagina hem had verteld, en komt hij tot conclusies die soms fout zijn — omdat het afleiden van bedoelingen uit gegenereerde code zelfverzekerde misverstanden oplevert, hetzelfde probleem waarmee dit artikel begon.

Er is ook een commerciële kant. Een product dat één persoon kan uitleggen, is een product met een sleutelpersoonrisico, en elke serieuze koper of investeerder ziet dat direct. Vier documenten in een repository zijn geen vervanging voor een tweede persoon die het systeem kent, en ze zijn de goedkoopste beschikbare verkleining van dat risico — wat voor een oprichter die denkt aan verkopen, geld ophalen of gewoon op vakantie gaan, aanzienlijk meer waard is dan de halve dag die het kost.

Een nuttige manier om te toetsen of u genoeg hebt: geef de repository aan iemand die hem nooit heeft gezien en vraag hem het draaiend te krijgen en te beschrijven wat het doet. Wat hij niet kan uitvogelen, is wat ontbreekt, en dat uitzoeken kost een middag.

## Dit Inrichten

Voor een bestaand project is dit doorgaans een halve dag: een README over inrichting en omgevingen, een afsprakenbestand met patronen, naamgeving, gekozen bibliotheken, onschendbare regels en woordenschat, een beslissingenlogboek gevuld met de tien keuzes die u zich nog herinnert en hun redenen, een operationele pagina over gepland werk, procedures bij storingen, back-ups en contacten bij aanbieders, commentaar toegevoegd waar code overbodig lijkt maar dat niet is, gegenereerde referentiedocumentatie voor de structuur, alles in de repository als platte tekst, en een gewoonte om de beslissingsregel op het moment zelf te schrijven in plaats van achteraf.

LaunchStudio levert alle vier wanneer we een product teruggeven aan de eigenaar, omdat een product dat u niet kunt uitleggen een product is dat u aan niemand kunt overdragen. De engineers zijn van Manifera — elf jaar, 160+ projecten, vanuit Amsterdam en Ho Chi Minh-stad.

[Vraag ons hoe uw project eruitziet voor iemand die het nooit heeft gezien](https://launchstudio.eu/nl/#contact).

## Echt voorbeeld

### De Controle Die Niemand Kon Uitleggen

Pieter-Jan Osseweijer bouwde Subsidieaanvraag in Cursor: administratie van subsidieaanvragen voor agrarische adviseurs en hun klanten, met zo'n 900 aanvragen per jaar voor 26 adviesbureaus.

Een AI-sessie die de validatiecode opruimde, verwijderde een conditie die overbodig leek: een controle die aanvragen afwees waarbij de perceeloppervlakte een drempel overschreed ten opzichte van het geregistreerde bedrijf. Ze had geen commentaar en geen test, en niets in de code verklaarde haar.

Ze bestond omdat een provinciale overheid het jaar ervoor 40 aanvragen had afgewezen om precies die mismatch, en de controle was toegevoegd om die vóór indiening op te vangen.

De verwijdering bleef twee maanden onopgemerkt. Eenendertig aanvragen werden met de mismatch ingediend en afgewezen, een aantal na de deadline van die ronde, wat voor vier boerenbedrijven betekende dat ze een financieringsronde volledig misliepen.

Drie werkdagen: de controle hersteld met een commentaar dat uitlegt wat ze voorkomt en een test afgeleid van de gepubliceerde regels van de overheid; een beslissingenlogboek gestart, gevuld met veertien regels over de keuzes die Pieter-Jan nog kon reconstrueren — waarom aanvragen na indiening onveranderlijk zijn, waarom de provinciale regels als data in plaats van code worden opgeslagen, waarom één aanbieder werd gekozen voor het genereren van documenten; een README over inrichting en omgevingen, die nooit had bestaan; een afsprakenbestand met patronen, naamgeving en vier onschendbare regels; een operationele pagina over de nachtelijke indieningstaak, back-ups, terugzetprocedure en contacten bij aanbieders; commentaar toegevoegd bij zes andere stukken code die overbodig leken en dat niet waren, elk met een verwijzing naar de bijbehorende beslissing; en referentiedocumentatie gegenereerd voor de endpointstructuur.

**Resultaat:** er zijn geen controles meer verwijderd. Pieter-Jan meldt dat het beslissingenlogboek vaker is geraadpleegd dan hij verwachtte — twee keer door een adviseur die vroeg waarom het product zich op een bepaalde manier gedraagt, één keer door een provinciale overheid, en herhaaldelijk door hemzelf.

> *"Een sessie verwijderde een controle die zinloos leek. Ze was zinloos, tenzij je wist dat het jaar ervoor veertig aanvragen om precies die reden waren afgewezen, en niets in mijn product wist dat."*
> — **Pieter-Jan Osseweijer, Oprichter, Subsidieaanvraag (Leeuwarden)**

**Kosten & Doorlooptijd:** €2.500 (controle hersteld met tests vanuit de regels, beslissingenlogboek met veertien regels, README, afsprakenbestand, operationele pagina, verklarend commentaar op zes plekken, gegenereerde referentiedocumentatie) — afgerond in 3 werkdagen.

## Veelgestelde vragen

### Waarom doet documentatie er meer toe in een AI-gebouwd product?

Omdat gegenereerde code geen bedoeling draagt. De reden waarom uw product op een bepaalde manier werkt, bestaat alleen in een gesloten gesprek, en de volgende sessie — mens of machine — heeft er geen toegang toe.

### Wat moet ik eigenlijk schrijven?

Vier documenten: hoe u het draait, de afspraken, een beslissingenlogboek met datums en redenering, en een operationele pagina. Ongeveer zes pagina's in totaal.

### Wat is het waardevolste document?

Het beslissingenlogboek. Zes maanden later weet niemand meer waarom een keuze werd gemaakt, en die redenering is wat voorkomt dat een toekomstige opschoning iets dragends verwijdert.

### Kan ik documentatie genereren met de assistent?

Het referentiemateriaal dat structuur beschrijft wel, en dat is er een goede toepassing van. Niet de redenering — een model dat wordt gevraagd waarom u een beslissing nam, levert plausibele redeneringen op die niet de uwe waren.

### Hoe voorkom ik dat documentatie veroudert?

Houd het kort, houd het in de repository, en schrijf beslissingsregels op het moment zelf in plaats van achteraf. Alles wat langer is dan een paar pagina's wordt niet bijgehouden.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom doet documentatie er meer toe in AI-gebouwde producten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Gegenereerde code draagt geen bedoeling — de redenen leven in gesloten gesprekken, ontoegankelijk voor de volgende persoon of sessie."
      }
    },
    {
      "@type": "Question",
      "name": "Welke documentatie heeft een klein product nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een README, een afsprakenbestand, een beslissingenlogboek met datums en redenering, en een operationele pagina — ongeveer zes pagina's in totaal."
      }
    },
    {
      "@type": "Question",
      "name": "Welk document is het waardevolst?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het beslissingenlogboek — het bewaart redeneringen die anders verloren gaan en voorkomt dat toekomstige opschoningen dragende code verwijderen."
      }
    },
    {
      "@type": "Question",
      "name": "Kan een assistent mijn documentatie schrijven?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Structureel referentiemateriaal wel; redeneringen niet — hij levert plausibele rechtvaardigingen op die nooit de uwe waren."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom ik dat documentatie veroudert?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Houd het kort en in de repository, en schrijf beslissingsregels op het moment van beslissen in plaats van achteraf."
      }
    }
  ]
}
</script>
