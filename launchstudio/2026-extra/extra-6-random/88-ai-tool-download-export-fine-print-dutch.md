---
Titel: "De exportknop die elke AI-codeertool heeft, en waarvan niemand de kleine lettertjes leest"
Trefwoorden: ai tool download, ai code export terms, ai builder export rights, exporting ai generated code
Koperfase: Overweging
Doelgroep: AI-Native oprichter (niet-technisch)
---
# De exportknop die elke AI-codeertool heeft, en waarvan niemand de kleine lettertjes leest

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "De exportknop die elke AI-codeertool heeft, en waarvan niemand de kleine lettertjes leest",
  "description": "Elke AI-tool-download of exportfunctie komt met voorwaarden die niemand leest totdat het ertoe doet. Dit is hoe u de kleine lettertjes van een AI-tool-download daadwerkelijk controleert voordat zes maanden aan klantgegevens die codebase raken.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-tool-download-export-fine-print" }
}
</script>

Elke AI-codeertool die de moeite waard is om te gebruiken heeft een export- of downloadknop, en bijna elke oprichter klikt daar precies één keer op — de dag dat ze van hostingprovider moeten wisselen, een ontwikkelaar aan boord halen, of om een andere praktische reden van het platform af moeten stappen. Die ene klik is meestal de eerste keer dat iemand de bijbehorende voorwaarden leest, en tegen die tijd is wat die voorwaarden zeggen vaak al maanden waar. Dit is hoe u de kleine lettertjes van een AI-tool-download daadwerkelijk controleert voordat het ertoe doet, niet erna.

## Stap 1: Vind de daadwerkelijke voorwaarden, niet de marketingpagina

De meeste AI-codeerplatforms hebben twee heel verschillende documenten: een marketingpagina die het exporteren van uw code beschrijft als een eenvoudige, oprichtersvriendelijke functie, en een gebruiksvoorwaarden- of gebruiksovereenkomstdocument dat uiteenzet welke rechten het platform behoudt over code die er via is gegenereerd. De voorwaarden die u nodig heeft, zijn bijna nooit degene die vanaf de exportknop zelf zijn gelinkt — zoek rechtstreeks op de juridische of gebruiksvoorwaardenpagina's van het platform, en let specifiek op taal over "gegenereerde content", "output" of "trainingsdata", niet alleen "uw code" of "eigendom".

## Stap 2: Zoek specifiek naar behouden trainingsrechten

De clausule die oprichters het vaakst verrast, gaat niet over wie de code bezit — de meeste platforms zijn redelijk duidelijk dat u bezit wat u heeft gebouwd. Het gaat om of het platform het recht behoudt om de code die u heeft gegenereerd, of patronen daaruit, te gebruiken om toekomstige versies van hun model te trainen. Dit is een apart recht van eigendom, en het kan bestaan zelfs in voorwaarden die duidelijk zeggen dat de code van u is. Lees specifiek voor uitdrukkingen als "mag output gebruiken om onze diensten te verbeteren" of "voor doeleinden van modeltraining en -ontwikkeling" — dit zijn de clausules die ertoe doen.

## Stap 3: Controleer wat er gebeurt met code die u al heeft gegenereerd

De voorwaarden van sommige platforms gelden vanaf het moment dat u ermee instemt; andere gelden met terugwerkende kracht voor alles wat u al op het platform heeft gebouwd. Als uw product al maanden live is tegen de tijd dat u de voorwaarden daadwerkelijk zorgvuldig leest, doet dit onderscheid ertoe — u wilt weten of zes maanden aan klantgegevens en bedrijfslogica in die codebase gedekt zijn door welke rechten het platform ook heeft geclaimd, of alleen werk dat na een specifieke datum is gegenereerd.

## Stap 4: Bepaal of de voorwaarden uw exporttijdlijn veranderen

Als u een clausule vindt die u zorgen baart — behouden trainingsrechten over code die echte klantgegevens raakt, bijvoorbeeld — is de praktische vraag niet of u moet panikeren, maar of u uw export- en migratietijdlijn moet versnellen. Uw code zo snel mogelijk naar infrastructuur brengen die u volledig zelf beheert, is meestal de meest directe manier om te beperken hoeveel van de geschiedenis van uw product onderworpen blijft aan de bredere voorwaarden van een platform.

## Stap 5: Laat het nog eens nalezen voordat u iets nieuws ondertekent

Als u een nieuw AI-codeerplatform evalueert voor een toekomstig project, lees dan de export- en trainingsrechtenvoorwaarden vóórdat u er iets van waarde op bouwt, niet erna. Tien minuten lezen aan het begin bespaart de haast die ontstaat wanneer een oprichter, midden in een migratie, ontdekt dat voorwaarden die ze nooit grondig hebben gelezen de hele tijd van toepassing waren.

LaunchStudio wordt mogelijk gemaakt door Manifera, een softwareontwikkelingsbedrijf met meer dan 11 jaar ervaring in het helpen van oprichters om door AI gegenereerde prototypes naar infrastructuur te verplaatsen die ze volledig zelf bezitten, en ons team, werkend vanuit Amsterdam, behandelt routinematig precies dit soort export en migratie voor oprichters die net hebben ontdekt wat de voorwaarden van hun platform daadwerkelijk zeggen. Als u midden in een export zit en een tweede blik wilt op wat u ziet, kunt u [uw project beschrijven via ons proces](https://launchstudio.eu/nl/#process) en wij helpen u begrijpen waarmee u daadwerkelijk instemt. De bredere ervaring van Manifera met het verplaatsen van software tussen platforms staat beschreven op de pagina [maatwerksoftwareontwikkeling](https://www.manifera.com/services/custom-software-development/).

## Een Zoek-en-Vind Lijst: Exacte Woorden om met Ctrl-F te Zoeken in Algemene Voorwaarden

Niemand leest met plezier de algemene voorwaarden van twintig pagina's van cloud- en AI-leveranciers. Open het document in uw browser, druk op Ctrl+F (of Cmd+F) en zoek specifiek naar deze vijf beslissende termen:

**1. Zoek op: "train" of "training"** Controleer of de leverancier uw gegevens mag gebruiken voor het trainen van eigen modellen. Zoek naar zinnen als *"We do not use customer data to train our models"* (veilig) versus *"You grant us a perpetual right to use inputs to improve our services"* (gevaarlijk).

**2. Zoek op: "retention" of "retain"** Hoe lang bewaart de leverancier uw data op zijn servers voor misbruikcontrole? Dertig dagen is gebruikelijk, maar voor gevoelige data eist u 'Zero Retention'.

**3. Zoek op: "sub-processor" of "third party"** Welke andere bedrijven schakelt de leverancier stiekem in? In het kader van de AVG moet u al deze partijen kunnen verantwoorden aan uw eigen klanten.

**4. Zoek op: "indemnif" (Indemnification)** Vrijwaart de aanbieder u tegen claims van derden wegens inbreuk op auteursrechten door gegenereerde content?

**5. Zoek op: "governing law" of "jurisdiction"** Welk recht is van toepassing? Voor Europese bedrijven is Nederlands recht of een rechtbank binnen de EU oneindig veel veiliger dan arbitrage in Californië of Delaware.

Binnen vijf minuten heeft u de juridische kern blootgelegd en weet u exact of u een zakelijk verantwoorde overeenkomst aangaat.
## Echt voorbeeld

### Een AI-native oprichter in actie: de exportknop die meer vragen opriep dan beantwoordde

Fleur Lisse, een oprichter in Lisse, bouwde "BloemBestel" — een bloemenbestelbeheertool voor bloemisten — met Bolt. Zes maanden na lancering, met echte klantgegevens die dagelijks door de app stroomden, besloot ze van hostingprovider te wisselen om kostenredenen en gebruikte ze de exportfunctie van het platform om haar code eruit te halen.

Pas tijdens het exportproces las Fleur de bijbehorende voorwaarden voor het eerst daadwerkelijk zorgvuldig door. Verstopt in de gebruiksovereenkomst van het platform stond een clausule die het recht van de AI-leverancier behield om delen van gegenereerde code — inclusief code specifiek gegenereerd voor BloemBestel — te hergebruiken in toekomstige modeltraining. Niets in de voorwaarden suggereerde dat dit met terugwerkende kracht beperkt was tot code gegenereerd vóór een bepaalde afsluitdatum; het leek alles te dekken wat ze op het platform had gebouwd, inclusief logica die was gevormd door maanden aan echte klant- en bedrijfsgegevens.

Fleur bracht de situatie naar LaunchStudio, met de wens om zowel te begrijpen wat de voorwaarden daadwerkelijk betekenden als hoe verder te gaan. Onze technici beoordeelden de geëxporteerde codebase, bevestigden dat deze functioneel en compleet was, en hielpen Fleur volledig migreren naar infrastructuur die ze rechtstreeks beheerde — waarmee elke doorlopende afhankelijkheid van het oorspronkelijke platform werd verwijderd. We hielpen haar ook in gewone taal documenteren waar ze precies mee had ingestemd en wat haar opties waren met betrekking tot de reeds gegenereerde code, zodat ze een weloverwogen beslissing kon nemen over haar volgende stappen in plaats van te gokken.

**Resultaat:** BloemBestel draait nu volledig op infrastructuur die Fleur beheert, zonder enige doorlopende afhankelijkheid van het oorspronkelijke AI-platform, en ze heeft een duidelijk begrip van de clausule over behouden rechten voor de toekomst.

> *"Ik las 'exporteer uw code' en dacht dat dat het hele verhaal was. Ik dacht er niet aan te vragen wat het platform er nog mee mocht doen."*
> — **Fleur Lisse, oprichter, BloemBestel (Lisse)**

**Kosten en tijdlijn:** € 1.100 (exportbeoordeling, volledige migratie naar onafhankelijke infrastructuur) — voltooid in 4 werkdagen.

---

## Veelgestelde vragen

### Behouden alle AI-codeertools rechten om gegenereerde code te hergebruiken voor training?

Dit verschilt per platform en verandert in de loop van de tijd, en precies daarom is het rechtstreeks controleren van de huidige voorwaarden — niet een marketingsamenvatting — belangrijk voordat u iets bouwt waarvan u van plan bent op de lange termijn afhankelijk te zijn.

### Zijn behouden trainingsrechten hetzelfde als het platform dat mijn code bezit?

Nee, dat zijn aparte zaken. Een platform kan u duidelijk eigendom van uw code toekennen en tegelijkertijd een apart recht behouden om het, of patronen daaruit, te gebruiken voor het trainen van toekomstige modellen — lees beide clausules apart.

### Wat moet ik doen als ik een verontrustende clausule vind in een platform waarop ik al heb gebouwd?

Overweeg om uw export en migratie naar infrastructuur die u volledig zelf beheert te versnellen, wat beperkt hoeveel van het doorlopende leven van uw product onderworpen blijft aan de voorwaarden van dat platform.

### Verwijdert het exporteren van mijn code uit een AI-tool mij volledig uit de voorwaarden ervan?

Niet automatisch — de voorwaarden waarmee u instemde tijdens het gebruik van het platform kunnen nog steeds van toepassing zijn op code die daar al is gegenereerd, zelfs na export, afhankelijk van de specifieke bewoordingen.

### Kan het Amsterdamse team van Manifera helpen bij een migratie die al bezig is?

Ja — het team stapt regelmatig midden in een migratie in om geëxporteerde code te beoordelen, te bevestigen dat deze compleet en functioneel is, en deze te verplaatsen naar infrastructuur die de oprichter volledig zelf beheert.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Behouden alle AI-codeertools rechten om gegenereerde code te hergebruiken voor training?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dit verschilt per platform en verandert in de loop van de tijd, en precies daarom is het rechtstreeks controleren van de huidige voorwaarden — niet een marketingsamenvatting — belangrijk voordat u iets bouwt waarvan u van plan bent op de lange termijn afhankelijk te zijn."
      }
    },
    {
      "@type": "Question",
      "name": "Zijn behouden trainingsrechten hetzelfde als het platform dat mijn code bezit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, dat zijn aparte zaken. Een platform kan u duidelijk eigendom van uw code toekennen en tegelijkertijd een apart recht behouden om het, of patronen daaruit, te gebruiken voor het trainen van toekomstige modellen — lees beide clausules apart."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet ik doen als ik een verontrustende clausule vind in een platform waarop ik al heb gebouwd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Overweeg om uw export en migratie naar infrastructuur die u volledig zelf beheert te versnellen, wat beperkt hoeveel van het doorlopende leven van uw product onderworpen blijft aan de voorwaarden van dat platform."
      }
    },
    {
      "@type": "Question",
      "name": "Verwijdert het exporteren van mijn code uit een AI-tool mij volledig uit de voorwaarden ervan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niet automatisch — de voorwaarden waarmee u instemde tijdens het gebruik van het platform kunnen nog steeds van toepassing zijn op code die daar al is gegenereerd, zelfs na export, afhankelijk van de specifieke bewoordingen."
      }
    },
    {
      "@type": "Question",
      "name": "Kan het Amsterdamse team van Manifera helpen bij een migratie die al bezig is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja — het team stapt regelmatig midden in een migratie in om geëxporteerde code te beoordelen, te bevestigen dat deze compleet en functioneel is, en deze te verplaatsen naar infrastructuur die de oprichter volledig zelf beheert."
      }
    }
  ]
}
</script>
