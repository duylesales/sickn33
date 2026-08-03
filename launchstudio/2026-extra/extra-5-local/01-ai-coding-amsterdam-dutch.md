---
Titel: "AI Coding in Amsterdam: Wat oprichters fout doen vóór de lancering"
Trefwoorden: ai coding, ai code generatie, vibe coding, productieklare code, Amsterdam
Koperfase: Overweging
Doelgroep: Technische solo-oprichter
---

# AI Coding in Amsterdam: Wat oprichters fout doen vóór de lancering

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Coding in Amsterdam: Wat oprichters fout doen vóór de lancering",
  "description": "Een blik op wat er gebeurt nadat AI-codingtools een werkend prototype genereren voor Amsterdamse oprichters, en waarom de kloof tussen demo en productie groter is dan de meeste technische oprichters verwachten.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-23",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-coding-amsterdam" }
}
</script>

Het is 23.00 uur in een gedeelde werkruimte nabij Amsterdam Zuid, en een solo-oprichter heeft zojuist toegekeken hoe Cursor in minder dan drie uur een werkende inlogflow, een dashboard en een Stripe-afrekenpagina genereerde. Het voelt alsof het harde werk erop zit. Dat is niet zo. AI-codingtools zijn buitengewoon goed in het produceren van iets dat draait — ze zijn aanzienlijk minder betrouwbaar in het produceren van iets dat het contact met echte gebruikers, echte betalingsgegevens en echte aanvallers overleefd.

## Waarom AI Coding u voor 80% helpt, maar niet voor 100%

Amsterdam heeft een van de hoogste concentraties solo technische oprichters van Nederland, waarvan velen voormalig engineers zijn die bureaus of scale-ups verlieten om hun eigen product te bouwen. Die achtergrond zorgt ervoor dat AI-codingtools zoals Cursor, Bolt en v0 aanvoelen als een superkracht — u weet al hoe "goed" eruitziet, dus u kunt zich snel een weg prompten naar een functionerende app. Het probleem is niet de code die draait. Het zijn de codepaden die niemand heeft getest: wat er gebeurt als twee gebruikers tegelijkertijd hetzelfde eindpunt aanroepen, wat er gebeurt als een API-sleutel in een openbare repository belandt, of wat er gebeurt als de database geen back-upstrategie heeft omdat de AI er nooit naar heeft gevraagd.

Dit is een patroon dat LaunchStudio voortdurend ziet in heel Noord-Holland, niet alleen in Amsterdam. Oprichters die AI-coderingsassistenten gebruiken, leveren binnen enkele dagen een overtuigend prototype op en ontdekken vervolgens — meestal na een waarschuwing, soms na een daadwerkelijk incident — dat "het werkt op mijn machine" nooit hetzelfde was als "het is veilig om hier mensen geld voor te vragen." Ongeveer 80% van de met AI gebouwde projecten haalt nooit een stabiele productielancering, en 45% van de AI-gegenereerde code bevat een vorm van beveiligingslek die ernstig genoeg is om er toe te doen.

Ook de specifieke stack speelt hierbij een rol. Een oprichter die zich een weg heeft geprompt naar een met Cursor gebouwde Next.js-app gekoppeld aan Supabase heeft een ander risicoprofiel dan iemand die een door Bolt gegenereerde backend op een eenvoudige Postgres-instantie draait — maar de categorie van uitval is bij alle tools vrijwel hetzelfde: autorisatiecontroles die wel op de frontend bestaan (een knop is verborgen), maar niet op de backend (de API-route achter die knop heeft helemaal geen controle). Een AI-codingtool genereert met plezier een UI die een "admin"-link verbergt voor gewone gebruikers, zonder ooit server-side logica toe te voegen die daadwerkelijk voorkomt dat een gewone gebruiker dat admin-eindpunt rechtstreeks aanroept. De interface liegt overtuigend; de API vertelt de waarheid.

## Het Amsterdamse patroon: Snel bouwen, langzame afrekening

Amsterdamse oprichters bouwen vaak in het openbaar — Twitter/X-threads, Product Hunt-lanceringen, LinkedIn-posts waarin hun AI-codingstack wordt getagd. Die zichtbaarheid is geweldig voor tractie en verschrikkelijk voor beveiligingsbeoordeling, omdat de druk om openbaar te lanceren vaak de onopvallende stap van een gedegen audit overslaat. Een lanceringsdatum op Product Hunt creëert een eigen vorm van deadlinedruk: oprichters die twee weken hebben besteed aan het verfijnen van onboardingflows en lege schermen, besteden zelden dezelfde energie aan de onzichtbare infrastructuur erachter, omdat niemand een screenshot maakt van een goed geconfigureerd autorisatiebeleid.

We hebben prototypes beoordeeld afkomstig uit WeWork-ruimtes aan de Herengracht en coworking-verdiepingen nabij het Amsterdam Science Park die admin-routes hadden zonder enige authenticatie, simpelweg omdat de AI-tool er nooit een controle voor genereerde en niemand erom vroeg. In meerdere gevallen had de oprichter werkelijk geen idee dat de route bereikbaar was, omdat hun eigen app er nooit rechtstreeks naar verwees — deze kwam pas aan het licht toen iemand uit nieuwsgierigheid een voorspelbaar URL-patroon zoals `/admin` of `/dashboard/internal` probeerde.

LaunchStudio wordt aangedreven door Manifera, een softwareontwikkelingsbedrijf met meer dan 11 jaar ervaring in het bouwen van productiesystemen voor enterprise-klanten zoals Vodafone en TNO. Ons eigen klantgerichte kantoor bevindt zich aan de Herengracht 420 in Amsterdam, wat betekent dat we deze exacte faalmodus van dichtbij meemaken — vaak van oprichters die op tien minuten fietsen afstand zitten. De oplossing is niet het herschrijven van de frontend die een Cursor- of Lovable-sessie al heeft opgeleverd. Het gaat om het ompakken met de zaken die AI-codingtools consistent overslaan: row-level security, deugdelijke authenticatie-middleware, hygiëne van omgevingsvariabelen en een databaseschema dat onder echt verkeer niet omvalt.

Als u twijfelt of uw prototype klaar is of noch kwetsbaar, is het de moeite waard om het [productie-gereedheidsproces](https://launchstudio.eu/en/#process) van LaunchStudio te doorlopen in plaats van te gokken. Het [custom software development team](https://www.manifera.com/services/custom-software-development/) van Manifera heeft dit uithardingswerk uitgevoerd in meer dan 160 opgeleverde projecten, dus de checklist is niet theoretisch — het is dezelfde checklist die wordt toegepast op enterprise-klanten, aangepast aan oprichtersbudgetten.

## Een praktische beveiligingschecklist vóór lancering voor AI-gecodeerde apps

De meeste Amsterdamse oprichters hebben geen volledige penetratietest nodig voordat hun eerste betalende klant zich aanmeldt. Ze moeten weten welke specifieke controles daadwerkelijk de fouten opvangen die AI-codingtools betrouwbaar missen, aangezien de overgrote meerderheid van de incidenten die LaunchStudio ziet, terug te voeren is op dezelfde korte lijst van tekortkomingen, niet op exotische aanvallen.

**Authenticatie en autorisatie**

- Elke API-route die gebruikersgegevens raakt, controleert wie de aanvraag doet, niet alleen of iemand is ingelogd — een geldige sessie mag niet automatisch toegang betekenen tot elk record
- Admin- of bevoorrechte routes worden server-side beschermd, niet alleen verborgen in het navigatiemenu
- Wachtwoordherstel- en accountherstelflows worden van begin tot eind getest, niet alleen de normale aanmeldingsflow

**Gegevensexpositie**

- Databaserecords zijn standaard afgestemd op de geauthenticeerde gebruiker (row-level security, niet alleen filtering op toepassingsniveau die omzeild kan worden)
- Foutmeldingen die naar de browser worden gestuurd, lekken geen stack traces, interne bestandspaden of databasestructuur

**Geheimen en configuratie**

- API-sleutels en databasereferenties leven in server-side omgevingsvariabelen, nooit in frontendcode die naar de browser wordt gestuurd
- De git-historie bevat geen referenties die vroegtijdig zijn gecommitteerd en later zijn "verwijderd" — het verwijderen uit de laatste commit verwijdert het niet uit de geschiedenis

**Misbruik en rate limiting**

- Publiek toegankelijke formulieren en API-eindpunten hebben basis rate limiting, zodat een script een registratieformulier of een wachtwoordhersteleindpunt niet duizenden keren per minuut kan bestoken
- Bestandsuploadeindpunten valideren het bestandstype en de bestandsgrootte server-side, niet alleen via een invoerbeperking aan de voorkant die iedereen kan omzeilen met een directe API-call

Een oprichter die deze lijst eerlijk en zelfstandig doorloopt vóór het betalen voor een formele audit, zal meestal al weten waar de zwakke plekken zitten — de lijst dwingt u vooraf om daadwerkelijk te controleren in plaats van aan te nemen. Het is de moeite waard om deze ronde uit te voeren vóór uw eerste externe betatester, niet erna, omdat het hele doel is om het gat te dichten terwijl de impact nog nul klanten bedraagt in plaats van twintig.

## Echt voorbeeld

### Een AI-Native Oprichter in Actie: Het datalek van Ledgerly dat niemand opmerkte

Sanne de Wit, een solo-oprichter gevestigd in Amsterdam, besteedde zes weken aan het bouwen van Ledgerly — een gedeelde tool voor het bijhouden van uitgaven voor freelancers die projectkosten delen — vrijwel volledig binnen Cursor. De app zag er af uit: strakke dashboards, werkende authenticatie, een gepolijste onboardingflow. Wat Cursor echter niet had gegenereerd, was row-level security op de database. De uitgavenrecords van elke gebruiker waren technisch bereikbaar voor elke andere ingelogde gebruiker, simpelweg door een ID in de URL te wijzigen, omdat de AI de query's had gebouwd zonder ze te beperken tot de geauthenticeerde gebruiker.

Sanne kwam er pas achter toen een betatester bijna in het voorbijgaan opmerkte dat hij de boodschappenbonnen van een vreemde kon zien. De engineers van LaunchStudio traceerden het naar één ontbrekende beleidslaag in de database en herbouwden de autorisatielogica zonder de bestaande frontend van Sanne aan te raken. We hebben ook rate limiting op de API toegevoegd en haar Stripe-geheimsleutel verplaatst uit een omgevingsbestand dat aan de client was blootgesteld.

**Resultaat:** Ledgerly werd negen dagen later opnieuw gelanceerd met volledige scheiding van gegevens en doorstond een vervolgpenetratiecontrole zonder kritieke bevindingen.

> *"Ik wist genoeg om snel te bouwen. Ik wist niet genoeg om te weten wat ik had gemist — en dat is een angstaanjagend gat als het om de financiële gegevens van anderen gaat."*
> — **Sanne de Wit, Oprichter, Ledgerly (Amsterdam)**

**Kosten & Doorlooptijd:** € 1.850 (beveiligingsaudit, RLS-implementatie, sleutelrotatie en belastingtesten) — afgerond in 6 werkdagen.

---

## Veelgestelde vragen

### Is AI-gegenereerde code daadwerkelijk minder veilig dan code geschreven door een menselijke ontwikkelaar?
Niet van nature, maar AI-codingtools optimaliseren voor "draait het" in plaats van "is het veilig", wat betekent dat beveiligingskritieke stappen zoals autorisatiecontrole en invoervalidatie vaak worden overgeslagen, tenzij er expliciet om wordt gevraagd. Onafhankelijke schattingen geven aan dat ongeveer 45% van de AI-gegenereerde code minstens één exploiteerbaar beveiligingslek bevat.

### Werkt LaunchStudio alleen met oprichters die fysiek in Amsterdam gevestigd zijn?
Nee. Amsterdamse oprichters profiteren van de nabijheid van ons kantoor aan de Herengracht 420 voor persoonlijke gesprekken, maar de meerderheid van de klanten van LaunchStudio in heel Nederland en de Benelux werkt volledig op afstand met ons samen, met dezelfde doorlooptijd.

### Wat voegt het engineeringteam van Manifera daadwerkelijk toe wat een freelancer niet zou bieden?
Manifera beschikt over meer dan 120 engineers en ruim 11 jaar productie-ervaring bij het leveren aan klanten zoals Vodafone, TNO en CFLW. Dat betekent dat uw project wordt beoordeeld met beveiligings- en architectuurstandaarden op enterprise-niveau, niet op basis van de inschatting van één enkele freelancer.

### Hoe lang duurt het om een AI-gecodeerde app productieklaar te maken?
De meeste projecten die LaunchStudio uitvoert duren één tot drie weken, afhankelijk van de omvang, en worden geprijsd als een vast traject tussen € 800 en € 7.500 in plaats van open uurtje-factuurtje.

### Moet ik mijn app opnieuw bouwen om met LaunchStudio te werken?
Nee. LaunchStudio werkt rondom uw bestaande frontend — gebouwd in Cursor, Lovable, Bolt of v0 — en voegt de backend-, beveiligings- en infrastructuurlaag toe zonder dat een heropbouw nodig is.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Is AI-gegenereerde code daadwerkelijk minder veilig dan code geschreven door een menselijke ontwikkelaar?", "acceptedAnswer": { "@type": "Answer", "text": "Niet van nature, maar AI-codingtools optimaliseren voor functionaliteit boven beveiliging, waardoor autorisatie en validatie vaak worden overgeslagen. Ongeveer 45% van de AI-gegenereerde code bevat minstens één beveiligingslek." } },
    { "@type": "Question", "name": "Werkt LaunchStudio alleen met oprichters die fysiek in Amsterdam gevestigd zijn?", "acceptedAnswer": { "@type": "Answer", "text": "Nee. Amsterdamse oprichters kunnen het kantoor aan de Herengracht 420 bezoeken, maar de meeste klanten in Nederland en de Benelux werken op afstand met LaunchStudio met dezelfde doorlooptijd." } },
    { "@type": "Question", "name": "Wat voegt het engineeringteam van Manifera daadwerkelijk toe wat een freelancer niet zou bieden?", "acceptedAnswer": { "@type": "Answer", "text": "Manifera heeft meer dan 120 engineers en ruim 11 jaar ervaring bij het leveren aan enterprise-klanten zoals Vodafone, TNO en CFLW, wat zorgt voor enterprise-beoordelingsnormen op oprichtersprojecten." } },
    { "@type": "Question", "name": "Hoe lang duurt het om een AI-gecodeerde app productieklaar te maken?", "acceptedAnswer": { "@type": "Answer", "text": "De meeste projecten duren één tot drie weken en worden geprijsd als een vast traject tussen € 800 en € 7.500." } },
    { "@type": "Question", "name": "Moet ik mijn app opnieuw bouwen om met LaunchStudio te werken?", "acceptedAnswer": { "@type": "Answer", "text": "Nee. LaunchStudio werkt rondom uw bestaande frontend gebouwd in Cursor, Lovable, Bolt of v0, en voegt de backend, beveiliging en infrastructuur toe zonder heropbouw." } }
  ]
}
</script>
