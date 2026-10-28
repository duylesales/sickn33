---
Titel: "Bolt-Beveiliging: Wat U Oplost Voordat een Bolt-App Echte Gebruikers Ontmoet"
Trefwoorden: bolt-beveiliging, bolt.new, prototype verstevigen, blootgestelde sleutels, autorisatie, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Bolt-Beveiliging: Wat U Oplost Voordat een Bolt-App Echte Gebruikers Ontmoet

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bolt-Beveiliging: Wat U Oplost Voordat een Bolt-App Echte Gebruikers Ontmoet",
  "description": "Bolt levert in minuten een werkende applicatie op, geoptimaliseerd voor demonstratie in plaats van blootstelling. De specifieke gaten die de uitvoer laat, in de volgorde waarin ze ertoe doen, en wat een dag verstevigen dekt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-01",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/bolt-security-what-to-fix-before-a-bolt-app-meets-real-users" }
}
</script>

Bolt is uitzonderlijk goed in waar het voor is: een applicatie beschrijven en minuten later een werkende versie hebben, draaiend in een browser, compleet genoeg om aan iemand te laten zien.

Die uitvoer is geoptimaliseerd voor demonstratie. Ze moet direct werken, wat betekent dat elke beslissing die snelheid inruilt voor veiligheid in het voordeel van snelheid uitvalt - niet uit slordigheid, maar omdat het alternatief iets zou opleveren dat in de eerste minuut niet draait.

Het gat tussen een Bolt-prototype en een applicatie die vreemden kunnen gebruiken, is echt, goed afgebakend, en meestal een dag of twee werk. Het probleem is dat niets aan het prototype aangeeft dat het gat bestaat, omdat het er af uitziet.

## Waar de Sleutels Staan

Begin hier, omdat het zowel het meest voorkomende als het meest ingrijpende is.

Bolt-applicaties bevatten vaak API-sleutels in frontendcode - een databasesleutel, een sleutel voor een model-API, een betaalsleutel - omdat dat de kortste weg is van niets naar een werkende functie. Alles in die code is te downloaden door iedereen die uw site opent.

Controleer drie plekken: de code zelf, de build-uitvoer, en het live JavaScript op uw site. Zoek naar de namen van providers en naar alles wat op een sleutel lijkt.

Alles wat u daar vindt, is gecompromitteerd en moet worden vervangen, niet alleen verplaatst. En verplaatsen betekent dat de handeling die de sleutel gebruikte een functie op de server wordt die controleert wie het vraagt voordat ze iets doet.

## Niemand Controleert Wie U Bent

Het tweede gat is autorisatie, en het is structureel in plaats van toevallig.

Een prototype toont een functie aan een persoon die haar mag gebruiken. Er is geen tweede gebruiker, dus de vraag of deze gebruiker dit record mag zien bestaat niet - en de gegenereerde code bevat zo'n controle niet.

Volg de systematische aanpak die elders in deze reeks is beschreven: twee accounts in twee organisaties, en een ronde langs elk endpoint waarbij u de records van de ander opvraagt. Lezen, bijwerken en verwijderen. In een Bolt-applicatie die rechtstreeks uit het prototype komt, kunt u verwachten dat de meeste slagen.

De oplossing is elke query te beperken tot het account dat het verzoek doet, en als u op Supabase zit, row-level security met policies in te schakelen in plaats van alleen op applicatiecode te vertrouwen.

## Validatie Zit in de Browser

Gegenereerde formulieren valideren in de interface, waar de developer het ziet werken. De server accepteert wat er wordt gestuurd.

Dat betekent dat verplichte velden leeg kunnen zijn, getallen negatief, teksten elke lengte, een e-mailadres van alles, een prijs wat de client zegt, en een status een waarde die uw product niet kent.

Elk endpoint heeft eigen validatie nodig, gedefinieerd op de server, die alles weigert wat niet klopt. Een bibliotheek voor schemavalidatie maakt dit een paar regels per endpoint, en het sluit een categorie problemen af die loopt van beschadigde data tot een klant die één euro betaalt voor een plan van honderd euro.

## Alles Is Standaard Publiek

Drie standaarden die specifiek in een Bolt-applicatie het controleren waard zijn.

Opslagbuckets, die doorgaans publiek worden aangemaakt omdat de upload daardoor in de demonstratie werkte.

API-routes, die vaak helemaal geen authenticatie vereisen - ze werden vanuit de interface aangeroepen en niets suggereerde dat iemand anders ze zou kunnen aanroepen.

En de gedeployde preview zelf, een publieke URL die misschien nog bestaat, met een eerdere versie van uw applicatie en een eerdere set sleutels.

## Nergens Limieten

Een prototype heeft één gebruiker die redelijke dingen doet. Een live applicatie heeft wie haar ook vindt.

Rate limits op authenticatie-endpoints, op alles wat e-mail of sms verstuurt, en op alles wat een model-API aanroept. Groottelimieten op uploads en op de inhoud van verzoeken. Een maximum aantal rijen dat een endpoint teruggeeft. Time-outs op elke externe aanroep.

Geen hiervan bestaat in gegenereerde uitvoer, en elk ervan is het verschil tussen een slechte middag en een rekening of een storing.

## De Volgorde van Oplossen

Hebt u een dag, besteed die dan in deze volgorde.

Sleutels uit de frontend en vervangen. Autorisatie op elk endpoint. Validatie op de server. Standaarden voor opslag en routes gecorrigeerd. Rate- en groottelimieten. Daarna sessies, afhankelijkheden, logging en al het andere op de bredere lijst voor productieklaar maken.

De eerste twee zijn verantwoordelijk voor het overgrote deel van wat er werkelijk misgaat, en het zijn de twee die een prototype structureel gegarandeerd mist.

## Waar het Prototype Nog Steeds Goed Voor Is

Niets hiervan is een argument tegen het bouwen van het prototype in Bolt. Het is een argument over wat er daarna gebeurt, en het onderscheid is het noemen waard omdat oprichters soms doorschieten naar opnieuw beginnen.

Het prototype heeft iets waardevols gedaan dat duur is om te reproduceren: het heeft vastgesteld wat het product moet doen, in een vorm die de klant heeft gezien en waarmee hij heeft ingestemd. Die kennis zit in de code, het datamodel en de interface, en die weggooien om opnieuw te beginnen met een zorgvuldig gekozen framework is meestal een vergissing die in weken wordt gemeten.

De realistische beoordeling, gemaakt door de code te lezen in plaats van op reputatie: is de structuur stevig genoeg om op voort te bouwen? Voor de meeste Bolt-uitvoer is het antwoord ja. Het datamodel is redelijk, de schermen zijn de juiste schermen, de processen zijn de juiste processen. Wat ontbreekt, is alles wat pas ertoe doet als er andere mensen bij betrokken zijn, en dat toevoegen is aanvullend werk, geen herschrijving.

De gevallen waarin opnieuw bouwen echt juist is, zijn smaller dan ze aanvoelen: een datamodel dat niet kan weergeven wat het bedrijf werkelijk nodig heeft, of een applicatie die zo verknoopt is dat het veranderen van één ding betrouwbaar iets anders breekt. Beide zijn bij inspectie zichtbaar, en geen van beide is de gebruikelijke uitkomst van een weekend prototypen.

De volgorde die de meeste oprichters dient, is dus: prototype in Bolt, laat het zien, bevestig dat het product klopt, en verstevig dan wat u hebt in plaats van het te bewonderen en opnieuw te beginnen.

## Laat de Agent het Verstevigen, Voorzichtig

Een voor de hand liggende vraag: kan de tool die het prototype bouwde het ook repareren? Gedeeltelijk, en de grenzen zijn het weten waard voordat u erop vertrouwt.

Wat goed werkt. Validatie op de server toevoegen aan een endpoint, als u het endpoint noemt en de regels geeft. Een specifieke handeling achter een serverfunctie zetten. Rate limiting toevoegen aan een route. Een policy schrijven voor een tabel als u beschrijft wie wat mag zien. Dat zijn afgebakende, goed gespecificeerde taken met heel veel voorbeelden, en de uitvoer is meestal correct.

Wat niet werkt. Vragen om "maak dit veilig", wat zelfverzekerde wijzigingen oplevert die gaan over wat het model met het woord associeert in plaats van wat uw applicatie werkelijk mist. Vragen om de problemen te vinden, wat het wisselend doet - het merkt een ontbrekende validatie op en mist de service role-sleutel in de frontend, omdat die sleutel zijn werk doet.

De productieve verdeling is dus dat u beslist wat er moet worden opgelost, vanaf een checklist, en dat de agent elke oplossing als benoemde taak uitvoert. Dat is aanzienlijk sneller dan het zelf schrijven, en het vereist geen vertrouwen in een oordeel dat de tool niet kan vellen.

Eén waarschuwing specifiek voor dit werk: controleer elke wijziging in plaats van haar te accepteren. Een policy die er goed uitziet en alles toestaat, of een validatie die na het wegschrijven naar de database draait, zijn allebei aannemelijke uitvoer - en precies het soort gebrek waarvan het oorspronkelijke prototype al liet zien dat de tool het kan maken.

De praktische opzet is dus: houd de checklist in de repository zodat elke sessie erbij kan, werk haar punt voor punt af, en test elk resultaat zelf. De tool levert snelheid; de lijst levert oordeel, en de lijst is het deel dat van buiten de tool moet komen.

## Dit Inrichten

Voor een Bolt-applicatie op weg naar echte gebruikers kost dit doorgaans één tot twee dagen: elke sleutel in code en bundel gevonden, vervangen en naar de server verplaatst, met de handelingen die ze gebruikten herschreven als geautoriseerde functies; systematisch testen tussen accounts, met autorisatie op elk endpoint en row-level security ingeschakeld waar van toepassing; validatie op de server voor elke invoer; opslagbuckets privé gemaakt met ondertekende toegang; API-routes die authenticatie vereisen; oude preview-deployments opgeheven; rate limits, groottelimieten en time-outs toegepast; en een korte schriftelijke vastlegging van wat er is gecontroleerd, zodat de volgende persoon het weet.

LaunchStudio doet precies dit werk binnen het Launch Ready-pakket, vanaf €800, meestal binnen een week. De engineers zijn van Manifera - elf jaar, 120+ engineers, klanten als Vodafone, TNO en CFLW, vanaf de Herengracht 420 in Amsterdam.

[Stuur ons uw Bolt-project](https://launchstudio.eu/nl/#contact) en wij vertellen u wat een vreemde er nu mee kan doen.

## Echt voorbeeld

### Een Demo Die Live Ging

Quinten Aardema bouwde Leveranciersportaal in een weekend met Bolt: een portaal waar de 90 leveranciers van een voedingsgroothandel prijslijsten, certificaten en leverschema's indienen.

Hij bouwde het om de groothandel te laten zien wat er mogelijk was. Ze vonden het goed, vroegen wanneer het live kon, en hij antwoordde "volgende week" - omdat het werkte.

De review vóór de lancering vond wat een weekendprototype bevat. De Supabase-sleutel in de frontend was de service role-sleutel, met onbeperkte databasetoegang voor iedereen die de pagina opende. Geen van de 23 endpoints controleerde welke leverancier het vroeg, dus elke ingelogde leverancier kon de prijslijst van elke concurrent lezen door een nummer te veranderen. Certificaten die leveranciers uploadden, gingen naar een publieke bucket met voorspelbare bestandsnamen. Validatie zat volledig in de browser, dus een negatieve prijs en een leverdatum in 1970 werden allebei geaccepteerd. Er waren nergens rate limits, en het endpoint dat de groothandel mailde over nieuwe inzendingen, kon herhaaldelijk worden aangeroepen door iedereen die het vond.

Twee werkdagen: de service role-sleutel vervangen en verwijderd, met alle databasetoegang verplaatst naar functies op de server met een anonieme sleutel en policies; row-level security ingeschakeld met policies op alle negen tabellen; autorisatie toegevoegd aan alle 23 endpoints, beperkt tot de leverancier die het verzoek doet; validatie op de server voor elke invoer, met een schema per endpoint; de certificatenbucket privé gemaakt met gegenereerde identificaties en ondertekende URL's; rate limits op authenticatie-, inzend- en meldings-endpoints; groottelimieten op uploads; time-outs op externe aanroepen; de oorspronkelijke publieke preview-deployment opgeheven, die nog de oude sleutels bevatte; en een vastlegging van één pagina van wat er is gecontroleerd.

**Resultaat:** het portaal ging een week later dan gepland live met 90 leveranciers en draait inmiddels twee jaar. Quinten vindt de week vertraging de beste beslissing in het project, omdat een lek van prijslijsten tussen concurrerende leveranciers de relatie met de groothandel direct had beëindigd.

> *"Het werkte perfect. Dat was precies het probleem - er was niets te zien, en elke leverancier had de prijzen van elke concurrent kunnen lezen door één nummer in de adresbalk te veranderen."*
> - **Quinten Aardema, Oprichter, Leveranciersportaal (Venlo)**

**Kosten & Doorlooptijd:** €2.900 (vervangen van sleutels en migratie naar de server, row-level security, autorisatie over 23 endpoints, validatie op de server, privé-opslag met ondertekende toegang, rate- en groottelimieten, opheffen van preview, documentatie) - afgerond in 2 werkdagen.

## Veelgestelde vragen

### Is Bolt onveilig?

Niet meer dan welke prototypingtool ook. Het optimaliseert voor iets wat direct werkt, wat betekent dat de controles die pas ertoe doen als vreemden binnenkomen, ontbreken. Het gat is voorspelbaar en te dichten.

### Wat moet ik als eerste controleren?

Waar uw API-sleutels staan. Doorzoek het live JavaScript op uw site op providernamen en sleutelpatronen. Alles wat u daar vindt, moet worden vervangen, niet alleen verplaatst.

### Hoe test ik autorisatie?

Maak twee accounts in twee verschillende organisaties, noteer in de ene de recordidentificaties, en vraag ze op als de andere - voor lezen, bijwerken en verwijderen. Alles wat data teruggeeft, is een bevinding.

### Waarom is validatie in de browser niet genoeg?

Omdat de server accepteert wat er wordt gestuurd, ongeacht wat de interface toestaat. Iedereen kan uw endpoints direct aanroepen met welke waarden ook, inclusief prijzen en statussen.

### Hoe lang duurt het verstevigen van een Bolt-app?

Eén tot twee dagen voor een typisch prototype, in een vaste volgorde: sleutels, autorisatie, validatie, standaarden, limieten. De eerste twee dekken het meeste van wat er werkelijk misgaat.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is Bolt onveilig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niet meer dan welke prototypingtool ook - het optimaliseert voor direct werkende uitvoer, dus controles die pas met echte gebruikers ertoe doen, ontbreken."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet ik als eerste controleren in een Bolt-app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Waar API-sleutels staan. Doorzoek het live JavaScript op providernamen en sleutelpatronen; alles wat u vindt, moet worden vervangen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe test ik autorisatie in een prototype?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Twee accounts in twee organisaties: vraag de records van de ene op als de andere, voor lezen, bijwerken en verwijderen. Elke teruggegeven data is een bevinding."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom is validatie in de browser onvoldoende?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De server accepteert wat hij ontvangt. Endpoints kunnen direct worden aangeroepen met welke waarden ook, inclusief prijzen en statussen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt het verstevigen van een Bolt-app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Eén tot twee dagen: sleutels, autorisatie, validatie, standaarden, limieten - de eerste twee dekken het meeste echte risico."
      }
    }
  ]
}
</script>
