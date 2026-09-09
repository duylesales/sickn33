---
Titel: "Case Study: Een AI-Gegenereerd EdTech-Platform Beveiligen in 3 Weken"
Trefwoorden: EdTech beveiliging, leerlinggegevens bescherming, AVG minderjarigen data, AI-gegenereerd onderwijsplatform, school data compliance, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Case Study: Een AI-Gegenereerd EdTech-Platform Beveiligen in 3 Weken

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Case Study: Een AI-Gegenereerd EdTech-Platform Beveiligen in 3 Weken",
  "description": "Een vibe-coded EdTech-platform dat academische dossiers van minderjarigen verwerkt heeft te maken met strengere eisen dan de meeste SaaS-producten, omdat schoolinkoopteams vragen stellen over gegevensbescherming die tijdens eigen tests nooit naar boven komen. Een overzicht van hoe die kloof in drie weken werd gedicht, zonder herbouw.",
  "inLanguage": "nl-NL",
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
  "datePublished": "2026-12-31",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/securing-ai-generated-edtech-platform-case-study"
  }
}
</script>

De eerste vraag van een inkoopmedewerker van een onderwijsinstelling aan een EdTech-oprichter gaat zelden over functionaliteiten — het is vrijwel altijd een variant van: "hoe worden leerlinggegevens beschermd, en wie heeft er toegang toe?" Het is een vraag die tijdens de eigen tests van de oprichter, die volledig gericht zijn op de vraag of het product didactisch werkt, vrijwel nooit vanzelf naar boven komt. EdTech bevindt zich in een specifieke en veel strengere categorie binnen door AI gegenereerde software: de gebruikers zijn veelal minderjarig, de gegevens betreffen academische en soms gedragsmatige dossiers die expliciet onder de privacywetgeving vallen, en de koper is een instelling waarvan de eigen compliance-verplichtingen betekenen dat zij hardere vragen zullen stellen dan een individuele consument ooit zou doen. 

Het beveiligen van een AI-gegenereerd EdTech-platform voor een daadwerkelijke uitrol is geen generieke hardening-ronde waar toevallig het label "onderwijs" op is geplakt — het is een specifieke, verhoogde norm. Begrijpen wat die norm exact inhoudt, maakt het verschil tussen een product dat soepel door de inkoopprocedure van een schoolbestuur komt en een product dat voor onbepaalde tijd vastloopt in een compliance-beoordeling waar niemand op voorbereid was.

## Waarom EdTech-Prototypes Een Hoger Basisrisico Dragen

Elk door AI gegenereerd prototype wordt opgeleverd met dezelfde generieke kwetsbaarheden — authenticatie die alleen aan de frontend plaatsvindt, inconsistente autorisatie, slecht beheerde geheimen en API-sleutels. Maar EdTech-platformen dragen een extra risicolaag die de meeste andere categorieën niet hebben: de data zelf is gevoeliger volgens de wet, niet enkel volgens de intuïtie van de oprichter. Leerlingdossiers bevatten regelmatig informatie over leerproblemen, gedragsnotities en historische cijfers, die allemaal onder aanzienlijk strengere privacyverwachtingen vallen dan bijvoorbeeld de takenlijst van een to-do app. 

Omdat een aanzienlijk deel van de gebruikers minderjarig is, ligt de lat voor het aantonen van "wie wat kan inzien, en waarom" meetbaar hoger. De Functionaris Gegevensbescherming (FG) van een school is contractueel en wettelijk verplicht hiernaar te vragen voordat er een handtekening wordt gezet. De compliance-vraag is dus geen optionele frictie waar u omheen kunt sturen; het is een vaste poort waar elke EdTech-oprichter vroeg of laat doorheen moet. Waar consumenten-apps soms eerst kunnen lanceren en pas achteraf reageren op databeveiligingsvragen, heeft EdTech die luxe zelden: de compliance-plichten van de institutionele inkoper forceren deze vraag direct naar de start van het verkoopproces.

## De Specifieke Kwetsbaarheden Die Steeds Terugkeren in AI EdTech-Apps

Bij de EdTech-prototypes die volgens ditzelfde patroon zijn geanalyseerd, keren drie specifieke kwetsbaarheden met opvallende regelmaat terug. 

Ten eerste wordt rolscheiding tussen leerlingen, docenten en ouders vaak uitsluitend op interfaceniveau geïmplementeerd. Het dashboard van een docent ziet er anders uit dan dat van een leerling, maar de onderliggende API verifieert niet zelfstandig of degene die het verzoek doet daadwerkelijk die rol bezit. Een technisch nieuwsgierige leerling kan daardoor via netwerkverzoeken data opvragen die uitsluitend voor de ogen van een docent bestemd is. 

Ten tweede worden toegangscontroles op rijniveau (Row-Level Security) op leerlingdossiers inconsistent toegepast over verschillende tabellen. Zelfs als het primaire scherm met "mijn eigen cijfers" correct is afgeschermd, is een latere secundaire feature — zoals een ranglijst, een klassenoverzicht of een voortgangsrapport voor ouders — vaak later gebouwd en nooit aan dezelfde strenge controle onderworpen. 

Ten derde vragen integraties met externe classroom-tools zoals Google Classroom of Microsoft Teams regelmatig veel bredere datatoegangsrechten (OAuth-scopes) dan voor de daadwerkelijke feature nodig is. Dit creëert een blootstelling die niets te maken heeft met de eigen code van de oprichter, maar alles met hoe de integratie is geconfigureerd. Deze laatste categorie wordt door een niet-technische oprichter uiterst makkelijk over het hoofd gezien: het accepteren van een brede scope is immers vaak de standaardinstelling van een AI-bouwtool, en aan een werkende demo valt aan de buitenkant niet af te zien dat er achter de schermen veel te veel rechten zijn toegekend.

## Het Drie-Weken Tijdpad: Week Voor Week

Een gestructureerd hardening-traject voor EdTech volgt een specifiek ritme, juist omdat de belangen een zorgvuldigere verificatie rechtvaardigen dan bij een consumenten-app met een laag risico. 

- **Week 1 (Audit):** Het in kaart brengen van elke tabel en elk endpoint dat gegevens van leerlingen, docenten of ouders raakt, en het direct testen van rolscheiding tegen de API in plaats van te vertrouwen op de interface.
- **Week 2 (Herstel):** Het consistent implementeren van Row-Level Security over alle geïdentificeerde tabellen — niet alleen de tabellen die toevallig in een eerdere bugmelding naar voren kwamen — en het terugbrengen van integratiescope van derden naar het absolute minimum dat het product nodig heeft.
- **Week 3 (Verificatie & Documentatie):** Het opnieuw testen van elk toegangspad met opzettelijk vijandige invoer (adversarial testing) — een leerlingaccount dat een docent-endpoint probeert aan te roepen, een ouderaccount dat dossiers van een ander gezin probeert in te zien — en het opstellen van de concrete documentatie die de Functionaris Gegevensbescherming van een school tijdens de inkoop wil zien.

## Waarom Inkoopafdelingen van Scholen Dit Niet-Onderhandelbaar Vinden

In tegenstelling tot een verkoopgesprek met een consument, waar de oprichter het gesprek grotendeels zelf stuurt, verloopt de inkoop bij een schoolbestuur via een formele toetsing. Deze omvat doorgaans een Data Protection Impact Assessment (DPIA) en vrijwel altijd een getekende verwerkersovereenkomst (DPA) waarin exact staat gespecificeerd hoe leerlingdata wordt opgeslagen, wie er toegang toe heeft en onder welke voorwaarden het wordt verwijderd. 

Een oprichter die deze vragen niet met concrete technische feiten kan beantwoorden — niet met algemene geruststellingen, maar met harde specificaties — verliest de deal niet op prijs of features. De deal blijft simpelweg voor onbepaalde tijd hangen in een wachtrij, vaak zonder formele afwijzing, enkel in stilte. Dit is een fundamenteel andere manier van falen dan een verloren consumentendeal, en het is iets wat gestructureerde, gedocumenteerde hardening direct voorkomt door de oprichter concrete antwoorden te geven nog vóór de vragen worden gesteld.

## Waarom Compliance Achteraf Inbouwen Niet Werkt

Een veelgemaakte fout onder EdTech-oprichters is het behandelen van gegevensbescherming als een administratieve invuloefening die pas wordt gedaan als het product al klaar is — schrijf een privacybeleid, vink een checklist af en ga door. Die aanpak faalt in EdTech omdat de documentatie waar een school om vraagt geen beleidsverklaring is, maar een verifieerbare beschrijving van hoe toegangscontrole in het actieve systeem wordt afgedwongen. 

Een beleidsdocument dat intenties beschrijft die niet overeenkomen met de werkelijke code is kwalijker dan helemaal geen document: het creëert een schriftelijk dossier dat direct wordt tegengesproken door een technische audit die het schoolbestuur mag eisen. Echte compliance moet vanaf de toegangscontrolelaag omhoog worden opgebouwd: de documentatie is een getrouwe beschrijving van wat het systeem aantoonbaar doet, opgesteld nadát de beveiliging daadwerkelijk bestaat, niet een belofte die eraan voorafgaat.

[LaunchStudio](https://launchstudio.eu/nl/) heeft EdTech- en andere privacygevoelige platforms gehard als onderdeel van Manifera's 11+ jaar ervaring in enterprise software engineering, waarbij exact die kwetsbaarheden worden gedicht waar schoolinkopers op getraind zijn om naar te zoeken.

[Zorg dat uw platform klaar is vóór uw volgende inkoopgesprek met een school](https://launchstudio.eu/nl/#contact) — tijdens een gerichte intake brengen we uw specifieke toegangscontrole-risico's in kaart voordat een Functionaris Gegevensbescherming ze voor u ontdekt.

## Echt voorbeeld
### Een AI-Native Oprichter in de Praktijk: De Vraag Die Ze Niet Kon Beantwoorden in het Inkoopgesprek

Femke van Dijk, voormalig docente in het voortgezet onderwijs in Groningen, bouwde LeerPad, een AI-gedreven adaptief leerplatform dat oefenstof aanpast aan de voortgang van individuele leerlingen, met behulp van Lovable. LeerPad werkte uitstekend in de klaslokalen van twee bevriende docenten die het informeel testten: leerlingen logden in, zagen hun eigen gepersonaliseerde oefeningen en verder niets, precies zoals Femke het had ontworpen en zelf had getest.

Het inkoopteam van een regionaal schoolbestuur, dat LeerPad evalueerde voor een uitrol op twaalf scholen, vroeg om een Data Protection Impact Assessment (DPIA) als standaardstap vóór ondertekening. Hun Functionaris Gegevensbescherming vroeg rechtstreeks of leerlingen via enige weg toegang konden krijgen tot de prestatiegegevens van andere leerlingen. Femke wist het eerlijke antwoord niet, omdat haar eigen tests zich altijd hadden beperkt tot de interface die ze had ontworpen — nooit tot de onderliggende API rechtstreeks, en nooit met opzettelijk vijandige intenties.

Femke bracht LeerPad naar LaunchStudio om een definitief antwoord te krijgen vóór de inkoopdeadline. De audit van het Manifera-team bracht aan het licht dat hoewel het leerlingendashboard elke leerling keurig beperkte tot zijn eigen oefeningen, een secundaire functie voor "klasvoortgang" — later toegevoegd voor docenten — prestatiedata opvroeg zonder zelfstandig de rol van de aanvrager te verifiëren. Een leerling die de netwerkverzoeken in de browser inspecteerde, kon daardoor de cijfers van de hele klas ophalen, niet alleen die van zichzelf.

**Resultaat:** LaunchStudio implementeerde consistente rolgebaseerde toegangscontrole over elk endpoint dat leerlinggegevens raakt, inclusief de secundaire features die Femke's eigen tests nooit hadden bereikt. Tevens leverden we de specifieke technische documentatie waarmee de privacyfunctionaris van het schoolbestuur de uitrol zonder verdere vertraging goedkeurde.

> *"Ik had LeerPad getest zoals een docent het zou gebruiken. Ik had het nooit getest zoals een nieuwsgierige leerling zou proberen het te breken — en dat was exact de vraag die de school stelde."*  
> — **Femke van Dijk, Oprichter, LeerPad (Groningen)**

**Kosten & Tijdlijn:** €3.400 (Relaunch & Scale Pakket, EdTech toegangscontrole en compliance-documentatie) — live in 15 werkdagen.

---

## Veelgestelde Vragen

### Waarom gelden voor EdTech strengere beveiligingseisen dan voor andere AI-gegenereerde SaaS-producten?

Omdat de data betrekking heeft op minderjarigen en academische of gedragsmatige dossiers bevat die onder verscherpt toezicht van de privacywetgeving vallen. Bovendien is de koper een onderwijsinstelling met een eigen wettelijke zorgplicht om gegevensverwerking vooraf te verifiëren, anders dan een individuele consument die deze vragen zelden stelt.

### Wat is de meest voorkomende kwetsbaarheid die Manifera specifiek in AI-gegenereerde EdTech-platforms aantreft?

Rolscheiding die uitsluitend op interfaceniveau is geïmplementeerd, zonder dat de onderliggende API zelfstandig verifieert of de aanvrager daadwerkelijk de rol bezit die het dashboard suggereert. Zoals in Femke's situatie, waar een latere "klasvoortgang"-feature data lekte buiten het dossier van de individuele leerling om.

### Waarom duurt dit traject drie weken in plaats van één, als het platform al werkte voor proefgebruikers?

De verhoogde belangen rondom leerlinggegevens rechtvaardigen een grondiger tempo: telkens een volledige week voor audit, herstelwerkzaamheden en vijandige hertesten (adversarial testing). De inkoopaudit van een school toetst immers exact de paden die een goedbedoelende oprichter zelf nooit doorloopt.

### Eisen scholen daadwerkelijk formele documentatie, of volstaat een algemene toezegging?

Vrijwel alle institutionele inkoopprocedures vereisen een DPIA en een ondertekende verwerkersovereenkomst met concrete technische details, geen algemene geruststellingen. Een oprichter die deze documentatie niet kan overleggen ziet een deal meestal geruisloos vastlopen in plaats van formeel te worden afgewezen.

### Betekent het beveiligen van een EdTech-platform dat de didactische werking of de interface verandert?

Nee. Zoals ook bij Femke het geval was, richt het hele traject zich uitsluitend op toegangscontrole en databeheer onder de motorkap. De adaptieve leerlogica, de vormgeving en de gebruikerservaring die de oprichter heeft gebouwd, blijven gedurende het hele proces onaangeroerd.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom gelden voor EdTech strengere beveiligingseisen dan voor andere AI-gegenereerde SaaS-producten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De gegevens betreffen minderjarigen en academische dossiers onder strikt toezicht, en de koper is een instelling met een wettelijke plicht tot voorafgaande verificatie."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de meest voorkomende kwetsbaarheid die Manifera specifiek in AI-gegenereerde EdTech-platforms aantreft?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Rolscheiding die uitsluitend op interfaceniveau bestaat, waardoor nieuwsgierige gebruikers via directe API-verzoeken toegang krijgen tot gegevens buiten hun eigen rol."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom duurt dit traject drie weken in plaats van één?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De verhoogde belangen rechtvaardigen aparte fasen voor audit, herstel en vijandige hertesten, om alle ongecontroleerde paden grondig af te sluiten."
      }
    },
    {
      "@type": "Question",
      "name": "Eisen scholen daadwerkelijk formele documentatie, of volstaat een algemene toezegging?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Institutionele inkoop vereist specifieke DPIA-antwoorden en verwerkersovereenkomsten; zonder concrete documentatie lopen deals vaak stilzwijgend vast."
      }
    },
    {
      "@type": "Question",
      "name": "Betekent het beveiligen van een EdTech-platform dat de didactische werking of de interface verandert?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, de werkzaamheden richten zich puur op toegangscontrole en databeveiliging in de backend, terwijl de onderwijsmethodiek en interface intact blijven."
      }
    }
  ]
}
</script>
