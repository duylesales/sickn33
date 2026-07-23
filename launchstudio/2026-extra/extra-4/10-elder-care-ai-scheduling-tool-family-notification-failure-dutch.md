---
Titel: "AI-planningstools voor de ouderenzorg: wanneer een gemiste melding meer is dan een bug"
Trefwoorden: ai prototype, ai secure, elder care scheduling app, family notification system, ai-generated code
Koperfase: Bewustzijn
Doelgroep: AI-Native oprichter (niet-technisch)
---
# AI-planningstools voor de ouderenzorg: wanneer een gemiste melding meer is dan een bug

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-planningstools voor de ouderenzorg: wanneer een gemiste melding meer is dan een bug",
  "description": "In apps voor thuiszorgplanning die met AI-tools zijn gebouwd, is een shift-swap die geen nieuwe familiemelding activeert geen klein randgeval; het is het verschil tussen een gezin dat weet dat er een bezoek heeft plaatsgevonden en dat het gelooft dat dit wel het geval is geweest.",
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
  "datePublished": "2026-07-23",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/elder-care-ai-scheduling-tool-family-notification-failure"
  }
}
</script>

Hier is een mythe die het waard is om vroegtijdig met pensioen te gaan: "als het boekingssysteem werkt, werken de meldingen ook." In de meeste softwarecategorieën is dat ongeveer waar: een bevestigingsmail is een leuk extraatje bovenop een werkende kernstroom. Bij de thuiszorgplanning is het tegenovergestelde het geval. De melding is geen laag bovenop het bezoek. Voor de familie die hun telefoon checkt, is de melding *het bezoek, voor zover zij weten.

## De mythe: boekingslogica en notificatielogica zijn hetzelfde

AI-bouwers zoals Bolt zijn echt goed in de kern van het boekingsproces: de zorgverlener krijgt een dienst toegewezen, de klant ziet deze op een kalender en iedereen krijgt een bevestiging. Waar ze veel zwakker in zijn, is de vertakkende logica die ontstaat als een plan achteraf verandert – met name een ploegwisseling tussen twee zorgverleners. In een naïeve implementatie wordt bij het wisselen van een dienst alleen maar een zorgverlener-ID opnieuw toegewezen aan een bestaand agenda-item. Het bezoek verloopt nog steeds zoals gepland. Er zijn geen nieuwe evenementenbranden. Er gaat geen nieuwe melding uit. Vanuit het perspectief van het systeem gebeurde er niets waarvan een gezin op de hoogte moest zijn: het bezoek staat nog steeds 'op de kalender', alleen met een andere naam eraan.

Het probleem is dat een ploegenwissel precies het soort verandering is waar een gezin *wel* van op de hoogte moet zijn, vooral als de ruil niet doorgaat, vertraging oploopt of de vervangende verzorger een ander aankomstvenster heeft. Een stille herplaatsing kan stilletjes uitmonden in een bezoek dat nooit plaatsvindt, waarbij de familie niets wijzer wordt totdat ze vragen waarom hun ouders er slechter uitzien.

## Waarom dit een vertrouwensprobleem is en geen randgeval

Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera, verwoordt het zo: “We zien een verschuiving in de softwarebehoeften. De uitdaging is niet langer het omzetten van goede ideeën in software. Het gaat nu om de architectuur en beveiliging die nodig is om die producten tot volwassenheid te brengen. Precies daarin hebben we elf jaar ervaring.” Het plannen van ouderenzorg is een scherp voorbeeld van wat hij bedoelt: het ‘idee’ van een planningsapp is eenvoudig te prototypen. De architectuur die het betrouwbaar maakt als een echt gezin erop vertrouwt voor een echt bezoek, is een ander, moeilijker probleem, en het is het probleem dat de meeste door AI gegenereerde prototypen nog niet hebben opgelost.

Een gemiste melding in de ouderenzorgcontext is geen ongemak. Het is de kloof tussen een gezin dat gelooft dat hun familielid is gecontroleerd en de realiteit dat niemand is komen opdagen. Die kloof heeft reële gevolgen, en het is precies het soort scenario dat pas aan de oppervlakte komt als een app echte zorgschema's afhandelt, en niet als het demogegevens verwerkt.

## Wat de notificatiearchitectuur op productieniveau vereist

Om dit op de juiste manier op te lossen, moet elke planningsmutatie – en niet alleen de initiële boeking – worden behandeld als een gebeurtenis die een melding kan activeren, en moet expliciet worden gedefinieerd welke mutaties dat moeten zijn. Een dienstwissel, een tijdswijziging, een annulering en een no-show hebben elk hun eigen meldingsregel nodig, in plaats van te vertrouwen op de originele boekingsbevestiging om elke toekomstige status van dat bezoek te dekken. Ons team, dat vanuit het Amsterdamse kantoor van LaunchStudio werkt, bouwt dit als een gebeurtenisgestuurde laag achter de planningsinterface, zodat elke wijziging in de status van een bezoek (ongeacht welk scherm of welke beheerdersactie deze heeft geactiveerd) op betrouwbare wijze de familie bereikt.

U kunt zien hoe dit soort beoordelingen doorgaans werkt via [LaunchStudio's process](https://launchstudio.eu/en/#process), en voor een idee van de technische standaard die erachter zit, omvat Manifera's [portfolio](https://www.manifera.com/portfolio/) werk voor gereguleerde, vertrouwenskritische sectoren waar deze exacte discipline van belang is.

## Echt voorbeeld

### Een AI-native oprichter in actie: de ruil die niemand heeft aangekondigd

Otto Jansen, een oprichter uit Maastricht, heeft ZorgAgenda gebouwd – een planningstool voor thuiszorgorganisaties om de bezoeken van zorgverleners te beheren en gezinnen op de hoogte te houden – met behulp van Bolt. De kernplanning en familiemeldingenstroom werkten goed tijdens de eerste tests: boek een bezoek, familie wordt op de hoogte gebracht, bezoek vindt plaats, familie krijgt een voltooiingsupdate.

De kloof kwam aan het licht toen twee zorgverleners onderling een dienst wisselden via de hertoewijzingsfunctie van de app. Het bezoek bleef precies zoals voorheen op de kalender staan, alleen met de naam van een andere verzorger erbij. Er werd geen nieuwe melding verzonden naar de familie van de klant, omdat de app alleen meldingen verzond bij de eerste boeking en annulering; een nieuwe toewijzing was geen erkende trigger. Toen de ruil van de vervangende verzorger mislukte en het bezoek nooit daadwerkelijk plaatsvond, had de familie geen reden om dit te controleren, omdat hun laatste melding had bevestigd dat het bezoek gepland was en niets hen sindsdien iets anders had verteld.

De technici van LaunchStudio hebben het meldingssysteem rond elke wijziging in de planningsstatus opnieuw opgebouwd in plaats van alleen de oorspronkelijke boeking, hebben expliciete meldingen over ruilen en opnieuw toewijzen toegevoegd en een bevestigingsstap voor de voltooiing van een bezoek geïntroduceerd, zodat gezinnen een duidelijk signaal ontvangen wanneer een bezoek daadwerkelijk plaatsvindt, en niet alleen wanneer het gepland is.

**Resultaat:** gezinnen ontvangen nu een melding voor elke materiële wijziging in een gepland bezoek, waardoor de kloof wordt gedicht tussen wat de kalender laat zien en wat er feitelijk is gebeurd.

> *"Ik heb een test gedaan met het boeken van een bezoek en het annuleren van een bezoek. Ik heb nooit twee zorgverleners getest die onderling een dienst ruilden - en dat bleek precies het scenario te zijn waarin een gezin in het ongewisse bleef."*
> — **Otto Jansen, oprichter, ZorgAgenda (Maastricht)**

**Kosten en tijdlijn:** € 900 (gebeurtenisgestuurde notificatiearchitectuur, shift-swap- en hertoewijzingstriggers, bevestigingen van bezoekvoltooiing) — voltooid in 4 werkdagen.

---

## Veelgestelde vragen

### Waarom heeft het oorspronkelijke meldingssysteem geen ploegenwissel opgemerkt?

Omdat de app de initiële boeking en annulering alleen behandelde als gebeurtenissen die meldingswaardig waren, veranderde een nieuwe toewijzing wie aan een bezoek was toegewezen zonder de status van het bezoek te wijzigen, zodat er geen nieuwe meldingslogica werd geactiveerd.

### Is dit een veelvoorkomend hiaat in door AI gegenereerde planningstools?

Ja – AI-bouwers implementeren op betrouwbare wijze de primaire stroom die in een prompt wordt beschreven, maar hebben de neiging secundaire statuswijzigingen zoals swaps, herschikkingen en nieuwe toewijzingen over het hoofd te zien, tenzij deze allemaal expliciet zijn gespecificeerd.

### Hoe denkt Herre Roelevink over dit soort risico's?

Hij heeft duidelijk gemaakt dat het harde deel van de huidige software niet het idee genereert; het zijn de architectuur en de beveiliging die een product op volwassen leeftijd betrouwbaar maken, en dat is precies de kloof tussen een werkende demo en een systeem waar families op kunnen vertrouwen.

### Wat verandert LaunchStudio eigenlijk om dit op te lossen?

We hebben de meldingslaag opnieuw opgebouwd zodat deze bij elke planningsmutatie door gebeurtenissen wordt aangestuurd, in plaats van alleen aan de oorspronkelijke boeking te zijn gekoppeld, zodat elke wijziging in een bezoek op betrouwbare wijze de mensen bereikt die het moeten weten.

### Werkt LaunchStudio rechtstreeks samen met het Amsterdamse team aan dit soort projecten?

Ja – het Amsterdamse kantoor van LaunchStudio is onze Europese klantgerichte hub, en vertrouwenskritische plannings- en notificatiewerkzaamheden als deze zijn daar een terugkerend projecttype.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why didn't the original notification system catch a shift swap?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The app only treated the initial booking and cancellation as notification-worthy events \u2014 a reassignment changed who was assigned to a visit without changing the visit's status, so no new notification logic fired."
      }
    },
    {
      "@type": "Question",
      "name": "Is this a common gap in AI-generated scheduling tools?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes \u2014 AI builders reliably implement the primary flow described in a prompt but tend to miss secondary state changes like swaps, reschedules, and reassignments unless each one is explicitly specified."
      }
    },
    {
      "@type": "Question",
      "name": "How does Herre Roelevink think about this kind of risk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "He argues the hard part of software today isn't generating the idea \u2014 it's the architecture and security that bring a product to maturity, which is exactly the gap between a working demo and a system families can rely on."
      }
    },
    {
      "@type": "Question",
      "name": "What does LaunchStudio actually change to fix this?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We rebuild the notification layer to be event-driven across every schedule mutation, rather than tied only to the original booking, so any change to a visit reliably reaches the people who need to know."
      }
    },
    {
      "@type": "Question",
      "name": "Does LaunchStudio work directly with the Amsterdam team on projects like this?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes \u2014 LaunchStudio's Amsterdam office is the European client-facing hub, and trust-critical scheduling and notification work is a recurring project type there."
      }
    }
  ]
}
</script>