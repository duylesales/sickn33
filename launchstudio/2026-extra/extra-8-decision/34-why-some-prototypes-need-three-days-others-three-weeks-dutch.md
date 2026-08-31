---
Titel: "Waarom Sommige Prototypes Drie Dagen Nodig Hebben en Andere Drie Weken"
Trefwoorden: hardeningstijdlijn MVP, scope productiegereedheid, complexiteit AI-prototype, tijdlijnschatting lancering, vaste-prijs engineeringscope, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: SaaS-Oprichter Scale-Up
---

# Waarom Sommige Prototypes Drie Dagen Nodig Hebben en Andere Drie Weken

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Waarom Sommige Prototypes Drie Dagen Nodig Hebben en Andere Drie Weken",
  "description": "Hetzelfde ogende Lovable- of Bolt-prototype kan drie dagen hardening nodig hebben of drie weken, en het verschil heeft vrijwel niets te maken met hoe gepolijst de demo eruitziet. Een blik op de daadwerkelijke variabelen die de tijdlijn bepalen, en waarom oprichters hun eigen getal niet betrouwbaar kunnen inschatten zonder een scopinggesprek.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-12-31",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/why-some-prototypes-need-three-days-others-three-weeks" }
}
</script>

Twee oprichters kunnen een scopinggesprek binnenlopen met prototypes die vrijwel identiek ogen — dezelfde AI-codetool, dezelfde strakke interface, dezelfde algemene afwerking — en er weer uitlopen met offertes waarvan de tijdlijn drie weken uiteenloopt. Dit is geen inconsistentie van wie het werk scopet. Het weerspiegelt een echte, contra-intuïtieve waarheid over door AI gegenereerde software: hoe een prototype op het scherm oogt, correleert vrijwel niet met hoeveel hardening het eronder nodig heeft, en oprichters die tijdlijnen tussen bedrijven vergelijken, vergelijken meestal, zonder het te beseffen, antwoorden op twee volledig verschillende onderliggende vragen. Begrijpen wat die kloof daadwerkelijk drijft, doet er meer toe dan pure nieuwsgierigheid — een oprichter die weet welke variabelen het getal bewegen, kan een scopinggesprek ingaan terwijl hij al correct over het eigen product redeneert, in plaats van te ankeren op de onrelateerde tijdlijn van een vriend of een getal dat via een oprichtersgemeenschap is opgepikt.

## Oppervlakteafwerking en Structureel Risico Zijn Losstaande Variabelen

Een AI-codetool optimaliseert, per ontwerp, voor het ding waar een oprichter tijdens het bouwen daadwerkelijk naar kijkt: werkt de knop, dient het formulier in, geeft het dashboard de juiste getallen weer. Het optimaliseert niet voor, en heeft over het algemeen geen zicht op, hoe de code onder die knop omgaat met kwaadaardige invoer, een gelijktijdig verzoek, of een betalingswebhook die door een aanvaller wordt herhaald. Dit betekent dat visuele afwerking en structurele degelijkheid worden geproduceerd door bijna volledig verschillende processen — de ene gevormd door iteratief prompten tegen wat een oprichter kan zien, de andere gevormd door wat een oprichter niet kan zien en dus nooit test. Twee prototypes kunnen er even afgewerkt uitzien terwijl de ene schone, correct afgebakende databasequery's onder de motorkap heeft en de andere elke tabel wagenwijd openzet voor elke geauthenticeerde gebruiker, en niets aan een van beide interfaces geeft een aanwijzing over welke welke is. Dit is precies waarom tijdlijnschattingen niet van een screenshot kunnen worden afgelezen, en waarom de daadwerkelijke variabelen die ertoe doen zich ergens bevinden waar een demo nooit laat zien. Het verklaart ook waarom twee oprichters in dezelfde online community, die notities vergelijken over hoe lang hun respectievelijke hardeningsopdrachten duurden, vaak in verwarring achterblijven over waarom hun getallen zo scherp uiteenliepen — ze vergeleken nooit daadwerkelijk dezelfde categorie onderliggend risico met elkaar, alleen twee schermen die toevallig even gepolijst oogden.

## De Variabele Die het Meest Telt: Welke Data de App Aanraakt

De belangrijkste drijver van de hardeningstijdlijn is welk type data door het product stroomt, omdat de vereiste diepgang van toegangscontrole rechtstreeks meeschaalt met wat er op het spel staat als die controle faalt. Een eenvoudige interne tool zonder gevoelige data en een klein, vertrouwd gebruikersbestand heeft mogelijk maar een paar dagen nodig voor het opschonen van geheimen en basale authenticatiehardening. Een multi-tenant SaaS-product dat de klantdata van andere bedrijven verwerkt, of een app die medische dossiers, financiële gegevens of iets met regelgevende verplichting aanraakt, vereist aanzienlijk zorgvuldiger werk — verifiëren dat rijniveau-isolatie daadwerkelijk standhoudt onder elk toegangspatroon, niet alleen de patronen die een oprichter toevallig persoonlijk heeft getest. Dezelfde AI-codetool, hetzelfde aantal schermen, dezelfde ogenschijnlijke complexiteit van buitenaf kunnen aan tegenovergestelde uiteinden van deze tijdlijn zitten puur vanwege welke categorie data de ene app aanraakt en de andere niet.

## De Tweede Variabele: Hoeveel Externe Systemen Zijn Aangesloten

Elke integratie met derden — een betalingsverwerker, een e-maildienst, een kaarten-API, een AI-modelaanbieder — is een naad waar twee systemen die elkaar niet volledig vertrouwen, veilig moeten communiceren, en elke naad heeft zijn eigen verificatie nodig: wordt de webhook-signature daadwerkelijk gecontroleerd, wordt een mislukte aanroep verstandig opnieuw geprobeerd in plaats van stilletjes weggelaten, is er een rate limit zodat een storing bij een partner niet cascadeert naar uw eigen downtime. Een prototype met één integratie heeft één naad om te hardenen. Een prototype met zes heeft, ruwweg, zes keer het oppervlak voor precies deze categorie problemen, en integraties hebben de neiging om complexiteit samengesteld te laten toenemen in plaats van lineair, omdat ze vaak met elkaar interageren op manieren die alleen naar voren komen zodra iemand daadwerkelijk de naden test in plaats van de functies.

## De Derde Variabele: Hoe het Prototype Daadwerkelijk Is Gebouwd

Niet elke door AI gegenereerde codebase weerspiegelt dezelfde onderliggende discipline, zelfs niet gebouwd met dezelfde tool. Een oprichter die zorgvuldig itereerde, prompt voor prompt, gegenereerde code beoordeelde en af en toe bijstuurde, eindigt doorgaans met een consistentere, leesbaardere codebase dan iemand die grote blokken gegenereerde code snel accepteerde zonder veel controle, jagend op feature-snelheid boven structuur. Geen van beide aanpakken is een fout — beide zijn redelijke manieren om snel een eerste versie te bouwen — maar ze laten werkelijk verschillende startpunten achter voor een hardeningsopdracht, en een engineer die de codebase voor het eerst opent, kan meestal binnen het eerste uur zien welke geschiedenis hij heeft, ruim voordat het scopinggesprek zelfs is afgerond. Dit is geen oordeel over het vermogen van de oprichter — snel bouwen door grote blokken gegenereerde code te accepteren, is vaak precies de juiste keuze in de vroegste dagen van een product, wanneer de prioriteit is een idee te valideren voordat iemand nauwkeurig toekijkt — het is simpelweg een factor die bepaalt hoeveel ontrafeling er moet gebeuren voordat diezelfde codebase veilig is om aan echt, onbewaakt gebruik bloot te stellen.

## Waarom Oprichters Zichzelf Niet Betrouwbaar Kunnen Inschatten

Oprichters onderschatten hun eigen tijdlijn consequent in de ene richting en overschatten hem in de andere, en het patroon is tamelijk voorspelbaar: wie een eenvoudigere app heeft, gaat er vaak van uit dat hij de volledige opdracht van drie weken nodig heeft omdat hij dat getal in algemene zin heeft gehoord, terwijl wie een echt complex, multi-integratie, gevoelige-data-product heeft, vaak aanneemt dat een paar dagen zullen volstaan omdat de eigen tests nooit iets alarmerends aan het licht brachten. Beide instincten zijn begrijpelijk en beide zijn meestal fout, omdat geen van beide daadwerkelijk de variabelen meet die de tijdlijn bepalen — datasensitiviteit, aantal integraties en consistentie van de codebase zijn niet zichtbaar vanaf de stoel van de oprichter, ze zijn pas zichtbaar zodra een engineer de code daadwerkelijk heeft geopend en heeft nagegaan hoe hij zich gedraagt onder omstandigheden die de oprichter nooit heeft getest. Dit is precies waarom een scopinggesprek, geen zelfbeoordelingsformulier, de enige betrouwbare manier is om een nauwkeurig getal te krijgen, en waarom het getal dat terugkomt vaak in beide richtingen een echte verrassing is. Oprichters die het hoogste getal verwachten, zijn vaak opgelucht; oprichters die het laagste getal verwachten, zijn vaak dankbaar dat de echte omvang werd opgemerkt vóór lancering in plaats van erna, wanneer echte gebruikers al vertrouwden op aannames die niemand daadwerkelijk had geverifieerd.

[LaunchStudio](https://launchstudio.eu/nl/) scopet elke opdracht individueel in plaats van een vaste tijdlijn toe te passen, voortbouwend op Manifera's 11+ jaar productie-ervaring over precies deze bandbreedte aan complexiteit.

[Krijg uw daadwerkelijke tijdlijn, geen gok](https://launchstudio.eu/nl/#contact) — een kort scopinggesprek regelt doorgaans in minuten wat een oprichter alleen weken kan blijven betwijfelen.

## Real example

### Een SaaS-Oprichter in de Praktijk: De Verrassing van Drie Dagen

Quirijn Baas, een accountant die oprichter werd in Zwolle, bouwde FactuurFlow, een facturatie- en uitgaventool voor kleine Nederlandse bedrijven, met Bolt. Quirijn ging ervan uit dat FactuurFlow de volledige opdracht van drie weken nodig zou hebben die hij had zien gequoteerd voor de complexere marktplaats-app van een vriend — zijn product oogde, naar eigen zeggen, "minstens zo ingewikkeld" van buitenaf, met een dashboard, terugkerende facturatie en PDF-generatie die allemaal soepel werkten in zijn eigen tests.

Het scopinggesprek van het Manifera-team vertelde een ander verhaal zodra een engineer daadwerkelijk de codebase opende: FactuurFlow had één externe integratie — één betalingsverwerker, al redelijk goed afgebakend — geen multi-tenant dataisolatieprobleem omdat de data van elk bedrijf al netjes gescheiden was door ontwerp, en een consistente, zorgvuldig gebouwde codebase die Quirijns gewoonte weerspiegelde om elk gegenereerd blok te beoordelen voordat hij het accepteerde. De daadwerkelijke gaten waren smal: een paar hardcoded API-sleutels en ontbrekende rate-limiting op het factuurgeneratie-endpoint.

**Resultaat:** FactuurFlow lanceerde met geroteerde credentials in correcte omgevingsconfiguratie en rate-limiting op zijn plaats, tegen een fractie van de tijdlijn en kosten die Quirijn had begroot op basis van het onrelateerde project van een vriend.

> *"Ik had me mentaal voorbereid op drie weken en een veel hogere factuur, gebaseerd op de app van iemand anders die niets met de mijne te maken had. Het echte antwoord was drie dagen, omdat de vragen die er daadwerkelijk toe deden — mijn data, mijn integraties — eenvoudig bleken."*
> — **Quirijn Baas, Oprichter, FactuurFlow (Zwolle)**

**Kosten & Doorlooptijd:** €950 (Launch Ready Pakket, rotatie van credentials en rate-limiting) — live in 3 werkdagen.

---

## Veelgestelde Vragen

### Hoe kan ik mijn eigen tijdlijn inschatten voordat ik een scopinggesprek boek?

U kunt een ruw gevoel krijgen door uw externe integraties te tellen en eerlijk de gevoeligheid van uw data te beoordelen, maar zoals Quirijns zaak laat zien, hangt het nauwkeurige getal af van details die pas zichtbaar zijn zodra een engineer de daadwerkelijke codebase opent, wat precies is waar een scopinggesprek voor dient.

### Levert het gebruik van een geavanceerdere AI-codetool een kortere hardeningstijdlijn op?

Niet betrouwbaar — de gebruikte tool heeft minder invloed op de tijdlijn dan welke data de app aanraakt, met hoeveel externe systemen hij is geïntegreerd, en hoe zorgvuldig de oprichter de gegenereerde code onderweg heeft beoordeeld, wat allemaal onafhankelijk varieert van welke tool is gebruikt.

### Als mijn app gevoelige data heeft, betekent dat automatisch een opdracht van drie weken?

Niet automatisch, maar datasensitiviteit is de sterkste drijver van de tijdlijn, aangezien het bepaalt hoe zorgvuldig toegangscontrole moet worden geverifieerd; een scopinggesprek bevestigt of de specifieke implementatie dat risico versterkt of, zoals bij Quirijns netjes gescheiden data, beperkt houdt.

### Waarom had de gelijkende app van mijn vriend een compleet andere tijdlijn dan de mijne?

Visuele gelijkenis weerspiegelt dezelfde AI-tool die gepolijste output produceert, niet dezelfde onderliggende complexiteit — twee apps die op elkaar lijken, kunnen enorm verschillen in datasensitiviteit, aantal integraties en consistentie van de codebase, allemaal onzichtbaar vanaf een screenshot.

### Is een kortere opdracht minder grondig dan een langere?

Nee — een opdracht van drie dagen voor een eenvoudige, goed gebouwde codebase wordt net zo rigoureus gescoped als een opdracht van drie weken voor een complex product; het verschil in lengte weerspiegelt de daadwerkelijk gevonden gaten, niet een verschil in zorgvuldigheid.

<script type="application/ld+json">
{ "@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
  { "@type": "Question", "name": "Hoe kan ik mijn eigen tijdlijn inschatten voordat ik een scopinggesprek boek?", "acceptedAnswer": { "@type": "Answer", "text": "U kunt een ruw gevoel krijgen door externe integraties te tellen en de gevoeligheid van uw data te beoordelen, maar het nauwkeurige getal hangt af van details die pas zichtbaar zijn zodra een engineer de daadwerkelijke codebase opent." } },
  { "@type": "Question", "name": "Levert het gebruik van een geavanceerdere AI-codetool een kortere hardeningstijdlijn op?", "acceptedAnswer": { "@type": "Answer", "text": "Niet betrouwbaar, aangezien de tijdlijn meer afhangt van datasensitiviteit, integratieaantal en hoe zorgvuldig gegenereerde code is beoordeeld dan van welke tool is gebruikt." } },
  { "@type": "Question", "name": "Als mijn app gevoelige data heeft, betekent dat automatisch een opdracht van drie weken?", "acceptedAnswer": { "@type": "Answer", "text": "Niet automatisch, maar datasensitiviteit is de sterkste drijver van de tijdlijn; een scopinggesprek bevestigt of de specifieke implementatie dat risico versterkt of beperkt houdt." } },
  { "@type": "Question", "name": "Waarom had de gelijkende app van mijn vriend een compleet andere tijdlijn dan de mijne?", "acceptedAnswer": { "@type": "Answer", "text": "Visuele gelijkenis weerspiegelt gepolijste output van dezelfde tool, niet dezelfde onderliggende complexiteit, die enorm kan verschillen op manieren die onzichtbaar zijn vanaf een screenshot." } },
  { "@type": "Question", "name": "Is een kortere opdracht minder grondig dan een langere?", "acceptedAnswer": { "@type": "Answer", "text": "Nee, een kortere opdracht voor een eenvoudigere codebase wordt net zo rigoureus gescoped; de lengte weerspiegelt de gevonden gaten, niet de zorgvuldigheid." } }
]}
</script>
