---
Titel: "Lovable Betalingen: Terugbetalingen, Opzeggingen en Pro-rata Verrekening Zonder Drama"
Trefwoorden: lovable betalingen, terugbetalingen, opzegproces, pro-rata verrekening, planwijzigingen, chargebacks, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Lovable Betalingen: Terugbetalingen, Opzeggingen en Pro-rata Verrekening Zonder Drama

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Betalingen: Terugbetalingen, Opzeggingen en Pro-rata Verrekening Zonder Drama",
  "description": "De onopvallende helft van facturatie in een door AI gebouwde app: opzeggen aan het eind van de periode, upgrades pro rata verrekenen, terugbetalingen die de boekhouding bereiken, en de chargeback die toch binnenkomt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-21",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-payments-refunds-cancellations-and-proration" }
}
</script>

Iedereen bouwt het deel waar geld binnenkomt. Bijna niemand bouwt het deel waar een deel ervan weer teruggaat — en dat is het deel waar uw reputatie van wordt gemaakt, want een klant die netjes vertrekt, vertelt mensen dat u eerlijk was, en een klant die de opzegknop niet kan vinden, vertelt het aan meer mensen en een stuk luider.

Er zit in Europa ook een regelgevend randje aan, en een praktisch: een app die niet goed kan opzeggen, genereert voor altijd supportwerk.

## Opzeggen Is een Productbeslissing Voordat Het Code Is

Beantwoord vier vragen en de implementatie volgt vanzelf.

**Wanneer eindigt de toegang?** Aan het eind van de betaalde periode, vrijwel altijd. De klant betaalde tot de 30e; neem de toegang op de 30e weg, niet op het moment dat hij klikt. Direct beëindigen bij opzegging voelt als straf en levert terugbetalingsverzoeken op die u anders nooit had gezien.

**Is er een terugbetaling?** Bij een maandabonnement meestal niet — hij houdt de maand waarvoor hij betaalde. Bij een jaarplan dat in maand twee wordt opgezegd, is een pro-rata terugbetaling de redelijke standaard en het waard om in uw voorwaarden te zetten, want het alternatief is er voor altijd per geval over discussiëren.

**Wat gebeurt er met hun data?** Zeg het expliciet: bewaard voor een vastgelegde periode, exporteerbaar binnen die termijn, daarna verwijderd. Dat is zowel goede praktijk als het antwoord op een vraag die uw privacyverklaring toch al moet beantwoorden.

**Kunnen ze terugkomen?** Heractiveren moet werken. Een terugkerende klant met zijn geschiedenis intact is de goedkoopste omzet die u ooit krijgt, en het verlies van zijn data bij opzegging laat terugkomen voelen als opnieuw beginnen.

Maak de opzegknop daarna vindbaar. Hem verstoppen is een tactiek die alleen werkt totdat iemand erover schrijft, en in de EU is een abonnement waar je moeilijk uitkomt steeds meer een juridisch risico in plaats van een slimme retentiehefboom.

## Verwijder Niet bij Opzegging

De fout verschijnt met enige regelmaat in door AI gegenereerde code: opzeggen verwijdert de gebruikersrij, of laat een verwijdering doorlopen over al zijn records.

Dat vernietigt uw boekhoudkundige geschiedenis — u hebt de facturen voor die betalingen nog jaren nodig. Het vernietigt uw mogelijkheid om te heractiveren. En het maakt elke vraag als "kunt u nagaan of er in april is afgeschreven?" onbeantwoordbaar.

Opzeggen is een statuswijziging, geen verwijdering. Het account bestaat, gemarkeerd als opgezegd, met beperkte toegang en een lopende bewaartermijn. Verwijderen is een aparte handeling met eigen regels, die de klant kan aanvragen en die u daarna bewust uitvoert.

## Pro-rata Verrekening: Kleine Functie, Grote Discussies

Een klant op €29 upgradet naar €79 op dag tien van een cyclus van dertig dagen. Wat betaalt hij vandaag?

Het gebruikelijke antwoord is het verschil voor de ongebruikte tijd: ruwweg twee derde van €50. Beide grote providers berekenen dit voor u. Het probleem is dat oprichters het gedrag vaak overschrijven zonder het te begrijpen, en vervolgens het afschrift van een klant niet kunnen uitleggen.

Twee regels houden het overzichtelijk. Upgrades gaan direct in en rekenen het pro-rata verschil — de klant vroeg nu om meer product. Downgrades gaan in aan het eind van de huidige periode en rekenen de lagere prijs vanaf de volgende — anders geeft u terugbetalingen bij planwijzigingen en wordt het rekenwerk vreemd als iemand twee keer in een maand wisselt.

Wat u ook kiest, laat het zien vóór de bevestiging: *U betaalt vandaag €33,50, daarna €79 per maand vanaf 1 november.* Eén zin, en uw supportwerk rond planwijzigingen nadert nul.

## Terugbetalingen Moeten op Drie Plekken Landen

Een terugbetaling is niet klaar wanneer het dashboard van de provider zegt dat er is terugbetaald.

Ze moet **de provider** bereiken, die het geld teruggeeft. Ze moet **uw database** bereiken, die het betaalrecord bijwerkt en eventuele toegang die het gaf — anders blijft een volledig terugbetaalde klant het product gebruiken en blijven uw omzetcijfers onjuist. En ze moet **uw boekhouding** bereiken als creditnota, doorlopend genummerd en met verwijzing naar de oorspronkelijke factuur, anders sluit uw kwartaal niet.

Terugbetalingen die met de hand in een dashboard worden gedaan, voltooien betrouwbaar alleen de eerste van de drie. Daarom is terugbetalen vanuit uw eigen applicatie — een kleine beheeractie die alle drie de stappen samen uitvoert — de middag waard die het kost om te bouwen, lang voordat u denkt een beheerpaneel nodig te hebben.

Gedeeltelijke terugbetalingen verdienen één extra gedachte: bepaal of ze het recht op toegang veranderen. De helft van een jaarplan terugbetalen moet de resterende toegang meestal niet halveren; het moet het abonnement óf op een datum beëindigen, óf ongemoeid laten. Kies, schrijf het op, implementeer het één keer.

## Chargebacks Zijn een Ander Beest

Een chargeback is geen terugbetaling. De klant ging naar zijn bank in plaats van naar u, en het geld wordt teruggehaald met kosten erbovenop, of u het er nu mee eens bent of niet.

De verdediging is bewijs, en dat bewijs moet al bestaan: wat er werd gekocht, wanneer, door wie, vanaf welk IP-adres en apparaat, dat de voorwaarden werden geaccepteerd, dat het product werd gebruikt, en eventuele supportcorrespondentie. Applicaties die niets hiervan vastleggen, kunnen niets betwisten.

De meeste chargebacks tegen kleine abonnementsproducten zijn geen fraude. Het zijn mensen die de regel op hun afschrift niet herkenden. Twee goedkope oplossingen pakken het merendeel aan: zorg dat de omschrijving op het bankafschrift uw productnaam is in plaats van een afkorting die niemand herkent, en mail bij elke afschrijving een betaalbewijs, ook bij verlengingen. Een verlenging die na elf stille maanden geruisloos binnenkomt, is de klassieke chargeback.

## De Beheeracties Die U op Dag Eén Wilt Hebben

De meeste supportverzoeken over facturatie zijn dezelfde handvol handelingen, en elke handeling die met de hand in een providerdashboard wordt uitgevoerd, is een kans om uw eigen database uit de pas te laten lopen. Een kleine interne pagina — alleen voor u zichtbaar, zonder noemenswaardig ontwerp — betaalt zichzelf binnen weken terug.

De set die u als eerste bouwt: **een terugbetaling doen** (volledig of gedeeltelijk, wat de provider, het betaalrecord, het recht op toegang en de creditnota samen bijwerkt); **een abonnement opzeggen** namens de klant, omdat sommige mensen altijd zullen mailen in plaats van klikken; **verlengen of crediteren**, voor het gebaar van goede wil dat een ontevreden klant behoudt; **een plan handmatig wijzigen**, voor de afspraken die u maakt en die uw prijspagina niet kent; en **de factuurgeschiedenis van een klant opzoeken**, zodat het beantwoorden van "is er in april afgeschreven?" seconden kost.

Voeg aan elk één ding toe: een notitieveld waarin staat wie het deed en waarom. Zes maanden later is de vraag over een ongebruikelijke creditering op een account te beantwoorden door te lezen in plaats van te herinneren.

Wat hier niet thuishoort, is het direct bewerken van bedragen op uitgegeven facturen, of een verwijderknop. Elke wijziging hoort een handeling te zijn met een vastgelegde reden, geen veld dat u kunt overschrijven. Een beheerpaneel dat stilletjes financiële geschiedenis kan herschrijven is erger dan geen beheerpaneel, omdat de wijzigingen geen spoor achterlaten en het gemak garandeert dat ze zullen gebeuren.

Toegang telt ook. Deze pagina voert onomkeerbare financiële handelingen uit, dus hoort ze achter een aparte rechtencontrole in plaats van een `is_admin`-vlag die elke accountrij kan dragen — en ze moet elk gebruik loggen, ook dat van uzelf.

## Schrijf de Regels Op Voordat U Ze Nodig Hebt

Elke beslissing over een terugbetaling of opzegging die in het moment wordt genomen, onder druk, naar aanleiding van een e-mail waardoor u zich schuldig voelt, wordt een informeel beleid dat u zich niet herinnert en niet consequent kunt toepassen.

Schrijf een pagina — intern, een half A4'tje — over de gevallen die werkelijk voorkomen. Jaarplan vroegtijdig opgezegd: pro-rata terugbetaling van volledige ongebruikte maanden. Maandplan opgezegd: geen terugbetaling, toegang tot het eind van de periode. Klant die vergat op te zeggen en gisteren werd afgeschreven: volledige terugbetaling, geen discussie, het kost minder dan de klacht. Klant die het vier maanden vergat: één maand terugbetaald als gebaar. Downgrade halverwege de cyclus: aan het eind van de periode. Storing aan uw kant: de getroffen periode terugbetalen zonder dat erom wordt gevraagd.

Twee voordelen, en het tweede is het voordeel dat oprichters onderschatten. Consistentie, uiteraard — dezelfde situatie krijgt hetzelfde antwoord, ongeacht hoe de e-mail was geschreven. Maar ook snelheid: een beslissing die al is genomen, is een beslissing waar u geen avond over piekert, en factuurcorrespondentie is bij uitstek goed in het opslokken van aandacht die bij het product hoort.

Publiceer de delen die klanten raken in uw voorwaarden, houd de rest intern, en herzie de pagina wanneer er een geval binnenkomt dat ze niet dekt.

## Dit Inrichten

Voor een product dat al klanten factureert, kost dit twee tot drie dagen: zelfstandig opzeggen dat de toegang aan het eind van de periode beëindigt, met een genoemde bewaar- en exporttermijn, heractiveren dat werkt, pro-rata verrekening ingesteld met upgrade-nu en downgrade-later en het bedrag getoond vóór bevestiging, terugbetalingen vanuit uw eigen beheer zodat provider, database en creditnota samen bewegen, de werking van gedeeltelijke terugbetalingen bepaald en geïmplementeerd, betaalbewijzen bij elke afschrijving inclusief verlengingen, een herkenbare omschrijving op het afschrift, en voldoende vastgelegd bewijs om een chargeback te betwisten.

LaunchStudio bouwt de volledige facturatiecyclus in plaats van alleen de checkout, binnen het Launch & Grow-pakket met managed hosting voor €49 per maand. De engineers zijn van Manifera — elf jaar, 160+ projecten, klantcontact vanaf de Herengracht 420 in Amsterdam en oplevering vanuit Ho Chi Minh-stad.

[Vertel ons wat er in uw app gebeurt als iemand opzegt](https://launchstudio.eu/nl/#contact).

## Echt voorbeeld

### Het Jaarplan Waar Niemand Uit Kon

Sander Kroese bouwde Clubkas in Lovable: abonnements- en contributieadministratie voor amateursportclubs, verkocht als jaarplan van €240 aan 95 clubs in Brabant en Limburg.

Opzeggen in zijn app was een e-mail aan Sander. Hij zegde dan op in het Stripe-dashboard, betaalde terug als hij dat redelijk vond, en paste met de hand een vlag aan. Met 95 klanten was dat te overleven; met de groei die hij wilde niet, en het ging al mis op manieren die hij kon zien.

Twee clubs waren in het dashboard terugbetaald en hielden maandenlang volledige toegang, omdat er in de database niets was veranderd. Eén club was twee keer terugbetaald voor dezelfde ongebruikte periode, een keer in juni en opnieuw in augustus toen een andere e-mail hem bereikte, en geen van beide terugbetalingen had een creditnota opgeleverd. En een chargeback in april had hem €240 plus kosten gekost zonder bewijs om die te betwisten, omdat zijn app niets vastlegde behalve de betaling zelf.

Vier werkdagen: zelfstandig opzeggen dat de toegang aan het eind van de periode beëindigt, met een bewaartermijn van 90 dagen, een export van de clubdata die in die periode beschikbaar is, en heractiveren dat alles herstelt; een pro-rata terugbetalingsregel voor jaarplannen opgenomen in de voorwaarden en geïmplementeerd als één beheeractie die via de provider terugbetaalt, de betaal- en toegangsrecords bijwerkt en in één stap een genummerde creditnota uitgeeft; pro-rata verrekening voor planwijzigingen halverwege het jaar, met het bedrag getoond vóór bevestiging; betaalbewijzen gemaild bij elke afschrijving inclusief verlengingen; de omschrijving op het afschrift gewijzigd van een afkorting naar "CLUBKAS"; en per account vastlegging van het accepteren van de voorwaarden, de inloggeschiedenis en het gebruik, voldoende om een geschil te betwisten.

**Resultaat:** de opzegmails aan Sander hielden volledig op, de boekhouding sloot voor het eerst aan het eind van het jaar zonder correcties, en van de drie chargebacks in het jaar daarna werden er twee met het vastgelegde bewijs succesvol betwist.

> *"De dubbele terugbetaling was het moment waarop ik het probleem begreep. Niets in mijn app wist dat er een terugbetaling had plaatsgevonden, dus niets kon me tegenhouden het twee keer te doen."*
> — **Sander Kroese, Oprichter, Clubkas (Tilburg)**

**Kosten & Doorlooptijd:** €2.600 (zelfstandig opzeggen met bewaartermijn en heractivering, gecombineerde terugbetalingsactie met creditnota's, pro-rata verrekening, betaalbewijzen, aangepaste afschriftomschrijving, vastlegging van bewijs voor geschillen) — afgerond in 4 werkdagen.

## Veelgestelde vragen

### Moet opzegging direct ingaan of aan het eind van de periode?

Aan het eind van de betaalde periode. De klant heeft ervoor betaald, direct afsluiten voelt als straf, en het levert terugbetalingsverzoeken op die u anders niet zou krijgen.

### Moet ik een vroegtijdig opgezegd jaarplan terugbetalen?

Niet automatisch, maar een pro-rata terugbetaling is de redelijke standaard en het waard om in uw voorwaarden op te nemen. Een geschreven regel die consequent wordt toegepast, voorkomt de onderhandeling per geval die anders uw tijd opslokt.

### Hoe moeten upgrades en downgrades pro rata worden verrekend?

Upgrade direct en reken het pro-rata verschil; downgrade aan het eind van de huidige periode, met de lagere prijs vanaf de volgende. Toon het exacte bedrag voordat de klant bevestigt.

### Waarom kan ik niet gewoon terugbetalen vanuit het dashboard van de provider?

Omdat dat alleen de provider bijwerkt. Uw database geeft nog steeds toegang, uw omzetcijfers blijven onjuist en er bestaat geen creditnota. Betaal terug vanuit uw eigen app, zodat alle drie samen bewegen.

### Hoe verminder ik chargebacks?

Gebruik een omschrijving op het afschrift die klanten herkennen en mail bij elke afschrijving een betaalbewijs, ook bij verlengingen. De meeste chargebacks tegen kleine producten zijn onherkende afschriftregels, geen fraude.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet opzegging direct ingaan of aan het eind van de periode?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Aan het eind van de betaalde periode. Direct afsluiten voelt als straf en levert terugbetalingsverzoeken op die u anders nooit zou zien."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik een vroegtijdig opgezegd jaarplan terugbetalen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niet automatisch, maar een vastgelegde pro-rata regel die consequent wordt toegepast is de redelijke standaard en voorkomt onderhandeling per geval."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe moeten upgrades en downgrades pro rata worden verrekend?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Upgrades direct, met het pro-rata verschil in rekening gebracht; downgrades aan het eind van de periode. Toon altijd het exacte bedrag vóór bevestiging."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom niet terugbetalen vanuit het dashboard van de betaalprovider?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dat werkt alleen de provider bij. Uw database geeft nog steeds toegang en er bestaat geen creditnota. Betaal terug vanuit uw eigen beheer, zodat provider, database en boekhouding samen bewegen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe verminder ik chargebacks bij een abonnementsproduct?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een herkenbare omschrijving op het afschrift en een betaalbewijs bij elke afschrijving, ook bij verlengingen. De meeste geschillen zijn onherkende afschriftregels, geen fraude."
      }
    }
  ]
}
</script>
