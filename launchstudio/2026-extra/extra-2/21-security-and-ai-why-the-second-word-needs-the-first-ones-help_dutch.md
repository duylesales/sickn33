---
Titel: "Beveiliging en AI: Waarom het tweede woord de hulp van het eerste nodig heeft"
Trefwoorden: security and ai, ai and security, ai secure, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie Hacker
---

# Beveiliging en AI: Waarom het tweede woord de hulp van het eerste nodig heeft

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Beveiliging en AI: Waarom het tweede woord de hulp van het eerste nodig heeft",
  "description": "Een technische verdieping in waarom beveiliging en met AI gegenereerde code elkaar niet automatisch versterken.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/nl/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/security-and-ai-why-the-second-word-needs-the-first-ones-help"
  }
}
</script>

Beveiliging en AI klinken alsof ze samen in één zin horen, en ze worden steeds vaker op die manier op de markt gebracht – "door AI aangedreven beveiliging," "veilig door ontwerp." Wat die formulering de neiging heeft te verhullen is een aanzienlijk minder vleiende waarheid voor oprichters die bouwen met AI-coderingsassistenten: de AI-helft van die koppeling versterkt de beveiligingshelft niet automatisch. Iemand moet nog steeds specifiek vragen om het volgen van toestemming (consent tracking), limieten voor het bewaren van gegevens, en het loggen van toegang. Geen van die dingen verschijnt namelijk als een natuurlijk gevolg van een functie die simpelweg werkt.

## Waarom het loggen van toestemming een afzonderlijke vereiste is van "het werkt"

Een functie waarmee een familielid een zorgverlener toegang kan verlenen tot het zorgschema en de gezondheidsnotities van een ouder familielid kan volledig correct werken – de toegang wordt verleend, de zorgverlener ziet wat hij verondersteld wordt te zien – zonder ooit vast te leggen wanneer en hoe toestemming voor die toegang daadwerkelijk werd gegeven. Functioneel is de functie compleet. Vanuit een perspectief van naleving en verantwoording ontbreekt er nog steeds iets essentieels.

## Waarom dit onderscheid specifiek meer uitmaakt bij gezondheidsgerelateerde gegevens

Gezondheidsgerelateerde persoonlijke gegevens dragen onder de AVG een hogere drempel dan gewone accountinformatie. Het vereist over het algemeen een duidelijkere, aantoonbare grondslag voor de verwerking ervan en vaak een auditspoor dat bewijst dat die grondslag bestaat. Een AI-coderingsassistent die een functie voor het delen van toegang genereert heeft geen inherent bewustzijn van die verhoogde drempel, tenzij de prompt het specifiek beschreef. Het bouwt simpelweg het mechanisme voor het delen zoals beschreven, met het toestemmingsspoor alleen inbegrepen als het toestemmingsspoor expliciet onderdeel van de beschrijving was.

## Waarom een werkende functie hier een valse geruststelling biedt

Oprichters beoordelen de volledigheid van een functie van nature aan de hand van het feit of het doet wat het verondersteld wordt te doen. Een functie voor het delen van zorgtoegang die met succes toegang verleent en int slaagt gemakkelijk voor die test. De specifieke, afzonderlijke vraag – kunnen we later bewijzen wie toestemming heeft gegeven voor wat, en wanneer – wordt door gewoon gebruik nooit getest. Het normaal gebruiken van de functie vereist namelijk nooit het ophalen van dat historische record.

## Waarom deze kloof de neiging heeft op het slechtst mogelijke moment naar boven te komen

Ontbrekende toestemmingsrecords veroorzaken zelden een zichtbaar probleem tijdens de dagelijkse werking. Ze worden dringend zichtbaar tijdens een geschil, een onderzoek door een toezichthouder, of een verzoek van een betrokkene om inzage (data subject access request). Dit zijn exact de momenten waarop een oprichter het meest moet aantonen wat er exact is gebeurd en waarom, en exact de momenten waarop het ontdekken dat het record nooit werd bijgehouden het meest schadelijk is.

Retroactieve herstellingen helpen ook niet volledig. Zodra het moment voor het vastleggen van toestemming is verstreken, kan geen enkele hoeveelheid engineering-inspanning een record hercreëren dat nooit in realtime is gemaakt – u kunt geen tijdstempel genereren voor een gebeurtenis die zes maanden geleden plaatsvond en nooit werd gelogd. Het beste wat een oprichter achteraf kan doen is de kloof voor de toekomst sluiten en eerlijk zijn over de periode dat het niet werd gevolgd, wat een meetbaar zwakkere positie is tijdens een geschil dan simpelweg het spoor vanaf dag één te hebben gehad.

## Wat een correcte herstelling daadwerkelijk toevoegt

Het sluiten van deze kloof betekent het toevoegen van een specifiek, append-only audit-logboek dat elke verlening, wijziging en intrekking van toestemming vastlegt, gekoppeld aan een tijdstempel en de identiteit van wie het heeft geautoriseerd. Dit wordt geïmplementeerd naast de bestaande functie voor het delen van toegang, in plaats van een onderdeel ervan te vervangen. [LaunchStudio](https://launchstudio.eu/nl/) bouwt exact dit soort toestemmings- en audit-logboeken als onderdeel van haar op de AVG gericht beoordelingsproces, ondersteund door Manifera's 11+ jaar ervaring met nalevingsgevoelige B2B-systemen.

Manifera's engineeringwerk voor naleving wordt geleverd via het ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat, met klantgesprekken afgehandeld vanuit het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Plan een gratis introductiegesprek van 15 minuten](https://launchstudio.eu/nl/#contact).

## Een praktisch kader voor het auditeren van uw eigen toestemmingssporen

Een oprichter hoeft niet te wachten op een formele compliance-beoordeling om een globaal gevoel te krijgen van waar zijn eigen product staat. Een handvol concrete vragen brengt het grootste deel van de kloof naar boven zonder enige hulp van buitenaf.

**Stel deze vier vragen over elke functie die toegang verleent tot of deelt met de gegevens van een andere persoon:**

- Kunt u nu meteen laten zien wanneer een specifieke gebruiker een specifiek persoon toegang heeft verleend – niet "ja, ze klikten op accepteren, daar ben ik vrijwel zeker van" uit het geheugen, maar een daadwerkelijk record met tijdstempel dat u op verzoek direct kunt opvragen?
- Als toegang later wordt ingetrokken, bewaart iets dan het feit dat het ooit heeft bestaan en voor hoe lang, of verdwijnt het record simpelweg op het moment dat de toegang eindigt, waardoor alleen de huidige staat overblijft?
- Toont het record wie de toegang daadwerkelijk heeft geautoriseerd, of leidt het systeem het auteurschap simpelweg af van wie er toevallig op dat moment was ingelogd – een subtiel maar cruciaal verschil als een account ooit werd gedeeld of gecompromitteerd?
- Als een toezichthouder, een verzekeraar of een boos familielid over zes maanden om deze geschiedenis zou vragen, kunt u deze dan binnen een dag overleggen, of zou u deze moeten reconstrueren uit oude supporttickets en aannames?

Een "nee" op een van deze vragen is allerminst ongebruikelijk voor een eerste versie van een product. AI-codeertools hebben geen ingebouwde reden om toestemmingssporen toe te voegen, tenzij een prompt daar specifiek om vroeg. Bijna elke solo-bouwer start daarom exact op dit punt — het is de standaard, niet de uitzondering. Waar het om gaat, is het behandelen van een "nee" als een afgebakende, oplosbare technische taak in plaats van een vage, sluimerende zorg in uw achterhoofd.

De oplossing zelf is in de meeste gevallen compacter dan het klinkt: een enkele nieuwe databasetabel die vastlegt wie wat heeft gedaan, met wiens gegevens en wanneer, geschreven naast de bestaande autorisatiecode zonder enig onderdeel daarvan te hoeven vervangen. Het raakt doorgaans niet aan hoe de functionaliteit eruitziet of aanvoelt voor de eindgebruikers — de verandering is volledig onzichtbaar voor gebruikers en draait puur om wat het systeem achteraf onomstotelijk kan bewijzen.


## Echt voorbeeld

### Een AI-native oprichter in actie: De zorgtoegang die niemand kon traceren

Bas, een voormalig thuiszorgcoördinator die oprichter werd in Almere, bouwde ZorgVerbind, een AI-ondersteund platform voor ouderenzorgcoördinatie gebouwd met Cursor, waarmee familieleden professionele zorgverleners toegang kunnen verlenen tot het schema en de zorgnotities van een familielid.

Een familiegeschil over wie de toegang van een specifieke zorgverlener had geautoriseerd leidde tot een verzoek dat Bas niet kon vervullen: een duidelijk record van wanneer en door wie die toegang oorspronkelijk was verleend. LaunchStudio's beoordeling bevestigde dat de functie voor het delen van toegang correct werkte, maar überhaupt geen historisch toestemmingsspoor bijhield – alleen de huidige status van wie momenteel toegang had.

**Resultaat:** LaunchStudio voegde een append-only audit-logboek toe dat elke verlening, wijziging en intrekking van toegang voor de toekomst vastlegt. LaunchStudio werkte met Bas om de praktijken voor gegevensafhandeling van het platform overeenkomstig te documenteren, wat de nalevingskloof sloot zonder te veranderen hoe families en zorgverleners de deelfunctie daadwerkelijk gebruikten.

> *"De functie zelf werkte de gehele tijd exact zoals bedoeld. Het was gewoon nooit bij me opgekomen dat 'werkte' en 'kunnen bewijzen wat er zes maanden geleden gebeurde' twee compleet verschillende dingen waren."*
> — **Bas Terpstra, Oprichter, ZorgVerbind (Almere)**

**Kosten en tijdlijn:** € 2.400 (audit-logboek voor toestemming en toegang) — voltooid in 8 werkdagen.

---

## Veelgestelde vragen

### Zou een functionaris voor gegevensbescherming (FG/DPO) ontbrekende toestemmingsregistratie beschouwen als een technische of een beleidsmatige kloof?

Beide in de praktijk, en de overlap is precies waar het om draait — het is een beleidsmatige en wettelijke vereiste (het aantonen van een geldige rechtmatige grondslag voor de gegevensverwerking) waaraan voldaan moet worden via een specifiek technisch mechanisme (een daadwerkelijk, onveranderlijk auditspoor). Geen van beide invalshoeken op zichzelf geeft volledig weer waarom dit bewuste technische engineering vereist in plaats van uitsluitend een statisch juridisch beleidsdocument.

### Geldt dit soort kloof alleen voor gezondheidsgerelateerde producten, of veel breder?

Het geldt het meest acuut voor gezondheidsgerelateerde en andere gevoelige gegevensproducten vanwege de aanzienlijk strengere wettelijke nalevingsdrempel onder de AVG, maar elk product dat persoonsgegevens verwerkt op basis van expliciete toestemming profiteert van exact ditzelfde type controleerbare auditspoor. De stelling 'we zijn er vrij zeker van dat dit destijds geautoriseerd was' is immers een uiterst zwakke verdediging bij elk juridisch of operationeel geschil.

### Manifera heeft gewerkt met onderzoeksgerichte instellingen zoals TNO aan datagevoelige projecten — beïnvloedt die achtergrond hoe toestemmingslogging wordt ontworpen?

Ja, direct — projecten met gevoelige onderzoeks- en gezondheidsdata vereisen al decennialang exact dit soort aantoonbare, auditeerbare toestemmingssporen. Ditzelfde beproefde ontwerppatroon vertaalt zich één-op-één naar een door een solo-oprichter gebouwd ouderenzorgplatform dat voor vergelijkbare, zij het kleinschaligere, wettelijke verplichtingen staat.

### Is dit het soort kloof waarnaar CEO Herre Roelevink verwijst wanneer hij de verschuiving beschrijft van software bouwen naar software verantwoord ontwerpen?

Ja, exact — een toestemmingslogboek is geen visuele feature waarmee een eindgebruiker rechtstreeks interacteert of die direct opvalt in een interface. Het valt precies in de categorie van onzichtbare architectuurbeslissingen die Roelevink herhaaldelijk heeft aangewezen als het moeilijkere, minder vanzelfsprekende onderdeel van softwareontwikkeling in het huidige AI-tijdperk.

### Zou een oprichter basis-toestemmingslogging zelf kunnen toevoegen zonder volledige audit, simpelweg door een spreadsheet bij te houden?

Een handmatig bijgehouden overzicht kan tijdelijk dienen als een noodoplossing, maar het schaalt niet betrouwbaar en is extreem vatbaar voor menselijke fouten, vergetelheid of het uit de pas lopen met de daadwerkelijke staat van het product. Een technisch ontworpen, 'append-only' logboek dat direct gekoppeld is aan de code die toegang verleent, is het enige dat daadwerkelijk garandeert dat de administratie nooit geruisloos kan afwijken van de werkelijkheid.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Zou een functionaris voor gegevensbescherming (FG/DPO) ontbrekende toestemmingsregistratie beschouwen als een technische of een beleidsmatige kloof?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Beide in de praktijk, en de overlap is precies waar het om draait — het is een beleidsmatige en wettelijke vereiste (het aantonen van een geldige rechtmatige grondslag voor de gegevensverwerking) waaraan voldaan moet worden via een specifiek technisch mechanisme (een daadwerkelijk, onveranderlijk auditspoor). Geen van beide invalshoeken op zichzelf geeft volledig weer waarom dit bewuste technische engineering vereist in plaats van uitsluitend een statisch juridisch beleidsdocument."
      }
    },
    {
      "@type": "Question",
      "name": "Geldt dit soort kloof alleen voor gezondheidsgerelateerde producten, of veel breder?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het geldt het meest acuut voor gezondheidsgerelateerde en andere gevoelige gegevensproducten vanwege de aanzienlijk strengere wettelijke nalevingsdrempel onder de AVG, maar elk product dat persoonsgegevens verwerkt op basis van expliciete toestemming profiteert van exact ditzelfde type controleerbare auditspoor. De stelling 'we zijn er vrij zeker van dat dit destijds geautoriseerd was' is immers een uiterst zwakke verdediging bij elk juridisch of operationeel geschil."
      }
    },
    {
      "@type": "Question",
      "name": "Manifera heeft gewerkt met onderzoeksgerichte instellingen zoals TNO aan datagevoelige projecten — beïnvloedt die achtergrond hoe toestemmingslogging wordt ontworpen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, direct — projecten met gevoelige onderzoeks- en gezondheidsdata vereisen al decennialang exact dit soort aantoonbare, auditeerbare toestemmingssporen. Ditzelfde beproefde ontwerppatroon vertaalt zich één-op-één naar een door een solo-oprichter gebouwd ouderenzorgplatform dat voor vergelijkbare, zij het kleinschaligere, wettelijke verplichtingen staat."
      }
    },
    {
      "@type": "Question",
      "name": "Is dit het soort kloof waarnaar CEO Herre Roelevink verwijst wanneer hij de verschuiving beschrijft van software bouwen naar software verantwoord ontwerpen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, exact — een toestemmingslogboek is geen visuele feature waarmee een eindgebruiker rechtstreeks interacteert of die direct opvalt in een interface. Het valt precies in de categorie van onzichtbare architectuurbeslissingen die Roelevink herhaaldelijk heeft aangewezen als het moeilijkere, minder vanzelfsprekende onderdeel van softwareontwikkeling in het huidige AI-tijdperk."
      }
    },
    {
      "@type": "Question",
      "name": "Zou een oprichter basis-toestemmingslogging zelf kunnen toevoegen zonder volledige audit, simpelweg door een spreadsheet bij te houden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een handmatig bijgehouden overzicht kan tijdelijk dienen als een noodoplossing, maar het schaalt niet betrouwbaar en is extreem vatbaar voor menselijke fouten, vergetelheid of het uit de pas lopen met de daadwerkelijke staat van het product. Een technisch ontworpen, 'append-only' logboek dat direct gekoppeld is aan de code die toegang verleent, is het enige dat daadwerkelijk garandeert dat de administratie nooit geruisloos kan afwijken van de werkelijkheid."
      }
    }
  ]
}
</script>
