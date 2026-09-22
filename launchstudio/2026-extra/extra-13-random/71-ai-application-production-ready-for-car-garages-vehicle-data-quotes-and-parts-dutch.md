---
Titel: "AI-Applicatie Productierijp voor Autogarages: Voertuigdata, Offertes en Onderdelen"
Trefwoorden: ai-applicatie productierijp, garagesoftware, privacy voertuiggegevens, reparatie offertes app, bolt garage app, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# AI-Applicatie Productierijp voor Autogarages: Voertuigdata, Offertes en Onderdelen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-Applicatie Productierijp voor Autogarages: Voertuigdata, Offertes en Onderdelen",
  "description": "Onafhankelijke garages en automotive-ondernemers bouwen klantgerichte apps met AI-tools. Deze beslissingsgids behandelt wat een AI-applicatie productierijp maakt voor garages: kentekenchecks, voertuigdata als persoonsgegevens, offerte-akkoorden, onderdelenprijzen, werkplaatsplanning en betalingen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-10",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-application-production-ready-for-car-garages-vehicle-data-quotes-and-parts" }
}
</script>

Onafhankelijke autobedrijven concurreren met dealernetwerken die over gelikte apps beschikken: online een onderhoudsbeurt inplannen, extra werkzaamheden met één tik goedkeuren en de factuur al inzien vóór het ophalen. Met tools als Bolt of Lovable kan een garagehouder of automotive-oprichter binnen enkele weken een soortgelijke app bouwen. Maar om die AI-applicatie écht productierijp te maken voor een drukke werkplaats, zijn beslissingen nodig waar generieke afspraken-apps nooit mee te maken krijgen — rondom kentekens, akkoorden op meerwerk, fluctuerende onderdelenprijzen en een digitaal planbord dat naadloos moet aansluiten op wat er werkelijk op de hefbruggen gebeurt.

## Beslissing 1: Zijn Voertuiggegevens Persoonsgegevens?

In veel gevallen wel. Een kenteken, een chassisnummer (VIN) en een kilometerstandhistorie kunnen direct of indirect worden herleid tot een identificeerbare eigenaar. Daarmee zijn het persoonsgegevens volgens de AVG. Een onderhoudshistorie kan bovendien onthullen waar iemand woont, werkt en reist. Behandel voertuigdossiers daarom met dezelfde zorgvuldigheid als klantgegevens: toegang strikt beperkt tot de betreffende klant en garage, hosting binnen de Europese Unie en heldere bewaartermijnen.

Veel Nederlandse garage-apps halen voertuiggegevens automatisch op via het kenteken met de openbare RDW Open Data. Die RDW-brongegevens zijn openbaar, maar zodra je ze in je systeem koppelt aan een specifieke klant en afspraak, ontstaan er persoonsgegevens — bovendien moet het zoek-endpoint worden beveiligd met rate-limiting zodat derden jouw app niet als gratis scrapingtool misbruiken.

## Beslissing 2 voor een Productierijpe AI-Applicatie: Hoe Worden Extra Reparaties Goedgekeurd?

De meest waardevolle functie voor een werkplaats brengt direct het grootste risico met zich mee: de monteur ontdekt tijdens een onderhoudsbeurt versleten remblokken, stuurt een prijsopgave met duidelijke foto's en de klant geeft in de app akkoord voor de meerprijs. Als die goedkeuring achteraf wordt betwist, heeft de garage sluitend bewijs nodig.

**De beslissingen:** bevries de exacte offerte die de klant heeft gezien (prijs, onderdelen, arbeid), leg de goedkeuring vast met een servertijdstempel en het geauthenticeerde account, zorg dat de geaccordeerde offerte niet meer kan worden gewijzigd en stuur direct een bevestiging. Goedkeuringslinks moeten cryptografisch onvoorspelbaar zijn en automatisch verlopen. Door AI gegenereerde apps laten vaak iedereen met een simpel ordernummer werk goedkeuren en herberekenen offertes achteraf live, met alle discussies van dien.

## Beslissing 3: Waar Komen Onderdelenprijzen Vandaan?

Prijzen van auto-onderdelen veranderen voortdurend en verschillen sterk per grossier. Als een offerte live rekent met een dynamische cataloguskoppeling, kan een reeds goedgekeurd bedrag verschuiven voordat de uiteindelijke factuur wordt opgemaakt. Sla de exacte inkoop- en verkoopprijs op op de offerteregel op het moment van offreren, inclusief leverancier en artikelnummer. Wijzigingen mogen uitsluitend plaatsvinden via een herziene offerteversie die de klant opnieuw accordeert.

## Beslissing 4: Sluit het Planbord Aan op de Werkelijkheid?

Werkplaatscapaciteit is afhankelijk van fysieke hefbruggen, specifieke gereedschappen, gecertificeerde monteurs en reële tijdsduur per klus. Een online boekingssysteem dat geen rekening houdt met werkelijke bezetting leidt steevast tot overboekte maandagochtenden. Dwing capaciteitsgrenzen af op de server per dag en resource, geef de werkplaats de optie om bloktijden in te stellen en vang uitloop van werkzaamheden flexibel op. Klanten moeten reëel beschikbare tijdsloten zien, geen optimistische kalender.

## Beslissing 5: Hoe Betalen Klanten?

Steeds meer particuliere klanten willen vooraf via hun smartphone betalen voordat ze hun auto ophalen. Dat vraagt om betrouwbare betaalkoppelingen via Mollie of Stripe met iDEAL, gevalideerd via geverifieerde server-webhooks, en een onlosmakelijke statuskoppeling tussen betaling, factuur en werkorder — zodat de baliemedewerker direct ziet dat de sleutel mag worden overhandigd. Lease- en zakelijke vlootklanten betalen daarentegen meestal achteraf op rekening via verzamelorders.

## Beslissing 6: Foto's en Bewijslast

Foto's van voor en na de reparatie, of foto's van versleten onderdelen, beschermen zowel het autobedrijf als de klant. Sla deze media privé op, strip locatiemetadata (EXIF), comprimeer beelden voor mobiele netwerken en koppel ze direct aan de bijbehorende werkorder en offerteregel.

## Beslissing 7: Meerdere Garages, Eén App (Multi-Tenant)

Wanneer jouw SaaS-app meerdere onafhankelijke garages bedient, moet elke vestiging strikt afgeschermd zijn: garages mogen uitsluitend hun eigen klanten, voertuigen, inkoopprijzen en werkorders zien, afgedwongen in de database via Row-Level Security. Monteurs die wisselen van werkgever moeten direct hun toegangsrechten verliezen.

## Een Datamodel voor Werkplaatsen

Een AI-applicatie die productierijp is voor de autobranche vereist een datamodel dat exact weerspiegelt hoe een professionele garage functioneert:

| Entiteit | Belangrijke velden | Opmerkingen |
| --- | --- | --- |
| Klant | Naam, contactgegevens, particulier/zakelijk, garage_id | Strikt gescheiden per garage in multi-tenant opzet |
| Voertuig | Kenteken, chassisnummer (VIN), merk/model, datum eerste toelating, tellerstand | Kan in de loop der tijd aan meerdere klanten gekoppeld zijn |
| Werkorder | Voertuig, gevraagde werkzaamheden, status, brug, monteur, geplande start/eind | De kerneenheid van de werkplaatsplanning |
| Offerte | Werkorder, versienummer, regels (onderdelen, arbeid), totalen, status, tijdsstempels | Onwijzigbaar (bevroren) per versie |
| Onderdeelregel | Artikelnummer, grossier, aantal, prijs op offertemoment | Opgeslagen vaste prijs, geen live koppeling |
| Goedkeuring | Offerteversie, goedgekeurd door, methode, servertijdstempel | Onweerlegbaar digitaal bewijs |
| Factuur | Werkorder, regels overgenomen van geaccordeerde offerte, btw-uitsplitsing, betaalstatus | Opeenvolgende ononderbroken nummering |
| Foto's / Media | Werkorder, fase (voor/na/defect), geüpload door, tijdstempel | Beveiligde private storage met signed URL's |

Omdat voertuigen van eigenaar wisselen, moet het voertuigdossier losstaan van de klantrelatie; een nieuwe eigenaar mag nooit de privégegevens of facturen van de vorige eigenaar kunnen inzien.

## Offerteversiebeheer en Goedkeuringen, Stap voor Stap

1. De monteur stelt tijdens de inspectie een offerte op voor aanvullende reparaties, voorzien van foto's en een duidelijke toelichting.
2. Het systeem bevriest de offerte als versie 1 en berekent het totaalbedrag op basis van vastgelegde onderdelen- en uurtarieven.
3. De klant ontvangt een sms of pushnotificatie met een veilige, cryptografische link (unieke token, gekoppeld aan de klant, met beperkte geldigheidsduur).
4. De klant accordeert of weigert in de app; de beslissing wordt onherroepelijk gelogd met een servertijdstempel en het gebruikersaccount.
5. Moet er nadien toch iets wijzigen? Dan genereert het systeem versie 2; versie 1 blijft bewaard als vervallen historisch document.
6. De eindfactuur wordt automatisch samengesteld uit de goedgekeurde versie, waardoor verrassingen bij het afrekenen zijn uitgesloten.

Deze workflow verandert discussies zoals "ik heb hier nooit toestemming voor gegeven" in een heldere dialoog met schriftelijk en digitaal bewijs.

## Capaciteitsplanningslogica

Werkplaatscapaciteit is een samenspel van fysieke middelen: beschikbare bruggen, speciale diagnoseapparatuur en monteurs met specifieke vakkennis (zoals certificering voor elektrische en hybride voertuigen). Een betrouwbare capaciteitscheck bij een online afspraak houdt rekening met de standaardduur van de werkzaamheden, de beschikbaarheid van een geschikte brug en monteur, en realistische marges voor uitloop. Sla standaardtijden per onderhoudsbeurt op en laat de werkplaatschef marges finetunen. Dwing beschikbaarheid af in de database, zodat twee klanten nooit op hetzelfde moment dezelfde brug kunnen reserveren.

## Verantwoord Omgaan met Voertuigdata (RDW)

Kentekenchecks via openbare voertuigregisters versnellen de invoer en voorkomen typefouten. Pas dit verantwoord toe: vereis authenticatie voor zoekopdrachten, implementeer rate-limiting, cache voertuigdata tijdelijk per kenteken om externe API-belasting te minimaliseren en bewaar uitsluitend de noodzakelijke velden. Zodra een kentekenopvraag wordt gekoppeld aan een klantaccount, valt het onder de privacyverklaring en retentieregels van je applicatie.

## Betalingen en Voertuigvrijgave

Het koppelen van de online betaling aan de fysieke voertuigvrijgave voorkomt ongemakkelijke situaties aan de receptiebalie. Zodra de factuur gereed is, stuurt de app een betaallink; zodra Mollie of Stripe de betaling via een betrouwbare webhook bevestigt, markeert het systeem de werkorder als 'Betaald' en toont de receptie de melding 'Gereed voor teruggave'. Voor zakelijke relaties op rekening wordt de status direct ingesteld op 'Factuur op termijn'. Eventuele aanbetalingen of deelbetalingen moeten direct inzichtelijk zijn op de werkorder.

## Onderdelenleveranciers en Prijswijzigingen

Grossiersprijzen kunnen dagelijks fluctueren. Wanneer jouw applicatie prijzen synchroniseert met leverancierscatalogi, leg dan altijd de actuele inkoopprijs en opslag vast op de offerteregel op het moment dat de prijsopgave wordt verstuurd. Als een grossier zijn prijs verhoogt voordat de klant akkoord heeft gegeven, kan de garagehouder besluiten de offerte te herzien. Sluit periodiek de inkoopfacturen van grossiers kort met de berekende offerteregels om eventuele margemarges te bewaken.

## Beveiliging voor Multi-Garage Platformen

Wanneer één SaaS-platform meerdere onafhankelijke autobedrijven ondersteunt, zijn klantgegevens, voertuighistories en uurtarieven strikt bedrijfsvertrouwelijk. Dwing isolatie tussen garages af op databaseniveau, valideer dit met geautomatiseerde penetratietests, vereis tweestapsverificatie (MFA) voor werkplaatspersoneel en log alle toegang tot klantinformatie. Monteurs die voor meerdere vestigingen werken, moeten beschikken over gescheiden rollen die direct kunnen worden ingetrokken.

## Communicatievoorkeuren van Klanten

Klanten willen tijdige updates, geen overbodige reclame. Laat klanten zelf kiezen via welke kanalen ze updates ontvangen (e-mail, sms of app-notificaties) voor statusberichten, offertes en facturen, en leg marketingtoestemming afzonderlijk vast. Automatische APK- en onderhoudsherinneringen op basis van datum of kilometerstand zijn zeer effectief, maar gelden juridisch vaak als commerciële communicatie; verstuur deze alleen met expliciete toestemming of een geldige wettelijke grondslag.

## Mobiele Workflows voor Monteurs

Monteurs werken met vuile handen, handschoenen en een strakke planning. De werkplaatsinterface van de app moet geoptimaliseerd zijn voor deze realiteit: snelle foto-opname direct gekoppeld aan de actieve werkorder, spraak-naar-tekst voor monteursnotities, grote aanraakknoppen, offline veerkracht bij een zwak wifi-signaal in de werkplaats en duidelijke statusknoppen ("Wachten op onderdelen", "Gereed voor proefrit"). Foto's moeten betrouwbaar op de achtergrond worden geüpload met automatische retry-logica.

## Garantie- en Terugroepinformatie

Garages voeren regelmatig werkzaamheden uit onder fabrieksgarantie of handelen terugroepacties af. Registreer welke klussen onder garantie vallen, welke onderdelen specifieke fabrieksgarantietermijnen dragen en koppel officiële terugroepmeldingen automatisch aan geregistreerde voertuigen in het klantenbestand. Dit biedt kansen voor gerichte service én beschermt de garage wanneer garantieclaims achteraf worden geaudit.

## Rapportages voor Garagehouders

Ondernemers in de autobranche sturen op duidelijke cijfers: bezettingsgraad van hefbruggen, gemiddelde doorlooptijd versus geplande uren, het conversiepercentage van meerwerkoffertes, omzet per monteur, openstaande debiteuren en terugkerende klanten. Bouw dashboards op basis van opgeslagen, historische data zodat rapportages over eerdere kwartalen stabiel en accuraat blijven. Deze analyses leveren direct bruikbare inzichten op — bijvoorbeeld dat offertes met duidelijke detailfoto's tot 40% vaker worden goedgekeurd.

## Launch Checklist voor Garage-Apps

Voordat de eerste klanten worden uitgenodigd:
- Voertuig- en klantdata strikt gescheiden per garage met geteste autorisatieregels.
- Offertes bevroren per versie met beveiligde, tijdelijke goedkeuringslinks.
- Onderdelenprijzen vastgelegd op regelniveau bij het verzenden.
- Werkplaatscapaciteit server-side afgedwongen per hefbrug en monteur.
- Betalingen geverifieerd via server-webhooks en gekoppeld aan voertuiggave.
- RDW-kentekenchecks voorzien van authenticatie en rate-limiting.
- Werkplaatsfoto's privé opgeslagen met gestripte metadata.
- Communicatievoorkeuren en opt-ins voor APK-herinneringen vastgelegd.
- Continue monitoring, geautomatiseerde back-ups en uptime-alerts actief.

Met deze basis versterkt de applicatie het vertrouwen waar lokale kwaliteitsgarages op bouwen.

## Waarom Juist Onafhankelijke Garages Hierbij Winnen

Grote dealernetwerken investeren miljoenen in software; onafhankelijke dorps- en stadsgarages onderscheiden zich door vakmanschap, eerlijkheid en persoonlijk contact. Een productierijpe klanten-app — met transparante offertes, betrouwbare planning en moeiteloos digitaal betalen — stelt de lokale garage in staat een moderne ervaring te bieden die de dealer evenaart of overtreft, terwijl het persoonlijke karakter behouden blijft.

## Veelvoorkomende Fouten in met AI Gebouwde Garage-Apps

Bij prototypes die met AI zijn gebouwd, zien we steeds dezelfde kwetsbaarheden terug: offertes die dynamisch meebewegen met fluctuerende catalogusprijzen, acceptatielinks die gebaseerd zijn op eenvoudige ordernummers die iedereen kan raden, boekingen die worden geaccepteerd zonder dat er een hefbrug vrij is, betaalstatussen die alleen in de browserredirect worden bijgewerkt, foto's in openbare buckets en één gedeeld beheerdersaccount voor de hele werkplaats. Geen van deze problemen vereist dat je opnieuw begint; het zijn gerichte technische ingrepen die binnen één tot twee weken kunnen worden gecorrigeerd.

## De Eerste Stap

Stuur jezelf vanuit je eigen applicatie een offerte voor een proefreparatie, keur deze goed en probeer vervolgens in het beheerderspaneel of de API de prijs aan te passen. Als dat lukt, is het bevriezen van offerteversies de allereerste prioriteit.

## Waar LaunchStudio het Verschil Maakt

LaunchStudio transformeert met AI gebouwde garage-apps naar robuuste productiesoftware: betrouwbare isolatie van voertuig- en klantdata, veilige offerte-acceptatie met onveranderbare prijzen en auditlogs, capaciteitsgestuurde planning, gevalideerde iDEAL-betalingen, beveiligde foto-opslag en multi-tenant architectuur. LaunchStudio wordt ondersteund door Manifera, een softwarebedrijf met meer dan 11 jaar ervaring in operationele en industriële platforms (waaronder MO Batteries in de energiesector), werkzaam vanuit Ho Chi Minhstad, Amsterdam en Singapore. Bekijk [Manifera's web app development diensten](https://www.manifera.com/services/web-app-develop/); het [RDW open data portaal](https://opendata.rdw.nl/) documenteert welke voertuigdata openbaar toegankelijk is.

[Bereken direct de investering voor jouw applicatie](https://launchstudio.eu/nl/#calculator) — de categorie "Tool" of "SaaS" met betalingsmodule sluit naadloos aan op de meeste garage-applicaties.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Garage-App en een Goedgekeurde Offerte die Veranderde

Ferry Janssen, eigenaar van een onafhankelijk autobedrijf in Helmond, bouwde Garagepost met behulp van Bolt: klanten plannen hun onderhoud op basis van kentekeninvoer, ontvangen foto-offertes voor geconstateerd meerwerk, keuren deze goed via hun smartphone en betalen voorafgaand aan het ophalen. Drie bevriende universele garages in de regio Helmond-Eindhoven sloten zich al snel aan.

Een klacht van een vaste klant legde het fundamentele probleem bloot. De klant had via de app akkoord gegeven op een offerte van € 480 voor nieuwe remschijven en blokken, maar op de factuur stond opeens € 560. De grossiersprijs van de onderdelen was tussen het akkoord en de facturatie gestegen, en de app herberekende offertes telkens live. Een grondige audit bracht nog meer risico's aan het licht: de acceptatielinks waren eenvoudige ordernummers die iedereen kon raden, klanten van de ene garage konden via de API werkorders en facturen van een andere garage inzien, maandagochtenden waren chronisch overboekt omdat er geen hefbrugcapaciteit werd gecontroleerd, betalingen werden al als voltooid gemarkeerd zodra de browser terugkeerde van de bank, en de RDW-kentekencheck kon duizenden keren per dag anoniem worden aangeroepen.

In acht werkdagen hebben de engineers van LaunchStudio offertes onherroepelijk bevroren op het moment van verzending, onderdelenprijzen vastgelegd per regel inclusief grossiersreferenties, de openbare links vervangen door cryptografische tijdelijke tokens gekoppeld aan het klantaccount, acceptaties gelogd met servertijdstempels, garage-isolatie afgedwongen met PostgreSQL Row-Level Security, capaciteitslimieten per brug en monteur ingebouwd in de afsprakenmodule, betalingen gekoppeld aan geverifieerde Mollie-webhooks met statusvrijgave voor de balie, rate-limiting geactiveerd op de RDW-zoekfunctie en foto's ondergebracht in private storage.

**Resultaat:** Discussies over factuurbedragen verdwenen volledig, omdat elke offerte nu een vaste prijs en een sluitend digitaal dossier heeft. Overboekingen op maandag behoren tot het verleden, en Garagepost heeft inmiddels vier extra autobedrijven in Noord-Brabant aangesloten.

> *"Klanten vertrouwen een garage die hen de foto en de prijs laat zien. Ze verliezen dat vertrouwen op het moment dat de prijs verandert nadat ze 'ja' hebben gezegd."*
> — **Ferry Janssen, Oprichter, Garagepost (Helmond)**

**Kosten & Tijdlijn:** € 2.200 (Launch Ready-pakket: offerte-integriteit, toegangscontrole, capaciteitsplanning, betalingen en databeveiliging) — afgerond in 8 werkdagen.

## Veelgestelde Vragen

### Is een kenteken een persoonsgegeven volgens de AVG?

In veel gevallen wel. Omdat een kenteken direct kan worden gekoppeld aan een identificeerbare voertuigeigenaar, geldt het onder de privacywetgeving als persoonsgegeven. Behandel voertuiggegevens daarom met dezelfde waarborgen als klantprofielen.

### Hoe moet een garage-app omgaan met klantakkoorden op meerwerk?

Bevries de offerte op het moment dat de klant deze te zien krijgt, leg het akkoord vast met een betrouwbare servertijdstempel en het geauthenticeerde account, blokkeer latere wijzigingen en stuur onmiddellijk een bevestiging.

### Mag een garage-app zomaar RDW-voertuigdata gebruiken?

De RDW stelt voertuiggegevens beschikbaar als Open Data, wat ideaal is voor automatische kentekenopzoekingen. Zodra je deze data echter combineert met klantprofielen, ontstaan persoonsgegevens in jouw systeem. Beveilig het zoek-endpoint bovendien tegen misbruik met rate-limiting.

### Hoe helpt Manifera's ervaring met operationele systemen bij garage-apps?

Manifera heeft ruime ervaring met het bouwen van complexe operationele platforms voor industriële en energiebedrijven (zoals MO Batteries). De engineers zijn gewend aan workflows waarin planning, voorraadbeheer, onderdelenprijzen en sluitend bewijsmateriaal naadloos moeten kloppen.

### Kan een online garage-app helpen om beter vindbaar te zijn in Google?

Zeker. Afspraakpagina's met heldere diensten, actuele openingstijden en Local Business structured data (JSON-LD) versterken de lokale vindbaarheid in zoekmachines en maken de garage zichtbaar in AI-zoeksystemen bij vragen zoals "waar kan ik betrouwbaar mijn auto laten onderhouden in de buurt".

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is een kenteken een persoonsgegeven volgens de AVG?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In veel gevallen wel, omdat een kenteken gekoppeld kan worden aan een identificeerbare eigenaar. Behandel voertuiggegevens met dezelfde beveiliging als andere klantgegevens."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe moet een garage-app omgaan met klantakkoorden op meerwerk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Bevries de offerteversie, registreer het akkoord met servertijdstempel en gebruikersaccount, blokkeer latere prijswijzigingen en verstuur een schriftelijke bevestiging."
      }
    },
    {
      "@type": "Question",
      "name": "Mag een garage-app zomaar RDW-voertuigdata gebruiken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, RDW-data is open data, maar gekoppeld aan klanten ontstaat persoonsdata in jouw database. Beveilig het zoek-endpoint met authenticatie en rate-limiting."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt Manifera's ervaring met operationele systemen bij garage-apps?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ervaring met industriële en energieplatforms (zoals MO Batteries) zorgt voor bewezen patronen in planning, onderdelenbeheer en sluitende bewijsvoering."
      }
    },
    {
      "@type": "Question",
      "name": "Kan een online garage-app helpen om beter vindbaar te zijn in Google?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, door gestructureerde afspraakpagina's met diensten, openingstijden en Local Business schema markup voor betere lokale zoekresultaten."
      }
    }
  ]
}
</script>
