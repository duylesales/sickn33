---
Titel: "Dev AI-tools in Dordrecht: Het dichten van de kloof tussen prototype en productie"
Trefwoorden: dev ai, ai dev tools, productie gereedheid, hosting infrastructuur, Dordrecht
Koperfase: Overweging
Doelgroep: Technische solo-oprichter
---

# Dev AI-tools in Dordrecht: Het dichten van de kloof tussen prototype en productie

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Dev AI-tools in Dordrecht: Het dichten van de kloof tussen prototype en productie",
  "description": "Een kostenoverzicht van wat er daadwerkelijk voor nodig is voor Dordtse oprichters die dev AI-tools gebruiken om van een werkend prototype naar een betrouwbaar productieproduct te gaan.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-23",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/dev-ai-dordrecht" }
}
</script>

Wat kost het daadwerkelijk om een met dev AI gegenereerd prototype te nemen en dit om te zetten in iets dat betrouwbaar online blijft? Voor een oprichter in Dordrecht, de oudste stad van Nederland, gelegen op het kruispunt van drie rivieren en historisch gebouwd op de handel via de waterwegen, is die vraag niet abstract — het is het verschil tussen een product dat stilletjes uitvalt tijdens het drukste uur van een klant en een product dat blijft draaien.

## Wat dev AI-tools opleveren, in financiële zin

Tools zoals Lovable, Bolt, Cursor en v0 — in brede zin dev AI-tools — hebben de kosten voor het bouwen van een eerste versie van een product drastisch verlaagd. Wat vroeger een ontwikkelingsteam en tientallen duizenden euro's vereiste, kan nu door een enkele oprichter worden geprototypeerd voor de prijs van een abonnement. Dat is een echte, goed gedocumenteerde verandering. Wat deze tools niet verlagen, zijn de kosten voor het betrouwbaar draaien van dat product zodra het echte gebruikers heeft — schaalbare hosting, monitoring die problemen opvangt voordat klanten dat doen, en een uitrolproces dat geen handmatige tussenkomst vereist elke keer dat er iets verandert.

Het is de moeite waard om precies te zijn over wat "de kosten verlaagd" hier daadwerkelijk betekent, omdat het gemakkelijk verkeerd gelezen kan worden. Dev AI-tools hebben de kosten verlaagd van de *eerste* versie — de demo, de pilot, het bewijs dat een idee werkt. Ze hebben niet de kosten verlaagd van de infrastructuur die een product nodig heeft zodra het ophoudt een demo te zijn en iets wordt waar een betalende klant operationeel van afhankelijk is. Dat zijn twee verschillende producten met dezelfde interface, en ze met elkaar verwarren is precies waar oprichters in de problemen komen.

De economie van Dordrecht is altijd gevormd door haar geografie — historisch een belangrijke binnenlandse handelshaven, en vandaag de dag nog steeds de thuisbasis van een aanzienlijke concentratie logistieke, scheepvaart- en maritiem-gerelateerde bedrijven die op de waterwegen tussen de stad, Rotterdam en daarbuiten werken. Oprichters die hier tools bouwen voor die sector erven een klantenbestand dat draait op uptime: een plannings- of volgtool die uitvalt tijdens een verzendvenster is geen kleine irritatie, het is een operationeel probleem voor de klant die het gebruikt.

Die verwachting is niet onredelijk van de kant van de klant — het is simpelweg hoe de sector altijd heeft gewerkt. Een ligplaatsplanningssysteem dat een telefoontje of een marifooncontrole vervangt, is alleen een verbetering als het minstens zo betrouwbaar is als wat het verving. Op het moment dat het minder betrouwbaar is dan het handmatige proces dat een scheepvaartagent voorheen gebruikte, wordt de tool een risico in plaats van een gemak, en nieuws daarover verspreidt zich snel onder een klantenbestand dat voortdurend met elkaar spreekt over hetzelfde traject waterweg.

## Kostenoverzicht: Prototype vs. Productie

Dit is ongeveer wat een dev-AI-prototype scheidt van een productiegereed product, in termen van wat er daadwerkelijk gebouwd moet worden:

- **Hosting die schaalt:** Een enkele niet-schaalbare serverinstantie, gebruikelijk in standaard dev AI-uitrollen, kost doorgaans weinig, maar valt om bij elke echte piek in het verkeer. Een deugdelijke auto-scaling infrastructuur is een eenmalige inrichtingskost, geen grote terugkerende post.
- **Monitoring en alarmering:** Zonder dit horen oprichters van klanten over storingen. Met dit koopt een kleine inrichting een vroege waarschuwing voordat een klein probleem een groot incident wordt.
- **Een echte uitrolpijplijn (CI/CD):** Handmatige uitrollen zijn gratis totdat de eerste slechte uitrol tot stilstand leidt; een deugdelijke CI/CD-pijplijn is een bescheiden vaste kost die dat risico permanent wegneemt.
- **Database-veerkracht:** Back-ups en failover zijn niet zichtbaar in een demo, maar ze zijn het verschil tussen een slechte dag en een bedrijfsbedreigend incident met gegevensverlies.

Zoals Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera, het verwoordt: "De uitdaging is niet langer het omzetten van goede ideeën in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot wasdom te brengen." Voor een Dordtse oprichter die logistieke en scheepvaartklanten bedient die uptime als uitgangspunt verwachten, is dat architectuurwerk geen optionele afwerking — het is het daadwerkelijke product.

De prijzen van LaunchStudio voor dit type productie-gereedheidswerk liggen tussen € 800 en € 7.500 als vast omlijnd traject, ongeveer een vijfde van wat een traditioneel ontwikkelbureau zou rekenen voor dezelfde infrastructuuruitbouw. LaunchStudio wordt aangedreven door Manifera, met een klantgericht kantoor aan de Herengracht 420 in Amsterdam en ruim 160 opgeleverde projecten achter zich, waaronder werk voor klanten zoals Statler BI en Maployer. U kunt [rechtstreeks contact opnemen](https://launchstudio.eu/en/#contact) om het specifieke gat tussen prototype en productie voor uw situatie in te schatten, en het [web application development](https://www.manifera.com/services/web-app-develop/) werk van Manifera laat dezelfde infrastructuurdiscipline zien over een reeks van klantgrootten.

## Hoe u uw eigen uitvalrisico inschat voordat het gebeurt

De meeste oprichters plakken nooit een getal op wat een storing hen daadwerkelijk kost, wat het gemakkelijk maakt om infrastructuurwerk voor onbepaalde tijd te blijven uitstellen. Een globale schatting, eerlijk uitgevoerd, verandert die berekening meestal snel.

**Een eenvoudige manier om er een getal op te plakken**

1. Tel hoeveel actieve klanten afhankelijk zijn van de bereikbaarheid van uw product tijdens hun werkuren
2. Schat welk percentage van die klanten een storing van twee uur tijdens een normale werkdag zou opmerken, vergeleken met een storing die 's nachts plaatsvindt
3. Vermenigvuldig dat met wat een enkele verloren of ernstig beschadigde klantrelatie daadwerkelijk waard is — niet alleen de maandelijkse abonnementsprijs, maar de aanbevelings- en reputatiekosten in een kleine, genetwerkte lokale markt

Voor een logistiek-gerelateerde tool die wordt gebruikt door scheepvaartagenten rond de waterwegen van Dordrecht, ligt dat getal doorgaans hoger dan oprichters aanvankelijk schatten, juist omdat de klanten afhankelijk zijn van de tool tijdens specifieke, tijdgevoelige operationele vensters in plaats van het passief gedurende de dag te gebruiken. Een gemist verzendvenster heeft ook stroomafwaartse kosten voor de klant — een vertraagde ligplaatstoewijzing kan doorwerken in liggeldkosten (demurrage) of een gemiste aansluiting verderop in de toeleveringsketen, wat precies het soort consequentie is dat een softwarestoring verandert in een echt duur telefoontje.

**Signalen dat uw huidige inrichting de veilige capaciteit al voorbij is**

- Uw server vertraagt af en toe merkbaar tijdens de drukste uren, zelfs als deze nog niet volledig is uitgevallen
- U heeft nooit daadwerkelijk getest wat er gebeurt onder een echte piek in het verkeer, alleen onder normaal dagelijks gebruik
- U zou van een telefoontje van een klant horen over een storing, niet van een geautomatiseerde melding, omdat er geen monitoring bestaat

**Wat er verandert zodra u een echt getal heeft**

Een oprichter die berekent dat een enkele slechte storing aannemelijk twee klantrelaties ter waarde van € 15.000 aan jaarlijkse omzet zou kunnen kosten, kijkt heel anders naar een infrastructuurinvestering van € 1.500–€ 2.000 dan iemand die de rekensom nooit heeft gemaakt. De investering verandert niet — de ervaren urgentie wel, wat doorgaans de werkelijke reden is waarom dit werk in de eerste plaats wordt uitgesteld. Het eenmalig, eerlijk uitvoeren van deze rekensom is meestal het moment waarop een oprichter stopt met het behandelen van infrastructuur als een project voor ooit, en het begint te behandelen als de belangrijkste engineeringbeslissing van dit kwartaal.

## Echt voorbeeld

### Een AI-Native Oprichter in Actie: De storing van Dockflow door een enkele serverinstantie

Eva Mulder bouwde Dockflow in Dordrecht met Lovable — een tool voor ligplaatsplanning en cargo-handoff coördinatie voor kleine scheepvaartagenten die op de rivieren rond de stad werken. Het lanceerde strak en kreeg binnen de eerste twee maanden vier regionale scheepvaartagenten als vroege gebruikers, gehost op een enkele niet-schaalbare serverinstantie die tijdens het testen prima had gewerkt.

Tijdens een week met ongewoon druk scheepvaartverkeer bereikte de server zijn limiet en ging gedurende vier uur zonder enige waarschuwing offline — er was geen monitoring ingericht, dus Eva kwam erachter toen twee agenten belden met de vraag waarom ze mid-operatie geen toegang hadden tot hun ligplaatsplanningen. Er was ook geen uitrolpijplijn, wat betekende dat de spoed-fix die ze pushte om de server weer online te krijgen handmatig, live en zonder tussentijdse teststap moest worden uitgevoerd.

**Resultaat:** LaunchStudio verplaatste Dockflow naar auto-scaling infrastructuur, voegde uptime-monitoring met realtime alarmering toe en bouwde een CI/CD-pijplijn met een staging-omgeving. Het product heeft in de vier maanden sinds de aanpassing nul ongeplande uitval gehad.

> *"Vier uur klinkt niet als veel, totdat het vier uur is tijdens een daadwerkelijk verzendvenster en twee klanten je tegelijkertijd bellen."*
> — **Eva Mulder, Oprichter, Dockflow (Dordrecht)**

**Kosten & Doorlooptijd:** € 1.850 (migratie naar auto-scaling, inrichting monitoring, CI/CD-pijplijn) — afgerond in 6 werkdagen.

---

## Veelgestelde vragen

### Hoeveel kost het dichten van de kloof tussen prototype en productie doorgaans?
De meeste projecten vallen binnen de vaste prijsklasse van LaunchStudio tussen € 800 en € 7.500, afhankelijk van de omvang, wat ongeveer een vijfde is van de prijzen van traditionele bureaus voor vergelijkbaar infrastructuurwerk.

### Is Dordrecht niet een te kleine markt voor dit type toegewijde productiewerk?
Nee. LaunchStudio werkt met oprichters in heel Nederland en de Benelux, ongeacht de stadsomvang, en de logistiekzware zakelijke basis van Dordrecht past uitstekend bij het hier beschreven werk gericht op uptime.

### Wat bedoelde Herre Roelevink over architectuur als de echte uitdaging nu?
Hij beschrijft een verandering waarbij AI-tools het probleem van het snel bouwen van software hebben opgelost, waardoor het moeilijkere, minder zichtbare werk — beveiliging en productie-architectuur — overblijft als wat daadwerkelijk bepaalt of een product overleeft.

### Is er doorlopende ondersteuning na de eerste productie-fix, of is het een eenmalige opdracht?
LaunchStudio biedt een optionele aanvullende ondersteuning aan voor € 49/maand voor oprichters die voortdurende monitoring en onderhoud willen nadat het eerste productie-gereedheidswerk is afgerond.

### Wie bouwt deze infrastructuur daadwerkelijk — wordt het uitbesteed aan willekeurige freelancers?
Nee. Het wordt gebouwd door het eigen engineeringteam van Manifera met meer dan 120 engineers, hetzelfde team achter meer dan 160 opgeleverde projecten voor enterprise-klanten waaronder Vodafone, TNO en Statler BI.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Hoeveel kost het dichten van de kloof tussen prototype en productie doorgaans?", "acceptedAnswer": { "@type": "Answer", "text": "De meeste projecten vallen binnen LaunchStudio's vaste prijsklasse van € 800 tot € 7.500, ongeveer een vijfde van traditionele bureauprijzen." } },
    { "@type": "Question", "name": "Is Dordrecht niet een te kleine markt voor dit type toegewijde productiewerk?", "acceptedAnswer": { "@type": "Answer", "text": "Nee. LaunchStudio werkt met oprichters in heel Nederland en de Benelux ongeacht stadsgrootte." } },
    { "@type": "Question", "name": "Wat bedoelde Herre Roelevink over architectuur als de echte uitdaging nu?", "acceptedAnswer": { "@type": "Answer", "text": "Hij beschrijft dat AI-tools het snel bouwen van software hebben opgelost, waardoor beveiliging en productie-architectuur de echte overlevingsfactor worden." } },
    { "@type": "Question", "name": "Is er doorlopende ondersteuning na de eerste productie-fix, of is het een eenmalige opdracht?", "acceptedAnswer": { "@type": "Answer", "text": "LaunchStudio biedt een optionele ondersteuning aan voor € 49/maand voor voortdurende monitoring en onderhoud." } },
    { "@type": "Question", "name": "Wie bouwt deze infrastructuur daadwerkelijk — wordt het uitbesteed aan willekeurige freelancers?", "acceptedAnswer": { "@type": "Answer", "text": "Het wordt gebouwd door het eigen engineeringteam van Manifera met meer dan 120 engineers, achter 160+ projecten voor klanten als Vodafone en TNO." } }
  ]
}
</script>
