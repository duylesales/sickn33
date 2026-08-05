---
Titel: "Cursor's automatisch aanvulvertrouwen is niet hetzelfde als productievertrouwen"
Trefwoorden: ai code tool, bolt ai, cursor autocomplete, ai code review, permission check bug
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie Hacker
---

# Cursor's automatisch aanvulvertrouwen is niet hetzelfde als productievertrouwen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cursor's automatisch aanvulvertrouwen is niet hetzelfde als productievertrouwen",
  "description": "Cursor's automatische aanvulling aarfelt nooit, zelfs wanneer het verkeerd is.",
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
    "@id": "https://launchstudio.eu/en/blog/cursor-autocomplete-confidence-vs-production-confidence"
  }
}
</script>

Cursor typt een suggestie nooit aarzelend. Het indekt zich niet in, markeert geen onzekerheid, en zegt niet "dit is mogelijk verkeerd voor uitzonderingsgevallen". Elke automatische aanvulling komt aan met een uiterlijk dat exact even zelfverzekerd is als elke andere, of het nu een triviale getter-functie is of een machtigingscontrole die bepaalt wie gevoelige gegevens kan zien. Dat uniforme vertrouwen is het daadwerkelijke gevaar – niet dat Cursor fouten maakt (elke tool doet dat), maar dat zijn fouten er identiek uitzien aan zijn correcte suggesties. En een ontwikkelaar die code doorneemt onder tijdsdruk heeft geen visuele of tekstuele aanwijzing die hem vertelt welke welke is.

## De specifieke manier van mislukken: aannemelijk, en niet correct

Vraag een ervaren ingenieur wat door AI gesuggereerde code gevaarlijk maakt, en het eerlijke antwoord is doorgaans niet "het produceert gebroken code die duidelijk niet werkt". Gebroken code wordt onmiddellijk opgevangen – het werpt een foutmelding op, faalt voor een test, of compileert niet. De gevaarlijke categorie is code die *aannemelijk* is – syntactisch schoon, logisch coherent bij een eerste lezing, consistent met de patronen die al in het bestand zitten – terwijl het subtiel verkeerd is op een manier die zich alleen manifesteert onder een specifieke voorwaarde die niemand toevallig heeft getest. Machtigings- en autorisatielogica is een van de plekken met het hoogste risico voor exact dit patroon, omdat het aantal rolcombinaties snel groeit. En een controle die de drie meest voorkomende combinaties tijdens de ontwikkeling correct afhandelt kan nog steeds verkeerd zijn voor de vierde die alleen verschijnt zodra echte gebruikers met echte roltoewijzingen het product beginnen te gebruiken.

Dit is geen kritiek die uniek is voor Cursor – Bolt, Lovable en elke andere AI-coderingsassistent dragen hetzelfde structurele risico. Maar het is in het bijzonder relevant voor technische solo-oprichters die specifiek Cursor gebruiken, omdat Cursor's werkwijze gebouwd is rond snelle, inline automatische aanvullingen die geaccepteerd worden met één toetsslag. Dat is een fundamenteel sneller beoordelingsmoment met minder wrijving dan het beoordelen van een groter door AI gegenereerd blok code dat gekopieerd is uit een chat-interface. De snelheid is de gehele waardepropositie van inline automatische aanvulling. Het is ook exact waarom een subtiel verkeerde suggestie waarschijnlijker is om er doorheen te glippen: er is minder natuurlijke pauze ingebouwd in de werkwijze voor controle.

## Waarom een snelle doorlezing dit niet opvangt

Een bug in een machtigingscontrole die alleen faalt onder één specifieke rolcombinatie is, door zijn constructie, onzichtbaar voor een snelle doorlezing. Het is vaak ook onzichtbaar voor handmatig testen, tenzij iemand specifiek die exacte combinatie construeert en test. Tijdens de ontwikkeling test een oprichter die zijn eigen product test doorgaans als zichzelf – één rol, misschien twee als hij een tweede testaccount heeft ingesteld. De bug kondigt zichzelf in geen van beide aan. Het wacht op een echt productiescenario: een gebruiker die toevallig twee rollen gelijktijdig bezit, of een machtiging geërfd via een teamstructuur die geen onderdeel was van de oorspronkelijke testmatrix. Alleen dan weigert de onjuiste controle ofwel toegang aan iemand die toegang zou moeten hebben, of, erger nog, verleent het toegang aan iemand die het niet zou moeten hebben.

Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera, verwoordt het zo: "We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer het omzetten van goede ideeën in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot wasdom te brengen. We hebben elf jaar ervaring in exact dat." Machtigingslogica is een precies voorbeeld van deze verschuiving – Cursor loste op "kan ik snel een rolcontrole schrijven", maar niemand loste op "dekt deze rolcontrole op de juiste manier elke combinatie die in productie zal bestaan", omdat dat een systematisch beoordelingsproces vereist, en niet alleen een werkende suggestie.

## Wat deze kloof sluit

De herstelling is niet het wantrouwen van Cursor in het algemeen – zijn automatische aanvulling is oprecht nuttig en krijgt het grote merendeel van de suggesties goed. De herstelling is het toepassen van bewust hogere controle op specifieke categorieën van code waar een subtiele fout onevenredige gevolgen heeft: authenticatie, autorisatie, betalingslogica, en alles wat de grenzen van gegevenstoegang raakt. Voor deze categorieën is een snelle doorlezing niet voldoende; ze hebben een expliciete testmatrix nodig die elke realistische rol- en machtigingscombinatie dekt, en niet alleen de twee of drie die gebruikt worden tijdens normale ontwikkeling. Onze ingenieurs, werkend vanuit Manifera's hub in Singapore, passen exact dit soort doelgerichte beoordeling toe wanneer ze een met AI gebouwde codebase auditeren voordat deze naar productie gaat – niet elke regel met gelijke intensiteit beoordelen, maar controle concentreren op de categorieën van code waar "aannemelijk maar verkeerd" reële schade veroorzaakt.

Als u een beoordeling van machtigingen en toegangsbeheer wilt laten uitvoeren op een met Cursor gebouwd product voordat meer gebruikers er afhankelijk van worden, legt onze [hoe het werkt](https://launchstudio.eu/en/#process)-pagina uit hoe LaunchStudio dat soort audit omvangt. En Manifera's praktijk voor [maatwerk softwareontwikkeling](https://www.manifera.com/services/custom-software-development/) heeft vergelijkbare autorisatiebeoordelingen uitgevoerd voor enterprise-systemen met aanzienlijk meer rolcomplexiteit dan een typisch SaaS-product in een vroeg stadium.

## Een testmatrix beschermt u slechts één keer, tenzij deze geautomatiseerd is

Het bouwen van de testmatrix voor rolcombinaties herstelt de bug die werd gevonden, maar het stopt de volgende niet om op dezelfde manier te arriveren. Cursor zal zelfverzekerd automatische aanvullingen blijven suggereren in de buurt van diezelfde machtigingslogica elke keer dat het product veranderd – er wordt een nieuwe rol toegevoegd, een ticketveld krijgt een nieuwe zichtbaarheidsregel, een gerelateerde functie wordt gerefactord. En elk van die momenten is een verse kans voor een aannemelijke-maar-verkeerde suggestie om voorbij een snelle beoordeling te glippen, exact zoals de eerste deed. Een testmatrix die bestaat als een document waar iemand één keer handmatig doorheen liep nadat de oorspronkelijke bug werd gevonden vangt niets daarvan op. Het bewijst alleen dat de bug die al bekend was is hersteld.

De matrix levert zijn waarde pas op zodra het stopt met een handmatige checklist te zijn en een geautomatiseerde testsuite wordt die draait bij elke wijziging die de machtigingslogica raakt, zodat een nieuwe suggestie door dezelfde combinaties moet slagen als de vorige voordat het productie kan bereiken:

```
test: support-agent + department-lead kan toegewezen ticket bekijken
test: support-agent + department-lead kan toegewezen ticket oplossen
test: admin + support-agent erft volledige ticket-zichtbaarheid
test: regular-user + department-lead kan eigenschapscontrole van ticket niet omzeilen
```

Aangesloten op de uitrolpijplijn draaien deze automatisch bij elke relevante wijziging in plaats van af te hangen van iemand die er aan denkt om ze handmatig opnieuw te controleren.

## Echt voorbeeld

### Een AI-native oprichter in actie: De rolcombinatie die niemand heeft getest

Twan Buitenhuis, een technische solo-oprichter in Coevorden, bouwde TicketVolg – een interne IT-ticketingtool – met behulp van Cursor. Tijdens het implementeren van toegangscontroles voor wie tickets kon bekijken en oplossen, suggereerde Cursor's automatische aanvulling zelfverzekerd een machtigingscontrole die er correct uitzag en exact overeenkwam met het patroon van de omringende code.

De suggestie slaagde voor Twan's eigen snelle doorlezing tijdens de ontwikkeling, en het slaagde ook voor zijn handmatige testen, omdat zijn testen de standaard rolcombinaties dekte die hij verwachtte dat er toe deden: normale gebruikers, beheerders en ondersteuningsagenten, individueel getest. De controle was subtiel verkeerd specifiek voor één combinatie – een gebruiker die zowel een ondersteuningsagent-rol als een afdelingshoofd-rol gelijktijdig bezat – een combinatie die niet bestond in Twan's testaccounts, maar wel bestond onder zijn daadwerkelijke vroege gebruikers zodra TicketVolg in echt gebruik ging. Die combinatie zorgde ervoor dat de machtigingscontrole onterecht toegang weigerde tot tickets die de gebruiker had moeten kunnen zien.

LaunchStudio's ingenieurs beoordeelden TicketVolg's volledige machtigingssysteem, en niet alleen de gemarkeerde controle. We bouwden een correcte testmatrix voor rolcombinaties die elke realistische koppeling van rollen dekt in plaats van alleen de individueel geteste koppelingen die Twan had gecontroleerd. De gemarkeerde machtigingslogica werd herschreven om gecombineerde rollen correct te evalueren. En de nieuwe testmatrix draait nu als onderdeel van elke toekomstige wijziging aan het toegangsbeheersysteem, zodat een vergelijkbare kloof productie niet meer onopgemerkt kan bereiken.

**Resultaat:** TicketVolg's machtigingssysteem handelt nu elke realistische rolcombinatie correct af. Twan heeft een daadwerkelijke testmatrix in plaats van te vertrouwen op een snelle handmatige controle voordat hij wijzigingen in het toegangsbeheer verzendt.

> *"De code zag er exact even zelfverzekerd uit als al het andere wat Cursor die week had gesuggereerd. Er was niets aan dat zei 'controleer deze dubbel'."*
> — **Twan Buitenhuis, Oprichter, TicketVolg (Coevorden)**

**Kosten en tijdlijn:** € 900 (beoordeling van het machtigingssysteem, testmatrix voor rolcombinaties, en herstelling van de gemarkeerde bug in het toegangsbeheer) — voltooid in 5 werkdagen.

---

## Veelgestelde vragen

### Moet ik stoppen met het gebruiken van Cursor's automatische aanvulling voor gevoelige logica?

Niet noodzakelijkerwijs – de automatische aanvulling zelf is een oprecht nuttige tool. De herstelling is het toepassen van bewustere controle specifiek op categorieën zoals authenticatie en machtigingen, in plaats van te vertrouwen op een snelle doorlezing zoals u dat zou doen bij code met een lagere inzet.

### Hoe bouw ik een testmatrix voor rolcombinaties als ik dat nog nooit heb gedaan?

Begin met het vermelden van elke rol of machtiging die uw product heeft, en test vervolgens expliciet elke realistische combinatie van twee of meer rollen die een echte gebruiker gelijktijdig zou kunnen bezitten, en niet alleen elke rol alleen getest.

### Wie voert dit soort machtigingsbeoordelingen uit bij LaunchStudio?

De beoordeling wordt uitgevoerd door Manifera's engineeringteam, inclusief de groep gevestigd in de hub in Singapore, gebruikmakend van hetzelfde systematische proces voor het testen van toegangsbeheer dat wordt toegepast bij Manifera's enterprise-trajecten.

### Zodra een machtigingsbug is hersteld en getest, kan deze dan terugkomen?

Ja, als de testmatrix een eenmalige handmatige controle blijft – elke toekomstige wijziging in de buurt van die machtigingslogica is een verse kans voor een vergelijkbare kloof om er doorheen te glippen. Daarom moet de matrix draaien als een geautomatiseerde test bij elke relevante wijziging.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom is Cursor inline autocomplete gevaarlijk bij autorisatie-logica?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cursor oppert code met 100% visuele zekerheid. Subtiele bugs (bijv. een rolen-combinatie check die faalt bij gecombineerde rollen) zien er exact zo strak uit als correcte code."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe ontdek je autorisatie-bugs die door AI zijn ingevoerd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Door een expliciete rol-combinatie matrix te bouwen en te testen (bijv. wat gebeurt er als een gebruiker GELIJKTIJDIG 'support agent' en 'afdelingshoofd' is?)."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom is handmatig testen van autorisatie niet voldoende?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat founders meestal maar 1 of 2 standaard rollen testen met hun eigen testaccounts. Zodra echte gebruikers meerdere rollen combineren, breekt het systeem."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe zorg je dat autorisatie-checks niet opnieuw breken bij nieuwe AI-prompts?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zet de rol-matrix om in een geautomatiseerde test-suite in de CI/CD pijplijn die verplicht draait bij elke commit die rechten raakt."
      }
    },
    {
      "@type": "Question",
      "name": "Wat kost een autorisatie-audit en rol-matrix testset bij LaunchStudio?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het auditeren van autorisaties, herstellen van role-combination bugs en bouwen van een geautomatiseerde testmatrix kost gemiddeld €900 en duurt 5 werkdagen."
      }
    }
  ]
}
</script>