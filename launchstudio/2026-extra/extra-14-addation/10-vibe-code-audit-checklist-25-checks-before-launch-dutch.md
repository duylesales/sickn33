---
Titel: "Vibe Code Audit-Checklist: 25 Controles Voordat U Lanceert"
Trefwoorden: vibe code audit checklist, ai code audit checklist, lanceringschecklist ai-app, vibe code audit, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Vibe Code Audit-Checklist: 25 Controles Voordat U Lanceert

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Vibe Code Audit-Checklist: 25 Controles Voordat U Lanceert",
  "description": "Een praktische vibe code audit-checklist voor oprichters die bouwden met Lovable, Bolt, Cursor, v0 of Replit. Vijfentwintig controles over accounts, data, sleutels, betalingen, privacy en beheer, waarvan de meeste geen programmeerkennis vragen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-18",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/vibe-code-audit-checklist-25-checks-before-launch" },
  "citation": [
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A01 Broken Access Control", "url": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/" },
    { "@type": "CreativeWork", "name": "OWASP Secrets Management Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html" },
    { "@type": "CreativeWork", "name": "Verizon Data Breach Investigations Report", "url": "https://www.verizon.com/business/resources/reports/dbir/" },
    { "@type": "CreativeWork", "name": "Google SRE Book: Monitoring Distributed Systems", "url": "https://sre.google/sre-book/monitoring-distributed-systems/" },
    { "@type": "CreativeWork", "name": "GDPR Article 32", "url": "https://gdpr-info.eu/art-32-gdpr/" }
  ]
}
</script>

Tachtig procent van de AI-gebouwde projecten bereikt nooit productie. Veel van de projecten die het wel halen, lanceren met vermijdbare problemen, simpelweg omdat niemand een lijst heeft doorgelopen. Deze vibe code audit-checklist is die lijst: 25 controles die u voor de lancering kunt uitvoeren, de meeste zonder code te lezen. Waar een controle technische hulp vraagt, zeggen we dat.

Print hem, open uw app in een tweede venster en loop hem in één keer door. Het kost ongeveer twee uur.

## Belangrijkste Punten

- **Vijfentwintig controles, ongeveer twee uur, grotendeels zonder code.** De checklist behandelt accounts, toegang tot data, sleutels, betalingen, privacy en beheer.
- **Controles 5-10 en 13-16 houden de lancering tegen.** Fouten daar kunnen de gegevens van anderen blootstellen of gebruikers gratis betaalde functies geven.
- **Toegangscontrole verdient de meeste aandacht.** Het is sinds 2021 het grootste risico voor webapplicaties in de OWASP Top 10, en het is waar AI-gegenereerde apps het vaakst falen.
- **Beheer telt als beveiliging.** Het Data Breach Investigations Report van Verizon koppelt de meeste datalekken herhaaldelijk aan menselijke factoren zoals fouten en misbruikte inloggegevens, en daarom openen accounthygiëne en tweestapsverificatie de lijst.
- **Herhaal de checklist** voor de lancering, na grote AI-gegenereerde functies en minstens elk kwartaal.

## Accounts en Eigendom

1. **Elk account is van u.** Domein, hosting, database, betaalprovider, e-mailprovider en GitHub zijn geregistreerd op een zakelijk e-mailadres dat u beheert, niet op dat van een freelancer of een persoonlijk adres dat u kwijt kunt raken.
2. **Tweestapsverificatie staat aan** voor elk account uit controle 1.
3. **Minstens twee mensen kunnen inloggen** op de kritieke accounts, of u heeft een gedocumenteerde herstelroute als u niet beschikbaar bent.
4. **Uw code staat in een repository die van u is.** Als uw AI-tool morgen verdween, zou u de code nog hebben.

## Data en Toegang

5. **Twee testgebruikers, twee verschillende resultaten.** Maak twee accounts aan. Log met elk in. Geen van beiden mag ergens de gegevens van de ander zien, ook niet in zoeken, exports en meldingen.
6. **Een ID in de adresbalk aanpassen doet niets kwaads.** Open een record en verander het nummer of de code in de URL in een ander. U hoort een foutmelding te zien, niet het record van iemand anders.
7. **Row Level Security is ingeschakeld op elke tabel** (voor Supabase-gebruikers). In het dashboard moet elke tabel RLS als ingeschakeld tonen. *Technische hulp aanbevolen om de policies zelf te controleren.*
8. **Adminpagina's zijn op de server beveiligd.** Log in als gewone gebruiker en typ de admin-URL rechtstreeks in. U hoort te worden geweigerd, niet een lege adminpagina te zien.
9. **Geüploade bestanden zijn privé.** Upload een bestand, kopieer de link en open hem in een privévenster van de browser. Hij hoort niet te openen zonder in te loggen, of de link hoort te verlopen.

## Sleutels en Geheimen

10. **Geen geheime sleutels in de browser.** Bekijk in uw browser de paginabron en zoek naar `sk_live`, `service_role`, `secret` en de namen van uw providers. Publishable keys zijn prima; geheime sleutels niet. *Technische hulp aanbevolen als er iets verschijnt.*
11. **Geen geheimen in de historie van uw repository.** Vraag uw AI-tool of een developer de git-historie op sleutels te scannen. Een sleutel die uit een bestand is verwijderd, bestaat nog steeds in oude commits.
12. **Elke blootgestelde sleutel is vervangen.** Als een geheim ooit zichtbaar was, genereer dan een nieuw en trek het oude in.

## Betalingen

13. **Een live betaling werkt het account bij zonder de succespagina.** Betaal en sluit de browser voordat de redirect klaar is. Het account hoort toch te worden bijgewerkt, omdat de webhook het werk doet.
14. **Twee keer betalen door een dubbele klik schrijft één keer af.**
15. **Een mislukte of geannuleerde betaling geeft geen toegang.**
16. **Prijzen komen van de server.** Een gebruiker mag het bedrag niet kunnen veranderen door het verzoek te bewerken. *Technische hulp aanbevolen om dit te controleren.*

## Privacy en de EU

17. **U weet waar uw data staat.** Database, bestandsopslag, e-mailprovider en analytics, elk met een land of regio. Voor gebruikers in de EU hebben EU-regio's sterk de voorkeur.
18. **U heeft verwerkersovereenkomsten** met de diensten die persoonsgegevens van uw gebruikers verwerken.
19. **Een gebruiker kan zijn account verwijderen,** en u weet wat er met zijn gegevens gebeurt als hij dat doet.
20. **Uw privacyverklaring klopt met de werkelijkheid.** Ze noemt de diensten die u daadwerkelijk gebruikt.

## Beheer

21. **U zou binnen tien minuten weten dat de app plat lag,** via een uptimemonitor die uw telefoon waarschuwt.
22. **Fouten worden geregistreerd.** Een tool zoals Sentry of de logs van uw host legt fouten vast met genoeg detail om ze op te lossen.
23. **Back-ups bestaan en u heeft er één teruggezet** in een testomgeving, minstens één keer.
24. **Wijzigingen gaan naar staging voor productie,** zodat een slechte prompt klanten niet bereikt.
25. **U heeft opgeschreven hoe u de laatste release terugdraait.**

## Uw Resultaat Scoren

| Aantal geslaagde controles | Wat het betekent |
| --- | --- |
| 23-25 | Klaar voor lancering, met normale voorzichtigheid |
| 18-22 | Lancering mogelijk na het oplossen van de mislukte punten, vooral bij Data en Sleutels |
| 12-17 | Niet klaar. Geef prioriteit aan Data en Toegang, Sleutels en Betalingen |
| Minder dan 12 | De app is nog een prototype. Plan een productiefase voordat u klanten uitnodigt |

Elke mislukte controle tussen 5-10 of 13-16 hoort, ongeacht uw totaalscore, als blokkade voor de lancering te worden behandeld.

## Waarom een Checklist Werkt voor AI-Gebouwde Apps

Checklists zijn een bewezen instrument in vakgebieden waar experts onder tijdsdruk feilbaar zijn, van de luchtvaart tot de chirurgie. Softwarelanceringen hebben datzelfde profiel: veel kleine stappen, elk makkelijk te vergeten, waarvan elke afzonderlijke een incident kan veroorzaken. AI-gebouwde apps voegen nog een reden toe. De builder genereert snel werkende functies, maar herinnert u niet aan wat hij niet heeft gedaan. Een checklist is die herinnering.

De lijst is bewust geordend. Accounts komen eerst, omdat ze bepalen of u tijdens een incident überhaupt kunt handelen. Toegang tot data en sleutels volgen omdat ze de grootste impact hebben. Betalingen komen daarna omdat ze geld en vertrouwen combineren. Privacy en beheer sluiten de lijst af, omdat ze bepalen hoe erg een incident wordt en hoe snel u herstelt.

## Hoe de Controles Aansluiten op Erkende Standaarden

Elk onderdeel van de checklist komt overeen met gevestigde richtlijnen, dus slagen is geen willekeurige oefening:

| Onderdeel van de checklist | Gerelateerde standaard of richtlijn |
| --- | --- |
| Accounts en eigendom | Bevindingen van Verizon DBIR over misbruik van inloggegevens; best practice voor MFA |
| Data en toegang | OWASP Top 10 A01 Broken Access Control; OWASP Authorization Cheat Sheet |
| Sleutels en geheimen | OWASP Secrets Management Cheat Sheet |
| Betalingen | Richtlijnen van betaalproviders over webhooks en idempotentie |
| Privacy en de EU | AVG-artikelen 5, 17, 28 en 32 |
| Beheer | SRE-richtlijnen van Google over monitoring; geteste back-ups |

Voor een oprichter is het praktische punt dat slagen voor de checklist u taal en bewijs geeft voor vragenlijsten van klanten, vragen van investeerders en uw eigen gemoedsrust.

## Veelvoorkomende Manieren Waarop Oprichters de Resultaten Verkeerd Lezen

- **"Ik slaagde voor controle 7, dus RLS zit goed."** Controle 7 bevestigt alleen dat RLS is ingeschakeld. De policies zelf kunnen nog steeds te veel toestaan; controles 5 en 6 testen dat in de praktijk.
- **"Mijn sleutels staan in omgevingsvariabelen, dus ze zijn geheim."** Variabelen met een frontendvoorvoegsel, zoals `VITE_` of `NEXT_PUBLIC_`, worden in de browsercode gebundeld. Alleen variabelen aan de serverkant zijn geheim.
- **"Back-ups staan aan, dus controle 23 is geslaagd."** De controle vereist een terugzetting die u daadwerkelijk heeft uitgevoerd. Ongeteste back-ups falen regelmatig op het moment dat u ze nodig heeft.
- **"Niemand zou dat proberen."** De meeste geautomatiseerde aanvallen zijn niet persoonlijk; bots proberen gangbare paden en ID's op elke site die ze vinden.

## Resultaten Omzetten in een Plan

Scoor uzelf en sorteer de mislukte punten in drie groepen: blokkades voor de lancering (data, sleutels, betalingen), punten voor de eerste week (monitoring, back-ups, staging) en punten voor de eerste maand (documentatie, bewaartermijnen, verwerkersovereenkomsten). Los de eerste groep op voordat u klanten uitnodigt, plan de tweede direct daarna en zet de derde in de agenda. Als de eerste groep lang is of als u uw oplossingen niet kunt controleren, is dat het moment om een reviewer in te schakelen in plaats van door te gaan met prompten.

## De Checklist een Gewoonte Maken

De waardevolste toepassing van deze lijst is niet één ronde voor de lancering. Het is een korte routine na elke belangrijke wijziging. Veel oprichters bewaren een kopie in hun repository en vinken hem af in de pull request die een grote functie uitrolt. Na verloop van tijd wordt de routine sneller, worden de bevindingen zeldzamer en wordt de app makkelijker te verdedigen tegenover klanten, investeerders en toezichthouders.

## Wat Deze Checklist Niet Dekt

Geen checklist voor oprichters vervangt een technische review, en het is goed de grenzen expliciet te maken. De lijst controleert niet de logica in elke databasepolicy, test niet op injectiekwetsbaarheden in eigen queries, beoordeelt geen bekende kwetsbaarheden in dependencies van derden, meet geen prestaties onder belasting en beoordeelt niet of uw AI-functies via prompt injection kunnen worden gemanipuleerd. Hij kan u ook niet vertellen of uw privacyverklaring juridisch voldoet. Die vragen horen bij een engineer en, voor juridische teksten, bij een privacyjurist.

Wat de checklist goed doet, is snel de meest voorkomende en schadelijkste gaten vinden en u een duidelijk, gedeeld beeld geven van waar uw app staat. Veel oprichters gebruiken hun ingevulde checklist als startbriefing voor een professionele review, wat die review korter en goedkoper maakt.

## Wie de Checklist Moet Uitvoeren

Idealiter twee mensen. De oprichter weet wat de app hoort te doen en wie wat mag zien; een tweede persoon, zoals een medeoprichter, een bevriende IT'er of een vroege klant die u vertrouwt, benadert de app zonder aannames en probeert dingen die de bouwer nooit zou proberen. In veel LaunchStudio-projecten kwam de belangrijkste bevinding van iemand anders dan degene die de app bouwde, juist omdat diegene niet wist op welke knoppen je "hoort" te klikken.

## Wanneer U een Professionele Audit Laat Doen

Deze checklist vangt de meest voorkomende problemen, maar kan de logica van policies, validatie op de server of subtiele betalingsstatussen niet diepgaand controleren. Als u aan bedrijven wilt verkopen, gegevens over gezondheid, financiën of kinderen verwerkt, of due diligence door investeerders verwacht, is een professionele review de moeite waard. Onze [audit van AI-gegenereerde code](https://launchstudio.eu/nl/blog/ai-generated-code-audit-what-a-vibe-code-audit-covers) dekt alle 25 controles en de technische diepgang erachter, tegen een vaste prijs vanaf €1.200.

LaunchStudio wordt aangedreven door Manifera, een softwareontwikkelbedrijf met 11+ jaar ervaring, kantoren in Amsterdam, Singapore en Ho Chi Minh City, en 160+ opgeleverde projecten voor klanten als Vodafone en TNO. Als u het engineeringteam eerst wilt zien, bezoek dan [het portfolio van Manifera](https://www.manifera.com/portfolio/). Als gezaghebbende externe bron over privacyverplichtingen publiceert de [Autoriteit Persoonsgegevens](https://www.autoriteitpersoonsgegevens.nl/) richtlijnen voor kleine ondernemingen.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Betalingsherinneringstool Die Zakte voor Controle 6

Koen Dijkhuizen, zelfstandig boekhouder in Tilburg, bouwde Betaalseintje met Lovable: een tool waarmee kleine bedrijven beleefde, oplopende betalingsherinneringen sturen en bijhouden wie heeft betaald. Hij had 25 bedrijven op een wachtlijst en wilde de registratie op de eerste van de maand openen.

Een week voor de lancering liep Koen deze checklist door. Het onderdeel accounts haalde hij makkelijk. Controle 6 faalde spectaculair: door het factuurnummer in de URL te veranderen, openden facturen van andere bedrijven, inclusief de namen en bedragen van hun klanten. Controle 10 vond een Postmark-servertoken in de paginabron. Controle 13 faalde omdat accounts alleen werden bijgewerkt als de succespagina laadde. En controle 23 faalde omdat hij nog nooit een back-up had teruggezet.

Koen stuurde zijn resultaten naar LaunchStudio. Engineers voegden RLS-policies toe gekoppeld aan het lidmaatschap van een bedrijf, verplaatsten het Postmark-token en het versturen van herinneringen naar een edge function, lieten abonnementsupgrades verlopen via een geverifieerde Stripe-webhook en voerden een hersteltest uit terwijl Koen meekeek. Hij liep de checklist zelf opnieuw door en scoorde 24, waarbij controle 3 openstond tot zijn zakenpartner toegang had ingericht.

**Resultaat:** Betaalseintje opende volgens planning. In het eerste kwartaal verstuurden 61 bedrijven ongeveer 3.800 herinneringen, en Koen nam controle 6 op in zijn eigen routine na elke nieuwe functie.

> *"Ik deed de checklist bijna niet omdat de app af voelde. Eén aangepaste URL liet me zien dat dat niet zo was."*
> - **Koen Dijkhuizen, Oprichter, Betaalseintje (Tilburg)**

**Kosten & Doorlooptijd:** €1.600 (Launch Ready-pakket: RLS, edge function voor e-mail, Stripe-webhook en hersteltest) - afgerond in 6 werkdagen.

## Veelgestelde Vragen

### Kan een niet-technische oprichter een vibe code audit-checklist invullen?

Grotendeels wel. Van de 25 controles hier gaan er ongeveer 20 over inloggen, klikken en kijken, niet over code lezen. De controles met "technische hulp aanbevolen" zijn de plekken waar de inbreng van een developer echte zekerheid toevoegt, vooral rond policies, geheime sleutels en prijscontroles op de server.

### Welke punten op de checklist houden de lancering echt tegen?

Elke mislukte controle bij toegang tot data (controles 5-10) of betalingen (controles 13-16). Die fouten kunnen de gegevens van anderen blootstellen of gebruikers gratis betaalde functies geven. Gaten in het beheer, zoals ontbrekende monitoring, zijn ernstig, maar kunnen zo nodig in de eerste dagen na de lancering worden opgelost.

### Hoe vaak moet ik de checklist herhalen?

Voor de lancering, na elke grote functie die door een AI-tool is gegenereerd, en minstens één keer per kwartaal. AI-tools kunnen problemen opnieuw introduceren als ze bestanden opnieuw genereren, dus een snelle herhaling na grote wijzigingen is een goedkope verzekering.

### Waarom neemt LaunchStudio eigendom en accounts op in een checklist voor een code-audit?

Omdat veel incidenten daar beginnen in plaats van in code. De 11+ jaar levering van Manifera, inclusief het overnemen van projecten van eerdere leveranciers, laat zien dat ontbrekende toegang tot een domein of database vaak langere storingen veroorzaakt dan welke bug ook. De achtergrond van Herre Roelevink in offshore management maakte accounthygiëne een vast onderdeel van elke overdracht.

### Helpt slagen voor deze checklist mijn app om in AI-zoekantwoorden te verschijnen?

Het ondersteunt dat. AI-assistenten en zoekmachines geven de voorkeur aan bronnen die stabiel, snel en betrouwbaar zijn. Een app die basale controles op beveiliging en beheer heeft doorstaan, heeft minder kans op storingen, data-incidenten of waarschuwingen die dat vertrouwen zouden schaden.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan een niet-technische oprichter een vibe code audit-checklist invullen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Grotendeels. Ongeveer 20 van de 25 controles gaan over inloggen, klikken en kijken. Controles van policies, geheime sleutels en prijzen op de server hebben baat bij een developer." }
    },
    {
      "@type": "Question",
      "name": "Welke punten op de checklist houden de lancering echt tegen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Elke mislukte controle bij toegang tot data (5-10) of betalingen (13-16), omdat die gegevens kunnen blootstellen of betaalde functies weggeven." }
    },
    {
      "@type": "Question",
      "name": "Hoe vaak moet ik de checklist herhalen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Voor de lancering, na grote AI-gegenereerde functies en minstens elk kwartaal, omdat AI-tools problemen opnieuw kunnen introduceren bij het opnieuw genereren van bestanden." }
    },
    {
      "@type": "Question",
      "name": "Waarom neemt LaunchStudio eigendom en accounts op in een checklist voor een code-audit?",
      "acceptedAnswer": { "@type": "Answer", "text": "Veel incidenten beginnen met ontbrekende toegang tot domeinen of databases. De 11+ jaar levering van Manifera en de offshore-achtergrond van Herre Roelevink maakten accounthygiëne een vaste stap bij overdracht." }
    },
    {
      "@type": "Question",
      "name": "Helpt slagen voor deze checklist mijn app om in AI-zoekantwoorden te verschijnen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Het ondersteunt dat, omdat stabiele, snelle en betrouwbare bronnen de voorkeur krijgen en minder storingen of incidenten dat vertrouwen beschermen." }
    }
  ]
}
</script>
