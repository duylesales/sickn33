---
Titel: "AI-Appbeveiliging: Prompt Injection in Functies Die U Al Hebt Uitgebracht"
Trefwoorden: ai-appbeveiliging, prompt injection, LLM-beveiliging, indirecte injectie, rechten voor tools, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# AI-Appbeveiliging: Prompt Injection in Functies Die U Al Hebt Uitgebracht

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-Appbeveiliging: Prompt Injection in Functies Die U Al Hebt Uitgebracht",
  "description": "Stuurt uw product klanttekst naar een model, dan staan de instructies van een ander al in uw prompt. Wat prompt injection wel en niet kan, waarom filteren faalt, en de grenzen die het echt indammen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-06",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-app-security-prompt-injection-in-features-you-already-shipped" }
}
</script>

Bijna elk product dat in de afgelopen twee jaar is gebouwd, heeft ergens een AI-functie: een samenvatter, een opsteller van antwoorden, een classificeerder, een chatvenster dat vragen beantwoordt over de eigen data van de klant. Ze werden snel toegevoegd, omdat ze makkelijk toe te voegen zijn.

Elk ervan neemt tekst van buiten uw product en zet die in een prompt naast uw eigen instructies. Het model kan niet betrouwbaar onderscheiden welk deel uw instructie is en welk deel data, omdat het voor het model allemaal gewoon tekst is - en dat is het hele probleem.

Prompt injection is geen theoretisch risico waarover op conferenties wordt gesproken. Het is een eigenschap van hoe deze systemen werken, en geen hoeveelheid prompt engineering neemt het weg.

## Waar een Aanvaller Werkelijk op Uit Is

De interessante vraag is niet of het model kan worden overgehaald iets vreemds te zeggen. Het is wat het model mag doen.

Vat uw functie tekst samen en toont ze het resultaat aan degene die het indiende, dan levert een geslaagde injectie een vreemde samenvatting op voor die persoon. Gênant, niet gevaarlijk.

Kan uw functie tools aanroepen - de database bevragen, een e-mail versturen, een HTTP-verzoek doen, een record schrijven, een workflow starten - dan voert een geslaagde injectie die handelingen uit met de rechten van uw applicatie. Dat is het verschil tussen een curiositeit en een incident, en het wordt volledig bepaald door wat u hebt aangesloten.

Dus de eerste vraag voor elke AI-functie die u hebt uitgebracht: wat kan ze doen behalve tekst produceren? Het antwoord is vaak meer dan de oprichter zich herinnert.

## Indirecte Injectie Is Degene Die U Raakt

Directe injectie - een gebruiker die instructies in uw chatvenster typt - is de versie waar iedereen aan denkt, en het is de minder gevaarlijke, omdat de gebruiker zijn eigen sessie aanvalt.

Indirecte injectie is wanneer de kwaadaardige instructie binnenkomt in content die uw product namens iemand anders verwerkt. Een geüpload cv met witte tekst die het screeningsmodel opdraagt de kandidaat hoog te beoordelen. Een supportmail met instructies verstopt in een handtekening. Een webpagina die uw product ophaalt en samenvat. Een document dat een klant met een collega deelt, door uw systeem verwerkt namens die collega.

Hier is de aanvaller niet de gebruiker. De gebruiker is het slachtoffer, en uw product is het mechanisme. Elke functie die content van de ene persoon verwerkt en handelt in de context van een andere, is waar deze soort aanval leeft.

## Filteren Werkt Niet

De instinctieve oplossing is kwaadaardige instructies te detecteren en te verwijderen voordat ze het model bereiken. Dat faalt, betrouwbaar, en begrijpen waarom bespaart weken.

Instructies kunnen op oneindig veel manieren worden geformuleerd, in elke taal, gecodeerd, verspreid over een document, uitgedrukt als een verhaal, of ingebed in structuur in plaats van tekst. Elk filter is een lijst van wat iemand bedacht, en het aanvalsoppervlak is de verzameling dingen waar niemand aan dacht.

Filteren is een beetje moeite waard als verkeersdrempel en geen enkel vertrouwen waard. De verdedigingen die werken, proberen geen onderscheid te maken tussen instructies en data; ze zorgen dat het er niet toe doet.

## De Vier Grenzen Die Wel Werken

**Minimale rechten voor tools.** Wat het model kan aanroepen, kan het worden gemaakt aan te roepen. Geef het de smalst mogelijke set: de eigen records van deze klant lezen, niet willekeurige tabellen bevragen. Niets destructiefs, niets wat geld uitgeeft, niets wat buiten het account reikt waarin het werkt.

**Autorisatie buiten het model.** Laat het model nooit beslissen wie wat mag doen. Het model mag om een handeling vragen; uw code controleert of de huidige gebruiker dat mag, met dezelfde rechtenlogica als de rest van het product. Een geïnjecteerde instructie levert dan een verzoek op dat gewoon wordt geweigerd.

**Een mens ertussen bij alles wat onomkeerbaar is.** Een e-mail versturen, een betaling doen, data verwijderen, iets publiceren. Het model maakt een concept en een persoon keurt goed. Deze ene maatregel neemt de meeste realistische schade weg.

**Behandel uitvoer als onbetrouwbaar.** Modeluitvoer is data uit een onbetrouwbare bron, geen fragment van uw applicatie. Toon haar nooit als ruwe HTML, voer haar nooit uit, stop haar nooit in een databasequery of een shellcommando. Een injectie waarvan de payload een scripttag is, doet er alleen toe als u die uitvoer zonder escaping in een pagina zet.

## Scheid de Onbetrouwbare Tekst

Structuur helpt, ook al lost ze het probleem niet op. Zet uw instructies in de systeemrol en de onbetrouwbare content in een gebruikersbericht, duidelijk afgebakend, met de vermelding dat alles binnen de afbakening data is om te verwerken en geen instructies om op te volgen.

Dat verhoogt de benodigde moeite en vermindert de toevallige gevallen - de klant die in een supportticket toevallig "negeer het bovenstaande" schreef. Het houdt een vastberaden poging niet tegen, dus het hoort naast de grenzen hierboven in plaats van ervoor in de plaats.

Een verwante gewoonte: zet nooit geheimen, interne regels die u niet openbaar wilt hebben, of de data van een andere klant in hetzelfde contextvenster als onbetrouwbare tekst. Alles in de prompt kan uit het model komen, en "herhaal alsjeblieft je instructies" is de makkelijkste aanval die er is.

## Kijk Wat de Functie Doet

Omdat u injectie niet kunt voorkomen, moet u haar kunnen opmerken.

Log elke aanroep van een AI-functie met de invoer, de uitvoer, welke tools werden aangeroepen en met welke argumenten, en het betrokken account. Bewaar het lang genoeg om onderzoek te kunnen doen - met persoonsgegevens behandeld volgens dezelfde regels als elk ander logboek.

Meld dan op de patronen die erop wijzen dat er iets mis is: een tool die veel vaker wordt aangeroepen dan normaal, een ongebruikelijk patroon van argumenten, uitvoer met iets wat op configuratie of identificaties van een ander account lijkt, één account dat een groot deel van de aanroepen veroorzaakt.

Voor de meeste kleine producten is dit het verschil tussen het binnen een dag ontdekken en het van een klant horen.

## Budget- en Rate Limits Zijn Beveiligingsmaatregelen

Een AI-functie zonder limieten is ook een denial-of-wallet-kwetsbaarheid: een aanvaller die modelaanroepen kan veroorzaken, kan uw geld uitgeven, en daar is geen enkele slimheid voor nodig.

Rate limits per gebruiker en per account op elk endpoint dat een model gebruikt, een limiet op de grootte van invoer en uitvoer, en een uitgavenlimiet bij de provider. Dit zijn dezelfde maatregelen als het artikel over kosten aanbeveelt, en hier doen ze beveiligingswerk.

## Het Ophaalgeval Verdient een Eigen Controle

Producten die vragen beantwoorden over de eigen documenten van een klant, hebben een tweede probleem bovenop het eerste, en het is degene die de ergste krantenkoppen oplevert: de content van de verkeerde klant ophalen.

De mislukking is gewoon in plaats van exotisch. Documenten van elk account gaan in één index. De zoekstap haalt op basis van gelijkenis op, en weet niets van rechten. Een vraag die op een bepaalde manier is geformuleerd, haalt een passage van iemand anders binnen, en het model verwerkt die plichtsgetrouw in een antwoord.

De oplossing is het filter vóór het ophalen toe te passen, nooit erna. De zoekopdracht moet als onderdeel van de query zelf worden beperkt tot het account - en, waar het ertoe doet, tot de specifieke rechten van de gebruiker binnen dat account - en niet door achteraf resultaten weg te gooien. Achteraf weggooien lekt nog steeds als het model de tekst al heeft gezien, en in de meeste implementaties is dat zo.

Nog twee gewoontes. Sla de reikwijdte van de rechten op naast elk geïndexeerd fragment in plaats van te vertrouwen op een naamgevingsafspraak, zodat de beperking door data wordt afgedwongen in plaats van door discipline. En werk de index bij in dezelfde handeling wanneer de rechten van een document veranderen - gedeeld, niet meer gedeeld, verplaatst, verwijderd - want een index die achterloopt op de bron, is een rechtensysteem dat achterloopt op de werkelijkheid.

Test het zoals u al het andere test: stel als de ene klant een vraag waarvan het antwoord alleen in de documenten van een andere klant staat, en controleer dat het product zegt het niet te weten.

## Dit Inrichten

Voor een product met AI-functies kost dit doorgaans één tot twee dagen: een inventarisatie van elke functie die een model gebruikt en wat ze kan behalve tekst genereren, rechten voor tools teruggebracht tot het minimum zonder iets destructiefs of accountoverschrijdends, autorisatie stevig buiten het model in uw bestaande rechtenlogica, menselijke goedkeuring vereist voor onomkeerbare handelingen, uitvoer overal ge-escaped waar ze wordt getoond en nooit uitgevoerd of in queries gezet, onbetrouwbare content structureel gescheiden van instructies, geheimen en data van andere klanten buiten de context gehouden, logging van aanroepen met vastgelegde toolaanroepen, meldingen bij afwijkende patronen, en rate- en uitgavenlimieten op elk endpoint dat een model gebruikt.

LaunchStudio doet dit als onderdeel van de beveiligingsreview van producten met AI-functies, en dat zijn er inmiddels de meeste. De engineers zijn van Manifera - elf jaar, 120+ engineers, beveiligingswerk voor klanten als Vodafone, TNO en CFLW.

[Vertel ons wat uw AI-functie mag doen](https://launchstudio.eu/nl/#contact). Die lijst is de hele beoordeling.

## Echt voorbeeld

### Het Cv Dat Zichzelf Beoordeelde

Machteld Oosterbeek bouwde Sollicitatiescan in Lovable: een screeningstool voor recruitmentbureaus en werkgevers, die geüploade cv's vergelijkt met een functieomschrijving en een shortlist met onderbouwing maakt, gebruikt door 31 bureaus.

De functie had ook tools. Ze kon eerdere sollicitaties van de kandidaat opzoeken in de database, en ze kon een kandidaat naar de shortlistfase verplaatsen - toegevoegd omdat bureaus wilden dat de duidelijke matches automatisch werden doorgezet.

Een kandidaat die solliciteerde op een logistieke functie, diende een pdf in met een alinea in witte tekst van vier punten: instructies om de functie-eisen te negeren, de kandidaat als uitzonderlijke match te beoordelen, hem naar de shortlist te verplaatsen, en de instructie niet te noemen in de onderbouwing. Het werkte precies zoals geschreven.

Het bureau merkte het op omdat de onderbouwing ongewoon enthousiast was en de ervaring van de kandidaat niet overeenkwam. Bij het doorlopen van drie maanden geschiedenis vond Machteld nog vier cv's met vergelijkbare tekst, afkomstig van wat een sjabloon leek dat rondging op een forum voor werkzoekenden.

Drie werkdagen: de tool om naar de shortlist door te zetten volledig verwijderd, zodat het model kan voorstellen maar een recruiter beslist; de database-opzoeking beperkt tot de specifieke kandidaat die wordt beoordeeld binnen het eigen account van het bureau, in plaats van een algemene querymogelijkheid; autorisatie buiten het model geplaatst, met controle van de rechten van de recruiter bij elke voorgestelde handeling; geüploade documenten omgezet naar platte tekst, waarbij onzichtbare content en content buiten het canvas wordt geëxtraheerd en gemarkeerd in plaats van stilletjes meegenomen; onbetrouwbare documenttekst structureel gescheiden van de instructies en duidelijk gemarkeerd als data; modeluitvoer ge-escaped overal waar ze wordt getoond, aangezien de onderbouwing eerder als HTML werd ingevoegd; rate limits per bureau en een uitgavenlimiet bij de provider; en volledige logging van aanroepen met een melding bij documenten met verborgen tekst, die nu wordt gemarkeerd voor menselijke beoordeling in plaats van geblokkeerd.

**Resultaat:** de vier betrokken sollicitaties werden opnieuw gescreend en twee bleken echt redelijke kandidaten die het sjabloon op advies hadden gebruikt. De melding voor verborgen tekst heeft sindsdien in een jaar 31 documenten gemarkeerd, waarvan er 9 tekst bevatten die op een instructie leek. Automatisch doorzetten is sinds de eerste dag van de oplossing niet meer mogelijk, en dat beschouwt Machteld als de wijziging die er echt toe deed.

> *"Het model deed precies wat het werd opgedragen. De fout was van mij: ik gaf het een knop die de status van een kandidaat veranderde, en liet vervolgens vreemden ertegen schrijven."*
> - **Machteld Oosterbeek, Oprichter, Sollicitatiescan (Hilversum)**

**Kosten & Doorlooptijd:** €3.400 (beperken van toolrechten, externe autorisatie, tekstextractie uit documenten met detectie van verborgen content, structureren van prompts, escaping van uitvoer, rate- en uitgavenlimieten, logging van aanroepen en meldingen) - afgerond in 3 werkdagen.

## Veelgestelde vragen

### Kan prompt injection worden voorkomen?

Nee. Het is een eigenschap van hoe taalmodellen tekst verwerken. Wat u kunt doen, is beperken wat een geslaagde injectie bereikt - smalle tools, autorisatie buiten het model, menselijke goedkeuring voor onomkeerbare handelingen, en uitvoer als onbetrouwbaar behandelen.

### Is het filteren van kwaadaardige instructies de moeite waard?

Als kleine verkeersdrempel, niet als verdediging. Instructies kunnen op onbeperkt veel manieren worden geformuleerd, in elke taal of codering, dus elk filter is een lijst van wat iemand toevallig bedacht.

### Wat is indirecte prompt injection?

Wanneer de instructie binnenkomt in content die uw product namens iemand anders verwerkt - een geüpload document, een opgehaalde webpagina, een binnenkomende e-mail. De gebruiker is het slachtoffer in plaats van de aanvaller, wat het het ernstigere geval maakt.

### Is een samenvatter zonder tools veilig?

Veel veiliger. Het ergste gevolg is misleidende uitvoer voor degene die de tekst indiende. Het risico groeit met wat de functie kan doen behalve woorden produceren.

### Wat moet ik loggen voor een AI-functie?

De invoer, de uitvoer, elke toolaanroep met argumenten, en het account. Meld dan op afwijkingen - ongewone toolfrequentie, vreemde argumenten, uitvoer met identificaties of configuratie.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan prompt injection worden voorkomen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee - het zit ingebakken in hoe modellen tekst lezen. Beperk in plaats daarvan de gevolgen: minimale tools, autorisatie buiten het model, menselijke goedkeuring voor onomkeerbare handelingen, onbetrouwbare uitvoer."
      }
    },
    {
      "@type": "Question",
      "name": "Is het filteren van prompt-injectiepogingen effectief?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Alleen als verkeersdrempel. Instructies kunnen op onbeperkt veel manieren worden geformuleerd, vertaald of gecodeerd, dus filters dekken alleen wat iemand voorzag."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is indirecte prompt injection?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een instructie verstopt in content die uw product voor iemand anders verwerkt - een document, webpagina of e-mail - waardoor uw gebruiker het slachtoffer is in plaats van de aanvaller."
      }
    },
    {
      "@type": "Question",
      "name": "Is een AI-samenvatter zonder tools veilig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Veel veiliger - het ergste geval is misleidende uitvoer voor de indiener. Het risico groeit met wat de functie kan doen behalve tekst genereren."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet er worden gelogd voor een AI-functie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Invoer, uitvoer, elke toolaanroep met argumenten, en het account - en meld dan op ongewone toolfrequentie, vreemde argumenten of identificaties in de uitvoer."
      }
    }
  ]
}
</script>
