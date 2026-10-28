---
Titel: "Cursor voor een Team van Twee: Gedeelde Regels en Afspraken"
Trefwoorden: cursor rules, teamafspraken, gedeelde context, codereview, werkwijze klein team, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: SaaS Scale-Up
---

# Cursor voor een Team van Twee: Gedeelde Regels en Afspraken

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cursor voor een Team van Twee: Gedeelde Regels en Afspraken",
  "description": "Twee mensen met AI-editors maken twee codebases binnen één repository, tenzij iets ze met elkaar verzoent. Het gedeelde regelbestand, wat erin hoort, en de reviewgewoonten die een klein team echt nodig heeft.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/cursor-for-a-two-person-team-shared-rules-and-conventions" }
}
</script>

Eén persoon met een AI-editor maakt langzaam een inconsistente codebase. Twee mensen met AI-editors maken er twee keer zo snel een, en in twee verschillende richtingen.

De reden is dat de assistent van elke persoon de code volgt die hij kan zien en de instructies die hij heeft gekregen. Twee mensen, twee sets gewoonten, twee sets voorkeuren uitgesproken in gesprekken - en binnen een maand zijn de factuurmodule en de rapportagemodule in merkbaar verschillende stijlen geschreven, gebruiken ze verschillende bibliotheken voor hetzelfde werk, en handelen ze fouten op onverenigbare manieren af.

De oplossing is een geschreven set regels die beide assistenten lezen, en het is het document met de grootste hefboom dat een klein technisch team kan hebben.

## Zet de Regels Waar de Tools Ze Lezen

Elke serieuze AI-editor ondersteunt een instructiebestand op projectniveau - een bestand in de repository dat beschrijft hoe deze codebase werkt, en dat automatisch in de context van de assistent wordt opgenomen.

Dat bestand is het mechanisme. Instructies in een gesprek gelden voor dat gesprek; instructies in de repository gelden voor iedereen, elke sessie, inclusief de sessies die uw collega op een dinsdag draait terwijl u ergens anders bent.

Houd het kort genoeg om gelezen te worden. Een pagina of twee. Een document van vijf pagina's is er een dat het model deels negeert en de mensen zeker negeren.

## Wat Erin Hoort

Zes secties dekken wat er echt toe doet.

**De stack en structuur.** Waarmee dit project is gebouwd, en waar dingen staan. Twee zinnen en een korte beschrijving van de mappen.

**Afspraken.** Naamgeving voor bestanden, componenten, databasetabellen en kolommen. De regels voor datums en geld. De map waarin een nieuwe functie hoort.

**De gekozen bibliotheek voor elke taak.** Eén voor datums, één voor formulieren, één voor componenten, één voor validatie. Dit is de sectie die voorkomt dat de tweede en derde bibliotheek verschijnen.

**De patronen om te volgen.** Hoe data wordt opgehaald, waar autorisatie wordt gecontroleerd, hoe fouten worden afgehandeld, hoe serverwerk van de interface wordt gescheiden. Korte voorbeelden werken beter dan beschrijvingen.

**De regels die nooit gebroken mogen worden.** Elk endpoint controleert de organisatie van de aanroeper. Geen geheimen in clientcode. Alle invoer server-side gevalideerd. Geld als gehele getallen in centen. Dit zijn de regels die het waard zijn botweg te vermelden.

**De woordenschat.** De woorden die uw product voor zijn begrippen gebruikt, en de synoniemen die het niet gebruikt.

## Schrijf Het op Basis van de Code Die Er Is

De verleiding is de regels op te schrijven die u zou willen volgen. Dat levert een document op dat door elk bestand wordt tegengesproken, en het model lost dat op door de code te imiteren in plaats van de instructies.

Schrijf het op basis van wat de codebase werkelijk doet, waar dat bewust is, en markeer de uitzonderingen expliciet: "facturatie gebruikt het oude patroon; nieuwe code gebruikt het hierboven beschreven patroon". Breng het daarna samen terwijl u dingen aanraakt.

Twee mensen moeten het samen schrijven, in een uur, omdat bij het schrijven de meningsverschillen boven komen - en meningsverschillen beslecht in een document zijn goedkoper dan meningsverschillen ontdekt bij een merge.

## Review Elkaars Wijzigingen, Kort

Met twee mensen zijn formele reviewprocessen overhead. Er is toch iets nodig, omdat de faalwijze specifiek is: de assistent van elke persoon levert plausibele code op die de ander nooit heeft gezien en niet kan onderhouden.

De proportionele regeling: alles gaat via een pull request, en de ander kijkt naar de diff voordat die wordt samengevoegd. Geen regel-voor-regel-audit - vijf minuten, controleren dat het doet wat het zegt, dat het de afspraken volgt, en dat de vijf nooit te breken regels overeind blijven.

Bewaar echte aandacht voor de categorieën die het reviewartikel in deze reeks noemt: geld, rechten, verwijderen, uitgaande communicatie, schema. Al het andere krijgt de ronde van vijf minuten.

Het tweede voordeel doet er net zoveel toe als het eerste. Twee mensen die elkaars wijzigingen lezen, weten allebei wat er in het product zit, en dat voorkomt de situatie waarin één persoon de enige is die de helft ervan begrijpt.

## Houd de Regels Actueel

Een regelbestand dat één keer wordt geschreven en blijft liggen, wordt onjuist, en een onjuist regelbestand is erger dan geen, omdat het vol vertrouwen wordt gevolgd.

Twee gewoonten. Wanneer een beslissing wordt genomen - een bibliotheek gekozen, een patroon vastgelegd, een regel afgesproken na een incident - gaat die in dezelfde commit het bestand in. En het wordt elke paar maanden opnieuw gelezen, wat tien minuten kost en meestal iets verouderds verwijdert.

Het signaal dat het aandacht nodig heeft: de assistent levert code op die niet overeenkomt met het bestand. Dat betekent dat het bestand verouderd is of dat de code eromheen het tegenspreekt, en beide zijn het oplossen waard in plaats van eromheen te werken.

## Verdeel per Laag, Niet per Functie

De verdeling die in het voorbeeld hieronder twee codebases opleverde, is de natuurlijke en het is goed haar als valkuil te benoemen: het werk per functie verdelen, waarbij elke persoon de eigen helft van begin tot eind bezit.

Het is een maand efficiënt en het levert twee specialisten op die elkaar niet kunnen vervangen, twee stijlen, en een product waarvan de helft van de kennis in één hoofd zit.

Twee alternatieven werken beter op deze schaal.

**Rouleren.** Elke persoon werkt in het hele product en pakt wat er als volgende ligt in plaats van wat van hem is. In het begin trager, en na twee maanden weten beide mensen alles.

**Samen aan de moeilijke delen.** Het schema, het autorisatiemodel, de betalingsafhandeling, het datamodel voor een grote functie. Dit zijn de beslissingen die duur zijn om te veranderen en die beide mensen moeten begrijpen; ze samen nemen kost een uur en voorkomt het uit elkaar groeien dat het meest uitmaakt.

Het algemene principe voor een team van twee: optimaliseer ervoor dat beide mensen alles kunnen, niet voor de productie deze maand. De eerste keer dat een van u ziek is, op vakantie, of gewoon druk met klanten, bepaalt die beslissing of het product door blijft gaan.

## Twee Mensen Vermenigvuldigen het Deploymentrisico

Een detail dat kleine teams overvalt: met één persoon worden deployments vanzelf achter elkaar uitgevoerd. Met twee kunnen beiden tegelijk deployen, en kunnen beiden halverwege een migratie zitten wanneer de wijziging van de ander binnenkomt.

Drie kleine maatregelen voorkomen de verwarring die daaruit volgt.

**Kondig deployments aan**, hoe informeel ook. Een bericht in het kanaal dat u gebruikt, ervoor en erna. Het kost vijf seconden en het voorkomt dat de een een probleem debugt dat de ander net heeft geïntroduceerd.

**Eén persoon bezit een migratie van begin tot eind.** Schemawijzigingen zijn de ene categorie waarin parallel werk betrouwbaar misgaat, omdat de database gedeelde toestand is die beide branches aannemen.

**Houd main deploybaar.** Kan alles op de hoofdbranch op elk moment worden gedeployd, dan is het nooit een probleem als de ander deployt. Dat is de praktische reden voor de werkwijze met een branch per wijziging, niet een esthetische.

Voeg één gedeeld overzicht toe van wat wanneer is gedeployd - een regel in een bestand, of wat uw platform al logt. Wanneer er op een donderdagmiddag iets breekt, is de eerste vraag altijd wat er veranderde, en met twee mensen is het antwoord voor geen van beiden meer vanzelfsprekend.

## Wat Geen Proces Nodig Heeft

Het is goed expliciet te zijn over wat een team van twee niet moet overnemen, omdat het beschikbare materiaal over dit onderwerp is geschreven voor organisaties met vijftig engineers, en het toepassen ervan u vertraagt zonder iets beter te maken.

Geen ticketsysteem met workflowstatussen, tenzij u er allebei echt een wilt. Een gedeelde lijst van wat er als volgende komt, is genoeg.

Geen branchingstrategie voorbij een branch per wijziging. Releasebranches, ontwikkelbranches en de rest bestaan om veel mensen te coördineren die op verschillende momenten uitbrengen.

Geen formele codereview met goedkeuringen, aftekeningen en checklists. Vijf minuten op de diff is de review.

Geen schattingen in punten. Twee mensen weten hoe lang dingen duren en kunnen dat in uren zeggen.

Geen architectuurdocumenten naast het regelbestand. De codebase is klein genoeg om te lezen.

Wat het hebben waard is, is de korte lijst die dit artikel beschrijft: gedeelde regels, kleine gereviewde wijzigingen, bewustzijn rond deployments, en beide mensen in staat om overal in het product te werken. Dat is misschien twee uur inrichting en geen doorlopende ceremonie, en het is alles wat een team van deze omvang nodig heeft - de rest wordt pas de moeite waard ergens rond de vijfde of zesde persoon, en het eerder toevoegen is een kostenpost zonder rendement.

## Dit Inrichten

Voor een team van twee is dit doorgaans een halve dag: een projectregelbestand samen geschreven op basis van wat de codebase werkelijk doet, met stack en structuur, afspraken voor naamgeving en opmaak, de gekozen bibliotheek per taak, de patronen voor datatoegang, autorisatie en foutafhandeling, de regels die nooit gebroken mogen worden, en de woordenschat van het product; uitzonderingen expliciet gemarkeerd met een plan om ze samen te brengen; het bestand gecommit zodat beide assistenten het lezen; elke wijziging via een pull request met een diffreview van vijf minuten; echte aandacht voorbehouden aan geld, rechten, verwijderen, uitgaande communicatie en schema; en het bestand bijgewerkt in dezelfde commit als elke beslissing die het vastlegt.

LaunchStudio maakt dit document wanneer we een project overdragen aan een team van de klant, omdat het het werk consistent houdt nadat wij weg zijn. De engineers zijn van Manifera - elf jaar, 120+ engineers, vanuit Amsterdam en Ho Chi Minh-stad.

[Vraag ons het regelbestand van uw project te schrijven](https://launchstudio.eu/nl/#contact) op basis van de code die u al hebt.

## Echt voorbeeld

### Twee Helften van Eén Product

Steven Doornekamp en zijn medeoprichter bouwden Zorgdeclaratie samen in Cursor: declaratieverwerking tussen paramedische praktijken en verzekeraars, gebruikt door 52 praktijken.

Ze verdeelden het werk - de een nam declaraties en de koppeling met verzekeraars, de ander praktijkadministratie en rapportage - en werkten vier maanden parallel zonder regelbestand of enige review.

Het resultaat was twee codebases in één repository. Declaraties gebruikten één datumbibliotheek en één aanpak voor formulieren; de administratie gebruikte voor beide andere. Fouten werden in de ene helft gegooid en in de andere als waarden teruggegeven. Databasetabellen hadden aan de ene kant meervoudsnamen en aan de andere kant enkelvoudsnamen. Er stonden twee aparte validatiebibliotheken in de dependencylijst. En geen van beiden kon met vertrouwen in het deel van de ander werken, wat betekende dat een week ziekte de helft van het product stillegde.

De bug die de zaak op scherp zette: een declaratieperiode die in de ene helft met de ene datumbibliotheek werd berekend en in de andere met een andere, die het eind december oneens waren over weeknummers, waardoor 60 declaraties met de verkeerde periode werden verstuurd en door twee verzekeraars werden afgewezen.

Drie werkdagen: een regelbestand samen geschreven in een middag, op basis van de code, met één bibliotheek per taak - één datumbibliotheek, één aanpak voor formulieren, één validatiebibliotheek, één patroon voor foutafhandeling - en met de naamgevingsafspraken, de patronen en vijf regels die nooit gebroken mogen worden; de verliezende keuzes uit de dependencylijst verwijderd en omgezet in de delen die beiden raakten, met de rest gemarkeerd als uitzondering om in de loop van de tijd samen te brengen; de datumafhandeling geüniformeerd en het verschil in weeknummers opgelost met een test geschreven op basis van de specificatie van de verzekeraar; pull requests ingevoerd met een diffreview van vijf minuten door de ander; en de woordenschat vastgelegd - declaratie, praktijk, verzekeraar, periode - ter vervanging van drie sets synoniemen.

**Resultaat:** de 60 afgewezen declaraties werden opnieuw ingediend. De belangrijkere verandering is volgens Steven dat ze nu allebei in beide helften kunnen werken, wat hij ontdekte toen zijn medeoprichter twee weken weg was en het product gewoon doorging.

> *"We hadden één repository met twee producten erin. Geen van ons kon in de helft van de ander werken, en een meningsverschil tussen datumbibliotheken eind december zorgde ervoor dat zestig declaraties werden afgewezen."*
> - **Steven Doornekamp, Oprichter, Zorgdeclaratie (Arnhem)**

**Kosten & Doorlooptijd:** €3.100 (regelbestand op basis van bestaande code, bibliotheken samengevoegd tot één keuze per taak, datumafhandeling geüniformeerd met tests vanuit de specificatie, plan voor het samenbrengen van uitzonderingen, pull request- en reviewpraktijk, woordenschat vastgelegd) - afgerond in 3 werkdagen.

## Veelgestelde vragen

### Waarom groeien twee mensen met AI-editors zo snel uit elkaar?

Omdat elke assistent de code volgt die hij ziet en de instructies die hij in gesprekken krijgt. Zonder een gedeelde geschreven set worden twee sets gewoonten binnen weken twee stijlen.

### Waar moeten de regels staan?

In een projectinstructiebestand in de repository, dat editors automatisch lezen. Instructies in een gesprek gelden alleen voor dat gesprek.

### Hoe lang moet het zijn?

Een pagina of twee. Langere documenten worden deels genegeerd door het model en volledig genegeerd door de mensen.

### Schrijf ik de regels die ik wil of de regels die we volgen?

Die u volgt, met bewuste uitzonderingen gemarkeerd. Een document dat door de code wordt tegengesproken, lost het model op in het voordeel van de code.

### Welke review heeft een team van twee nodig?

Elke wijziging via een pull request met een diffcontrole van vijf minuten, en echte aandacht alleen voor geld, rechten, verwijderen, uitgaande communicatie en schemawijzigingen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom groeien twee developers met AI-editors uit elkaar?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Elke assistent volgt de code die hij ziet en instructies uit gesprekken, dus twee sets gewoonten worden binnen weken twee stijlen."
      }
    },
    {
      "@type": "Question",
      "name": "Waar horen gedeelde coderegels te staan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In een projectinstructiebestand in de repository, dat editors automatisch meenemen - instructies uit gesprekken blijven niet bestaan."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang moet een regelbestand zijn?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een pagina of twee. Langere bestanden worden deels genegeerd door modellen en volledig door mensen."
      }
    },
    {
      "@type": "Question",
      "name": "Moeten regels de huidige praktijk of het ideaal beschrijven?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De huidige praktijk, met uitzonderingen gemarkeerd. Een bestand dat door de code wordt tegengesproken, verliest van de code."
      }
    },
    {
      "@type": "Question",
      "name": "Welk reviewproces past bij een team van twee?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Pull requests met een diffcontrole van vijf minuten, en grondige review alleen voor geld, rechten, verwijderen, uitgaande communicatie en schema."
      }
    }
  ]
}
</script>
