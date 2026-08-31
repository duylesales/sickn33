---
Titel: "Case Study: Een Freelance Designer Levert een Compleet Product zonder Een Regel Backend te Schrijven"
Trefwoorden: freelance designer backendpartner, designer levert product, white-label backendontwikkeling, technische partner ontwerpbureau, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Bureau / Freelancer (White-Label Partner)
---

# Case Study: Een Freelance Designer Levert een Compleet Product zonder Een Regel Backend te Schrijven

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Case Study: Een Freelance Designer Levert een Compleet Product zonder Een Regel Backend te Schrijven",
  "description": "Een freelance UX-designer in Leiden bouwde met AI-tools een prachtige frontend voor haar klant, en gebruikte LaunchStudio vervolgens als white-label backendpartner om een compleet, productieklaar product te leveren — waardoor een design-only opdracht een volledige productlevering werd, zonder een engineer aan te nemen.",
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
  "datePublished": "2026-12-31",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/freelance-designer-delivers-full-product-without-backend"
  }
}
</script>

Nina de Jong had een probleem dat de meeste freelance designers zouden herkennen. Haar klant — een boutique interieurontwerpbureau in Leiden — wilde een klantportaal waar huiseigenaren moodboards konden bekijken, materiaalkeuzes konden goedkeuren, projecttijdlijnen konden volgen, en mijlpaalbetalingen konden doen. Nina kon elk scherm ontwerpen, elke interactie prototypen, en een pixel-perfect Figma-bestand opleveren. Maar de klant wilde geen Figma-bestand. Ze wilden een werkend product. En de kloof tussen "ontworpen" en "werkend" was de kloof tussen Nina's vaardigheden en een productiebackend — authenticatie, database, betalingen, deployment — die ze nog nooit gebouwd had en niet wist te beoordelen als iemand anders die zou bouwen.

## Het Dilemma van de Freelancer

Nina had deze splitsing al eerder meegemaakt. In eerdere projecten had ze het op een van drie manieren aangepakt: de klant doorverwijzen naar een developer en zelf uit het project stappen (waarbij ze de controle over het eindproduct en de grotere opdracht verloor), samenwerken met een freelance developer die ze online had gevonden (wisselende kwaliteit, moeilijk te managen zonder technische kennis, en de klantrelatie ongemakkelijk verdeeld over twee contractors), of de projectscope afwijzen en alleen het ontwerp leveren (geld op tafel laten liggen en toekijken hoe de klant worstelde om iemand anders te vinden om te bouwen wat zij ontworpen had). Geen van deze opties was goed. Ze zijn allemaal wat de meeste designfreelancers doen.

## Wat Er Veranderde: AI-Tools en de Frontendkloof

Lovable veranderde Nina's rekensom. Met de AI-tool kon ze haar Figma-ontwerpen omzetten in een functionele React-frontend — geen statische mockups, maar interactieve pagina's met routing, animaties, formulierafhandeling en responsieve layouts die nauw aansloten bij haar ontwerpspecificaties, genoeg om aan de klant te demonstreren. Voor het eerst kon ze het zichtbare product zelf bouwen, creatieve controle behouden over elke pixel, en de klant iets presenteren dat aanvoelde als het uiteindelijke product.

De kloof was niet langer "ik kan niks bouwen." De kloof was: "ik kan alles bouwen wat de gebruiker ziet, maar niets wat de gebruiker eronder nodig heeft." Het klantportaal had gebruikersauthenticatie nodig (huiseigenaren en interieurontwerpers die inloggen met verschillende rechten), een database (opslaan van moodboardkeuzes, materiaalgoedkeuringen, tijdlijnupdates), betalingsverwerking (mijlpaalbetalingen via Mollie), e-mailmeldingen (goedkeuringsbevestigingen, betalingsbonnen), en deployment op een domein dat de klant beheerde. Niets hiervan was zichtbaar in de UI. Alles ervan was vereist om de UI te laten functioneren.

## Hoe het White-Label-Traject Werkte

Nina nam contact op met LaunchStudio nadat ze de dienst had gevonden via een verwijzing in een Nederlandse designcommunity op Slack. Het traject werd opgezet als een white-label-partnerschap: het engineeringteam van Manifera van LaunchStudio deed al het backendwerk onder Nina's merk, zonder klantcontact tussen de engineers en Nina's klant. Vanuit het perspectief van de klant leverde Nina het complete product — ontwerp, frontend, en een werkende backend.

De scope was specifiek: Supabase-authenticatie met rolgebaseerde toegang (huiseigenaar versus ontwerper), een PostgreSQL-database met Row-Level Security-policies die ervoor zorgden dat huiseigenaren alleen hun eigen projecten konden zien, Mollie-integratie voor mijlpaalbetalingen met webhookverificatie, e-mailmeldingen via Resend voor belangrijke events (nieuw moodboard gedeeld, materiaal goedgekeurd, betaling bevestigd), en deployment naar Vercel met het aangepaste domein van de klant, SSL, en basale uptime-monitoring.

Nina bleef eigenaar van de frontend — ze maakte ontwerpaanpassingen, voegde nieuwe pagina's toe, en verfijnde interacties in Lovable — terwijl LaunchStudio parallel de backend bouwde en testte. Communicatie verliep via een gedeeld projectkanaal, waarbij het Manifera-team zijn API-endpoints aanpaste aan de frontend die Nina bouwde, in plaats van andersom.

## De Levering

De klant ontving een compleet, productieklaar product: een klantportaal waar huiseigenaren konden inloggen, moodboards konden bekijken die de designer had geüpload, materialen konden selecteren met getoonde prijzen, keuzes konden goedkeuren met een digitale handtekening, mijlpaalbetalingen konden doen via Mollie, en hun projecttijdlijn konden bekijken — allemaal beveiligd met correcte authenticatie, dataisolatie en betalingsverificatie.

Nina's klant heeft nooit geweten dat LaunchStudio bestond. De factuur kwam van Nina. Het supportcontact was Nina. Het product droeg de branding van Nina's designstudio in de footer. Daarachter onderhielden de engineers van Manifera de infrastructuur onder het doorlopende Launch & Grow-supportplan.

**Resultaat:** Nina factureerde haar klant €8.500 voor de complete productlevering — haar ontwerptarief plus een marge op de backendontwikkelingskosten. Haar LaunchStudio-traject kostte €2.800, wat haar omzet opleverde die ze nooit had kunnen vangen binnen een design-only scope. Belangrijker nog: ze had een werkend product geleverd, geen Figma-bestand, en de perceptie van de klant over haar capaciteiten verschoof permanent van "onze designer" naar "de persoon die ons platform gebouwd heeft."

> *"Vroeger leverde ik een Figma-bestand op en hoopte ik dat de developer het niet zou verpesten. Nu lever ik een werkend product op en is de developer onzichtbaar. Mijn klanten denken dat ik alles doe, en technisch gezien doe ik dat ook — ik heb alleen een backendteam dat ze nooit zullen ontmoeten."*
> — **Nina de Jong, Freelance UX-Designer (Leiden)**

**Kosten & Doorlooptijd:** €2.800 (Launch & Grow Package, white-label backend + deployment + support) — geleverd in 11 werkdagen.

---

[LaunchStudio](https://launchstudio.eu/nl/) werkt als uw stille productiepartner — uw branding, uw klantrelatie, Manifera's engineering. Niemand hoeft het te weten.

[Vertel ons over uw volgende klantproject](https://launchstudio.eu/nl/#contact) — als u het kunt ontwerpen, kunnen wij het deel bouwen dat uw klant niet ziet.

---

## Veelgestelde Vragen

### Neemt LaunchStudio ooit rechtstreeks contact op met mijn klant tijdens een white-label-traject?

Nooit — alle communicatie verloopt via de freelancer of het bureau. LaunchStudio opereert als een backendpartner achter de schermen, zonder klantcontact, tenzij u dat specifiek aanvraagt.

### Kan ik de prijs van LaunchStudio ophogen bij het factureren aan mijn klant?

Absoluut — het white-label-model is hierop gebouwd. U bepaalt zelf uw prijs aan uw klant, en uw marge is uw eigen zaak. De factuur van LaunchStudio gaat naar u, niet naar uw klant.

### Wat als mijn klant na de eerste levering wijzigingen in de backend nodig heeft?

U kunt op elk moment aanvullend werk aanvragen bij LaunchStudio. Als het project op het Launch & Grow-supportplan zit, vallen bugfixes en kleine aanpassingen onder het maandelijkse plan. Nieuwe features worden als aparte trajecten gescoped.

### Heb ik technische kennis nodig om met LaunchStudio samen te werken als designpartner?

Minimaal — u moet kunnen beschrijven wat het product moet doen (wat u al kunt, aangezien u het ontworpen heeft), maar u hoeft niet te begrijpen hoe de backend het implementeert. Het Manifera-team vertaalt uw ontwerpspecificaties naar technische vereisten.

### Kan ik dit model gebruiken voor meerdere klanten, of is het een eenmalige regeling?

LaunchStudio werkt met meerdere freelancers en kleine bureaus op een doorlopende partnerbasis. Hoe meer projecten u inbrengt, hoe efficiënter de werkrelatie wordt, omdat het team uw ontwerppatronen en geprefereerde tools leert kennen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Neemt LaunchStudio ooit rechtstreeks contact op met mijn klant tijdens een white-label-traject?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nooit — alle communicatie verloopt via de freelancer of het bureau. LaunchStudio opereert als een backendpartner achter de schermen, zonder klantcontact, tenzij u dat specifiek aanvraagt."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik de prijs van LaunchStudio ophogen bij het factureren aan mijn klant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Absoluut — het white-label-model is hierop gebouwd. U bepaalt zelf uw prijs aan uw klant, en uw marge is uw eigen zaak. De factuur van LaunchStudio gaat naar u, niet naar uw klant."
      }
    },
    {
      "@type": "Question",
      "name": "Wat als mijn klant na de eerste levering wijzigingen in de backend nodig heeft?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "U kunt op elk moment aanvullend werk aanvragen bij LaunchStudio. Als het project op het Launch & Grow-supportplan zit, vallen bugfixes en kleine aanpassingen daaronder. Nieuwe features worden als aparte trajecten gescoped."
      }
    },
    {
      "@type": "Question",
      "name": "Heb ik technische kennis nodig om met LaunchStudio samen te werken als designpartner?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Minimaal — u moet kunnen beschrijven wat het product moet doen, maar u hoeft niet te begrijpen hoe de backend het implementeert. Het Manifera-team vertaalt uw ontwerpspecificaties naar technische vereisten."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik dit model gebruiken voor meerdere klanten, of is het een eenmalige regeling?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LaunchStudio werkt met meerdere freelancers en kleine bureaus op een doorlopende partnerbasis. Hoe meer projecten u inbrengt, hoe efficiënter de werkrelatie wordt."
      }
    }
  ]
}
</script>
