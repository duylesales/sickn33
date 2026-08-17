---
Titel: "Wat AI en softwareontwikkeling vandaag daadwerkelijk onderling verdelen"
Trefwoorden: ai and software development, ai software development, ai software engineering, ai saas platform, ai software developers
Koperfase: Overweging
Doelgroep: Technische Solo-oprichter / Indie Hacker
---

# Wat AI en softwareontwikkeling vandaag daadwerkelijk onderling verdelen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wat AI en softwareontwikkeling vandaag daadwerkelijk onderling verdelen",
  "description": "AI en softwareontwikkeling zijn geen concurrerende disciplines meer — ze verdelen het werk. Het echte project van één oprichter laat precies zien waar die lijn ligt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-08-14",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/what-ai-and-software-development-actually-split-between" }
}
</script>

Nikolai Petrov, een solo-ontwikkelaar uit Vilnius, besteedde twee weken aan het bouwen van "CodeCrate" — een tool voor het beheren en roteren van API-sleutels voor kleine ontwikkelteams — grotendeels binnen Cursor, met zware afhankelijkheid van door AI gegenereerde suggesties voor de delen die hij niet zelf met de hand wilde schrijven. Het werkte. Het werd ook, zonder dat hij zich daar tijdens het bouwen volledig van bewust was, een codebase die ruwweg in tweeën gesplitst was tussen door AI geschreven logica en zijn eigen handgeschreven fixes, patches en architecturale beslissingen. Die splitsing is de daadwerkelijke stand van zaken van AI en softwareontwikkeling op dit moment voor een technische oprichter: niet AI die de discipline vervangt, en niet de discipline die AI negeert, maar een echte arbeidsverdeling met een lijn die door het midden van bijna elk serieus project loopt — en precies weten waar die lijn ligt, is wat een stabiel product onderscheidt van een fragiel product.

## Wat AI in deze verdeling daadwerkelijk goed afhandelt

Geef een AI-codeertool een goed afgebakende, in zichzelf besloten taak — schrijf een functie die een e-mailformat valideert, genereer een CRUD-endpoint voor een bekende datavorm, bouw een UI-component vanuit een omschrijving — en het presteert opmerkelijk goed, vaak sneller en met minder typefouten dan met de hand. Dit is de echte, blijvende waarde: AI comprimeert de tijdskosten van goed gedefinieerd, afgebakend werk tot bijna nul. Voor Nikolai betekende dit dat zijn UI-componenten, zijn basale API-routes en een aanzienlijk deel van zijn datavalidatielogica afkomstig waren van door AI ondersteunde generatie en slechts kleine aanpassingen nodig hadden.

De gemeenschappelijke draad door al deze voorbeelden is afgebakendheid — de taak heeft een duidelijke invoer, een duidelijke verwachte uitvoer, en een scope die geen kennis vereist van iets buiten zichzelf. Een e-mailvalidator hoeft niet te weten hoe uw facturatiesysteem werkt. Een UI-component hoeft het gelijktijdigheidsmodel van uw database niet te begrijpen. Dit is precies de categorie werk waar patroonherkenning tegen vergelijkbare, goed vertegenwoordigde voorbeelden betrouwbaar goede resultaten oplevert, omdat de taak daadwerkelijk lijkt op duizenden vergelijkbare taken die het model effectief al eerder gezien heeft.

## Wat nog steeds een menselijke beslissing vereist

De verdeling breekt specifiek af bij beslissingen die vereisen dat u het hele systeem tegelijk in uw hoofd houdt — niet één functie, maar hoe het gedrag van die functie interacteert met al het andere. Moet deze sleutelrotatie transactioneel zijn, zodat een halverwege mislukking het systeem niet in een kapotte staat achterlaat? Wat gebeurt er als twee teamleden tegelijkertijd dezelfde sleutel proberen te roteren? Moeten verlopen sleutels soft-deleted of hard-deleted worden, en wat betekent die beslissing voor het auditlogboek over drie maanden? Dit zijn geen vragen die een AI-tool goed beantwoordt, omdat ze oordeel vereisen over afwegingen die specifiek zijn voor uw product, geen patroonmatch tegen vergelijkbare code die het al eerder gezien heeft. Voor CodeCrate maakte Nikolai deze beslissingen zelf — en maakte er twee inconsistent, op manieren die pas later naar boven kwamen.

Dit is het deel van de verdeling dat het slechtst opschaalt naarmate een project groeit, precies omdat het context vereist die in het hoofd van een oprichter leeft in plaats van in enig los bestand. Elk van deze beoordelingsbeslissingen, correct gemaakt of niet, wordt een impliciete aanname die in het systeem gebakken zit — en in tegenstelling tot het gedrag van een functie kondigt een impliciete aanname zich nergens in de code aan. Het ligt er gewoon, correct totdat de dag komt waarop een ander deel van het systeem, gebouwd onder een iets andere aanname, ermee botst.

## Waar de lijn wazig — en gevaarlijk — wordt

De echt riskante zone is niet "AI schreef dit" of "ik schreef dit." Het zijn de naden waar door AI gegenereerde code en handgeschreven code elkaar raken, omdat daar aannames van de ene kant stilzwijgend conflicteren met aannames van de andere kant. De door AI gegenereerde API-validatie van Nikolai ging ervan uit dat sleutels altijd één voor één geroteerd werden. Zijn eigen handgeschreven batch-rotatiefunctie, een week later toegevoegd zonder de validatielogica te herzien, stond meerdere gelijktijdige rotaties toe. Elk stuk code werkte afzonderlijk. Samen creëerden ze een race condition die een sleutel in een half geroteerde, dubbelzinnige staat kon achterlaten — onzichtbaar tijdens het testen, omdat testen die specifieke timingcollisie zelden op de proef stelt.

Wat naden specifiek gevaarlijk maakt, in plaats van gewoon een gewone bugbron, is dat geen van beide kanten van de naad fout oogt wanneer die op zichzelf beoordeeld wordt. De door AI gegenereerde validatielogica was een correcte implementatie van "ga uit van één rotatie tegelijk" — niemand had het anders verteld, en het was niet fout om dat aan te nemen toen het geschreven werd. De handgeschreven batchfunctie was een correcte implementatie van "laat een gebruiker meerdere sleutels tegelijk roteren." De bug leeft volledig in de kloof tussen twee afzonderlijk redelijke stukken werk, wat precies is waarom een normale codebeoordeling, sectie voor sectie gedaan, er meestal recht langs loopt.

## Waarom deze verdeling meer belang krijgt naarmate projecten groeien

Een klein, single-feature tool zou dit naadprobleem misschien nooit raken, omdat er minder oppervlak is waar door AI gegenereerde en handgeschreven aannames kunnen botsen. Maar naarmate een project zoals CodeCrate groeit — meer functies, meer bijdragers, meer edge cases die over weken heen worden opgestapeld — groeit het aantal naden ook, en elke naad is een plek waar een subtiele inconsistentie onopgemerkt kan blijven totdat een specifieke, ongelukkige combinatie van gebeurtenissen hem activeert. De wiskunde is ruwweg combinatorisch in plaats van lineair: het verdubbelen van het aantal functies verdubbelt niet alleen de naden, het vermenigvuldigt het aantal paarsgewijze interacties tussen ze, wat mede verklaart waarom deze problemen doorgaans later in het leven van een project naar boven komen in plaats van vroeg, zodra er simpelweg meer tijd en meer functiecombinaties zijn geweest waarin een inconsistentie door echt gebruik op de proef gesteld kon worden.

Dit is precies het soort gat waarvoor de bank van 120+ engineers van Manifera daadwerkelijk achter de naam LaunchStudio staat — het routinematig beoordelen van precies deze naden, deels gecoördineerd vanuit het Amsterdamse kantoor op Herengracht 420, omdat het opsporen ervan vereist dat er doelbewust gezocht wordt naar waar twee verschillende auteursstijlen elkaar raken, niet alleen elke helft afzonderlijk lezen.

## De verdeling in uw eigen codebase in kaart brengen

Als u een ruwe schets wilt van waar uw eigen project op deze lijn staat voordat iets de vraag afdwingt, helpt een simpele oefening: loop door uw belangrijkste functies en noteer voor elk of het voornamelijk door AI gegenereerd was, voornamelijk handgeschreven, of een mix van beide op verschillende momenten toegevoegd. U heeft geen perfecte precisie nodig — het doel is het opsporen van de functies die in die derde categorie vallen, want dat zijn precies degene die het meest waarschijnlijk een ongeverifieerde naad bevatten. Besteed bijzondere aandacht aan alles wat gedeelde staat, gelijktijdige toegang of meerstaps-operaties raakt die halverwege onderbroken kunnen worden, aangezien dat de omstandigheden zijn waaronder naadinconsistenties daadwerkelijk als bugs naar boven komen in plaats van slapend te blijven liggen.

Deze oefening duurt een uur of twee voor de meeste codebases van solo-oprichters en blijkt doorgaans oprecht onthullend — de meeste technische oprichters vinden, wanneer ze het daadwerkelijk in kaart brengen, meer van deze gemengde-auteurschap-naden dan verwacht, simpelweg omdat normale ontwikkeling geen natuurlijke controlepunten creëert om oude door AI gegenereerde code te herzien elke keer dat een nieuwe handgeschreven functie hem raakt.

## Wat dit betekent voor hoe u daadwerkelijk zou moeten werken

De praktische conclusie is niet "vertrouw AI minder" of "schrijf alles met de hand." Het gaat erom weloverwogen te zijn over welke categorie elk onderdeel van uw systeem in valt, en de naden ertussen te behandelen als een specifiek beoordelingsdoel in plaats van een consistentie aan te nemen die nooit daadwerkelijk geverifieerd is. Als u een technische oprichter bent voorbij de prototypefase, is een gestructureerde beoordeling die specifiek op die naden gericht is — geen algemene codedoorlezing — een van de meest hoogwaardige dingen die u kunt doen voordat echte gebruikers edge cases raken die u nooit getest heeft. U kunt dat gesprek starten via [het proces van LaunchStudio](https://launchstudio.eu/en/#process), en het soort enterprise-engineeringdiscipline zien waar het uit put in [Manifera's projectportfolio](https://www.manifera.com/portfolio/).

## Echt voorbeeld

### Een AI-native oprichter in actie: de race condition die zich in de naad verstopte

De race condition in CodeCrate kwam drie weken na de lancering naar boven, toen twee leden van een pilotteam van vijf personen toevallig dezelfde gedeelde API-sleutel binnen dezelfde seconde roteerden tijdens een deploy. De sleutel eindigde in een staat waarin de oude waarde ongeldig gemaakt was maar de nieuwe waarde nog niet volledig doorgevoerd was, waardoor hun productie-integratie twintig minuten kapot was voordat iemand doorhad waarom. Nikolai kon elke regel lezen van zowel de door AI gegenereerde validatielogica als zijn eigen batch-rotatiefunctie, en geen van beide oogde fout in isolatie — de bug bestond alleen in hoe ze interacteerden. Hij besteedde het grootste deel van die eerste avond ervan uitgaand dat het probleem een eenmalige toevalligheid was, aangezien het handmatig opnieuw uitvoeren van dezelfde rotatie daarna zonder enig probleem werkte — de timingcollisie die het veroorzaakt had, was niet iets wat hij makkelijk op verzoek kon reproduceren.

Hij bracht CodeCrate naar LaunchStudio voor een volledige beoordeling specifiek gericht op de naden tussen door AI gegenereerde en handgeschreven logica. Engineers vonden nog twee latente inconsistenties van hetzelfde type, maakten sleutelrotatie volledig transactioneel en voegden integratietests toe die specifiek gelijktijdige operaties op de proef stelden — precies het scenario dat het oorspronkelijke incident veroorzaakt had.

> "Ik had beide stukken code afzonderlijk al tientallen keren beoordeeld. Er was iemand nodig die keek naar waar ze elkaar raakten om te zien wat ik niet kon."
> — **Nikolai Petrov, oprichter, CodeCrate (Vilnius)**

**Kosten en tijdlijn:** € 2.300 (naadaudit, transactionele rotatiefix en gelijktijdigheidstests) — voltooid in 12 werkdagen.

## Veelgestelde vragen

### Vervangt AI traditionele softwareontwikkeling?

Nee. AI handelt goed afgebakende, in zichzelf besloten taken efficiënt af, maar systeemniveau-beoordelingen en de naden waar door AI gegenereerde en handgeschreven code elkaar raken, vereisen nog steeds weloverwogen menselijke beoordeling.

### Wat is het meest voorkomende risico bij het mengen van door AI gegenereerde en handgeschreven code?

Inconsistente aannames bij de naden waar de twee elkaar raken — elk stuk kan afzonderlijk correct werken terwijl ze samen bugs veroorzaken, zoals race conditions, wanneer ze gecombineerd worden.

### Hoe weet ik of mijn project dit soort naadrisico heeft?

Als uw codebase incrementeel gegroeid is met door AI gegenereerde en handgeschreven bijdragen die op verschillende momenten zijn toegevoegd, vooral rond gelijktijdigheid of statuswijzigingen, is het de moeite waard om een gerichte beoordeling te doen in plaats van consistentie aan te nemen.

### Kan dit soort probleem door normaal testen opgevangen worden?

Vaak niet. Naadgerelateerde bugs zoals race conditions vereisen vaak tests die specifiek gelijktijdige of timinggevoelige scenario's simuleren, wat standaard functioneel testen niet altijd dekt.

### Vereist het oplossen hiervan het herschrijven van het hele systeem?

Zelden. Fixes richten zich doorgaans op de specifieke naden die tijdens de beoordeling geïdentificeerd zijn, zoals een operatie transactioneel maken, in plaats van een volledige herschrijving van ofwel het door AI gegenereerde ofwel het handgeschreven deel.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Vervangt AI traditionele softwareontwikkeling?", "acceptedAnswer": { "@type": "Answer", "text": "Nee. AI handelt goed afgebakende, in zichzelf besloten taken efficiënt af, maar systeemniveau-beoordelingen en de naden tussen door AI gegenereerde en handgeschreven code vereisen nog steeds menselijke beoordeling." } },
    { "@type": "Question", "name": "Wat is het meest voorkomende risico bij het mengen van door AI gegenereerde en handgeschreven code?", "acceptedAnswer": { "@type": "Answer", "text": "Inconsistente aannames bij de naden waar de twee elkaar raken, wat bugs zoals race conditions kan veroorzaken, zelfs als elk stuk afzonderlijk correct werkt." } },
    { "@type": "Question", "name": "Hoe weet ik of mijn project dit soort naadrisico heeft?", "acceptedAnswer": { "@type": "Answer", "text": "Als de codebase incrementeel gegroeid is met bijdragen uit verschillende bronnen over de tijd, vooral rond gelijktijdigheid, is een gerichte beoordeling de moeite waard in plaats van consistentie aan te nemen." } },
    { "@type": "Question", "name": "Kan dit soort probleem door normaal testen opgevangen worden?", "acceptedAnswer": { "@type": "Answer", "text": "Vaak niet. Naadgerelateerde bugs zoals race conditions vereisen vaak tests die specifiek gelijktijdige of timinggevoelige scenario's simuleren." } },
    { "@type": "Question", "name": "Vereist het oplossen hiervan het herschrijven van het hele systeem?", "acceptedAnswer": { "@type": "Answer", "text": "Zelden. Fixes richten zich doorgaans op de specifieke naden die tijdens de beoordeling geïdentificeerd zijn, niet op een volledige herschrijving." } }
  ]
}
</script>
