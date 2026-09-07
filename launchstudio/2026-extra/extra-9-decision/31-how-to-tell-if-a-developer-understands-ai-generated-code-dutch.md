---
Titel: "Hoe U Ziet Of een Developer AI-Gegenereerde Code Werkelijk Begrijpt"
Trefwoorden: ontwikkelaar screenen, AI code review, ontwikkelaar inhuren niet-technische oprichter, Lovable code audit, interviewvragen software developer, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Hoe U Ziet Of een Developer AI-Gegenereerde Code Werkelijk Begrijpt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe U Ziet Of een Developer AI-Gegenereerde Code Werkelijk Begrijpt",
  "description": "Een niet-technische oprichter kan code niet beoordelen, maar wél hoe een developer praat over code die hij niet zelf schreef. De exacte vragen voor een kennismakingsgesprek, wat een competent antwoord kenmerkt en wanneer u direct moet afhaken.",
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
  "datePublished": "2027-01-04",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/hoe-u-ziet-of-een-developer-ai-gegenereerde-code-werkelijk-begrijpt"
  }
}
</script>

"Dus u heeft dit volledig in Lovable gebouwd?"

"Klopt — van begin tot eind. Het werkt en ik heb momenteel twaalf actieve gebruikers."

"Duidelijk. Eerlijk gezegd is het snelste om met een schone lei te beginnen. Ik zou het netjes herbouwen in Next.js, reken op een maand of drie, en dan heeft u een codebase die fatsoenlijk onderhoudbaar is."

Dit gesprek vindt dagelijks plaats in kennismakingsgesprekken. Voor een niet-technische oprichter klinkt zo'n reactie vaak als geruststellende deskundigheid. In werkelijkheid is het dat zelden. Het is het geluid van iemand die uw repository niet heeft geopend en daar ook geen zin in heeft — simpelweg omdat het lezen van andermans code aanzienlijk moeilijker is dan zelf iets nieuws schrijven, en het ontleden van door AI geschreven code nóg weerbarstiger is. U kunt hun technische claims wellicht niet inhoudelijk controleren. U kunt echter wél feilloos vaststellen of ze uw code daadwerkelijk hebben bekeken. En dat blijkt in de praktijk vrijwel dezelfde lakmoesproef te zijn.

## Stop met Toetsen op de Verkeerde Criteria

De eerste impuls van een niet-technische oprichter is toetsen op cv-elementen: jarenlange werkervaring, specifieke frameworks, GitHub-sterren of de vraag of ze "al eerder met Supabase hebben gewerkt". Aan al die criteria is eenvoudig te voldoen, maar ze vertellen u nagenoeg niets over de opgave die er ligt. Uw vraagstuk is immers geen 'greenfield' ontwikkeling vanaf nul. Uw vraagstuk is begrijpend lezen: iemand moet een codebase openen die door een AI op basis van uw prompts is gegenereerd, doorgronden wat er momenteel gebeurt, bepalen welke componenten dragend zijn en welke puur decoratief, en uitsluitend aanpassen wat noodzakelijk is.

Dat vereist een fundamenteel andere vaardigheid. Veel bekwame programmeurs zijn hier ronduit zwak in. Zij hebben hun hele carrière doorgebracht met het schrijven van code binnen zelfgekozen architectuurconventies, en voelen zich zichtbaar ongemakkelijk in een codebase zonder consistente standaarden — precies wat een AI-tool produceert na veertig prompts verspreid over drie weken. Dat ongemak uit zich steevast als: "dit moet volledig herbouwd worden." Soms is dat waar. Meestal is het een persoonlijke voorkeur verpakt als diagnose, die u uw volledige frontend en drie kostbare maanden kost.

Toets daarom rechtstreeks op codebegrip. Dit is hoe u dat aanpakt.

## De Traceertest: Laat Hen Één Pad Hardop Doorlopen

Geef de kandidaat een dag vóór het gesprek leesrechten op uw repository (een besloten GitHub-omgeving met read-only rechten volstaat). Stel tijdens het videogesprek exact deze vraag:

**"Loop eens stap voor stap met mij door wat er gebeurt wanneer een nieuwe gebruiker zich registreert. Begin bij de klik op de knop en eindig bij de nieuwe rij in de database. Vertel mij elke tussenstop die de data onderweg maakt."**

U hoeft de technische details niet eens te begrijpen; u hoeft enkel te letten op de *structuur* van het antwoord. Een ontwikkelaar die de code werkelijk heeft bestudeerd, antwoordt specifiek en in logische volgorde: het component waarin het formulier zit, de functie die wordt aangeroepen, of dat verzoek naar uw eigen backend gaat of direct vanuit de browser naar Supabase of Firebase schiet, wat er waar wordt weggeschreven en wat er gebeurt als het proces halverwege faalt. Zij noemen bestandsnamen. Zij zeggen dingen zoals: "er zit een `signup`-handler in `app/api/auth/`, maar de rij voor het gebruikersprofiel wordt daarna pas client-side aangemaakt. Dat betekent dat als die tweede aanroep hapert, u een geregistreerd account heeft zónder profiel."

Die laatste observatie is het bewijs. Specifiek, ietwat ongemakkelijk, beschrijft een reële ontwerpfout die daadwerkelijk in de codebase zit en uitsluitend opgemerkt kan worden door iemand die de datastroom handmatig heeft getraceerd.

Een ontwijkend antwoord blijft daarentegen zweven op het niveau van abstracte concepten: "Het is een standaard authenticatieflow, Supabase regelt dat onder water, vrij generiek allemaal." Dat is een beschrijving van software in het algemeen, niet van úw specifieke applicatie. Hoort u twee van zulke antwoorden achter elkaar, vraag dan direct: "Welk bestand heeft u zojuist bekeken om dat te beoordelen?" Een kandidaat die de code kent, antwoordt binnen twee seconden. Een kandidaat die bluft, moet ineens "even zoeken op het andere scherm".

## Vraag Wat Ze Zouden Behouden, Niet Wat Ze Willen Veranderen

Iedereen kan een lijst opnoemen van wat er niet deugt. Stel de omgekeerde vraag:

**"Welke onderdelen van wat ik heb gebouwd zou u exact zo behouden?"**

Een ontwikkelaar die bedreven is in het werken met AI-gegenereerde software zal het overgrote deel met plezier laten staan. Een eerlijk en deskundig antwoord klinkt typisch zo: "Uw frontend is prima — de componenten bevatten wat herhalende code, maar ze werken, en uw testgebruikers vinden de interface prettig. Daar zou ik niets aan veranderen. De databasetabellen zijn qua opzet eveneens bruikbaar. Wat ik wel direct vervang, is het stuk waar de browser rechtstreeks communiceert met de database, en ik verplaats de Stripe-afhandeling naar de server, want momenteel kan elke bezoeker handmatig een willekeurig bedrag meesturen."

Dit antwoord laat zien dat de kandidaat het cruciale onderscheid maakt tussen *visuele rommel* en *structureel risico*. AI-gegenereerde code zit vol met het eerste en is gevaarlijk vanwege het tweede. Visuele rommel — dubbele functies, vreemde naamgeving, drie nagenoeg identieke knop-componenten — is lelijk, maar kost u operationeel niets. Structureel risico — ontbrekende permissiecontroles op de server, API-sleutels die naar de browser lekken, betalingsbedragen die blindelings vanaf de client worden vertrouwd — is onzichtbaar en levensgevaarlijk om te negeren.

Iemand die deze twee niet uit elkaar kan houden, zal ofwel alles willen slopen (omdat hij rommel verwart met risico) ofwel alles goedkeuren (omdat hij risico aanziet voor onschuldige rommel). Beide vergissingen zijn op hun eigen manier bijzonder kostbaar.

## Stel een Vraag Waarvan U het Antwoord Al Kent

Dit is de meest waardevolle manoeuvre voor een niet-technische oprichter, en het kost u niets.

Kies vóór het gesprek één specifiek defect waarvan u al weet dat het stuk is of ontbreekt. Bijna elk prototype heeft er wel een: wachtwoordherstel ontbreekt; het beheerderspaneel is enkel verborgen in het menu maar openbaar bereikbaar via de URL; het verwijderen van een account wist de bijbehorende data niet; uitnodigingsmails komen niet aan; of het uploadformulier accepteert bestanden van willekeurige formaten en groottes. Kies er één die u in één zin kunt samenvatten.

Breng het tijdens het gesprek niet zelf ter sprake, maar vraag:

**"Als ik u hier vandaag een uur mee aan het werk zet, waar kijkt u dan als eerste naar, en wat verwacht u aan te treffen?"**

Kijk vervolgens of ze uw bekende pijnpunt zelfstandig blootleggen, of een ander reëel probleem aanwijzen dat u zelf nog niet had opgemerkt. Ontwikkelaars die de code daadwerkelijk hebben ingezien, vinden concrete zaken. Ontwikkelaars die dat niet deden, produceren een generiek rijtje: "Ik zou kijken naar security, schaalbaarheid en performance" — het technische equivalent van een daghoroscoop.

Mocht de kandidaat het niet spontaan noemen, leg het dan zelf op tafel en observeer de reactie: "Mijn admin-pagina is eigenlijk alleen verstopt in de navigatiebalk. Iedereen die de URL raadt, kan erin. Hoe ernstig is dat, en wat kost het om op te lossen?" Een sterk antwoord legt het achterliggende mechanisme helder uit (de browser bepaalt wat er te zien is, de server bepaalt wat geoorloofd is, en momenteel beslist alleen de browser), geeft een realistische inschatting van de doorlooptijd (een middag werk, geen complete herbouw) en noemt direct welke andere kwetsbaarheden hierdoor waarschijnlijk ook aanwezig zijn. Een zwak antwoord verzandt in paniekvoetbal of haalt nonchalant de schouders op.

## Luister naar de Vragen Die de Developer U Stelt

Draai de rollen eens om. Tijdens een gesprek van een half uur zal een ontwikkelaar die geschikt is voor dit werk u vragen stellen over de zakelijke context van uw product, niet alleen over uw deadline. Waardevolle vragen klinken als volgt:

- "Wie mag welke data inzien? Mag een coach de gegevens van de cliënten van een andere coach bekijken?"
- "Waar vindt de transactie precies plaats — bepaalt Stripe de prijs, of stuurt uw frontend het bedrag mee?"
- "Wat doet u operationeel wanneer een gebruiker morgen mailt met het verzoek zijn account te verwijderen?"
- "Hoeveel mensen gebruiken het platform nu, en bij welk aantal gebruikers maakt u zich zorgen over de capaciteit?"
- "Draait er al iets live met echte klantgegevens, of test u uitsluitend met bekenden?"

Elk van deze vragen raakt rechtstreeks aan risicobeheersing en afbakening. Een kandidaat die dit vraagt, brengt uw werkelijke situatie in kaart. Een kandidaat die enkel vraagt "wat is uw budget?" en "wanneer moet het af zijn?", berekent louter uw financiële speelruimte.

## Vijf Vaktermen Die Bewijzen Dat Ze Dit Eerder Hebben Gedaan

U hoeft de technologie niet tot in detail te beheersen om het vakjargon te herkennen dat specifiek wordt gebruikt door engineers die vaker met AI-code hebben gewerkt. Let op de volgende termen:

**"Row-level security (RLS)"** — de permissieregels binnen de database zelf. AI-tools laten deze vaak uitgeschakeld staan, waardoor de database alle gegevens uitlevert aan iedereen die erom vraagt. Een ontwikkelaar die dit direct controleert, weet exact waar de risico's zitten.

**"Server-side validation"** — het controleren van invoervelden en bedrijfsregels op de server in plaats van uitsluitend in de browser. Prototypes valideren bijna altijd alleen in de frontend, wat een vrijblijvend advies is in plaats van een harde beveiliging.

**"De service role key staat in de client bundle"** — een hoofdsleutel tot uw database die per ongeluk is meegeleverd in de code die elke bezoeker in zijn browser kan inzien. Dit is een van de meest voorkomende vondsten in AI-applicaties en vereist directe sanering.

**"Webhook signature verification"** — het wiskundig verifiëren dat een melding ("deze klant heeft betaald") daadwerkelijk afkomstig is van Stripe of Mollie, en niet van een kwaadwillende die een nepmelding simuleert.

**"Idempotentie"** — de garantie dat wanneer een betalingsverzoek per ongeluk twee keer binnenkomt via een netwerkfout, de creditcard van de klant slechts één keer wordt belast. Niemand noemt dit tenzij hij in het verleden te maken heeft gehad met dubbele afschrijvingen.

Het gaat er niet om dat u deze concepten zelf programmeert. Het gaat erom dat u waarneemt of een ontwikkelaar concrete technische mechanismen noemt, of vlucht in vage verkooptermen zoals "robuust" en "enterprise-grade".

## Hoe een Goed Antwoord Klinkt bij Slecht Nieuws

De allerbeste graadmeter is de manier waarop iemand slecht nieuws brengt. U zoekt naar gevoel voor proportionaliteit: "Er zijn drie serieuze kwetsbaarheden en ongeveer tien cosmetische slordigheden. Twee van die drie moet u direct oplossen voordat u geld aanneemt van vreemden; de derde kan wachten tot u een paar honderd actieve gebruikers heeft. Dit is globaal wat elk onderdeel kost om te herstellen."

Wat u beslist wilt vermijden, zijn de twee uitersten. Doemdenken ("dit is levensgevaarlijk, dit kunt u absoluut niet lanceren") is vaak een onderhandelingstactiek die toewerkt naar een dure offerte voor complete herbouw. Grenzeloze geruststelling ("ziet er prima uit, we poetsen het onderweg wel bij") betekent dat men niet serieus heeft gekeken. Immers, 45% van de AI-gegenereerde code bevat beveiligingslekken; niemand die daadwerkelijk een Lovable-export heeft geanalyseerd, kan beweren dat alles in één keer klopt.

Het eerlijke midden klinkt nuchter, realistisch en enigszins zakelijk. Dat is hoe echte engineeringcompetentie klinkt.

## Pas Deze Zelfde Toets Toe op Ons

Het zou hypocriet zijn om deze richtlijnen te publiceren en onszelf erboven te stellen: pas al deze tests gerust toe op [LaunchStudio](https://launchstudio.eu/nl/). Deel uw repository vóór het kennismakingsgesprek, vraag ons uw registratieflow te traceren, vraag wat we zouden laten staan en confronteer ons met uw bekende bug. Wij behouden uw frontend omdat het herschrijven van een werkende interface doorgaans de duurste manier is om een backend-probleem op te lossen — niet omdat hergebruik altijd zaligmakend is. Als uw prototype daadwerkelijk ongeschikt is voor productie, vertellen we u dat eerlijk en kosteloos. De technische slagkracht wordt geleverd door [Manifera](https://www.manifera.com/about-us/), dat al meer dan elf jaar complexe software levert aan enterprise-organisaties. De afrondende werkzaamheden — beveiliging, authenticatie, betalingen en hosting — liggen doorgaans tussen de € 800 en € 3.500 vast tarief, met een doorlooptijd van één tot drie weken.

Als een andere partij de traceertest overtuigender doorstaat dan wij, kies dan voor hen. Het doel van deze aanpak is immers dat u het verschil voortaan zelfstandig herkent.

**Deel uw prototype met ons en wij leveren u kosteloos een schriftelijke analyse van uw registratietraject — vrijblijvend, zonder verplicht verkoopgesprek, als betrouwbaar ijkpunt voor elke andere offerte die u ontvangt.**

## Praktijkvoorbeeld

### Een Oprichter in Actie: De Kandidaat Die het Bestand Bij Naam Noemde

Sanne Bakkers, voormalig praktijkmanager van een fysiotherapiekliniek in Utrecht, bouwde RehabTrack: een in Bolt ontwikkelde applicatie waarmee praktijken oefenprogramma's toewijzen aan patiënten. Ze sprak in twee weken tijd met drie softwareontwikkelaars. Twee van hen begonnen het gesprek direct met het advies om alles van de grond af opnieuw op te bouwen. Geen van beiden had de repository geopend die zij vier dagen eerder had toegezonden.

De derde kandidaat traceerde de uitnodigingsflow voor patiënten hardop, noemde het exacte route-bestand waarin de logica stond en wees erop dat de uitnodigingslink het interne patiënt-ID in platte tekst bevatte. Door simpelweg één cijfer in de URL aan te passen, kon een willekeurige gebruiker het complete medische oefenschema van een andere patiënt inzien. Sanne wist dit niet. Het was tevens exact het soort datalek waar ze bang voor was, maar dat ze zelf niet kon controleren.

Zij gebruikte die specifieke bevinding vervolgens als maatstaf voor elk volgend gesprek: *"Er zit een kwetsbaarheid in de autorisatiecontrole op de uitnodigingsroute — hoe zou u dat oplossen?"*

**Resultaat:** De uitnodigingen van RehabTrack werden omgezet naar cryptografisch ondertekende tokens met een beperkte geldigheidsduur, en de datascheiding tussen praktijken werd serverside herbouwd binnen negen werkdagen voor een vaste prijs van € 2.400 — waarbij de oorspronkelijke Bolt-frontend volledig intact bleef.

> *"Ik ben gestopt met proberen te beoordelen wie op papier de beste programmeur was. Ik stelde ze simpelweg allemaal dezelfde gerichte vraag over mijn eigen kwetsbare link. Het verschil in deskundigheid tussen de antwoorden was direct overduidelijk."*
> — **Sanne Bakkers, Oprichter, RehabTrack (Utrecht)**

---

## Veelgestelde Vragen

### Moet ik een vreemde toegang geven tot mijn code vóórdat ik hem inhuur?

Leesrechten (read-only) op een besloten repository zijn standaard in de sector, brengen minimaal risico met zich mee en trekt u direct na het gesprek weer in. Weigert een kandidaat uw code te bekijken voordat hij een offerte opstelt, dan is dat een duidelijk signaal: niemand kan serieus werk begroten dat hij niet heeft gezien. Een prijsopgave zonder code-inspectie is een ruwe gok die u later dubbel betaalt.

### Wat als een ontwikkelaar oprecht adviseert om opnieuw te beginnen — is dat altijd een alarmsignaal?

Nee. Soms is een prototype technisch simpelweg niet te redden, met name wanneer het onderliggende datamodel niet aansluit bij hoe het bedrijf in werkelijkheid opereert. Het verschil zit in de onderbouwing: een professioneel herbouwadvies noemt exact welke componenten falen, waarom aanpassing onmogelijk is en wat een gerichte reparatie zou kosten. Een herbouwadvies dat wordt gegeven vóórdat de code is bekeken, is een persoonlijke voorkeur, geen diagnose.

### Ik beheers het technisch jargon niet. Kan ik deze evaluatie wel uitvoeren?

Jazeker. U beoordeelt immers de structuur en scherpte van het antwoord, niet de syntaxis. Specifiek wint van algemeen, bestandsnamen en functies winnen van abstracte categorieën, en evenwichtigheid wint van sensatiezucht. U merkt het verschil binnen twee gesprekken, zelfs als u de exacte werking van database-autorisatie niet kent.

### Hoe lang duurt zo'n technisch evaluatiegesprek idealiter?

Dertig minuten volstaan voor de traceertest, de vraag over wat behouden kan blijven en uw controle-defect. Als een ontwikkelaar een uur nodig heeft om iets zinnigs over uw code te zeggen, ligt het probleem doorgaans niet aan een gebrek aan tijd.

### Is het verstandig om kandidaten een kleine betaalde proefopdracht te laten doen?

Een kleine, betaalde praktijkopdracht is een uitstekende manier om de knoop door te hakken tussen twee sterke finalisten, maar het is een tijdrovende methode om op iedereen toe te passen. Gebruik de vragen uit dit artikel om te schiften van vijf kandidaten naar twee, en betaal de laatste twee vervolgens voor enkele uren echt programmeerwerk als u nog twijfelt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik een vreemde toegang geven tot mijn code vóórdat ik hem inhuur?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Leesrechten op een besloten repository zijn standaard, brengen minimaal risico met zich mee en trekt u na afloop direct in. Een kandidaat die weigert de code te bekijken vóór hij offreert, doet een gok waar u later voor betaalt."
      }
    },
    {
      "@type": "Question",
      "name": "Wat als een ontwikkelaar oprecht adviseert om opnieuw te beginnen — is dat altijd een alarmsignaal?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Soms is een datamodel structureel ontoereikend. Een eerlijk herbouwadvies benoemt echter exact welke componenten niet voldoen, waarom aanpassing faalt en wat reparatie zou kosten, in plaats van herbouw voor te stellen zonder de code te openen."
      }
    },
    {
      "@type": "Question",
      "name": "Ik beheers het technisch jargon niet. Kan ik deze evaluatie wel uitvoeren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Jazeker, omdat u let op de vorm van het antwoord: specifieke bestanden en logische stappen winnen van vage categorieën, en nuchterheid wint van paniek of loze beloftes."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt zo'n technisch evaluatiegesprek idealiter?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dertig minuten is ruim voldoende voor de traceertest, de vraag wat bewaard kan blijven en uw controlevraag over een bekend probleem."
      }
    },
    {
      "@type": "Question",
      "name": "Is het verstandig om kandidaten een kleine betaalde proefopdracht te laten doen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Als beslissende test tussen twee sterke finalisten wel, maar niet als eerste filter. Gebruik gerichte vragen om terug te gaan naar twee kandidaten, en betaal die eventueel voor een korte proefopdracht."
      }
    }
  ]
}
</script>
