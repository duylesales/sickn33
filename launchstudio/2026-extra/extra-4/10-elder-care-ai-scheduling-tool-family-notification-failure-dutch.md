---
Titel: "AI-planningstools voor ouderenzorg: Wanneer een gemiste melding meer is dan een bug"
Trefwoorden: ai prototype, ai secure, elder care scheduling app, family notification system, ai-generated code
Koperfase: Bewustzijn
Doelgroep: AI-Native oprichter (niet-technisch)
---

# AI-planningstools voor ouderenzorg: Wanneer een gemiste melding meer is dan een bug

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-planningstools voor ouderenzorg: Wanneer een gemiste melding meer is dan een bug",
  "description": "In thuiszorg-planningsapps die met AI-tools zijn gebouwd, is een dienstwissel die geen nieuwe melding triggert geen klein randgeval.",
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

Hier is een mythe die het waard is om vroegtijdig met pensioen te sturen: "als het boekingssysteem werkt, werken de meldingen." In de meeste softwarecategorieën is dat ongeveer waar – een e-mailbevestiging is iets wat fijn is om te hebben, bovenop een werkende kernstroom. In de thuiszorgplanning is het precies het tegenovergestelde. De melding is geen laag bovenop het bezoek. Voor de familie die hun telefoon controleert, *is* de melding het bezoek, voor zover zij weten.

## De mythe: Boekingslogica en meldingslogica zijn hetzelfde ding

AI-bouwers zoals Bolt zijn oprecht goed in de kernboekingslus: de zorgverlener krijgt een dienst toegewezen, de klant ziet deze op een kalender, en iedereen krijgt een bevestiging. Waar ze aanzienlijk zwakker in zijn is de vertakkende logica die optreedt wanneer een plan achteraf verandert – specifiek een dienstwissel tussen twee zorgverleners. In een eenvoudige implementatie herverdeelt een dienstwissel gewoon een ID van de zorgverlener op een bestaande kalender-invoer. Het bezoek toont nog steeds als ingepland. Er vuurt geen nieuwe gebeurtenis af. Er gaat geen nieuwe melding uit. Vanuit het perspectief van het systeem is er niets gebeurd waar een familie over geïnformeerd hoefde te worden – het bezoek staat nog steeds "op de kalender", alleen met een andere naam eraan gekoppeld.

Het probleem is dat een dienstwissel exact het soort wijziging is waar een familie *wel* over geïnformeerd moet worden, vooral als de wissel mislukt, vertraging oplopt, of de vervangende zorgverlener een ander aankomstvenster heeft. Een stille hernieuwde toewijzing kan stilletjes veranderen in een bezoek dat nooit plaatsvindt, zonder dat de familie iets weet totdat ze vragen waarom hun ouder er slechter aan toe lijkt te zijn.

## Waarom dit een vertrouwensprobleem is, en geen randgeval

Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera, formuleert het zo: "We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer het omzetten van goede ideeën in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot wasdom te brengen. We hebben elf jaar ervaring in exact dat." Planning in de ouderenzorg is een haarscherp voorbeeld van wat hij bedoelt – het "idee" van een plannings-app is eenvoudig te prototypen. De architectuur die het betrouwbaar maakt wanneer een echte familie erop vertrouwt voor een echt bezoek is een ander, moeilijker probleem. En het is degene die de meeste met AI gegenereerde prototypes nog niet hebben opgelost.

Een gemiste melding in een context van ouderenzorg is geen ongemak. Het is de kloof tussen een familie die gelooft dat hun familielid is gecontroleerd en de werkelijkheid dat er niemand is opgekomen. Die kloof brengt echte consequenties met zich mee. Het is exact het soort scenario dat pas naar boven komt zodra een app echte zorgschema's afhandelt, en niet zodra het demodag-gegevens afhandelt.

## Wat een meldingsarchitectuur op productieniveau vereist

Het op de juiste manier herstellen hiervan betekent het behandelen van elke mutatie in het schema – en niet alleen de initiële boeking – als een gebeurtenis die een melding kan triggeren, en het expliciet definiëren welke mutaties dat moeten doen. Een dienstwissel, een tijdswijziging, een annulering en een niet-verschijnen hebben elk een eigen meldingsregel nodig, in plaats van te vertrouwen op de oorspronkelijke boekingsbevestiging om elke toekomstige status van dat bezoek te dekken. Ons team, werkend vanuit LaunchStudio's kantoor in Amsterdam, bouwt dit als een gebeurtenisgestuurde laag die achter de plannings-UI zit. Zo bereikt elke wijziging in de status van een bezoek – ongeacht welk scherm of welke beheerdersactie het heeft getriggerd – betrouwbaar de familie.

U kunt zien hoe dit soort beoordeling doorgaans werkt via [LaunchStudio's proces](https://launchstudio.eu/en/#process). En voor een gevoel van de engineeringstandaard op productieniveau erachter, omvat Manifera's [portfolio](https://www.manifera.com/portfolio/) werk voor gereguleerde, vertrouwenskritieke sectoren waar deze exacte discipline er toe doet.

## Verzonden betekent niet ontvangen

Het herstellen van het triggerprobleem – ervoor zorgen dat elke schemawijziging een melding afvuurt – lost de helft van het probleem op. De andere helft is dat "melding verzonden" en "familie heeft het daadwerkelijk gezien" niet dezelfde gebeurtenis zijn, en de meeste meldingssystemen volgen alleen de eerste. Een SMS kan stilletjes mislukken tegen een niet-aangesloten nummer. Een pushmelding kan mislukken tegen een app die de familie in weken niet heeft geopend. Een e-mail kan in de spambox belanden en daar ongelezen blijven zitten. Als het systeem "melding verzonden" als succes logt, ongeacht wat er daarna gebeurde, kan een familie technisch geïnformeerd zijn en functioneel nog steeds in het duister tasten. Dat is de exacte manier van mislukken die de herstelling hierboven moest dichten, alleen één laag stroomafwaarts.

Een meer verdedigbare versie volgt aflevering en bevestiging afzonderlijk van het verzenden, en escaleert wanneer geen van beide binnen een redelijk venster gebeurt:

```
async function notifyFamily(visitEvent, primaryContact, secondaryContact) {
  const result = await sendNotification(primaryContact, visitEvent);
  await logDelivery(visitEvent.id, primaryContact.id, result.status);

  scheduleCheck(visitEvent.id, '2 hours', async () => {
    const acknowledged = await wasAcknowledged(visitEvent.id, primaryContact.id);
    if (!acknowledged && secondaryContact) {
      await sendNotification(secondaryContact, visitEvent);
      await logDelivery(visitEvent.id, secondaryContact.id, 'escalated');
    }
  });
}
```

Dit hoeft niet ingewikkeld te zijn – een afleverlogboek en een enkel secundair contactpersoon dekken de meeste echte gevallen abdekken. Wat het niet kan zijn, is verondersteld. Een zorgfamilie die vertrouwt op een enkel, onbevestigd meldingskanaal is één geweigerde SMS verwijderd van het geloof dat een bezoek heeft plaatsgevonden terwijl niemand daadwerkelijk heeft bevestigd dat dat zo was.

## Echt voorbeeld

### Een AI-native oprichter in actie: De wissel die niemand aankondigde

Otto Jansen, een oprichter in Maastricht, bouwde ZorgAgenda – een planningstool voor thuiszorgorganisaties om bezoeken van zorgverleners te beheren en families geïnformeerd te houden – met behulp van Bolt. De kernstroom voor planning en familiemeldingen werkte goed bij vroege testen: boek een bezoek, familie krijgt een melding, bezoek vindt plaats, familie krijgt een voltooiingsupdate.

De kloof kwam naar boven toen twee zorgverleners een dienst onderling ruilden via de hernieuwde toewijzingsfunctie van de app. Het bezoek bleef exact zoals daarvoor op de kalender staan, alleen met een andere naam van de zorgverlener eraan gekoppeld. Er ging geen nieuwe melding uit naar de familie van de klant, omdat de app alleen meldingen stuurde bij initiële boeking en annulering – een hernieuwde toewijzing was geen herkende trigger. Wanneer de wissel van de vervangende zorgverlener mislukte en het bezoek daadwerkelijk nooit plaatsvond, had de familie geen enkele reden om te controleren. Hun laatste melding had immers bevestigd dat het bezoek was gepland en niets sindsdien had hen anders verteld.

LaunchStudio's ingenieurs herbouwden het meldingssysteem rond elke mutatie in de status van het schema in plaats van alleen de oorspronkelijke boeking, voegden expliciete wissel- en her-toewijzingsmeldingen toe, en introduceerden een bevestigingsstap voor het voltooien van het bezoek. Zo ontvangen families een duidelijk signaal wanneer een bezoek daadwerkelijk plaatsvindt, en niet alleen wanneer het gepland is.

**Resultaat:** families ontvangen nu een melding voor elke materiële wijziging in een gepland bezoek, wat de kloof dicht tussen wat de kalender toont en wat er daadwerkelijk is gebeurd.

> *"Ik testte het boeken van een bezoek en het annuleren van een bezoek. Ik heb nooit getest dat twee zorgverleners een dienst onderling ruilden – en dat bleek exact het scenario te zijn waarin een familie in het duister werd gelaten."*
> — **Otto Jansen, Oprichter, ZorgAgenda (Maastricht)**

**Kosten en tijdlijn:** € 900 (gebeurtenisgestuurde meldingsarchitectuur, triggers voor dienstwissel en her-toewijzing, bevestigingen van voltooiing van het bezoek) — voltooid in 4 werkdagen.

---

## Veelgestelde vragen

### Waarom ving het oorspronkelijke meldingssysteem een dienstwissel niet op?

Omdat de app alleen de initiële boeking en annulering behandelde als gebeurtenissen die een melding waard waren – een hernieuwde toewijzing veranderde wie er aan een bezoek was toegewezen zonder de status van het bezoek te veranderen, dus er vuurde geen nieuwe meldingslogica af.

### Is dit een veelvoorkomende kloof in met AI gegenereerde planningstools?

Ja – AI-bouwers implementeren betrouwbaar de primaire stroom die in een prompt wordt beschreven, maar hebben de neiging om secundaire statuswijzigingen zoals wissels, herplanningen en hernieuwde toewijzingen te missen, tenzij ze elk expliciet worden gespecificeerd.

### Hoe denkt Herre Roelevink over dit soort risico's?

Hij is er direct over geweest dat het moeilijke deel van software vandaag de dag niet het genereren van het idee is – het is de architectuur en beveiliging die een product betrouwbaar maken bij volwassenheid, wat precies de kloof is tussen een werkende demo en een systeem waar families op kunnen vertrouwen.

### Wat veranderd LaunchStudio daadwerkelijk om dit te herstellen?

We herbouwen de meldingslaag om gebeurtenisgestuurd te zijn over elke mutatie in het schema, in plaats van alleen gekoppeld te zijn aan de oorspronkelijke boeking, zodat elke wijziging in een bezoek betrouwbaar de mensen bereikt die het moeten weten.

### Wat gebeurt er als een familie de melding die de app stuurt nooit daadwerkelijk ziet?

Zonder afzonderlijke tracking voor aflevering en bevestiging: niets – het systeem logt het bericht als verzonden en gaat verder. Daarom controleert een verdedigbare opzet of een melding werd geopend of bevestigd, en escaleert naar een secundair contactpersoon als dat niet zo was.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom opende het meldingssysteem geen waarschuwing bij een dienstwissel?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De app zag alleen boeken en annuleren als relevante triggers. Een wissel veranderde wel de zorgverlener, maar niet de status van de afspraak."
      }
    },
    {
      "@type": "Question",
      "name": "Komt dit meldingsprobleem vaak voor bij AI-planningstools?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, AI-tools richten de primaire workflow in, maar vergeten secundaire statuswijzigingen zoals dienstwissels en herindelingen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat zegt Herre Roelevink over dit soort systeemrisico's?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Herre Roelevink benadrukt dat niet het idee, maar de architectuur en betrouwbaarheid het echte verschil maken voor volwassen software."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe herstelt LaunchStudio dit meldingsprobleem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Door een event-driven meldingsarchitectuur in te richten die bij elke statuswijziging (dus ook wissels) direct de familie informeert."
      }
    },
    {
      "@type": "Question",
      "name": "Wat gebeurt er als een familie een pushmelding of SMS mist?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een robuust systeem houdt aflevering én leesbevestiging bij, en escaleert naar een tweede contactpersoon bij geen gehoor."
      }
    }
  ]
}
</script>