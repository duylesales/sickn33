---
Titel: "Hoe We met Uw Code en Klantgegevens Omgaan Tijdens een Project"
Trefwoorden: toegang ontwikkelaar tot klantgegevens, gegevensbescherming tijdens ontwikkelproject, verwerkersovereenkomst ontwikkelaar, minimale toegang bureau, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Hoe We met Uw Code en Klantgegevens Omgaan Tijdens een Project

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe We met Uw Code en Klantgegevens Omgaan Tijdens een Project",
  "description": "Een uitleg van hoe LaunchStudio tijdens projecten aan apps gebouwd met Lovable, Bolt, v0, Cursor of Claude Code omgaat met de code, accounts en klantgegevens van oprichters: werken in uw accounts, minimale toegang, staging met testgegevens, regels voor toegang tot productiegegevens, verwerkersovereenkomsten, engineers in Ho Chi Minh City, gebruik van AI-tools op uw code, vertrouwelijkheid, afhandeling van incidenten en het intrekken van toegang aan het einde.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-10-16",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-we-handle-your-code-and-customer-data-during-a-project" },
  "citation": [
    { "@type": "CreativeWork", "name": "EUR-Lex: General Data Protection Regulation (EU) 2016/679", "url": "https://eur-lex.europa.eu/eli/reg/2016/679/oj" },
    { "@type": "CreativeWork", "name": "European Commission: Standard contractual clauses for international transfers", "url": "https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens: Verwerkersovereenkomst", "url": "https://www.autoriteitpersoonsgegevens.nl/themas/basis-avg/avg-algemeen/verwerkersovereenkomst" },
    { "@type": "CreativeWork", "name": "OWASP: Principle of least privilege", "url": "https://owasp.org/www-community/Access_Control" }
  ]
}
</script>

Wanneer u een team uitnodigt om aan uw app te werken, geeft u toegang tot twee waardevolle zaken: uw code en de gegevens van uw klanten. Oprichters vragen terecht hoe met die toegang wordt omgegaan. Wie kan wat zien? Waar zitten de engineers? Kopiëren ze de database? Plakken ze uw code in AI-tools? Wat gebeurt er daarna met de toegang? En wat vertelt u uw eigen klanten als zij vragen wie hun gegevens verwerkt?

Deze pagina legt uit hoe LaunchStudio tijdens een project omgaat met uw code, accounts en klantgegevens. Het is een beschrijving van onze standaardpraktijk; de specifieke afspraken voor uw project worden bevestigd in de offerte en, waar persoonsgegevens een rol spelen, in een verwerkersovereenkomst.

## Belangrijkste Punten

- **We werken in uw accounts,** met individuele toegang die u kunt zien en intrekken.
- **Toegang is beperkt tot wat het werk nodig heeft,** en toegang tot productiegegevens is de uitzondering.
- **Staging met testgegevens is de standaard** voor ontwikkeling en testen.
- **Een verwerkersovereenkomst dekt persoonsgegevens,** inclusief onze engineeringlocatie buiten de EU.
- **Toegang wordt aan het einde ingetrokken,** tenzij u doorgaat met doorlopende zorg.

## Werken in Uw Accounts

We verplaatsen uw code niet naar onze repository en uw gegevens niet naar onze servers. In plaats daarvan nodigt u onze teamleden uit in uw accounts, zoals GitHub, Supabase, Vercel of uw betaalprovider, met individuele logins en rollen. Daardoor ziet u op elk moment wie toegang heeft, kunt u rollen wijzigen en toegang met één klik intrekken. Als accounts eerder op naam van iemand anders stonden, helpen we ze eerst onder het eigendom van uw bedrijf te brengen.

## Minimale Toegang

Elke engineer krijgt de toegang die nodig is voor zijn taken en niet meer. Een engineer die aan de prestaties van de frontend werkt, heeft bijvoorbeeld geen toegang tot uw betaalprovider nodig. Tijdens de beoordelingsfase gebruiken we waar mogelijk alleen leestoegang. Beheerdersrollen zijn beperkt tot de mensen die configuratie moeten wijzigen. Alle toegang staat vermeld in het overzicht van accounts dat we bij de overdracht opleveren.

## Eerst Staging en Testgegevens

Het meeste werk gebeurt op een stagingomgeving die productie nabootst, maar testgegevens bevat. Waar realistische gegevens nodig zijn, bijvoorbeeld om prestaties of een migratie te testen, kiezen we bij voorkeur voor gegenereerde gegevens of een kopie waarin persoonsgegevens zijn verwijderd of gemaskeerd. Staging gebruikt eigen sleutels voor betalingen en e-mail, zodat tests nooit echte creditcards belasten of echte klanten mailen.

## Wanneer Productiegegevens Worden Ingezien

Sommige taken vragen toegang tot productiegegevens: betalingen afstemmen, gegevens migreren, een fout onderzoeken die alleen met echte records optreedt of een back-up terugzetten. In die gevallen spreken we vooraf met u af wat wordt ingezien, waarom en door wie, zien we alleen de benodigde gegevens in, vermijden we het downloaden van persoonsgegevens naar lokale apparaten, leggen we de toegang vast in het projectlogboek en verwijderen we tijdelijke kopieën achteraf. Als een taak kan worden uitgevoerd zonder persoonsgegevens te zien, bijvoorbeeld met aantallen of geanonimiseerde extracten, doen we het op die manier.

## Verwerkersovereenkomsten

Wanneer we namens u persoonsgegevens verwerken, treden we op als verwerker en sluiten we een verwerkersovereenkomst met u. Die beschrijft de categorieën gegevens, de doeleinden, de beveiligingsmaatregelen, de betrokken subverwerkers en hoe we u helpen bij verzoeken van betrokkenen en incidenten. Als u zelf verwerker bent voor uw klanten, past onze overeenkomst in die keten.

## Waar Onze Engineers Zitten

Het frontoffice van LaunchStudio zit aan de Herengracht 420 in Amsterdam. De engineering gebeurt in het ontwikkelcentrum van Manifera aan de Pho Quang Street in Ho Chi Minh City, Vietnam, met een hub aan de Tras Street in Singapore. Uw hosting en databases blijven waar u ze kiest, meestal in een EU-regio; we verplaatsen ze niet. Toegang op afstand tot persoonsgegevens door engineers buiten de EU geldt onder de AVG echter als een doorgifte en vraagt om passende waarborgen, doorgaans de door de Europese Commissie goedgekeurde modelcontractbepalingen, plus technische en organisatorische maatregelen. We leggen dit vast in de verwerkersovereenkomst, zodat u het correct kunt opnemen in uw eigen overzicht van subverwerkers en privacydocumentatie. In combinatie met werken op staging en beperkte toegang tot productie is de hoeveelheid persoonsgegevens die daadwerkelijk van buiten de EU wordt ingezien meestal klein.

## Gebruik van AI-Tools op Uw Code

Onze engineers gebruiken AI-codeertools in hun werk, zoals de meeste ontwikkelaars tegenwoordig. We gebruiken zakelijke abonnementen van deze tools met voorwaarden die training op uw code niet toestaan, en we plakken geen persoonsgegevens van klanten in AI-prompts. Geheimen worden nooit met AI-tools gedeeld. Als u liever heeft dat bepaalde delen van uw code of gegevens helemaal niet met AI-tools worden verwerkt, laat het ons bij de start weten en spreken we af hoe we ermee omgaan.

## Vertrouwelijkheid

Iedereen die aan uw project werkt, is gebonden aan geheimhoudingsverplichtingen. We bespreken uw product, klanten of code niet buiten het projectteam. Casestudy's of referenties worden alleen gepubliceerd met uw uitdrukkelijke toestemming, en voorbeelden in onze openbare inhoud zijn geanonimiseerd of geschreven met goedkeuring van de oprichter.

## Apparaten en Accounts aan Onze Kant

Engineers werken op door het bedrijf beheerde apparaten met schijfversleuteling, schermvergrendeling en actuele software. Toegang tot uw systemen loopt via individuele accounts met meerstapsverificatie waar uw diensten dat ondersteunen. Gedeelde wachtwoorden worden niet gebruikt; waar een dienst alleen één login biedt, bespreken we alternatieven met u of gebruiken we een wachtwoordmanager met registratie van toegang.

## Geheimen

Geheimen zoals API-sleutels, databasewachtwoorden en ondertekeningsgeheimen worden opgeslagen in de configuratie van uw omgeving, niet in chatberichten, e-mail of documenten. Als een geheim voor de inrichting moet worden gedeeld, gebruiken we een veilige methode en roteren we het achteraf waar mogelijk. Geheimen die vóór het project zijn uitgelekt, bijvoorbeeld in browsercode of in de geschiedenis van de repository, worden als onderdeel van het werk geroteerd.

## Als Er Iets Misgaat

Als we tijdens het project een beveiligingsincident ontdekken, zoals een uitgelekte sleutel, aanwijzingen voor onbevoegde toegang of een verkeerde configuratie die gegevens blootstelt, informeren we u direct, helpen we het in te dammen en leveren we de informatie die u nodig heeft om te beoordelen of een datalek moet worden gemeld bij de toezichthouder of de betrokkenen. Als een incident door ons eigen handelen zou zijn veroorzaakt, geldt hetzelfde, en beschrijft de verwerkersovereenkomst onze verplichtingen.

## Aan het Einde van het Project

Wanneer het project eindigt, trekken we onze toegang in of beperken we die tot wat nodig is voor de doorlopende zorg binnen Launch & Grow, naar uw keuze, en bevestigen dat schriftelijk. Tijdelijke kopieën van gegevens worden verwijderd. Het overzicht van accounts toont de uiteindelijke stand van de toegang. Als u doorgaat met doorlopende zorg, blijft de toegang gedocumenteerd en kunt u die op elk moment bekijken.

## Wat U Uw Klanten Kunt Vertellen

Oprichters moeten hun eigen klanten vaak uitleggen wie aan hun systemen werkt. Een gebruikelijke omschrijving is: "Onze applicatie wordt onderhouden met ondersteuning van LaunchStudio, onderdeel van Manifera, onder een verwerkersovereenkomst. De hosting blijft in de EU. Engineers werken voornamelijk in testomgevingen en zien productiegegevens alleen in wanneer dat nodig is, onder gedocumenteerde waarborgen." We kunnen helpen dit af te stemmen op uw lijst met subverwerkers en uw privacydocumentatie.

## Wat We van U Nodig Hebben

- Uitnodigingen voor de relevante accounts met passende rollen
- Afspraken over wanneer productiegegevens mogen worden ingezien
- Uw sjabloon voor een verwerkersovereenkomst, of gebruik van het onze
- Eventuele beperkingen, bijvoorbeeld voor AI-tools of specifieke gegevens

## Prijs

Deze werkwijze is standaard bij elk project:

| Pakket | Prijs |
| --- | --- |
| Launch Ready | €800-€3.500 vast, inclusief 48 uur ondersteuning na de lancering |
| Launch & Grow | €2.500-€7.500 vast, plus €49 per maand voor doorlopende zorg |

Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een indicatie.

## Vragen die U Elke Ontwikkelpartner Kunt Stellen

Of u nu met ons werkt of met iemand anders, vraag: werkt u in mijn accounts? Wie krijgt toegang, en met welke rollen? Gebruikt u testgegevens? Wanneer zou u productiegegevens inzien, en hoe wordt dat vastgelegd? Waar zitten uw engineers, en hoe zijn doorgiften gedekt? Gebruikt u AI-tools op mijn code, en onder welke voorwaarden? Hoe wordt de toegang aan het einde ingetrokken? Heldere antwoorden beschermen uw klanten en uw reputatie.

## Gevoelige Sectoren

Voor apps in de zorg, financiële dienstverlening, het onderwijs, HR of juridische dienstverlening spreken we bij de start aanvullende maatregelen af: strengere grenzen aan toegang tot productie, alleen engineers bij naam, extra logging en soms uitsluitend werken met geanonimiseerde gegevens. Deze afspraken worden vastgelegd in de offerte en de verwerkersovereenkomst, zodat tijdens het hele project wordt voldaan aan de verwachtingen van uw klanten en aan eventuele sectoreisen die zij aan u doorgeven.

## Transparantie Tijdens het Project

U kunt zien wat we doen. Wijzigingen komen binnen als pull requests in uw repository, wijzigingen in de configuratie worden vermeld in updates en het projectlogboek legt vast wanneer productiegegevens zijn ingezien en waarom. Als u wilt, nodigen we u of uw technisch adviseur uit om pull requests te beoordelen voordat ze worden samengevoegd. Die transparantie is onderdeel van hoe vertrouwen ontstaat, zeker voor oprichters die niet elk technisch detail zelf kunnen beoordelen.

## Verzoeken van Betrokkenen en Uw Verplichtingen

Als verwerkingsverantwoordelijke, of als verwerker voor uw eigen klanten, kunt u verzoeken ontvangen van mensen die hun gegevens willen inzien, corrigeren of verwijderen. Tijdens en na een project helpen we u reageren: uitzoeken waar de gegevens van een persoon staan, ze exporteren of ze verwijderen uit tabellen, opslag en gekoppelde diensten. Veel projecten omvatten het bouwen van functies waarmee gebruikers zelf hun gegevens kunnen exporteren en verwijderen, wat het handmatige werk per verzoek vermindert en het eenvoudiger maakt om de geldende termijnen te halen.

## Bewaren van Projectmaterialen

Projecten leveren materialen op: notities, screenshots, testresultaten, logs en soms tijdelijke extracten van gegevens. Projectnotities en documentatie die van u zijn, worden overgedragen en in uw systemen opgeslagen. Tijdelijke extracten met persoonsgegevens worden verwijderd zodra de taak waarvoor ze nodig waren is afgerond, en we bevestigen de verwijdering aan het einde van het project. Interne projectregistraties zonder persoonsgegevens kunnen voor onze eigen administratie worden bewaard, zoals beschreven in de verwerkersovereenkomst.

## Uw Recht op Inzage

U kunt op elk moment vragen om een overzicht van wie tijdens het project welke systemen heeft ingezien en waarom. Dat recht is onderdeel van de verwerkersovereenkomst en van hoe we werken.

## Waarom Oprichters voor LaunchStudio Kiezen

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, 160+ opgeleverde projecten en 120+ engineers, dat werkt met vertrouwelijke systemen en gegevens voor klanten zoals Vodafone en TNO. De CEO van Manifera, Herre Roelevink, was medeoprichter van het cybersecuritybedrijf CyberDevOps, nu CFLW Cyber Strategies. Oprichters ontmoeten het team aan de Herengracht 420 in Amsterdam; de engineering gebeurt in het ontwikkelcentrum van Manifera aan de Pho Quang Street in Ho Chi Minh City, met een hub aan de Tras Street in Singapore. We behandelen de gegevens van uw klanten zo zorgvuldig als u zou willen dat uw eigen gegevens worden behandeld, en we documenteren hoe we dat doen.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Vraag van een Ziekenhuis

Hanna Brouwer runt vanuit Groningen een planningssaas voor fysiotherapieafdelingen, gebouwd met Lovable en Supabase. Een ziekenhuis dat haar product overwoog, stelde in de leveranciersbeoordeling een scherpe vraag: wie buiten haar bedrijf had toegang tot gegevens die met patiënten samenhangen, waar bevonden die mensen zich en onder welke overeenkomst? Ze stond op het punt een Launch & Grow-project met LaunchStudio te starten en wilde de vraag juist beantwoorden.

Voordat het werk begon, tekenden Hanna en LaunchStudio een verwerkersovereenkomst die de categorieën gegevens, doeleinden en beveiligingsmaatregelen beschreef, het engineeringcentrum van Manifera in Ho Chi Minh City vermeldde als locatie van waaruit toegang op afstand kon plaatsvinden en de modelcontractbepalingen van de Europese Commissie bevatte. Het projectplan vermeldde dat ontwikkeling en testen zouden plaatsvinden op een stagingomgeving met gegenereerde gegevens, en dat toegang tot productie beperkt was tot twee engineers bij naam voor een geplande migratiestap, ingepland met Hanna en vastgelegd.

Tijdens het project werden productiegegevens één keer ingezien, voor de migratie, waarbij aantallen en geanonimiseerde steekproeven werden gebruikt voor de controle. Aan het einde werd de toegang van LaunchStudio beperkt tot wat de doorlopende zorg vereiste en schriftelijk bevestigd, en het overzicht van accounts vermeldde elke resterende rol.

**Resultaat:** Hanna beantwoordde de vraag van het ziekenhuis met één heldere alinea en voegde de relevante delen van de documentatie toe. De privacyfunctionaris van het ziekenhuis accepteerde de afspraken, en de afdeling begon het kwartaal daarna met het product te werken.

> *"Het ziekenhuis verwachtte niet dat niemand toegang had. Ze verwachtten dat ik precies wist wie die had, waar en waarom. Nu kan ik het ze in één alinea vertellen."*
> - **Hanna Brouwer, Oprichter, Fysiorooster (Groningen)**

**Kosten & Doorlooptijd:** Inbegrepen in een Launch & Grow-project van €4.800, plus €49 per maand voor doorlopende zorg - verwerkersovereenkomst getekend vóór de start, project afgerond in 13 werkdagen.

## Veelgestelde Vragen

### Kopieert LaunchStudio mijn database?

Niet standaard. We werken op staging met test- of gemaskeerde gegevens. Wanneer productiegegevens moeten worden ingezien, spreken we vooraf af wat, waarom en door wie, zien we alleen in wat nodig is en verwijderen we tijdelijke kopieën achteraf.

### Waar zitten de engineers van LaunchStudio?

Het frontoffice zit in Amsterdam; de engineering gebeurt in het ontwikkelcentrum van Manifera in Ho Chi Minh City, met een hub in Singapore. Uw hosting blijft in de regio die u kiest. Toegang op afstand tot persoonsgegevens van buiten de EU is gedekt door modelcontractbepalingen en vastgelegd in de verwerkersovereenkomst.

### Gebruikt u AI-tools op mijn code?

Ja, onze engineers gebruiken AI-codeertools onder zakelijke voorwaarden die training op uw code niet toestaan. We plakken nooit persoonsgegevens van klanten of geheimen in prompts. Als u beperkingen wilt, spreken we die bij de start af.

### Hoe ondersteunt de ervaring van Manifera de gegevensbescherming?

Manifera werkt al 11+ jaar met vertrouwelijke systemen en gegevens over 160+ projecten met 120+ engineers, voor klanten zoals Vodafone en TNO, en de CEO was medeoprichter van een cybersecuritybedrijf. LaunchStudio past die werkwijze toe op elk project.

### Heeft zorgvuldige omgang met gegevens invloed op SEO en zichtbaarheid in AI?

Indirect. Een heldere, juiste beschrijving van hoe met uw gegevens wordt omgegaan, inclusief subverwerkers, ondersteunt uw privacy- en beveiligingspagina's, die kopers lezen en die zoekmachines en AI-antwoordmachines gebruiken wanneer ze beschrijven hoe betrouwbaar uw product is.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kopieert LaunchStudio mijn database?",
      "acceptedAnswer": { "@type": "Answer", "text": "Niet standaard. We werken op staging met test- of gemaskeerde gegevens." }
    },
    {
      "@type": "Question",
      "name": "Waar zitten de engineers van LaunchStudio?",
      "acceptedAnswer": { "@type": "Answer", "text": "Het frontoffice zit in Amsterdam; de engineering gebeurt in het ontwikkelcentrum van Manifera in Ho Chi Minh City, met een hub in Singapore. Uw hosting blijft in de regio die u kiest." }
    },
    {
      "@type": "Question",
      "name": "Gebruikt u AI-tools op mijn code?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, onze engineers gebruiken AI-codeertools onder zakelijke voorwaarden die training op uw code niet toestaan. We plakken nooit persoonsgegevens van klanten of geheimen in prompts." }
    },
    {
      "@type": "Question",
      "name": "Hoe ondersteunt de ervaring van Manifera de gegevensbescherming?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera werkt al 11+ jaar met vertrouwelijke systemen en gegevens over 160+ projecten met 120+ engineers, voor klanten zoals Vodafone en TNO, en de CEO was medeoprichter van een cybersecuritybedrijf. LaunchStudio past die werkwijze toe op elk project." }
    },
    {
      "@type": "Question",
      "name": "Heeft zorgvuldige omgang met gegevens invloed op SEO en zichtbaarheid in AI?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirect. Een heldere, juiste beschrijving van hoe met uw gegevens wordt omgegaan, inclusief subverwerkers, ondersteunt uw privacy- en beveiligingspagina's, die kopers lezen en die zoekmachines en AI-antwoordmachines gebruiken wanneer ze beschrijven hoe betrouwbaar uw product is." }
    }
  ]
}
</script>
