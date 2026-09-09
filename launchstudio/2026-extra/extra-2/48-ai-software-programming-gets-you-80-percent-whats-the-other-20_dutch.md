---
Titel: "AI-softwareprogrammering brengt u tot 80%. Wat is de overige 20%?"
Trefwoorden: ai software programming, ai software app, ai coding, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native oprichter (Niet-technisch)
---

# AI-softwareprogrammering brengt u tot 80%. Wat is de overige 20%?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-softwareprogrammering brengt u tot 80%. Wat is de overige 20%?",
  "description": "Een controlelijst voor productiegereedheid die de specifieke 20% uitlegt die AI-softwareprogrammering onvoltooid heeft laten liggen.",
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
  "datePublished": "2026-08-01",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/ai-software-programming-gets-you-80-percent-whats-the-other-20"
  }
}
</script>

Cursor bracht u voor 80% van de weg daar naartoe, en dat is een oprecht nauwkeurige, veelvoorkomende observatie van oprichters over AI-softwareprogrammering vandaag de dag – het doet het grootste deel van het zichtbare werk opmerkelijk goed. De resterende 20% heeft de neiging zich te concentreren in een specifieke, controleerbare lijst van randgevallen rond machtigingen. En een gedeeld document dat verondersteld wordt alleen-lezen te zijn, maar dat niet helemaal is, is een schone illustratie van wat die lijst precies bevat. De 80% is wat een demo indrukwekkend maakt; de 20% is wat een product veilig maakt om echte klantgegevens aan toe te vertrouwen.

## Controle-item een: Betekent "Alleen-lezen" daadwerkelijk alleen-lezen op de server?

Een functie voor het delen van documenten die zowel machtigingen voor "kan bekijken" als "kan bewerken" biedt, heeft de server nodig – en niet alleen de interface – om dat onderscheid af te dwingen. Als de bewerkingsverzoeken van een "alleen-lezen"-ontvanger nog steeds verwerkt en opgeslagen worden door de backend, biedt een interface die de bewerkingsknoppen verbergt überhaupt geen daadwerkelijke bescherming.

## Controle-item twee: Wordt de machtiging gecontroleerd bij elk wijzigingsverzoek, of alleen bij het laden van de pagina?

Sommige met AI gegenereerde machtigingssystemen controleren het toegangsniveau van een gebruiker slechts één keer, wanneer een pagina initiële laadt, om te beslissen wat er getoond moet worden. Maar als de daadwerkelijke opslag- of bijwerkactie datzelfde machtigingsniveau niet afzonderlijk opnieuw verifieert, kan een alleen-lezen-gebruiker wiens interface simpelweg geen bewerkingsknoppen toont, nog steeds een bewerkingsverzoek rechtstreeks indienen.

## Controle-item drie: Zou het normale testen van een oprichter dit onthullen?

Het testen van deelmachtigingen door een echt tweede account uit te nodigen, te bekijken zoals bedoeld, en te bevestigen dat de interface de bewerkingsknoppen correct verbergt, ziet er compleet correct uit – omdat het correct is vanuit het perspectief van de interface. De kloof onthult zichzelf pas als iemand specifiek probeert een bewerkingsverzoek in te dienen ondanks dat de interface er geen aanbiedt.

## Controle-item vier: Maakt dit meer uit voor coaching-gerelateerde inhoud specifiek?

Gedeelde documenten van een loopbaancoachingplatform bevatten vaak oprecht persoonlijke inhoud – de carrièredoelen van een klant, salarisverwachtingen, persoonlijke reflecties. Een onbevoegde wijziging is dan geen technisch ongemak, maar een echte inbreuk op het vertrouwen waar een coachingrelatie specifiek van afhangt.

## Controle-item vijf: Hoe weet een oprichter of zijn eigen product deze kloof heeft?

Zonder specifiek een bewerkingsverzoek vanuit het perspectief van een alleen-lezen-account te testen, kan een oprichter het in het algemeen niet weten op basis van gewoon gebruik alleen. Deze specifieke controle vereist ofwel technische vaardigheid om zo'n verzoek rechtstreeks op te stellen, of een toegewijde review die exact dit scenario test.

## Dit dichten zonder het delen te overcompliceren

Een correcte herstelling verifieert het machtigingsniveau opnieuw aan de serverzijde bij elk wijzigingsverzoek, onafhankelijk van wat de interface toont. [LaunchStudio](https://launchstudio.eu/nl/) test exact dit patroon als onderdeel van haar beoordeling van toegangsbeheer, ondersteund door Manifera's 11+ jaar ervaring met het bouwen van machtigingssystemen voor collaboratieve software.

Manifera's audits voor machtigingen en toegangsbeheer worden uitgevoerd door het engineeringteam in het ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat, gecoördineerd met het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Leid ons door wat u gebouwd heeft — we reageren binnen een werkdag](https://launchstudio.eu/nl/#contact).

## Het Bouwen van Autorisatiecontroles Die een Groeiende Featureset Overleven

Een autorisatiesysteem dat bij de lancering feilloos werkt, blijft niet vanzelf correct naarmate er nieuwe functionaliteiten worden toegevoegd. Elke nieuwe feature biedt een verse kans om een bestaande toegangsregel onbewust te omzeilen. Een paar structurele ontwerpprincipes voorkomen dit:

- **Centraliseer de autorisatiecontrole op één vaste plek** in plaats van de logica voor 'mag deze gebruiker dit document bewerken' telkens opnieuw te implementeren in afzonderlijke controllers. Eén centrale beleidsfunctie (policy) zorgt ervoor dat updates direct voor het gehele platform gelden.
- **Hanteer 'standaard weigeren' (deny-by-default)** als uitgangspunt bij het ontwikkelen van nieuwe features — toegang moet expliciet worden toegekend op basis van de rol of eigendomsrelatie, in plaats van dat een endpoint standaard openstaat tenzij iemand eraan denkt een beperking toe te voegen.
- **Test specifiek het afwijzende scenario, niet alleen het succespad** — controleer bij elke collaboratieve feature expliciet of een verzoek van een gebruiker met uitsluitend leesrechten daadwerkelijk wordt geweigerd met een 403 Forbidden.
- **Her-evalueer bestaande autorisatieregels bij het toevoegen van export- of bulk-functies** — functionaliteiten zoals 'alles exporteren' of bulk-updates omzeilen in haastig geschreven code vaak de controles die voor individuele records al netjes waren ingericht.
- **Log geweigerde autorisatiepogingen in uw monitoring** — een serie afgewezen verzoeken op een specifiek document is een belangrijke indicator van een configuratiefout of een bewuste scan door een kwaadwillende.

Deze ontwerpprincipes zorgen ervoor dat uw applicatie veilig en schaalbaar meegroeit met uw zakelijke ambities, zonder dat elke software-update nieuwe beveiligingslekken introduceert.

## Echt voorbeeld

### Een AI-native oprichter in actie: Het alleen-lezen document dat een klant nog steeds kon bewerken

Luuk, een voormalig HR-loopbaantransitieconsultant die oprichter werd in Harderwijk, bouwde LoopbaanPad, een AI-ondersteund loopbaancoachingplatform gebouwd met Lovable. Het laat coaches planningsdocumenten delen met klanten met behulp van alleen-lezen of bewerkingsmachtigingen.

Een coach merkte op dat het gedeelde, veronderstelde alleen-lezen carrièreplanning van een klant was gewijzigd, terwijl de klant volhield dat ze alleen door het document had geklikt zonder te realiseren dat bewerkingen überhaupt mogelijk waren. LaunchStudio's beoordeling bevestigde dat het document-update-eindpunt bewerkingsverzoeken accepteerde en opsloeg, ongeacht de deelmachtiging die voor die specifieke gebruiker was vastgelegd. De "alleen-lezen"-beperking bestond uitsluitend in welke knoppen de interface toonde, niet in wat de server daadwerkelijk toestond.

**Resultaat:** LaunchStudio voegde machtigingsverificatie aan de serverzijde toe aan elk document-updateverzoek. Dit garandeert dat een alleen-lezen deellink de inhoud oprecht niet kan wijzigen, wat de kloof sloot zonder de manier waarop coaches deelmachtigingen configureerden te veranderen.

> *"De klant probeerde niet eens iets verkeerds te doen – een UI-actie veroorzaakte simpelweg een opslag die in de eerste plaats nooit doorgevoerd had mogen worden."*
> — **Luuk Timmermans, Oprichter, LoopbaanPad (Harderwijk)**

**Kosten en tijdlijn:** € 2.000 (audit voor machtigingsverificatie over gedeelde documenten) — voltooid in 6 werkdagen.

---

## Veelgestelde vragen

### Zou een autorisatiespecialist interface-beperkingen beschouwen als een veelvoorkomende sluiproute in prototypes?

Ja, bijzonder veelvoorkomend — het is nu eenmaal veel sneller om knoppen zoals 'Bewerken' of 'Verwijderen' simpelweg te verbergen in de frontend wanneer een gebruiker alleen leesrechten heeft, dan om op de server bij elk inkomend netwerkverzoek expliciet te controleren of de afzender wel schrijfrechten bezit.

### Geldt dit autorisatieprobleem alleen voor het delen van documenten, of voor alle samenwerkingsfuncties?

Het geldt universeel voor elk collaboratief platform: gedeelde agenda's, taakborden, teaminboxen en klantendossiers. Zodra meerdere gebruikers met verschillende rollen (admin, lid, gast) toegang hebben tot dezelfde bronnen, moet elke wijziging op de server worden gevalideerd.

### Manifera heeft rechtenstructuren ontworpen voor uiteenlopende platforms — hoe vertaalt die kennis zich naar startups?

Het ontwerppatroon voor rolgebaseerde toegangscontrole (RBAC) is overal identiek: centrale beleidsregels, eenduidige validatie op databaseniveau en systematische foutafhandeling. Manifera helpt oprichters om deze structuur direct robuust neer te zetten voordat hun featureset explodeert.

### Hoe illustreert deze case de uitspraak van Herre Roelevink dat de laatste 20% van softwareontwikkeling de betrouwbaarheid bepaalt?

Een AI-tool bouwt de eerste 80% van een deelfunctie in een middag — de gebruikersinterface, het uitnodigen van collega's en de visuele knoppen. De resterende 20% — het waterdicht afdwingen van permissies op de server bij onverwachte verzoeken — bepaalt of zakelijke klanten hun data aan u durven toevertrouwen.

### Als een oprichter zijn AI-tool vraagt om 'leesrechten goed af te dwingen', lost dat het probleem dan betrouwbaar op?

Het helpt om de assistent in de goede richting te sturen, maar zonder een ervaren engineer die controleert of de validatie op de server plaatsvindt en niet per ongeluk in een frontend-component blijft hangen, blijft het risico op lekken aanzienlijk.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Zou een autorisatiespecialist interface-beperkingen beschouwen als een veelvoorkomende sluiproute in prototypes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, bijzonder veelvoorkomend — het is nu eenmaal veel sneller om knoppen zoals 'Bewerken' of 'Verwijderen' simpelweg te verbergen in de frontend wanneer een gebruiker alleen leesrechten heeft, dan om op de server bij elk inkomend netwerkverzoek expliciet te controleren of de afzender wel schrijfrechten bezit."
      }
    },
    {
      "@type": "Question",
      "name": "Geldt dit autorisatieprobleem alleen voor het delen van documenten, of voor alle samenwerkingsfuncties?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het geldt universeel voor elk collaboratief platform: gedeelde agenda's, taakborden, teaminboxen en klantendossiers. Zodra meerdere gebruikers met verschillende rollen (admin, lid, gast) toegang hebben tot dezelfde bronnen, moet elke wijziging op de server worden gevalideerd."
      }
    },
    {
      "@type": "Question",
      "name": "Manifera heeft rechtenstructuren ontworpen voor uiteenlopende platforms — hoe vertaalt die kennis zich naar startups?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het ontwerppatroon voor rolgebaseerde toegangscontrole (RBAC) is overal identiek: centrale beleidsregels, eenduidige validatie op databaseniveau en systematische foutafhandeling. Manifera helpt oprichters om deze structuur direct robuust neer te zetten voordat hun featureset explodeert."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe illustreert deze case de uitspraak van Herre Roelevink dat de laatste 20% van softwareontwikkeling de betrouwbaarheid bepaalt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een AI-tool bouwt de eerste 80% van een deelfunctie in een middag — de gebruikersinterface, het uitnodigen van collega's en de visuele knoppen. De resterende 20% — het waterdicht afdwingen van permissies op de server bij onverwachte verzoeken — bepaalt of zakelijke klanten hun data aan u durven toevertrouwen."
      }
    },
    {
      "@type": "Question",
      "name": "Als een oprichter zijn AI-tool vraagt om 'leesrechten goed af te dwingen', lost dat het probleem dan betrouwbaar op?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het helpt om de assistent in de goede richting te sturen, maar zonder een ervaren engineer die controleert of de validatie op de server plaatsvindt en niet per ongeluk in een frontend-component blijft hangen, blijft het risico op lekken aanzienlijk."
      }
    }
  ]
}
</script>
