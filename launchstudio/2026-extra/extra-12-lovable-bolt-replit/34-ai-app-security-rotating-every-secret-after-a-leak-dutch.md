---
Titel: "AI-Appbeveiliging: Elk Geheim Vervangen Na een Lek"
Trefwoorden: ai-appbeveiliging, geheimen vervangen, gelekte inloggegevens, gecompromitteerde sleutel, incidentrespons, git-geschiedenis, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische solo-oprichter / Indie hacker
---

# AI-Appbeveiliging: Elk Geheim Vervangen Na een Lek

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-Appbeveiliging: Elk Geheim Vervangen Na een Lek",
  "description": "Er is een sleutel blootgesteld. Wat u vervangt, in welke volgorde, waarom het verwijderen van de commit niets doet, en hoe u uitzoekt of hij is gebruikt - geschreven voor de oprichter die dit op een dinsdagavond ontdekt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-20",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-app-security-rotating-every-secret-after-a-leak" }
}
</script>

U hebt een sleutel gevonden op een plek waar hij niet hoort. In een publieke repository. In de JavaScript-bundel die uw site serveert. In een schermafbeelding in een supportgesprek. Geplakt in een chat met een opdrachtnemer die in maart vertrok.

Het volgende uur doet ertoe, en het instinct - verwijder het, snel, voordat iemand het merkt - is de verkeerde zet. Een geheim verwijderen van de plek waar u het vond, zorgt er niet voor dat het ophoudt te werken, en terwijl u aan het opruimen bent, is de sleutel nog steeds geldig.

Dit artikel is de volgorde van handelen, geschreven om te volgen in plaats van te bewonderen.

## Eerst Vervangen, Daarna Opruimen

De enige handeling die het risico verlaagt, is de oude waarde nutteloos maken. Al het andere is huishouden.

Dus: ga naar de provider, genereer nieuwe inloggegevens, deploy ze, en trek de oude in. In die volgorde - genereren en deployen vóór intrekken, zodat uw product niet platgaat terwijl u werkt, tenzij de blootstelling zo ernstig is dat downtime de voorkeur heeft boven voortdurende toegang.

Bij de meeste providers kost dit minuten. Doe het vóór u onderzoekt hoe het gebeurde, vóór u beslist of iemand het heeft gevonden, en vóór u het bestand verwijdert.

## De Commit Verwijderen Doet Niets

Werd het geheim in een repository gecommit, dan verwijdert een nieuwe commit het alleen uit de huidige stand en nergens anders uit. De oude commit bevat het nog, iedereen die de repository kloonde heeft het, en is de repository publiek, dan staat het misschien al in archieven van geautomatiseerde scanners.

De geschiedenis herschrijven is mogelijk en, voor een repository met medewerkers, ontwrichtend - en het helpt nog steeds niet tegen kopieën die al bestaan. Behandel de inloggegevens als gecompromitteerd, voorgoed, en vervang ze. De geschiedenis daarna opschonen is redelijke hygiëne, geen herstel.

Hetzelfde geldt voor een sleutel die in een JavaScript-bundel stond: elke bezoeker die die pagina laadde, heeft een kopie, en caches blijven bestaan. Vervangen is het enige wat helpt.

## Vervang Ook Wat Ernaast Stond

Een gelekte sleutel reist zelden alleen. Bereikte een `.env`-bestand een repository, dan is alles erin blootgesteld, niet alleen de waarde die u opmerkte. Gaat het om de machine of het account van een opdrachtnemer, dan valt elke sleutel waartoe die toegang had binnen de reikwijdte.

Werk vanuit de container in plaats van vanuit de ene waarde. Welk bestand, welke machine, welk account, welk kanaal - en dan alles wat erin zat.

Sorteer op gevolg. Database-inloggegevens en alles wat beheerdersrechten geeft eerst. Sleutels van de betaalprovider daarna. Gegevens voor e-mail en berichten daarna, aangezien een gecompromitteerde verzendidentiteit ook de reputatie van uw domein beschadigt. Analytics- en dienstsleutels met weinig rechten als laatste.

## Zoek Dan Uit of Hij Is Gebruikt

Zodra de sleutel dood is, stelt u vast wat er gebeurde. De meeste providers kunnen u meer vertellen dan oprichters verwachten.

Zoek naar: verzoeken vanaf adressen of regio's die u niet herkent, activiteit op tijden dat niemand werkte, volumes die niet passen bij het normale patroon van uw product, en beheerhandelingen - aangemaakte sleutels, gewijzigde instellingen, nieuwe gebruikers, exports.

Kijk bij een databasesleutel naar wat er werd gelezen, niet alleen naar wat er werd gewijzigd. Bulklezingen zijn het kenmerk van data die wordt meegenomen, en ze worden makkelijk gemist omdat er achteraf niets anders is.

Schrijf op wat u vindt en wanneer u keek, inclusief een duidelijke vermelding als u niets vond. Die registratie hebt u nodig als u het iemand moet vertellen, en haar later uit het geheugen reconstrueren is veel zwakker.

## Beslis of U Moet Melden

Kunnen persoonsgegevens zijn ingezien, dan hebt u verplichtingen onder de AVG, en de klok is kort: 72 uur vanaf het moment dat u het weet, bij de Autoriteit Persoonsgegevens, tenzij het lek waarschijnlijk geen risico oplevert voor de betrokkenen.

Twee punten waarin oprichters zich vergissen. "Waarschijnlijk geen risico" is een beoordeling die u moet kunnen onderbouwen, geen standaard. En het informeren van de betrokken personen is een aparte vraag, vereist wanneer het risico voor hen hoog is.

Maak de beoordeling bewust en leg de redenering vast: welke data bereikbaar was, of er bewijs is van toegang, wat het realistische gevolg zou zijn. Vraag advies als het nipt is. Een echt lek te weinig melden is een veel slechtere positie dan een melding die achteraf uit voorzorg blijkt te zijn.

## Sluit de Route

Een sleutel lekt via een route, en blijft de route open, dan volgt de volgende.

De routes, ongeveer naar frequentie in door AI gebouwde producten: een geheim dat een publiek voorvoegsel kreeg en zo in de browserbundel werd gecompileerd; een omgevingsbestand dat werd gecommit omdat de ignore-regels het niet dekten; een sleutel geplakt in een chat, een ticket of een schermafbeelding; een gedeeld account met een wachtwoord dat meerdere mensen kennen; en de toegang van een opdrachtnemer die nooit werd ingetrokken.

Elk heeft een specifieke oplossing, en nu - terwijl het incident vers is en de motivatie er is - is de enige keer dat het ook echt gebeurt. Scannen tijdens de build dat de build laat falen bij een gevonden geheim, gecontroleerde ignore-regels, een wachtwoordmanager met toegang per persoon in plaats van gedeelde logins, en een checklist voor vertrek.

## Verklein Wat Eén Lek Kost

Twee structurele wijzigingen maken het volgende incident kleiner.

Gebruik smalle inloggegevens. Eén sleutel per integratie, beperkt tot wat die integratie nodig heeft, zodat een lek één ding raakt. Eén beheerderssleutel die overal wordt gebruikt, betekent dat elk lek totaal is.

En weet waar elke sleutel wordt gebruikt. Een eenvoudige lijst - deze sleutel, deze provider, gebruikt door deze delen van het product, laatst vervangen op deze datum - maakt van vervangen een taak in plaats van een onderzoek. De meeste oprichters ontdekken tijdens een incident dat ze niet weten welke sleutel waar wordt gebruikt, en die ontdekking maakt een dinsdagavond lang.

## Vervangen Zonder Storing

De reden dat geheimen jarenlang niet worden vervangen, is dat vervangen gevaarlijk aanvoelt: verander de waarde en iets stopt met werken, meestal het ding waar u niet aan dacht.

Drie patronen nemen de angst weg, en ze in kalme omstandigheden invoeren maakt een noodvervanging een klus van twintig minuten.

**Twee geldige waarden tijdens een overgang.** Waar de provider meerdere actieve sleutels toestaat - de meeste doen dat - maakt u de nieuwe aan, deployt u haar, bevestigt u dat het verkeer haar gebruikt, en verwijdert u daarna de oude. Niets is ooit zonder werkende sleutel.

**Verificatie die beide accepteert.** Voor dingen die u verifieert in plaats van verstuurt, zoals webhookhandtekeningen: accepteer een paar dagen zowel het huidige als het vorige geheim. Het omzetten bij de provider wordt dan een niet-gebeurtenis.

**Configuratie, geen code.** Een sleutel waarnaar vanuit omgevingsconfiguratie wordt verwezen, vervangt u door een waarde te wijzigen en te herstarten. Een sleutel die hard in de broncode staat, vereist een commit, een review en een deployment, en daarom doet niemand het om negen uur op een zondagavond.

Vervang daarna volgens schema in plaats van alleen bij incidenten - jaarlijks is redelijk voor de meeste producten, en vaker voor alles met brede toegang. De waarde van het schema is niet dat het een lek voorkomt; het is dat de procedure vertrouwd, getest en ondramatisch is op de dag dat u haar haastig nodig hebt.

Eén waarschuwing die het noemen waard is: vervang één sleutel tegelijk, en bevestig dat het product nog werkt voordat u naar de volgende gaat. Negen geheimen in één wijziging vervangen levert een storing op waarvan de oorzaak elk van de negen kan zijn, en dat is een slechtere avond dan degene die u al had.

## Dit Inrichten

Voor een product dat net een blootstelling had, of dat voorbereid wil zijn: de betrokken sleutel vervangen en ingetrokken met de vervanger eerst gedeployd, alles in dezelfde container vervangen in volgorde van gevolg, logs van providers bekeken op gebruik met de bevindingen opgeschreven, een gedocumenteerde lekbeoordeling tegen de verplichting van 72 uur, de route gesloten met scannen op geheimen tijdens de build en gecontroleerde ignore-regels, gedeelde accounts vervangen door toegang per persoon, een checklist voor vertrek, sleutels teruggebracht tot één per integratie met minimale reikwijdte, en een inventarisatie die vastlegt waar elke sleutel wordt gebruikt en wanneer hij voor het laatst werd vervangen.

LaunchStudio doet dit zowel als incidentrespons als ter voorbereiding, en binnen de managed regeling van €49 per maand worden het scannen en de inventarisatie bijgehouden in plaats van onthouden. De engineers zijn van Manifera - elf jaar, 120+ engineers, klanten als Vodafone, TNO en CFLW.

[Vertel ons wat u vond en waar](https://launchstudio.eu/nl/#contact). Het eerste uur is het uur dat ertoe doet.

## Echt voorbeeld

### Een Repository die Per Ongeluk Publiek Werd

Suzanne Grotenhuis bouwde Inspectierapport in Lovable: inspectierapportage voor bouwkundig inspecteurs en keurmeesters van installaties, 39 bedrijven die samen zo'n 2.000 rapporten per maand maken.

Ze maakte haar repository publiek om een codevoorbeeld te delen met een potentiële opdrachtnemer, met de bedoeling het terug te draaien. Dat deed ze, vier dagen later. Elf maanden eerder was er een omgevingsbestand gecommit, voordat er ignore-regels waren, en dat bevatte de service role-sleutel van Supabase, de gegevens van de e-mailprovider, een API-sleutel voor een kaartdienst die op gebruik afrekent, en het signing-secret voor haar betaalwebhooks.

Binnen een dag nadat de repository publiek werd, hadden geautomatiseerde scanners het gevonden. Ze hoorde het van de kaartprovider, die haar account opschortte wegens afwijkend gebruik - 140.000 verzoeken in elf uur vanaf adressen die ze niet herkende.

Dezelfde avond, en daarna twee werkdagen: de kaartsleutel als eerste vervangen, omdat het misbruik gaande was; de service role-sleutel van Supabase daarna vervangen en gedeployd, als de sleutel met onbeperkte databasetoegang; e-mailgegevens en het webhook-signing-secret daarna vervangen, waarbij de webhookhandler tijdelijk zowel het oude als het nieuwe accepteerde om geen leveringen te missen; elke sleutel in het bestand als gecompromitteerd behandeld, ongeacht of hij gebruikt leek; database-toegangslogs bekeken met de support van Supabase, zonder queries vanaf onbekende bronnen in de periode van blootstelling; logs van de e-mailprovider bekeken, zonder verzonden mails; een lekbeoordeling gedocumenteerd met de conclusie dat persoonsgegevens in de database bereikbaar waren geweest maar zonder bewijs van toegang, met de redenering vastgelegd en juridisch advies ingewonnen, wat leidde tot een melding uit voorzorg bij de Autoriteit Persoonsgegevens; scannen op geheimen tijdens de build toegevoegd; ignore-regels gecorrigeerd en de geschiedenis herschreven als hygiëne; gedeelde logins vervangen door toegang per persoon in een wachtwoordmanager; en een inventarisatie van inloggegevens gemaakt met negen geheimen, hun reikwijdte, waar elk wordt gebruikt en wanneer het voor het laatst werd vervangen.

**Resultaat:** de kaartprovider schold €2.840 aan gebruik kwijt na het bekijken van de tijdlijn. Er werd geen bewijs gevonden van toegang tot de database of e-mail. Suzannes conclusie was dat de service role-sleutel die elf maanden in dat bestand stond het echte incident was, en dat de vier publieke dagen gewoon het moment waren waarop het werd opgemerkt.

> *"Ik vervang de kaartsleutel als eerste, omdat die me geld kostte. Het kostte me een uur om te beseffen dat het bestand ook de sleutel bevatte die elk inspectierapport in het product kan lezen."*
> - **Suzanne Grotenhuis, Oprichter, Inspectierapport (Amersfoort)**

**Kosten & Doorlooptijd:** €3.100 (noodvervanging van negen sleutels in volgorde van gevolg, webhookovergang met twee geheimen, controle van providerlogs, lekbeoordeling en melding bij de toezichthouder, scannen op geheimen, herstel van geschiedenis en ignore-regels, toegangsbeheer, inventarisatie van inloggegevens) - afgerond in 2 werkdagen na triage dezelfde avond.

## Veelgestelde vragen

### Wat is het eerste wat ik doe als een sleutel lekt?

Vervang haar. Genereer de vervanger, deploy die, trek de oude waarde in. Onderzoek en opruimen komen daarna; terwijl u opruimt, werkt de oude sleutel nog.

### Lost het verwijderen van de commit een gelekt geheim op?

Nee. De oude commit bevat het nog, er bestaan al klonen, en publieke repositories worden binnen minuten automatisch gescand. Vervangen is het enige herstel; de geschiedenis opschonen is hygiëne.

### Wat moet ik nog meer vervangen dan de sleutel die ik vond?

Alles in dezelfde container - het hele omgevingsbestand, elke sleutel die het gecompromitteerde account of de machine kon bereiken - in volgorde van gevolg, te beginnen met database- en beheerdersrechten.

### Moet ik het melden?

Kunnen persoonsgegevens zijn ingezien, dan hebt u 72 uur om de Autoriteit Persoonsgegevens te informeren, tenzij u kunt onderbouwen dat een risico onwaarschijnlijk is. Documenteer de beoordeling hoe dan ook en vraag advies als het nipt is.

### Hoe maak ik het volgende lek goedkoper?

Smalle inloggegevens - één per integratie met minimale reikwijdte - en een inventarisatie die vastlegt waar elke sleutel wordt gebruikt en wanneer hij werd vervangen, zodat vervangen een taak is in plaats van een onderzoek.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is de eerste stap als een sleutel lekt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vervang haar - genereer de vervanger, deploy die, trek de oude in. Onderzoek en opruimen komen daarna, omdat de oude waarde werkt tot ze is ingetrokken."
      }
    },
    {
      "@type": "Question",
      "name": "Lost het verwijderen van de commit een gelekt geheim op?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Oude commits bevatten het nog, er bestaan klonen, en publieke repositories worden binnen minuten gescand. Alleen vervangen herstelt het."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet er naast de blootgestelde sleutel nog meer worden vervangen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Alles in hetzelfde bestand, op dezelfde machine of in hetzelfde account, in volgorde van gevolg - database- en beheerderssleutels eerst."
      }
    },
    {
      "@type": "Question",
      "name": "Moet een gelekte sleutel worden gemeld bij de toezichthouder?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Kunnen persoonsgegevens zijn ingezien, dan binnen 72 uur, tenzij u kunt onderbouwen dat een risico onwaarschijnlijk is. Documenteer de beoordeling hoe dan ook."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe beperk ik de schade van een toekomstig lek?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Eén smal afgebakende sleutel per integratie, plus een inventarisatie van waar elke sleutel wordt gebruikt en wanneer hij voor het laatst werd vervangen."
      }
    }
  ]
}
</script>
