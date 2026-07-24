---
Titel: "Het bezwaar dat we het vaakst horen van technische medeoprichters (en waarom het meestal onjuist is)"
Trefwoorden: ai code tool, technical co-founder, rewrite vs fix, ai-generated code, bolt code review
Koperfase: Overweging
Doelgroep: Technische solo-oprichter
---
# Het bezwaar dat we het vaakst horen van technische medeoprichters (en waarom het meestal onjuist is)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Het bezwaar dat we het vaakst horen van technische medeoprichters (en waarom het meestal onjuist is)",
  "description": "De meest gehoorde tegenwerping die LaunchStudio krijgt van technische medeoprichters over het repareren van door AI gegenereerde code in plaats van herschrijven, en waarom een gerichte reparatie meestal beter is dan een volledige herschrijving.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/technical-cofounder-objection" }
}
</script>

"Als het door een AI-coderingstool is geschreven, moeten we het gewoon weggooien en het goed herschrijven." We horen een variant van deze zin vaker dan elk ander bezwaar van technische medeoprichters die overwegen externe hulp in te schakelen bij een Lovable-, Bolt- of Cursor-prototype. Het wordt met volledige overtuiging uitgesproken, meestal door iemand die jarenlang op de traditionele manier software heeft gebouwd en een instinctief wantrouwen heeft tegen alles wat een model heeft gegenereerd. Het is ook, in de meeste gevallen die wij zien, de duurdere en langzamere optie — en het is de moeite waard om precies uit te leggen waarom.

## Het bezwaar, eenvoudig gesteld

De redenering gaat als volgt: door AI gegenereerde code is onvoorspelbaar, inconsistent gestructureerd en onmogelijk volledig te vertrouwen. In plaats van tijd te besteden aan het begrijpen en patchen van wat er is, herschrijft een technische medeoprichter liever een schone versie vanaf een leeg bestand, met patronen die hij kent en beheerst. Het voelt verantwoord aan. Het voelt als het "juiste engineeringantwoord". En het komt voort uit een redelijk instinct — niemand wil een bedrijf bouwen op code die niemand begrijpt.

## Waar het bezwaar spaak loopt

Het probleem is dat "vanaf nul herschrijven" alle door AI gegenereerde code als even slecht behandelt, terwijl in de praktijk de daadwerkelijke defecten meestal beperkt en identificeerbaar zijn. Een ontbrekende index hier, een auth-check die alleen client-side draait daar, een webhook-handler zonder retry-logica — dit zijn gerichte, oplosbare problemen, geen bewijs dat elke regel moet worden vervangen. Een herschrijving vervangt niet alleen de slechte tien procent; het gooit ook de negentig procent weg die al werkt, al door echte gebruikers is getest, en tegen echte tijdskosten opnieuw zou moeten worden gebouwd.

Er zit ook een verborgen aanname in het bezwaar: dat een herschrijving inherent veiliger is omdat de nieuwe medeoprichter het zelf heeft geschreven. In werkelijkheid introduceert een overhaaste herschrijving onder tijdsdruk van de oprichter zijn eigen nieuwe bugs — alleen minder zichtbare, omdat nog niemand de vervanging heeft stressgetest. De door AI gegenereerde versie, met al zijn tekortkomingen, heeft meestal al echt gebruik doorstaan. Dat is niet niks.

## De drie vragen die we stellen in plaats van "herschrijven of niet"

Voordat u standaard voor een volledige herschrijving kiest, is het de moeite waard deze vragen te beantwoorden:

- **Wat is er specifiek kapot?** Niet "de code voelt niet lekker" — een daadwerkelijke lijst van concrete defecten: ontbrekende validatie, een race condition, een onveilig endpoint.
- **Is het defect geïsoleerd of systemisch?** Een slechte databaseschema-beslissing die elke tabel raakt, is systemisch. Een enkel ongevalideerd formulier is geïsoleerd. De meeste AI-tooldefecten zijn geïsoleerd.
- **Wat kost de reparatie in vergelijking met de herschrijving?** Een gerichte reparatie van een specifieke module wordt meestal in dagen gemeten. Een volledige herschrijving wordt meestal in weken gemeten — en dat vertraagt het daadwerkelijke bedrijf dat de oprichter probeert te bouwen.

In vrijwel elk geval dat we hebben beoordeeld, wijst het eerlijke antwoord op deze drie vragen naar een gerichte reparatie, geen herschrijving. Het instinct om door AI gegenereerde code te wantrouwen is terecht. De conclusie dat dat wantrouwen vereist dat u helemaal opnieuw begint, meestal niet.

Onze engineers — werkzaam vanuit Ho Chi Minh-stad, waar Manifera zijn belangrijkste engineeringcentrum heeft — beoordelen deze precieze afweging bijna wekelijks, omdat het het meest voorkomende splitsingspunt is voor technische medeoprichters die een Bolt- of Lovable-prototype evalueren. Achter LaunchStudio staat Manifera's team van 120+ ervaren engineers, en het beoordelingsproces is bewust zo opgezet dat "repareren of herschrijven" met bewijs wordt beantwoord, niet met een onderbuikgevoel. Als u midden in een discussie zit met een technische medeoprichter, kunt u [het project beschrijven en een gerichte beoordeling krijgen](https://launchstudio.eu/en/#contact) voordat een van beide partijen zich zes weken vastlegt op het verkeerde antwoord. Het team voor [aangepaste softwareontwikkeling](https://www.manifera.com/services/custom-software-development/) van Manifera past dezelfde repareer-eerst-discipline toe op zakelijke codebases, niet alleen op door AI gegenereerde.

## Echt voorbeeld

### Een AI-native oprichter in actie: De herschrijving van zes weken die niet nodig was

Roos Dijkstra, een oprichter in Den Bosch, bouwde PersoneelPlan — een planningstool voor HR-teams die ploegenmedewerkers beheren — met Bolt. Het product werkte, had betalende pilotklanten en had één echt probleem: onder bepaalde omstandigheden konden twee managers per ongeluk dezelfde werknemer aan overlappende diensten toewijzen zonder dat een van beiden een waarschuwing kreeg.

De technische medeoprichter van Roos bekeek de codebase, besloot dat door AI gegenereerde code op geen enkel niveau kon worden vertrouwd, en drong aan op een volledige herschrijving vanaf nul met een framework dat hij goed kende. Roos ging er, met tegenzin, mee akkoord, en het team besteedde zes weken aan het herbouwen van de hele planningsengine — inclusief de negentig procent ervan die nog nooit een probleem had veroorzaakt.

Toen LaunchStudio er daarna bij werd gehaald om de nieuwe versie te beoordelen vóór een tweede pilot, ontdekten onze engineers dat het daadwerkelijke defect in de oorspronkelijke Bolt-versie een enkele ontbrekende conflictcontrole in de dienst-toewijzingsfunctie was geweest — een reparatie die een paar dagen zou hebben gekost om te isoleren, te testen en uit te brengen, zonder verder iets aan het product te raken. De herschrijving van zes weken was niet nodig geweest; het had het team simpelweg zes weken gekost die het niet meer terugkreeg.

**Resultaat:** LaunchStudio bevestigde dat de herbouwde versie functioneel gelijkwaardig was aan wat een gerichte reparatie zou hebben opgeleverd, en hielp het team een lichter beoordelingsproces op te zetten zodat het volgende bezwaar niet meteen naar "alles herschrijven" zou grijpen.

> *"Mijn medeoprichter had geen ongelijk om voorzichtig te zijn met door AI geschreven code. Hij had wel ongelijk over waar die voorzichtigheid toe zou moeten leiden. We verloren zes weken om een punt te bewijzen dat we niet hoefden te bewijzen."*
> — **Roos Dijkstra, oprichter, PersoneelPlan (Den Bosch)**

**Kosten en tijdlijn:** € 900 (beoordeling na herschrijving, validatie conflictcontrole, lichter beoordelingsproces) — voltooid in 4 werkdagen.

---

## Veelgestelde vragen

### Is het ooit terecht dat een technische medeoprichter aandringt op een volledige herschrijving?

Ja, als de defecten systemisch zijn — bijvoorbeeld een databaseschema dat fundamenteel ongeschikt is voor de schaal van het product — dan kan een herschrijving van die specifieke laag gerechtvaardigd zijn. De meeste AI-tooldefecten zijn echter geïsoleerd en oplosbaar zonder de rest van de codebase aan te raken.

### Hoe beslist LaunchStudio tussen een reparatie en een herschrijving?

Onze engineers, waaronder het team gevestigd in Ho Chi Minh-stad, beginnen met een concrete lijst van defecten in plaats van een algemene indruk van de code, en bepalen vervolgens de kleinst mogelijke veilige wijziging die deze oplost.

### Wat als mijn technische medeoprichter de reparatie nog steeds niet vertrouwt?

We leveren een geschreven scope van precies wat er is gewijzigd en waarom, zodat een sceptische technische medeoprichter de specifieke diff kan beoordelen in plaats van alleen op vertrouwen te varen.

### Werkt Manifera alleen met niet-technische oprichters?

Nee — een aanzienlijk deel van ons werk bestaat precies hieruit: technische medeoprichters en CTO's die een extern engineeringteam willen laten valideren of een reparatie of een herschrijving de juiste keuze is voor door AI gegenereerde code.

### Hoe lang duurt een gerichte reparatie doorgaans in vergelijking met een herschrijving?

Een gerichte reparatie van een geïsoleerd defect duurt doorgaans een paar dagen tot een paar weken, afhankelijk van de complexiteit, vergeleken met de vier tot acht weken die we vaak zien bij onnodige volledige herschrijvingen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Is it ever right for a technical co-founder to insist on a full rewrite?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, if the defects are systemic, such as a database schema fundamentally wrong for the product's scale. Most AI-tool defects, though, are isolated and fixable without a full rewrite." } },
    { "@type": "Question", "name": "How does LaunchStudio decide between a fix and a rewrite?", "acceptedAnswer": { "@type": "Answer", "text": "Our engineers, including the team based in Ho Chi Minh City, start with a concrete list of defects rather than a general impression of the code, then scope the smallest safe change that resolves them." } },
    { "@type": "Question", "name": "What if my technical co-founder still doesn't trust the fix?", "acceptedAnswer": { "@type": "Answer", "text": "We provide a written scope of exactly what was changed and why, so a skeptical technical co-founder can review the specific diff rather than relying on trust alone." } },
    { "@type": "Question", "name": "Does Manifera only work with non-technical founders?", "acceptedAnswer": { "@type": "Answer", "text": "No. A meaningful share of our work involves technical co-founders and CTOs who want an outside engineering team to validate whether a fix or a rewrite is the right call on AI-generated code." } },
    { "@type": "Question", "name": "How long does a scoped fix usually take compared to a rewrite?", "acceptedAnswer": { "@type": "Answer", "text": "A scoped fix for an isolated defect typically takes a few days to a couple of weeks, compared to the four-to-eight-week range common for unnecessary full rewrites." } }
  ]
}
</script>
