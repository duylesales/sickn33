---
Titel: "Een AI-Recruitmenttool Bouwen? Productieproblemen van AI-Apps met CV's en Toestemming"
Trefwoorden: ai app productieproblemen, ai recruitment tool, cv data avg, kandidaat toestemming, eu ai act werving, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Een AI-Recruitmenttool Bouwen? Productieproblemen van AI-Apps met CV's en Toestemming

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Een AI-Recruitmenttool Bouwen? Productieproblemen van AI-Apps met CV's en Toestemming",
  "description": "Recruitmenttools die zijn gebouwd met AI verwerken cv's, contactgegevens en vaak gevoelige persoonsgegevens van kandidaten. Dit artikel behandelt de specifieke productieproblemen bij AI-werving: cv-opslag, bewaartermijnen, toestemming, recruiter-autorisaties, AI-selectieregels en kandidaatrechten.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-25",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/building-an-ai-recruitment-tool-ai-app-production-problems-with-cvs-and-consent" }
}
</script>

Een oprichter in Friesland uploadde haar eerste echte batch cv's - 180 sollicitaties voor vacatures in lassen en installatietechniek - in de recruitmenttool die ze in Lovable had gebouwd. De AI-matching werkte. Recruiters waren enthousiast. Toen mailde een kandidaat met de vraag waarom een bedrijf waar hij nooit had gesolliciteerd hem had gebeld, en besefte ze dat elke recruiter op het platform elk cv kon doorzoeken, inclusief kandidaten die op één specifieke vacature bij één specifiek bedrijf hadden gereageerd - een schoolvoorbeeld van de productieproblemen van AI-apps waar recruitmenttools tegenaan lopen.

Bouwt u een AI-recruitmenttool, dan zijn dit de problemen die bepalen of u kunt lanceren: niet of de matching werkt, maar of kandidaatdata wordt behandeld zoals kandidaten, werkgevers en toezichthouders verwachten.

## Waarom Cv's Gevoeliger Zijn dan Ze Lijken

Een cv is per definitie persoonsgegevens: naam, adres, telefoon, e-mail, geboortedatum, werkervaring, opleiding, vaak een foto. Veel cv's bevatten ook informatie die kandidaten niet breed zouden delen - gaten door gezondheid, nationaliteit, religie die blijkt uit scholen of vrijwilligerswerk, functies binnen een vakbond. Een deel daarvan zijn bijzondere persoonsgegevens onder artikel 9 van de AVG, waarvoor strengere bescherming geldt.

Werving kent ook een machtsongelijkheid. Kandidaten kunnen moeilijk weigeren gegevens te delen met een mogelijke werkgever, en daarom letten toezichthouders extra op hoe wervingsdata wordt gebruikt en bewaard.

## Probleem 1: Iedereen Kan Alles Zien

AI-gegenereerde recruitmentapps hebben meestal één cv-tabel en een zoekfunctie. De interface toont een recruiter misschien alleen de kandidaten voor zijn eigen vacatures, maar de API geeft alles terug. In een omgeving met meerdere werkgevers of een uitzendbureau betekent dat dat kandidaten worden blootgesteld aan organisaties waar ze nooit op hebben gesolliciteerd.

Het model voor productie beperkt de toegang expliciet: de gegevens van een kandidaat zijn zichtbaar voor de organisatie waarop hij heeft gesolliciteerd (of voor recruiters met wie hij heeft ingestemd te delen), afgedwongen in de database. Talentpools - waarin kandidaten ermee instemmen te worden overwogen voor andere functies - vereisen aparte, expliciete toestemming.

## Probleem 2: Cv's voor Altijd Opgeslagen, en Openbaar

Geüploade cv-bestanden belanden vaak in opslagbuckets met openbare URL's, omdat dat de makkelijkste manier is om een bestand te tonen. Iedereen met de link - of iedereen die het patroon kan raden - kan ze downloaden. En er wordt nooit iets verwijderd.

Afhandeling op productieniveau betekent privéopslag met kortlevende ondertekende links, virusscans bij uploaden en bewaarregels. Richtlijnen van de Nederlandse toezichthouder geven al lang aan dat sollicitatiegegevens doorgaans binnen ongeveer vier weken na afloop van een procedure moeten worden verwijderd, of tot een jaar met toestemming van de kandidaat voor toekomstige vacatures. Uw tool moet dat automatisch uitvoeren; recruiters gaan het niet met de hand doen.

## Probleem 3: Toestemming Die Niet Wordt Vastgelegd

"Door te solliciteren gaat u akkoord met ons privacybeleid" is geen registratie van toestemming. Houdt u kandidaten in een talentpool, deelt u ze met andere klanten of gebruikt u hun gegevens om de matching te trainen of te verbeteren, dan heeft u een duidelijke, vastgelegde keuze nodig: waarmee ze instemden, wanneer en met welke versie van de tekst. Kandidaten moeten die toestemming even makkelijk kunnen intrekken als ze die gaven.

## Probleem 4: Regels voor AI-Screening

Werving is een van de gebieden die de EU AI Act als hoog risico classificeert wanneer AI-systemen worden gebruikt om kandidaten te screenen, te filteren of te beoordelen. Rangschikt of wijst uw tool kandidaten automatisch af, dan gelden verplichtingen rond risicobeheer, menselijk toezicht, transparantie en registratie, die de komende periode gefaseerd ingaan. Daarnaast beperkt artikel 22 van de AVG besluiten die uitsluitend op geautomatiseerde verwerking zijn gebaseerd en aanzienlijke gevolgen hebben, zoals afwijzing.

In de praktijk hoort een recruitmenttool in productie een mens in de besluitvorming te houden, recruiters uit te leggen waarom een matchscore is gegeven, het gebruik van beschermde kenmerken te vermijden (direct of via proxy's zoals foto's, namen of postcodes), te loggen hoe scores tot stand kwamen en kandidaten te vertellen dat AI het proces ondersteunt. Het [overzicht van de EU AI Act](https://artificialintelligenceact.eu/) vat de eisen voor hoog risico samen.

## Probleem 5: Rechten van Kandidaten

Kandidaten kunnen om inzage, correctie of verwijdering van hun gegevens vragen. Ze kunnen ook vragen wat een organisatie na een afwijzing nog over hen bewaart. Een tool in productie heeft een manier nodig om alle gegevens over één persoon te vinden - over sollicitaties, notities, berichten en bestanden heen - ze te exporteren en volledig te verwijderen, ook uit zoekindexen en eventuele AI-embeddings die van hun cv zijn gemaakt.

## Probleem 6: Notities van Recruiters

Recruiters schrijven notities. Soms zijn die notities onprofessioneel of bevatten ze gevoelige observaties. Kandidaten kunnen om inzage erin vragen. Tools moeten notities alleen zichtbaar maken binnen de werving organiserende organisatie, feitelijke inhoud stimuleren en ze opnemen in processen voor inzage en verwijdering.

## Productieproblemen van AI-Apps Oplossen: Zo Ziet een Gereede Recruitmenttool Eruit

- Toegang per organisatie afgedwongen in de database
- Privéopslag van cv's, ondertekende links, scannen bij uploaden
- Automatisch bewaren en verwijderen
- Vastgelegde, intrekbare toestemming voor talentpools en delen
- Menselijke beoordeling van AI-scores, met uitleg en logs
- Zoeken, exporteren en volledig verwijderen per kandidaat
- Hosting in de EU, ook voor verwerking door AI-modellen waar mogelijk
- Een lijst met verwerkers die elke dienst omvat die met cv's in aanraking komt

## De Toestemmingsflow Goed Ontwerpen

Toestemming bij werving wordt vaak verkeerd begrepen. Voor het verwerken van een sollicitatie op een specifieke vacature is de rechtsgrond meestal het nemen van stappen richting een mogelijke overeenkomst, niet toestemming. Toestemming wordt relevant voor wat daarbuiten valt: een kandidaat in een talentpool houden, zijn profiel met andere werkgevers delen of zijn gegevens gebruiken om de matching te verbeteren. Een productierijpe toestemmingsflow dus:

- Legt in gewone taal uit wat er met de sollicitatie zelf gebeurt, zonder om toestemming te vragen.
- Biedt **aparte, niet-aangevinkte keuzes** voor talentpools, delen en verbetering van het model.
- Legt elke keuze vast met de exacte getoonde tekst, de versie en een tijdstempel.
- Laat kandidaten hun keuzes wijzigen vanuit hun account of via een link in elke e-mail.
- Voert intrekking automatisch door - de kandidaat wordt direct uit pools en gedeelde weergaven verwijderd.

Een tabel met toestemmingsregistraties kan `candidate_id`, `purpose`, `granted`, `text_version`, `recorded_at` en `source` bevatten. Die kleine structuur beantwoordt de vraag die toezichthouders en werkgevers het vaakst stellen: "kunt u laten zien waarmee deze persoon instemde, en wanneer?"

## AI-Matchscores Uitleggen

Rangschikt of scoort uw tool kandidaten, dan zullen recruiters en kandidaten vragen waarom. Een uitlegbare score laat zien aan welke eisen werd voldaan (certificaten, jaren ervaring, talen, locatie) en welke ontbraken, in plaats van één ondoorzichtig getal. Beperk de invoer van de score tot functierelevante criteria, log de versie van het model of de regels die de score maakten, en houd scores adviserend: de recruiter beslist, het systeem ondersteunt. Deze aanpak sluit aan bij de nadruk van de EU AI Act op menselijk toezicht en transparantie bij toepassingen met een hoog risico, en het maakt de tool nuttiger - recruiters vertrouwen suggesties die ze begrijpen.

## Indirecte Discriminatie via Proxy's Vermijden

Ook als beschermde kenmerken worden uitgesloten, kunnen andere velden als proxy werken: postcode (voor etniciteit of inkomen), afstudeerjaar (voor leeftijd), foto's (voor geslacht, etniciteit en leeftijd), gaten in de loopbaan (voor ouderschapsverlof of ziekte), namen (voor herkomst). Praktische maatregelen zijn onder meer foto's en geboortedata weglaten uit wat de matchinglogica ziet, locatie op postcodeniveau niet in de score gebruiken (maar reisafstandsbanden), uitkomsten tussen groepen testen waar dat wettelijk mag en haalbaar is, en deze keuzes documenteren. Het is makkelijker dit vanaf het begin in te bouwen dan achteraf uit te leggen waarom een model een bepaalde groep bevoordeelde.

## Bewaartermijnen in de Praktijk

Bewaarregels werken alleen als ze automatisch draaien. Een typische implementatie:

| Data | Standaard bewaartermijn | Trigger |
| --- | --- | --- |
| Sollicitatie op een vacature | Ongeveer vier weken na sluiting van de vacature | Wijziging van de vacaturestatus |
| Profiel in de talentpool | Tot een jaar met toestemming | Datum van toestemming; herinnering vóór afloop |
| Notities van recruiters | Gelijk aan de sollicitatie waar ze bij horen | Gekoppeld aan de sollicitatie |
| Cv-bestanden en embeddings | Gelijk aan het profiel | Verwijderd met het profiel |
| Auditlogs | Langer, zonder cv-inhoud | Apart vastgesteld |

Een nachtelijke taak past deze regels toe, en een rapport laat zien wat er is verwijderd. Vraagt een kandidaat "heeft u mijn cv nog?", dan is het antwoord precies.

## Scheiding tussen Werkgevers en Bureaus

Op platforms die meerdere werkgevers of bureaus bedienen, moet de scheiding absoluut zijn: een werkgever ziet sollicitanten op zijn eigen vacatures en, alleen met toestemming, kandidaten uit de pool; bureaus zien alleen kandidaten die zij hebben voorgesteld of die zich hebben aangemeld. Dwing dit af in de database, pas het toe op zoekindexen en embeddings net zo goed als op tabellen, en test het met negatieve tests. Veel datalekken in werving gebeuren in zoekfuncties, waar één index alle tenants omvat.

## Beveiliging van Kandidaataccounts

Kandidaten solliciteren vaak één keer en vergeten hun account. Bied inloggen zonder wachtwoord of via een magische link met korte geldigheid, vermijd langlevende sessies, sta het verwijderen van een account toe zonder contact met support, en stuur cv's nooit als e-mailbijlage naar recruiters - stuur in plaats daarvan een link naar het platform. Eis voor recruiteraccounts meerfactorauthenticatie, omdat een gecompromitteerd recruiteraccount veel kandidaten tegelijk blootstelt.

## Voorbereiden op Vragen van Werkgevers

Werkgevers en uitzendbureaus vragen leveranciers van recruitmenttools steeds vaker naar verwerkersovereenkomsten, bewaartermijnen, AI-gebruik, biastests en hostinglocatie. Stel een kort document op dat deze vragen beantwoordt, in lijn met hoe het systeem werkelijk werkt. Het verkort verkooptrajecten en laat zien dat de productieproblemen van uw AI-app zijn opgelost voordat ze de problemen van uw klanten werden.

## Verzoeken van Kandidaten Efficiënt Afhandelen

Kandidaten oefenen hun AVG-rechten vaker uit dan gebruikers van veel andere apps, omdat het hen uitmaakt wie hun cv heeft. Bouw een weergave per kandidaat die alles verzamelt: sollicitaties, notities, berichten, bestanden, toestemmingsregistraties, matchscores en verzonden e-mails. Vanuit die weergave moeten medewerkers alles in een leesbaar formaat kunnen exporteren en in één actie kunnen verwijderen of anonimiseren, inclusief zoekindexen en embeddings. Log elk verzoek en de datum van afhandeling. Zo kost een verzoek dat anders uren zoeken zou vergen een paar minuten, en is de termijn van één maand geen bron van stress meer.

## Beveiligingsincidenten Specifiek voor Werving

Recruitmentplatforms trekken specifieke dreigingen aan: nepvacatures om cv's te verzamelen, frauduleuze "recruiters" die kandidaten benaderen, en overname van recruiteraccounts om kandidatendatabases te downloaden. Tegenmaatregelen zijn onder meer werkgeversaccounts verifiëren voordat vacatures live gaan, bulkdownloads beperken en bewaken, waarschuwen bij ongebruikelijke exportactiviteit, MFA eisen voor recruiters en kandidaten een eenvoudige manier geven om verdacht contact te melden. Deze maatregelen beschermen kandidaten direct en beschermen de reputatie van het platform bij werkgevers.

## Hoe Het Er Goed Uitziet na de Lancering

Een recruitmenttool die zijn productieproblemen als AI-app heeft opgelost, laat dat in de dagelijkse praktijk zien: recruiters zien alleen hun eigen kandidaten, cv's verdwijnen volgens schema, kandidaten kunnen hun toestemming inzien en wijzigen, matchscores komen met redenen, en elk verzoek over rechten wordt ruim binnen een maand afgesloten. Dat zijn de signalen waar werkgevers en toezichthouders naar kijken.

## Hoe LaunchStudio Helpt

Het werk van LaunchStudio aan recruitmenttools implementeert deze maatregelen met behoud van de interface die uw recruiters al waarderen. Het omvat ook de minder zichtbare delen: cv-tekst uit logs en foutrapporten verwijderen, zorgen dat AI-API-aanroepen waar mogelijk geen data bewaren, en controleren dat verwijderingen embeddings en back-ups binnen hun bewaartermijn bereiken.

Achter LaunchStudio staat het team van Manifera met 120+ ervaren engineers, met 11+ jaar ervaring over 160+ projecten. De wortels van Manifera omvatten HR-gerelateerde en data-intensieve systemen, en de achtergrond in cybersecurity van CEO Herre Roelevink bepaalt mee hoe gevoelige data wordt behandeld. De engineering gebeurt in het ontwikkelcentrum in Ho Chi Minh-stad, met Europees contact via de Herengracht 420 in Amsterdam. Zie voor meer [maatwerksoftware van Manifera](https://www.manifera.com/services/custom-software-development/).

Staan er al kandidaten in uw systeem, [plan dan liever eerder dan later een gratis kennismakingsgesprek van 15 minuten](https://launchstudio.eu/nl/#contact).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Recruitmentplatform voor Technische Vakken in Friesland

Sophie Lambrecht, die in Leeuwarden een uitzendbureau voor technische vakken had geleid, bouwde Vakkracht in Lovable: een recruitmentplatform waarop installatie-, las- en bouwbedrijven vacatures plaatsen en een AI-model binnenkomende cv's matcht aan eisen zoals certificaten en rijbewijzen. Twaalf werkgevers en twee uitzendbureaus sloten zich in het eerste kwartaal aan, en ongeveer 1.400 kandidaten solliciteerden.

De hierboven beschreven klacht van een kandidaat leidde tot een review. LaunchStudio ontdekte dat alle recruiters via de API alle kandidaten konden doorzoeken; cv-bestanden stonden in een openbare opslagbucket met voorspelbare bestandsnamen; er werd nooit iets verwijderd; het vakje voor de talentpool was vooraf aangevinkt en werd nergens opgeslagen; de AI-matchscore zette kandidaten onder de 40% automatisch op "afgewezen" zonder menselijke beoordeling; en de volledige cv-tekst werd naar de foutregistratiedienst geschreven telkens als het parsen mislukte.

In elf werkdagen dwong het team toegang per organisatie af met row level security, verplaatste het cv's naar privéopslag met ondertekende links en malwarescans, implementeerde het automatische verwijdering vier weken na sluiting van een vacature (of twaalf maanden met vastgelegde toestemming voor de talentpool), verving het het vooraf aangevinkte vakje door een expliciete, geversioneerde toestemmingsregistratie met intrekking in één klik, veranderde het de automatische afwijzing in een beoordelingswachtrij voor recruiters met de uitleg van de match zichtbaar, verwijderde het cv-tekst uit logs, en bouwde het een tool voor export en verwijdering van kandidaatdata die ook embeddings verwijderde.

**Resultaat:** Vakkracht informeerde op advies de getroffen kandidaten en de toezichthouder, zonder verdere klachten. Daarna tekende een regionaal uitzendbureau dat eerder om privacyredenen had afgehaakt, en groeide het platform binnen zes maanden naar 31 werkgevers.

> *"De matching was het slimme deel, en het deel waar niemand zich zorgen over maakte. Iedereen maakte zich zorgen over wie de cv's kon zien - en terecht."*
> - **Sophie Lambrecht, Oprichter, Vakkracht (Leeuwarden)**

**Kosten & Tijdlijn:** € 3.300 (Launch Ready-pakket met toegangsbeheer, opslag, bewaartermijnen, toestemming en beoordelingsworkflow voor AI) - afgerond in 11 werkdagen.

## Veelgestelde Vragen

### Hoe lang mag een AI-recruitmenttool cv's bewaren?

Richtlijnen van de Nederlandse toezichthouder wijzen doorgaans op verwijdering van sollicitatiegegevens binnen ongeveer vier weken na afloop van een procedure, of tot een jaar met toestemming van de kandidaat. Bouw bewaartermijnen in het systeem in, zodat het automatisch gebeurt.

### Is de EU AI Act van toepassing op mijn kleine recruitmenttool?

Gebruikt uw tool AI om kandidaten te screenen, te filteren of te beoordelen, dan valt hij waarschijnlijk in de categorie hoog risico, met verplichtingen die gefaseerd ingaan. Mensen in de besluitvorming houden, scores uitleggen en processen loggen zijn nu al verstandige fundamenten.

### Kunnen kandidaten vragen wat recruiters over hen hebben geschreven?

Ja. Onder de AVG kunnen kandidaten inzage vragen in persoonsgegevens over hen, en daar kunnen notities van recruiters onder vallen. Tools moeten notities per kandidaat vindbaar en exporteerbaar maken.

### Hoe helpt de beveiligingsachtergrond van Manifera recruitmentstartups?

Wervingsdata is gevoelig en aantrekkelijk voor misbruik. De cybersecurity-ervaring van Herre Roelevink en het werk van Manifera aan data-intensieve systemen vormen een aanpak waarin het afbakenen van toegang, bewaartermijnen en logging worden ingebouwd in plaats van later toegevoegd.

### Kan zorgvuldige omgang met data helpen hoe kandidaten mijn platform vinden?

Ja. Kandidaten en werkgevers zoeken steeds vaker naar betrouwbare platforms, en AI-antwoordmachines putten uit reviews en openbare informatie. Een duidelijke privacypagina en een geschiedenis zonder incidenten ondersteunen aanbevelingen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe lang mag een AI-recruitmenttool cv's bewaren?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nederlandse richtlijnen wijzen doorgaans op ongeveer vier weken na afloop van een procedure, of tot een jaar met toestemming. Automatiseer de bewaartermijnen." }
    },
    {
      "@type": "Question",
      "name": "Is de EU AI Act van toepassing op mijn kleine recruitmenttool?",
      "acceptedAnswer": { "@type": "Answer", "text": "AI die kandidaten screent of beoordeelt valt waarschijnlijk onder hoog risico. Menselijke besluiten, uitgelegde scores en logging zijn verstandige fundamenten." }
    },
    {
      "@type": "Question",
      "name": "Kunnen kandidaten vragen wat recruiters over hen hebben geschreven?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Het inzagerecht onder de AVG kan notities van recruiters omvatten, dus notities moeten per kandidaat vindbaar en exporteerbaar zijn." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de beveiligingsachtergrond van Manifera recruitmentstartups?",
      "acceptedAnswer": { "@type": "Answer", "text": "Het zorgt ervoor dat afbakening van toegang, bewaartermijnen en logging voor gevoelige wervingsdata vanaf het begin worden ingebouwd." }
    },
    {
      "@type": "Question",
      "name": "Kan zorgvuldige omgang met data helpen hoe kandidaten mijn platform vinden?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Een duidelijke privacypagina en een schone staat van dienst ondersteunen vertrouwen en aanbevelingen door AI-antwoordmachines." }
    }
  ]
}
</script>
