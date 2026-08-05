---
Titel: "Overdrachtsdocumentatie: Wat uw eerste technische werknemer nodig heeft uit uw met AI gebouwde codebase"
Trefwoorden: ai code tool, ai native, handover documentation, first developer hire, ai codebase onboarding
Koperfase: Beslissing
Doelgroep: AI-Native oprichter
---

# Overdrachtsdocumentatie: Wat uw eerste technische werknemer nodig heeft uit uw met AI gebouwde codebase

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Overdrachtsdocumentatie: Wat uw eerste technische werknemer nodig heeft uit uw met AI gebouwde codebase",
  "description": "De automatisch gegenereerde README van een AI-tool is geen inwerkdocumentatie.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-07-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/handover-documentation-first-engineer-hire"
  }
}
</script>

Het aannemen van uw eerste ontwikkelaar verondersteld wordt u snelheid te kopen. Voor veel AI-native oprichters koopt het twee weken waarin die nieuwe werknemer stilletjes code leest, gokt naar de intentie, en beslissingen probeert te herleiden die nergens zijn opgeschreven – omdat de enige documentatie die bestaat de README is die de AI-tool op dag één automatisch heeft gegenereerd. Dat bestand beschrijft hoe de mappen heten, en niet waarom iets werkt op de manier waarop het werkt.

## Waarom de eigen documentatie van de AI-tool niet telt als overdrachtsmateriaal

Tools zoals Bolt, Lovable en Cursor genereren een README als beleefdheid, en het is oprecht nuttig voor de vijf minuten die het kost om het project lokaal te draaien. Het vermeldt afhankelijkheden, misschien een overzicht van de projectstructuur, soms een beschrijving van één regel voor elke map. Wat het niet bevat – omdat de AI-tool geen manier heeft om dit te weten – is *waarom* het product is gebouwd op de manier waarop het is gebouwd. Waarom loopt de facturatielogica via twee verschillende diensten in plaats van één? Waarom is er een schijnbaar overtollige tabel in de database? Waarom probeert de ene API-integratie drie keer opnieuw terwijl een andere überhaupt niet opnieuw probeert? Deze beslissingen stapelen zich op over weken of maanden van prompten, itereren en patchen. Niets van die redenering wordt ergens vastgelegd tenzij iemand het bewust opschrijft.

Een nieuwe ontwikkelaar die zich aansluit bij een met AI gebouwde codebase leert niet alleen een technologie-stack – hij probeert een beslissingsgeschiedenis te reconstrueren die volledig in het hoofd van de oprichter leefde en in een lang geleden voorbijgescrolde chatgeschiedenis met een AI-assistent. Dat is een fundamenteel moeilijkere en tragere taak dan het lezen van onbekende maar goed gedocumenteerde code, omdat er geen spoor is om te volgen. Ze moeten zich een weg testen naar begrip, wat traag is. Erg nog: ze moeten gokken welke delen van de code dragende bedrijfslogica zijn versus welke delen overgebleven met AI gegenereerde steigers zijn die niemand heeft opgeruimd.

## Wat echte overdrachtsdocumentatie daadwerkelijk bevat

Effectieve overdrachtsdocumentatie voor een met AI gebouwd product hoeft niet uitputtend te zijn – het moet de vragen beantwoorden die een nieuwe ontwikkelaar anders zou moeten herleiden. Dat omvat: een kaart in gewone taal van de belangrijkste systemen en hoe ze verbinden (geen mappenlijst, een uitleg van de daadwerkelijke architectuur), een lijst van elke dienst van derden en API waar het product van afhangt en waarom elke dienst werd gekozen, bekende tijdelijke oplossingen of opzettelijke afsnijdingen die eruitzien als bugs maar het niet zijn, en – net zo belangrijk – een lijst van de delen van de codebase die *wel* waarschijnlijk echte bugs of technische schuld bevatten, zodat een nieuwe werknemer geen tijd verspilt aan het vertrouwen van code die nooit volledig werd beoordeeld. LaunchStudio wordt aangedreven door Manifera, een softwareontwikkelingsbedrijf met meer dan 11 jaar ervaring in productie-engineering. Het produceren van exact dit soort overdrachtsdocumentatie – het lezen van een onbekende met AI gegenereerde codebase en het opschrijven van wat een nieuwe ingenieur daadwerkelijk moet weten – is een taak die ons team, gevestigd in Manifera's hub in Singapore, routinematig uitvoert voor oprichters die zich voorbereiden om hun eerste werknemer aan te nemen.

## Een inwerktijd van twee weken veranderen in een van twee dagen

De meest efficiënte manier om deze documentatie te produceren is niet om de oprichter het uit zijn geheugen te laten schrijven – oprichters kunnen hun eigen redenering maanden later vaak ook niet meer volledig reconstrueren, in het bijzonder voor beslissingen die de AI-tool semi-autonoom heeft gemaakt. Het is effectiever om iemand de codebase vers te laten lezen, op de manier waarop een nieuwe werknemer dat zou doen, en te documenteren wat hij onderweg vindt: het markeren van onduidelijke logica, het in kaart brengen van gegevensstromen tussen systemen, en het noteren van alles wat er kwetsbaar uitziet. Die uitvoer wordt het inwerkdocument, geschreven vanuit het perspectief van iemand die de code voor het eerst tegenkomt – wat exact het perspectief is dat een nieuwe werknemer nodig heeft.

Als u op het punt staat uw eerste ingenieur aan te nemen en u wilt de codebase gedocumenteerd hebben voordat hij begint, schetst onze [hoe het werkt](https://launchstudio.eu/en/#process)-pagina hoe LaunchStudio dit soort traject omvangt. Manifera's [portfolio](https://www.manifera.com/portfolio/) toont het bereik van codebases dat onze ingenieurs hebben geonboard en gedocumenteerd, van producten in een vroeg stadium tot gevestigde enterprise-systemen.

## Documentatie die één keer is geschreven begint te verouderen op het moment dat deze klaar is

Het produceren van de overdrachtsdocumentatie lost het onmiddellijke probleem op, maar het creëert een stillere: op het moment dat een oprichter of een nieuwe werknemer weer begint te prompten met een AI-tool om de volgende functie te bouwen, begint de architectuur die de documentatie beschrijft af te wijken van de architectuur die daadwerkelijk bestaat. Niets markeert die afwijking naarmate het gebeurt. Het document leest nog steeds als gezaghebbend, de nieuwe werknemer vertrouwt het nog steeds, en zes weken later is het zelfverzekerd verkeerd over welke wachtrij wat afhandelt of waarom een specifieke tabel bestaat. Dat is aantoonbaar erger dan helemaal geen documentatie hebben, omdat een nieuwe werknemer verkeerde informatie langer vertrouwt dan hij een eerlijke kloof zou tolereren.

De herstelling is niet het periodiek herschrijven van het gehele document – dat is exact het soort onglamoureus onderhoud dat voor onbepaalde tijd wordt uitgesteld. Het is het toevoegen van een korte beslissingslogboek-invoer aan elke wijziging die de bestaande documentatie verkeerd zou maken, geschreven op het moment dat de wijziging wordt gemaakt, wanneer de redenering nog vers in het geheugen ligt:

```
## 2026-08-04 — Facturatiewachtrij gesplitst van gebruiks-meetwachtrij
Reden: een meetfout liet facturatietaken tijdelijk vastlopen; het isoleren
ervan betekent dat een meetstoring een betaling niet meer kan vertragen.
Bestanden aangeraakt: /server/queues/billing.ts, /server/queues/metering.ts
Documentatiegedeelte bij te werken: Architectuurkaart > Facturatiesubsysteem
```

Een handvol van deze invoeren per maand is een triviale gewoonte om op te bouwen en houdt de architectuurkaart eerlijk zonder ooit een toegewijde herschrijfstap te vereisen.

## Echt voorbeeld

### Een AI-native oprichter in actie: Twee weken om een codebase te begrijpen die niemand heeft uitgelegd

Rick Nieuwenhuis, een oprichter in Winschoten, bouwde KlantSignaal – een SaaS voor klantfeedback – met behulp van Bolt. Na een jaar van solo-iteratie nam hij zijn eerste ontwikkelaar aan om hem te helpen sneller te bewegen. De enige beschikbare documentatie was Bolt's automatisch gegenereerde README, die de mappenstructuur beschreef en geïnstalleerde afhankelijkheden vermeldde.

De nieuwe werknemer besteedde twee volledige weken simpelweg aan het uitzoeken hoe de codebase was gestructureerd voordat hij een enkele regel nieuwe functiecode schreef. Basisvragen hadden nergens antwoorden: waarom feedback-indieningen werden verwerkt via twee afzonderlijke wachtrijen, waarom op de ene integratie aangepaste herhaallogica was vastgeplakt terwijl een bijna identieke dat niet had, en welke delen van de authenticatiestroom opzettelijk waren versus overgebleven uit een eerdere, verlaten benadering. Rick kon sommige hiervan uit zijn geheugen beantwoorden, maar niet betrouwbaar, en niet snel genoeg om zijn nieuwe werknemer productief te houden.

LaunchStudio werd ingeschakeld om KlantSignaal's codebase van buitenaf door te lezen en vanaf nul inwerkdocumentatie te produceren: een architectuurkaart die toont hoe de feedback-inname, verwerking en notificatiesystemen daadwerkelijk verbonden waren, een lijst van elke integratie van derden en de redenering achter elk daarvan, en een gemarkeerde lijst van de kwetsbare gebieden die aandacht nodig hadden voordat er verder op werd gebouwd.

**Resultaat:** Rick's volgende werknemer werkte binnen drie dagen in met behulp van de documentatie die LaunchStudio produceerde, in plaats van de twee weken die zijn eerste werknemer nodig had met niets om vanuit te werken.

> *"Mijn eerste werknemer moest in feite een archeoloog worden voordat hij een ontwikkelaar kon worden. Ik wil iemand daar nooit meer doorheen laten gaan."*
> — **Rick Nieuwenhuis, Oprichter, KlantSignaal (Winschoten)**

**Kosten en tijdlijn:** € 1.050 (volledige codebase-doorlezing en overdrachtsdocumentatie, inclusief architectuurkaart en het markeren van technische schuld) — voltooid in 6 werkdagen.

---

## Veelgestelde vragen

### Zou ik overdrachtsdocumentatie zelf moeten schrijven, of moet ik het door iemand anders laten doen?

Iemand die de codebase vers leest, op de manier waarop een nieuwe werknemer dat zou doen, produceert doorgaans nuttigere documentatie dan een oprichter die uit zijn geheugen schrijft – het is gemakkelijk te vergeten welke beslissingen daadwerkelijk uitleg nodig hebben zodra u maandenlang in de code heeft geleefd.

### Wat is het verschil tussen dit en simpelweg het opruimen van code-opmerkingen?

Code-opmerkingen leggen uit wat een specifieke regel doet; overdrachtsdocumentatie legt uit waarom het systeem als geheel gestructureerd is op de manier waarop het is en welke onderdelen veilig zijn om op te bouwen versus kwetsbaar – een niveau hoger dan regel-voor-regel commentaar.

### Vervangt overdrachtsdocumentatie de noodzaak van een code-audit?

Nee – documentatie legt uit hoe de code werkt en waarom; een audit evalueert of het veilig, schaalbaar en productie-gereed is. Ze zijn aanvullend op elkaar.

### Hoe voorkom ik dat overdrachtsdocumentatie verouderd raakt?

Voeg een korte beslissingslogboek-invoer toe aan elke wijziging die de bestaande documentatie onjuist zou maken, geschreven op het moment dat de wijziging plaatsvindt – een gewoonte die aanzienlijk goedkoper te onderhouden is dan een periodieke volledige herschrijfbeurt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom is de README van Cursor of Bolt geen echte overdrachtsdocumentatie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat AI-gegenereerde READMEs alleen mappen en npm-installatie uitleggen, maar NIET de architectonische keuzes, werkbonnen of verborgen technische schuld."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt het inwerken van een 1e developer op een niet-gedocumenteerde AI-codebase?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Gemiddeld 2 tot 3 weken 'archeologie' en gokken. Met een professionele architectuurkaart en beslissingslogboek wordt dit teruggebracht naar 2-3 dagen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet er minimaal in AI-overdrachtsdocumentatie staan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1. Systeem-architectuurkaart 2. API & 3rd party afhankelijkheden 3. Bekende hacks & tijdelijke afsnijdingen 4. Database-relatie toelichting."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom je dat documentatie direct veroudert bij nieuwe AI-prompts?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Door een lichtgewicht `DECISION_LOG.md` bij te houden waarin bij grote structuurwijzigingen in 3 regels de reden en gewijzigde bestanden worden genoteerd."
      }
    },
    {
      "@type": "Question",
      "name": "Wat kost het opstellen van overdrachtsdocumentatie bij LaunchStudio?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een volledige codebase doorlezing en inwerk-overdrachtsdocumentatie kost gemiddeld €1.050 en duurt 6 werkdagen."
      }
    }
  ]
}
</script>