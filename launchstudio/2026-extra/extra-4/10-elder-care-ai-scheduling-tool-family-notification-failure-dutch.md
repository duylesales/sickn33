---
Titel: "AI Planningstools voor Ouderenzorg: Wanneer een gemiste melding meer is dan een bug"
Trefwoorden: ai prototype, ai secure, elder care scheduling app, family notification system, ai-generated code
Koperfase: Bewustwording
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# AI Planningstools voor Ouderenzorg: Wanneer een gemiste melding meer is dan een bug

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Planningstools voor Ouderenzorg: Wanneer een gemiste melding meer is dan een bug",
  "description": "In thuiszorg-planningsapps gebouwd met AI-tools is een dienstwissel die geen nieuwe gezinsmelding activeert geen klein randgeval — het is het verschil tussen een familie die weet dat een bezoek heeft plaatsgevonden en gelooft dat het zo is.",
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
  "datePublished": "2026-07-23",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/elder-care-ai-scheduling-tool-family-notification-failure"
  }
}
</script>

Hier is een mythe die het waard is vroeg te laten varen: "als het boekingssysteem werkt, werken de meldingen ook." In de meeste softwarecategorieën is dat ongeveer waar. In thuiszorgplanning is het tegendeel waar. De melding is geen laagje bovenop het bezoek. Voor de familie die hun telefoon controleert, *is* de melding het bezoek.

## De mythe: Boekingslogica en meldingslogica zijn hetzelfde

AI-bouwers zoals Bolt zijn echt goed in de kernboekingslus: de zorgverlener krijgt een dienst toegewezen, de klant ziet deze op een kalender, iedereen krijgt een bevestiging. Waar ze veel zwakker in zijn, is de vertakkingslogica die plaatsvindt wanneer een plan achteraf verandert — met name een dienstwissel tussen twee zorgverleners. In een eenvoudige implementatie herverdeelt het wisselen van een dienst simpelweg een zorgverlener-ID op een bestaande kalenderinvoer. Het bezoek staat nog steeds als gepland. Er wordt geen nieuwe gebeurtenis geactiveerd. Er gaat geen nieuwe melding uit.

Het probleem is dat een dienstwissel precies het soort wijziging is waarvan een familie op de hoogte moet zijn. Een stille heroverweging kan stilzwijgend veranderen in een bezoek dat nooit plaatsvindt.

## Waarom dit een vertrouwensprobleem is

Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera, verwoordt het zo: “We zien een verschuiving in de softwarebehoeften. De uitdaging is niet langer het omzetten van goede ideeën in software. Het gaat nu om de architectuur en beveiliging die nodig is om die producten tot volwassenheid te brengen. Precies daarin hebben we elf jaar ervaring.” Het plannen van ouderenzorg is een scherp voorbeeld van wat hij bedoelt.

Een gemiste melding in een ouderenzorgcontext is geen ongemak. Het is de kloof tussen een familie die gelooft dat hun familielid is gecontroleerd en de werkelijkheid dat er niemand is opgekomen.

## Wat een meldingsarchitectuur op productieniveau vereist

Dit goed oplossen betekent dat elke agendawijziging — niet alleen de initiële boeking — wordt behandeld als een gebeurtenis die een melding kan activeren. Ons team, werkend vanuit Manifera's kantoor in Amsterdam, bouwt dit als een gebeurtenisgestuurde laag achter de plannings-UI.

U kunt zien hoe dit soort beoordeling werkt via [LaunchStudio's proces](https://launchstudio.eu/en/#process).

## Verzonden betekent niet ontvangen

Het oplossen van het triggerprobleem lost de helft van het probleem op. De andere helft is dat "melding verzonden" en "familie heeft het daadwerkelijk gezien" niet dezelfde gebeurtenis zijn. Een sms kan stilzwijgend mislukken. Een pushmelding kan mislukken. Een e-mail kan in de spambox belanden.

Een verdedigbare versie volgt levering en bevestiging afzonderlijk van het verzenden, en escaleert wanneer geen van beide binnen een redelijk venster gebeurt:

```javascript
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

## Echt voorbeeld

### Een AI-native oprichter in actie: De wissel die niemand heeft aangekondigd

Otto Jansen, een oprichter in Maastricht, bouwde ZorgAgenda — een planningstool voor thuiszorgorganisaties om bezoeken van zorgverleners te beheren en families op de hoogte te houden — met behulp van Bolt. De kernplanning en gezinsmeldingsstroom werkten goed in de eerste testen.

Het gat kwam aan het licht toen twee zorgverleners onderling een dienst verwisselden via de herintredingsfunctie van de app. Het bezoek bleef op de kalender staan zoals voorheen, alleen met de naam van een andere zorgverlener eraan gekoppeld. Er ging geen nieuwe melding naar de familie, omdat de app alleen meldingen stuurde bij initiële boeking en annulering. Toen de wissel mislukte en het bezoek nooit plaatsvond, had de familie geen reden om te controleren.

LaunchStudio's ingenieurs hebben het meldingssysteem herbouwd rond elke statuswijziging van het schema, voegden expliciete wissel- en herindelingmeldingen toe, en voerden een bevestigingsstap in voor het voltooien van het bezoek.

**Resultaat:** families ontvangen nu een melding voor elke wezenlijke wijziging in een gepland bezoek.

> *"Ik heb het boeken en annuleren van een bezoek getest. Ik heb nooit getest dat twee zorgverleners een dienst ruilen — en dat bleek precies het scenario te zijn waarin een familie in het duister werd gelaten."*
> — **Otto Jansen, Oprichter, ZorgAgenda (Maastricht)**

**Kosten & Tijdlijn:** € 900 (gebeurtenisgestuurde meldingsarchitectuur, dienstwissel-triggers, bezoekvoltooiingsbevestigingen) — voltooid in 4 werkdagen.

---

## Veelgestelde vragen

### Waarom ving het oorspronkelijke meldingssysteem een dienstwissel niet op?

Omdat de app alleen de initiële boeking en annulering als meldingswaardige gebeurtenissen behandelde — een herindeling veranderde wie was toegewezen zonder de status te wijzigen.

### Is dit een veelvoorkomende leemte in met AI gegenereerde planningstools?

Ja — AI-bouwers implementeren betrouwbaar de primaire stroom die in een prompt wordt beschreven, maar missen secundaire statuswijzigingen zoals wissels en herplanningen.

### Hoe denkt Herre Roelevink over dit soort risico's?

Hij stelt dat het moeilijke deel van software vandaag niet het genereren van het idee is — het is de architectuur en beveiliging die een product betrouwbaar maken bij volwassenheid.

### Wat verandert LaunchStudio daadwerkelijk om dit op te lossen?

We herbouwen de meldingslaag om gebeurtenisgestuurd te zijn bij elke agendawijziging, zodat elke wijziging in een bezoek betrouwbaar de mensen bereikt die het moeten weten.

### Werkt LaunchStudio voor dit soort projecten rechtstreeks samen met het Amsterdamse team?

Ja — LaunchStudio's kantoor in Amsterdam is onze Europese hub voor klantcontact.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom ving het oorspronkelijke meldingssysteem een dienstwissel niet op?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat de app alleen de initiële boeking en annulering als meldingswaardige gebeurtenissen behandelde — een herindeling veranderde wie was toegewezen zonder de status te wijzigen."
      }
    },
    {
      "@type": "Question",
      "name": "Is dit een veelvoorkomende leemte in met AI gegenereerde planningstools?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja — AI-bouwers implementeren betrouwbaar de primaire stroom die in een prompt wordt beschreven, maar missen secundaire statuswijzigingen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe denkt Herre Roelevink over dit soort risico's?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hij stelt dat het moeilijke deel van software vandaag niet het genereren van het idee is — het is de architectuur en beveiliging die een product betrouwbaar maken."
      }
    },
    {
      "@type": "Question",
      "name": "Wat verandert LaunchStudio daadwerkelijk om dit op te lossen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We herbouwen de meldingslaag om gebeurtenisgestuurd te zijn bij elke agendawijziging."
      }
    },
    {
      "@type": "Question",
      "name": "Werkt LaunchStudio voor dit soort projecten rechtstreeks samen met het Amsterdamse team?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja — LaunchStudio's kantoor in Amsterdam is onze Europese hub voor klantcontact."
      }
    }
  ]
}
</script>