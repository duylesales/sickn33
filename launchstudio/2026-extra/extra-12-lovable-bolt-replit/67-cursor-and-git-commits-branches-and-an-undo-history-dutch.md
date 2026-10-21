---
Titel: "Cursor en Git: Commits, Branches en een Ongedaan-maakgeschiedenis"
Trefwoorden: cursor git, versiebeheer, branches, commitberichten, AI-wijzigingen terugdraaien, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Cursor en Git: Commits, Branches en een Ongedaan-maakgeschiedenis

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cursor en Git: Commits, Branches en een Ongedaan-maakgeschiedenis",
  "description": "Versiebeheer doet er meer toe wanneer een machine de code schrijft, omdat u moet kunnen zien wat er veranderde en het ongedaan moet kunnen maken. De minimale werkwijze voor een solo-oprichter, uitgelegd zonder jargon.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/cursor-and-git-commits-branches-and-an-undo-history" }
}
</script>

Versiebeheer wordt meestal gepresenteerd als iets wat professionele teams nodig hebben om samen te werken. Voor een oprichter die alleen werkt met een AI-editor is het iets heel anders: het enige mechanisme waarmee u kunt zien wat een machine in uw product heeft veranderd en het ongedaan kunt maken als het fout was.

Dat maakt het hier belangrijker dan bij traditionele ontwikkeling, niet minder. Een mens die code schrijft, herinnert zich wat hij deed. Een tool die elf bestanden aanpaste naar aanleiding van een verzoek over één ervan, laat u geen andere manier om erachter te komen.

## De Drie Dingen Die Het U Geeft

**Een overzicht van wat er veranderde.** Elke aanpassing, wanneer, en idealiter waarom. In een codebase die grotendeels door een tool is geschreven, is dit de enige verklaring van waarom het product is zoals het is.

**De mogelijkheid om terug te draaien.** Niet één toetsaanslag, maar elke wijziging, op elk moment, inclusief een van drie weken geleden die iets blijkt te hebben gebroken dat u pas vandaag opmerkte.

**Een plek om te experimenteren.** Een branch is een kopie die u vrij kunt slopen. Met een branch wordt een sessie die slecht afloopt in een seconde weggegooid in plaats van in een middag uitgeplozen — en dat is, zoals het kostenartikel in deze reeks beschrijft, ook waar het meeste geld heen gaat.

## De Minimale Werkwijze

Negeer het meeste van wat er over branchingstrategieën wordt geschreven. Voor één persoon is dit genoeg.

**Eén hoofdbranch** die altijd werkt en die wordt gedeployd.

**Een branch voor elk stuk werk**, aangemaakt voordat u begint, genoemd naar wat het is. Werkt het, voeg het samen met main en verwijder de branch. Gaat het mis, verwijder hem en begin opnieuw — dit is het moment waarop de hele praktijk zich terugbetaalt.

**Commit zodra iets werkt**, niet wanneer een functie af is. Kleine commits, vaak, elk een punt waarnaar u kunt terugkeren. Een dag met twaalf commits is een dag met twaalf checkpoints.

**Push naar een remote** — een gehoste repository — minstens dagelijks. Lokaal gecommit werk leeft op één laptop.

Dat is de hele werkwijze. Het duurt een paar dagen voordat het automatisch gaat, en het neemt een hele categorie zorgen over het accepteren van wijzigingen weg.

## Schrijf Berichten Die Uitleggen Waarom

Een commitbericht is de ene plek waar de bedoeling wordt vastgelegd, en in een AI-gebouwde codebase vaak de enige.

"Update" zegt niets. "Btw-berekening gecorrigeerd zodat de korting vóór de belasting wordt toegepast in plaats van erna, wat facturen voor regels met korting één tot twee euro te hoog maakte" is een zin die de vraag beantwoordt die een toekomstige lezer zal hebben.

De gewoonte die dit makkelijk maakt: schrijf het bericht eerst, vóór de wijziging. Het verheldert wat u gaat doen, het houdt de wijziging bij één ding, en het betekent dat het bericht de bedoeling beschrijft in plaats van achteraf te worden gereconstrueerd.

Twee conventies die het overnemen waard zijn. Een korte eerste regel die zegt wat er veranderde en, waar het niet vanzelf spreekt, een alinea die uitlegt waarom. En één commit per logische wijziging, zodat de geschiedenis kan worden gelezen als een reeks beslissingen in plaats van als een stapel.

## Commit Vóór Elke Sessie, Zonder Uitzondering

De nuttigste regel bij het werken met een AI-editor: begin nooit een sessie met niet-gecommitte wijzigingen.

De reden is eenvoudig. Is de werkende toestand gecommit, dan kan alles wat de tool doet met één commando volledig ongedaan worden gemaakt. Is dat niet zo, dan zijn de wijzigingen van de tool en die van u door elkaar gemengd, en ze scheiden is handwerk op precies het moment dat u gefrustreerd bent.

Maak er een reflex van. Commit, dan prompten. Het kost vijf seconden en het voordeel is dat elke sessie omkeerbaar wordt.

## Wat U Niet Moet Committen

Drie categorieën, en de eerste is ernstig.

**Geheimen.** Omgevingsbestanden, sleutels, inloggegevens. Eenmaal gecommit blijven ze na verwijdering in de geschiedenis staan, en daarom is het juiste antwoord op het vinden van een geheim het roteren ervan. Een ignore-bestand voor omgevingsbestanden is het eerste wat u aan elk project toevoegt.

**Gegenereerde uitvoer.** Buildartefacten, dependency-mappen. Ze zijn groot, veranderen voortdurend en zijn reproduceerbaar.

**Persoonsgegevens.** Database-exports, klantvoorbeelden, screenshots met echte records. Deze belanden vaker in repositories dan iemand zou willen, en een repository die later openbaar wordt, neemt ze mee.

Al het andere — inclusief uw voorbeeldconfiguratiebestand, uw afsprakenbestand en uw migraties — hoort erin.

## Wanneer Er Iets Breekt en U Niet Weet Wanneer

De situatie die de hele praktijk rechtvaardigt: een klant meldt iets dat vroeger werkte, en u hebt geen idee wanneer het ophield.

Met een geschiedenis is dit te beantwoorden in plaats van mysterieus. Zoek een commit van voordat het probleem bestond, zet die in een tijdelijke toestand neer, en kijk of het gedrag daar correct is. Werk dan vooruit — of, sneller, gebruik de bisect-functie, die de exacte commit vindt die een probleem introduceerde door punten in de geschiedenis te testen zoals u zou gokken, maar dan systematisch.

Voor een product met een jaar aan kleine commits vindt dit de verantwoordelijke wijziging doorgaans in een handvol controles. Voor een product met een jaar aan enorme commits vindt het een commit met veertig bestanden, wat minder nuttig is — en dat is het praktische argument voor kleine commits, concreet gemaakt.

Twee gewoonten zorgen dat dit werkt wanneer u het nodig hebt. Commits die elk één ding doen, zodat het antwoord specifiek is. En een werkende toestand bij elke commit, zodat een commit die u neerzet ook echt draait; commits die niet draaien zijn gaten in de geschiedenis die de zoektocht breken.

Niets hiervan is geavanceerd. Het is het routinematige gebruik van een overzicht dat u al hebt, en het is het verschil tussen "het ging ergens dit voorjaar kapot" en "het ging kapot in deze wijziging, om deze reden, en hier is de fix".

## De Repository Is het Bezit

Er is een reden om dit te doen die niets met ongedaan maken te maken heeft, en oprichters lopen er meestal plotseling tegenaan.

Op een gegeven moment wil iemand weten wat u hebt gebouwd. Een investeerder die due diligence doet. Een developer die u aanneemt. Een overnemer. De technische beoordelaar van een klant. Een partner die een integratie overweegt.

Wat u hun geeft, is de repository, en wat erin zit zegt veel meer dan de code. Een geschiedenis van kleine, beschreven wijzigingen over achttien maanden leest als een product dat iemand heeft gerund. Eén commit genaamd "initial commit" van afgelopen dinsdag leest als een product zonder enige geschiedenis — en als het werk over achttien maanden is gedaan, is dat een verhaal dat verloren is gegaan in plaats van een dat nooit bestond.

Hetzelfde geldt voor overdracht. Een developer die bij een project met een leesbare geschiedenis komt, kan zien hoe het zich ontwikkelde en waarom beslissingen werden genomen. Een die bij een project zonder geschiedenis komt, heeft alleen de huidige toestand en moet alles afleiden.

En er is een praktische kant: een repository onder uw eigen account, met de geschiedenis, is wat uw product overdraagbaar maakt tussen tools, platforms en mensen. Zonder die bezit u wat er op dit moment gedeployd is, en al het andere is de regeling van iemand anders.

Dat is het sterkste argument om het op dag één in te richten in plaats van in maand vijf, en het kost een uur.

Het is voor de meeste oprichters ook het moment waarop het product als een bedrijf begint te voelen in plaats van een project — wat geen technisch voordeel is, en vaak genoeg wordt gemeld door wie het doet om het te noemen.

Er is nog een klein voordeel dat het hebben waard is: een repository maakt het mogelijk om vanaf een andere machine te werken, wat ertoe doet de eerste keer dat een laptop uitvalt en het product alleen daarop blijkt te bestaan.

En het maakt de eerste aanname eenvoudig in plaats van archeologie: wat u een nieuw persoon geeft, is een repository die hij kan klonen, met een geschiedenis die hij kan lezen.

## Dit Inrichten

Voor een oprichter die met een AI-editor werkt, is dit doorgaans een uur om op te zetten en een week om eigen te maken: een repository met alles gecommit en gepusht naar een gehoste remote, een ignore-bestand voor omgevingsbestanden, sleutels, builduitvoer en alle data, een branch voor elk stuk werk met de gewoonte om branches die misgaan te verwijderen in plaats van te redden, een commit vóór elke sessie zonder uitzondering, kleine frequente commits met berichten die de bedoeling uitleggen, een dagelijkse push, en een controle dat er niet al een geheim in de geschiedenis staat — met rotatie als dat wel zo is.

LaunchStudio richt dit in bij het overnemen van een project, en het is het eerste wat we doen, omdat niets anders veilig is zonder. De engineers zijn van Manifera — elf jaar, 120+ engineers, vanuit Amsterdam en Ho Chi Minh-stad.

[Vraag ons te controleren of uw repository een geheim in zijn geschiedenis heeft](https://launchstudio.eu/nl/#contact). Bij veel is dat zo.

## Echt voorbeeld

### Drie Dagen met de Hand Herbouwd

Karin Zoetelief bouwde Praktijkfacturatie in Cursor: facturatie voor paramedische praktijken — fysiotherapie, diëtetiek, logopedie — die de facturatie aan verzekeraars en patiënten verzorgt voor 41 praktijken.

De eerste vijf maanden werkte ze zonder versiebeheer. Het project stond in een map, geback-upt door een cloudsynchronisatie die een paar versies van afzonderlijke bestanden bewaarde.

Gevraagd om te veranderen hoe declaratiecodes van verzekeraars werden verwerkt, voerde een sessie wijzigingen door in het hele project. Het resultaat werkte niet en de fouten hadden niet duidelijk iets te maken met wat ze had gevraagd. Ze probeerde het ongedaan te maken door te prompten, wat het erger maakte, en daarna door afzonderlijke bestanden terug te zetten uit haar synchronisatiegeschiedenis, wat een mengeling van oude en nieuwe code opleverde die intern inconsistent was.

Ze herbouwde de week daarna drie dagen werk met de hand, en bleef maandenlang onzeker of er nog iets van het incident was achtergebleven.

Twee werkdagen, daarna een andere werkwijze: het project in een repository gezet met een eerste commit en gepusht naar een gehoste remote; een ignore-bestand toegevoegd voor omgevingsbestanden, builduitvoer en een map met testexports met echte patiëntgegevens, die vijf maanden naar een cloudaccount was gesynchroniseerd; twee in de map gevonden inloggegevens geroteerd; een werkwijze met een branch per wijziging ingevoerd, met verwijderen als antwoord op een slechte sessie; een regel om vóór elke sessie te committen; de wijziging van de declaratiecodes opnieuw gedaan op een branch, wat een middag kostte in plaats van een week; en een korte geschreven notitie van de werkwijze in de repository voor eigen gebruik.

**Resultaat:** in het jaar daarna gooide Karin 23 sessies weg die misgingen, elk in een paar seconden, terwijl ze eerder een week aan één was kwijtgeraakt. Ze omschrijft de regel van committen vóór elke sessie als de verandering die het gebruik van de tools comfortabel maakte in plaats van zenuwslopend.

> *"Ik heb drie dagen met de hand herbouwd omdat ik niet terug kon. De oplossing was een repository, wat een uur kostte, en ik had dat vijf maanden niet gedaan omdat het klonk als iets voor teams."*
> — **Karin Zoetelief, Oprichter, Praktijkfacturatie (Nijmegen)**

**Kosten & Doorlooptijd:** €1.300 (repository-inrichting met remote, ignore-regels, rotatie van inloggegevens na het vinden van geheimen en patiëntgegevens in de projectmap, branchwerkwijze, sessiediscipline, documentatie van de werkwijze) — afgerond in 2 werkdagen.

## Veelgestelde vragen

### Heb ik versiebeheer nodig als ik alleen werk?

Meer dan een team, wanneer een tool de code schrijft. Het is de enige manier om te zien wat er veranderde en de enige betrouwbare manier om het ongedaan te maken.

### Wat is de minimale werkwijze?

Een hoofdbranch die altijd werkt, een branch per stuk werk, een commit zodra iets werkt, een commit vóór elke sessie, en een dagelijkse push naar een gehoste remote.

### Waarom committen voordat ik een AI-sessie begin?

Zodat alles wat de tool doet met één commando ongedaan kan worden gemaakt. Niet-gecommitte wijzigingen mengen uw werk met dat van de tool, en ze achteraf scheiden is handwerk.

### Wat hoort niet in een repository?

Geheimen, builduitvoer en echte data. Een gecommit geheim blijft na verwijdering in de geschiedenis staan, dus het vinden van een geheim betekent het roteren in plaats van het bestand verwijderen.

### Wat maakt een goed commitbericht?

Eén regel die zegt wat er veranderde en, waar het niet vanzelf spreekt, waarom. Schrijf het vóór de wijziging — het verheldert het werk en houdt de commit bij één ding.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is versiebeheer nodig als u alleen werkt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Meer dan in een team wanneer een tool de code schrijft — het is de enige manier om te zien wat er veranderde en het betrouwbaar ongedaan te maken."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de minimale git-werkwijze voor een solo-oprichter?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een werkende hoofdbranch, een branch per taak, frequente commits, een commit vóór elke AI-sessie, en een dagelijkse push naar een gehoste remote."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom committen voordat u een AI-sessie begint?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zodat de wijzigingen van de sessie volledig kunnen worden weggegooid. Niet-gecommit werk mengt zich met de bewerkingen van de tool en moet met de hand worden gescheiden."
      }
    },
    {
      "@type": "Question",
      "name": "Wat mag nooit worden gecommit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Geheimen, buildartefacten en echte data. Een gecommit geheim blijft na verwijdering in de geschiedenis en moet worden geroteerd."
      }
    },
    {
      "@type": "Question",
      "name": "Wat maakt een nuttig commitbericht?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een korte regel over wat er veranderde plus waarom als dat niet vanzelf spreekt — geschreven vóór de wijziging, wat de commit ook gericht houdt."
      }
    }
  ]
}
</script>
