---
Titel: "Een interview met een LaunchStudio-engineer: wat niemand u vertelt over het beoordelen van vibe-coded apps"
Trefwoorden: ai coding, vibe coding review, code review, cursor pull requests, ai-generated code audit
Koperfase: Bewustzijn
Doelgroep: AI-Native oprichter (niet-technisch)
---
# Een interview met een LaunchStudio-engineer: wat niemand u vertelt over het beoordelen van vibe-coded apps

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Een interview met een LaunchStudio-engineer: wat niemand u vertelt over het beoordelen van vibe-coded apps",
  "description": "Een gesprek met een LaunchStudio-engineer over wat er daadwerkelijk gebeurt wanneer een mens een door AI gegenereerde codebase beoordeelt, inclusief een echt voorbeeld van het beoordelen van pull requests uit een met Cursor gebouwde CRM.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/engineer-interview-reviewing-vibe-coded-apps" }
}
</script>

We gingen in gesprek met een van de engineers van LaunchStudio — onderdeel van het team gevestigd in Amsterdam dat wekelijks door AI gegenereerde codebases beoordeelt — om een simpele vraag te stellen: wat gebeurt er daadwerkelijk wanneer een mens voor het eerst een "vibe-coded" app opent? Het antwoord bleek minder over bugs te gaan en meer over een specifiek soort blindheid die AI-coderingstools onbedoeld creëren. Hieronder vindt u het gesprek, licht geredigeerd voor de lengte.

## Het interview

**Vraag: Wat is het eerste waar u naar kijkt wanneer u een project opent dat is gebouwd met een AI-coderingstool?**

Antwoord: Eerlijk gezegd niet meteen de code zelf. Ik kijk naar wat er ontbreekt — waar een menselijke engineer een opmerking over zou hebben geschreven, of een vraag over zou hebben gesteld in een standup, die simpelweg nooit is gesteld. AI-coderingstools zijn zelfverzekerd. Ze laten geen spoor achter van "hier was ik niet zeker van, iemand zou dit moeten controleren". Een junior developer zou dat spoor wel achterlaten. Een AI-tool verzendt de beslissing gewoon stilzwijgend, en het ziet er precies zo gepolijst uit als de delen die daadwerkelijk solide zijn.

**Vraag: Is vibe-coded software slechter dan wat een junior developer zou schrijven?**

Antwoord: Niet per se slechter — anders. De fouten van een junior developer neigen te clusteren: als ze authenticatie verkeerd begrijpen, begrijpen ze het waarschijnlijk consequent verkeerd door de hele app heen, wat eigenlijk makkelijker te vangen is. Door AI gegenereerde fouten zijn verspreid. De ene functie behandelt edge cases prachtig. De functie ernaast, die structureel iets vergelijkbaars doet, heeft een controle volledig overgeslagen. Er is geen consistente "blinde vlek" om naar te zoeken, omdat de tool niet over de app als geheel redeneert zoals een mens dat zou doen.

**Vraag: Wat is het meest voorkomende dat oprichters aannemen dat in orde is, maar niet is?**

Antwoord: Dat "het werkte in de demo" betekent dat het geregeld is. Ik beoordeelde onlangs een CRM-tool — een oprichter genaamd Milan Verhagen bouwde iets genaamd KlantStroom met Cursor — en pull request na pull request zag er op het eerste gezicht netjes uit. Functies hadden zinnige namen, de UI werkte, niets crashte. Maar toen ik natraceerde hoe klantrecords daadwerkelijk werden aangemaakt, was er een gat waarbij een webhook twee keer voor dezelfde gebeurtenis kon afgaan en een duplicaatklant kon aanmaken zonder dat een unieke constraint dit tegenhield. Het kwam nooit naar voren in tests, omdat niemand precies de timing testte die het triggert. Dat is het patroon: dingen die elke keer werken wanneer u ze op de natuurlijke manier zou proberen, en alleen falen onder omstandigheden die een mens niet zou bedenken om te simuleren.

**Vraag: Hoe beoordeelt u zo'n codebase daadwerkelijk efficiënt?**

Antwoord: We lezen niet elke regel — dat schaalt niet en daar zit het risico niet. We volgen de paden die het meest belangrijk zijn: hoe geld beweegt, hoe auth-beslissingen worden genomen, hoe klantdata wordt geschreven en verwijderd. We behandelen die als hoogrisicozones, ongeacht hoe netjes de omringende code eruitziet. De rest krijgt een lichtere doorloop. Het is minder "codebeoordeling" in de traditionele zin en meer "risicomapping" — uitzoeken waar een stille AI-beslissing daadwerkelijk iemand pijn zou kunnen doen.

**Vraag: Wat wilt u dat oprichters begrijpen voordat ze een vibe-coded app ter beoordeling overdragen?**

Antwoord: Dat een netjes ogende app en een veilige app niet hetzelfde zijn, en dat is geen kritiek op de tools — Lovable, Bolt, Cursor, v0 zijn oprecht goed in het snel produceren van werkende software. Het is alleen dat "werkend" en "productieklaar" verschillende lat zijn, en niemand vertelt oprichters dat de AI-tool alleen de eerste heeft gehaald.

Manifera brengt meer dan 11 jaar productie-engineeringervaring naar precies dit soort beoordeling, en onze Amsterdamse engineers doen dit werk dagelijks bij Lovable-, Bolt-, Cursor- en v0-projecten. Als u een tweede paar ogen op uw eigen prototype wilt, kunt u [ons uw prototypelink sturen voor gratis advies](https://launchstudio.eu/nl/#contact) voordat u uw eigen versie van Milans webhookbug op de harde manier ontdekt. Voor een breder beeld van hoe dit soort engineeringbeoordeling past in grotere builds, zie Manifera's [diensten voor webapp-ontwikkeling](https://www.manifera.com/services/web-app-develop/).

## Een Snelle Zelfevaluatie: Drie Vragen over Uw Eigen App Vóór U Lanceert

U hoeft geen doorgewinterde software-architect te zijn om een eerste risico-inventarisatie van uw eigen applicatie uit te voeren. Vóórdat u de deuren opent voor betalende klanten of uw product presenteert aan investeerders, dient u deze drie kritieke vragen eerlijk te beantwoorden:

**1. Wat gebeurt er als een gebruiker midden in een betaaltransactie zijn browser sluit?** Wordt de betaling wel afgeschreven door Stripe, maar krijgt de gebruiker nooit zijn abonnement geactiveerd in uw database? Zonder idempotente webhook-verwerking en status-synchronisatie aan de serverzijde leidt dit direct tot gefrustreerde klanten en handmatige administratieve correcties.

**2. Kan een kwaadwillende gebruiker uw database leegtrekken via publieke API's?** Heeft u gecontroleerd of uw zoek- of exportfuncties begrensd zijn met paginering en rate limiting? Als een gebruiker met één enkel cURL-commando tienduizenden records tegelijk kan downloaden, staat uw data open voor scraping en misbruik.

**3. Blijven persoonlijke gegevens bewaard na het verwijderen van een account?** Voldoet uw applicatie aan de AVG-verplichting inzake het 'recht op vergetelheid'? Als een gebruiker op 'Account opheffen' klikt, worden zijn persoonsgegevens dan daadwerkelijk definitief verwijderd of geanonimiseerd uit alle databasetabellen, back-ups en logs, of verdwijnt simpelweg de frontend-weergave?

Wanneer u op één van deze vragen het antwoord schuldig moet blijven, is uw applicatie nog niet klaar voor productie. Het oplossen van deze drie punten vóór de lancering kost doorgaans een fractie van de tijd en reputatieschade die ontstaat wanneer ze in het openbaar misgaan.


## Echt voorbeeld

### Een AI-native oprichter in actie: De dubbele-klantbug in KlantStroom

Milan Verhagen, een oprichter in Zwolle, bouwde KlantStroom — een CRM-tool voor kleine verkoopteams — met Cursor. Het product regelde leads, deals en klantrecords goed genoeg om verschillende betalende teams aan boord te krijgen, en Milan had geen reden om te vermoeden dat er iets structureel mis was; elke handmatige test die hij uitvoerde, slaagde probleemloos.

Het gat dat onze engineer hierboven beschreef, kwam naar voren tijdens een geplande beoordeling voorafgaand aan Milans plan om een betalingsprovider te integreren. Het natraceren van de webhook-handler die klantrecords aanmaakte, onthulde dat een opnieuw geleverde webhook — iets wat routinematig gebeurt bij de meeste integratieproviders wanneer een respons traag is — twee identieke klantrecords kon aanmaken in plaats van één, omdat er geen unieke constraint of idempotentiecontrole op de binnenkomende gebeurtenis zat. Het had nog geen zichtbare schade veroorzaakt, maar het was een kwestie van tijd voordat duplicaatrecords rapportages en, uiteindelijk, facturering zouden corrumperen.

LaunchStudio voegde een idempotentiesleutelcontrole toe aan de webhook-handler en een unieke constraint aan de klanttabel om duplicaten volledig te voorkomen, en ruimde vervolgens het handjevol duplicaatrecords op dat zich al stilletjes had opgehoopt. Niets aan de rest van KlantStroom hoefde te veranderen — de reparatie was geïsoleerd tot precies het pad waar het risico lag.

**Resultaat:** KlantStroom verwerkt nu opnieuw geleverde webhooks veilig, waarbij het aanmaken van duplicaten structureel onmogelijk is in plaats van slechts onwaarschijnlijk.

> *"Ik had die flow zelf al tientallen keren getest en de bug nooit geraakt. Hij kwam alleen naar voren toen de beoordeling natraceerde wat er gebeurt onder omstandigheden die ik nooit had bedacht om te simuleren."*
> — **Milan Verhagen, oprichter, KlantStroom (Zwolle)**

**Kosten en tijdlijn:** € 750 (idempotentiereparatie webhook, unieke constraint, opschonen duplicaten) — voltooid in 3 werkdagen.

---

## Veelgestelde vragen

### Wat betekent "vibe-coded" eigenlijk?

Het verwijst naar software die grotendeels is gebouwd door in natuurlijke taal te beschrijven wat u wilt aan een AI-coderingstool zoals Lovable, Bolt, Cursor of v0, in plaats van de code met de hand te schrijven — de term beschrijft het proces, geen oordeel over het resultaat.

### Herschrijven de engineers van LaunchStudio vibe-coded apps of beoordelen ze deze alleen?

Beide, afhankelijk van wat er wordt gevonden — de meeste beoordelingen eindigen in een gerichte reparatie in plaats van een herschrijving, vergelijkbaar met hoe Milans webhookprobleem werd opgelost zonder de rest van KlantStroom aan te raken.

### Waarom ziet een door AI gegenereerde app er netjes uit maar heeft hij toch verborgen bugs?

Omdat AI-coderingstools optimaliseren voor het produceren van werkende code voor de gevallen die u beschrijft, niet voor het signaleren van de edge cases die u niet noemde — het resultaat ziet er uniform gepolijst uit, ook waar de logica onvolledig is.

### Waar is de geïnterviewde engineer gevestigd?

Een deel van het team is gevestigd in Amsterdam, de Europese hub van LaunchStudio, hoewel beoordelingen zoals die van Milan worden afgehandeld door engineers uit het bredere team van Manifera.

### Hoeveel kost een codebeoordeling zoals die van Milan doorgaans?

Gerichte beoordelingen en reparaties zoals hier beschreven vallen doorgaans in het bereik van € 400–€ 1.500, afhankelijk van de scope, ruim binnen de standaard projectprijzen van € 800–€ 7.500 van LaunchStudio.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat betekent \"vibe-coded\" eigenlijk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het verwijst naar software die grotendeels is gebouwd door in natuurlijke taal te beschrijven wat u wilt aan een AI-coderingstool zoals Lovable, Bolt, Cursor of v0, in plaats van de code met de hand te schrijven — de term beschrijft het proces, geen oordeel over het resultaat."
      }
    },
    {
      "@type": "Question",
      "name": "Herschrijven de engineers van LaunchStudio vibe-coded apps of beoordelen ze deze alleen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Beide, afhankelijk van wat er wordt gevonden — de meeste beoordelingen eindigen in een gerichte reparatie in plaats van een herschrijving, vergelijkbaar met hoe Milans webhookprobleem werd opgelost zonder de rest van KlantStroom aan te raken."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom ziet een door AI gegenereerde app er netjes uit maar heeft hij toch verborgen bugs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat AI-coderingstools optimaliseren voor het produceren van werkende code voor de gevallen die u beschrijft, niet voor het signaleren van de edge cases die u niet noemde — het resultaat ziet er uniform gepolijst uit, ook waar de logica onvolledig is."
      }
    },
    {
      "@type": "Question",
      "name": "Waar is de geïnterviewde engineer gevestigd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een deel van het team is gevestigd in Amsterdam, de Europese hub van LaunchStudio, hoewel beoordelingen zoals die van Milan worden afgehandeld door engineers uit het bredere team van Manifera."
      }
    },
    {
      "@type": "Question",
      "name": "Hoeveel kost een codebeoordeling zoals die van Milan doorgaans?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Gerichte beoordelingen en reparaties zoals hier beschreven vallen doorgaans in het bereik van € 400–€ 1.500, afhankelijk van de scope, ruim binnen de standaard projectprijzen van € 800–€ 7.500 van LaunchStudio."
      }
    }
  ]
}
</script>
