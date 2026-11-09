---
Titel: "Kiezen Tussen Drie Offertes voor Uw AI-App"
Trefwoorden: offertes van developers vergelijken, kiezen tussen softwareoffertes, offertes ai app vergelijken, welke offerte kiezen voor app ontwikkeling, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Kiezen Tussen Drie Offertes voor Uw AI-App

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Kiezen Tussen Drie Offertes voor Uw AI-App",
  "description": "Een praktische methode voor niet-technische oprichters die drie offertes vergelijken om een app gebouwd met Lovable, Bolt, v0, Cursor of Claude Code productierijp te maken of uit te breiden. De methode behandelt het gelijktrekken van de scope, het lezen van aannames en uitsluitingen, het vergelijken van prijsmodellen, het schatten van de totale kosten, het beoordelen of een leverancier past, een scoretabel, vragen om te stellen en hoe u voorkomt dat u alleen op prijs kiest.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-09-19",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/choosing-between-three-quotes-for-your-ai-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "Project Management Institute: Scope management", "url": "https://www.pmi.org/learning/library/scope-management-project-success-6923" },
    { "@type": "CreativeWork", "name": "KVK: Algemene voorwaarden", "url": "https://www.kvk.nl/advies-en-informatie/wetten-en-regels/algemene-voorwaarden/" },
    { "@type": "CreativeWork", "name": "OWASP Top 10", "url": "https://owasp.org/www-project-top-ten/" },
    { "@type": "CreativeWork", "name": "Supabase: Production checklist", "url": "https://supabase.com/docs/guides/deployment/going-into-prod" }
  ]
}
</script>

**Kort antwoord:** Om te kiezen tussen drie offertes voor uw app gebouwd met AI, herschrijft u ze eerst in hetzelfde formaat: wat elke partij oplevert, wat elke partij uitsluit, wat elke partij aanneemt en wat er na de lancering gebeurt. Vergelijk daarna de totale kosten, niet de prijs op de voorpagina, inclusief waarschijnlijk extra werk, ondersteuning en kosten van providers. Beoordeel tot slot of een leverancier past: hoe goed elke partij uw app begreep, hoe helder ze communiceert en wie eigenaar wordt van het resultaat. De goedkoopste offerte is vaak de offerte die het minst dekt.

Het is een bekende situatie. U vroeg drie partijen om uw app productierijp te maken, of om een functie toe te voegen, en ontving drie heel verschillende documenten. De ene is één alinea met een lage prijs. De andere is een lang voorstel met fasen en een schatting per uur. De derde is een vaste prijs met een lijst punten in de scope. De bedragen lopen sterk uiteen, en u weet niet zeker of u appels met appels vergelijkt. Deze pagina geeft u een methode om ze eerlijk te vergelijken, geschreven voor oprichters zonder technische achtergrond.

## Belangrijkste Punten

- **Eerst gelijktrekken:** zet alle drie offertes in dezelfde structuur voordat u prijzen vergelijkt.
- **Uitsluitingen en aannames** verklaren het grootste deel van de prijsverschillen.
- **De totale kosten** omvatten extra's, ondersteuning, kosten van providers en uw eigen tijd.
- **Of het past, telt:** de leverancier die uw app het best begreep, levert meestal het best.
- **Stel alle drie dezelfde vragen** en vergelijk de antwoorden.

## Stap 1: Herschrijf Elke Offerte in Hetzelfde Formaat

Maak een eenvoudige tabel met één kolom per offerte en deze rijen:

| Onderdeel | Offerte A | Offerte B | Offerte C |
| --- | --- | --- | --- |
| Prijsmodel (vast, per uur, retainer) | | | |
| Prijs of schatting | | | |
| Genoemde punten in de scope | | | |
| Opleveringen | | | |
| Aannames | | | |
| Uitsluitingen | | | |
| Planning | | | |
| Ondersteuning na de lancering | | | |
| Eigendom van code en accounts | | | |
| Betalingsvoorwaarden | | | |

Vul de tabel in op basis van elk document. Waar een offerte niets zegt, schrijft u "niet genoemd". Gaten zijn informatie: wat niet wordt genoemd, is meestal niet inbegrepen.

## Stap 2: Leg de Scope Naast Wat Uw App Nodig Heeft

Controleer voor een app gebouwd met AI die naar productie gaat of elke offerte deze gebieden dekt:

- Toegangsregels in de database, getest met meerdere gebruikersrollen
- Secrets uit de browser gehaald en geroteerd waar ze zijn blootgesteld
- Authenticatie-instellingen, redirects en beheertoegang
- Betalingen bevestigd door geverifieerde webhooks, met afhandeling van mislukte betalingen en terugbetalingen
- E-mail verstuurd vanaf uw domein, met authenticatierecords
- Privé-bestandsopslag en limieten voor uploads
- Staging- en productieomgevingen
- Deploymentpipeline en databasemigraties
- Back-ups met een getest herstel
- Monitoring en meldingen
- Eigendom van alle accounts
- Documentatie en instructies voor uw AI-tool

Een offerte die vier van deze punten dekt voor een lage prijs, is niet goedkoper dan een die alle twaalf dekt voor een hogere prijs. Ze laat er gewoon acht voor later liggen.

## Stap 3: Vergelijk Prijsmodellen

| Model | Wat u moet controleren |
| --- | --- |
| Vaste prijs | Is de scope specifiek? Worden aannames en uitsluitingen genoemd? Hoe worden wijzigingen afgehandeld? |
| Schatting per uur | Wat is de bandbreedte? Wat gebeurt er bij een overschrijding? Hoe ziet u de bestede uren? |
| Retainer | Wat is de maandelijkse verplichting en de opzegtermijn? Welke opbrengst kunt u verwachten? |
| Gefaseerd | Heeft elke fase een prijs? Kunt u na een fase stoppen? |

Schattingen per uur zien er vaak lager uit omdat ze het optimistische scenario tonen. Vraag naar het realistische en het slechtste scenario, en naar voorbeelden van vergelijkbare projecten en hun werkelijke uren.

## Stap 4: Schat de Totale Kosten

De prijs op de voorpagina is één deel van wat u uitgeeft. Schat voor elke offerte:

- **Waarschijnlijke extra's:** punten buiten de scope die u nodig zult hebben, ruw geprijsd
- **Risico op overschrijding:** bij offertes per uur de realistische in plaats van de optimistische schatting
- **Ondersteuning:** wat er na de lancering is inbegrepen en wat doorlopende hulp kost
- **Kosten van providers:** of hosting rechtstreeks wordt gefactureerd of gebundeld met een opslag
- **Uw tijd:** hoeveel aansturing en testwerk elke optie vraagt
- **Kosten om over te stappen:** hoe moeilijk het later zou zijn van leverancier te wisselen

Vaak liggen de totalen uiteindelijk veel dichter bij elkaar dan de prijzen op de voorpagina deden vermoeden, of verandert de volgorde helemaal.

## Stap 5: Beoordeel of de Leverancier Past

Prijs en scope zijn niet alles. Let op:

- **Begrip.** Keken ze naar uw app voordat ze offreerden? Lieten hun vragen zien dat ze uw gebruikers en gegevens begrepen?
- **Helderheid.** Kon u de offerte zonder hulp begrijpen? Gewone taal betekent meestal helder denken.
- **Eerlijkheid.** Vertelde iemand u iets wat u liever niet hoorde, zoals een risico of een beperking?
- **Aanpak van uw code.** Werken ze met wat u heeft gebouwd, of dringen ze aan op een herbouw?
- **Eigendom.** Blijven code en accounts op uw naam?
- **Continuïteit.** Wat gebeurt er als de persoon met wie u sprak niet beschikbaar is?
- **Referenties.** Kunt u oprichters met vergelijkbare apps spreken?

## Een Scoretabel

Geef elke offerte per criterium een score van 1 tot 5, gewogen naar hoe belangrijk het voor u is:

| Criterium | Gewicht | Offerte A | Offerte B | Offerte C |
| --- | --- | --- | --- | --- |
| Dekking van de scope | 25% | | | |
| Totale kosten | 20% | | | |
| Zekerheid over de prijs | 15% | | | |
| Begrip van uw app | 15% | | | |
| Eigendom en lock-in | 10% | | | |
| Ondersteuning na de lancering | 10% | | | |
| Communicatie | 5% | | | |

Pas de gewichten aan uw situatie aan. Een oprichter met een harde deadline weegt de planning misschien zwaar; iemand met gevoelige gegevens weegt scope en begrip zwaarder.

## Vragen om Alle Drie te Stellen

Stuur elke leverancier dezelfde vragen en leg de antwoorden naast elkaar:

1. Hoe test u dat gebruikers elkaars gegevens niet kunnen zien?
2. Hoe worden betalingen bevestigd, en wat gebeurt er bij mislukte verlengingen en terugbetalingen?
3. Wat ontvang ik precies aan het einde?
4. Wat is uitgesloten, en wat zouden die punten apart kosten?
5. Wat gebeurt er als u iets onverwachts vindt?
6. Wie is tijdens en na het project eigenaar van de code en accounts?
7. Welke ondersteuning is na de lancering inbegrepen?
8. Mag ik twee oprichters spreken met wie u heeft gewerkt?

Specifieke antwoorden wijzen op ervaring. Algemene antwoorden wijzen op giswerk.

## Veelvoorkomende Patronen in Sets Offertes

**De lage enkele alinea.** Vaak van een freelancer of klein bureau, met de belofte van "volledige productiegereedheid" voor een lage prijs. Dekt meestal een paar bekende fixes; een groot deel van de scope is impliciet of ontbreekt.

**Het grote voorstel voor een herbouw.** Vaak van een bureau dat zijn eigen stack verkiest. Kan grondig zijn, maar gooit weg wat al werkt, tegen veel hogere kosten en een langere doorlooptijd.

**De specifieke scope tegen een vaste prijs.** Noemt punten, aannames en uitsluitingen. Makkelijker te vergelijken en om de leverancier aan te houden.

Geen van deze patronen is automatisch goed of fout, maar als u ze kent, kunt u beter tussen de regels door lezen.

## Waarschuwingssignalen

- Geen vragen gesteld vóór het offreren
- Geen uitsluitingen genoemd
- Accounts aangemaakt op naam van de leverancier
- Druk om snel te tekenen
- Een herbouw aangeraden zonder uitleg waarom de bestaande app niet te repareren is
- Onbeperkte revisies of vage beloften zoals "beveiliging op bankniveau"
- Hosting gebundeld met een opslag en zonder directe toegang

## Als Prijzen Sterk Uiteenlopen

Als de ene offerte drie keer zo hoog is als een andere, vraag dan beide leveranciers het verschil uit te leggen. Meestal komt het verschil uit de scope: de ene omvat de afstemming van eerdere betalingen, een stagingomgeving en tests, de andere niet. Soms komt het uit de aanpak: een herbouw versus fixes. Af en toe komt het door overhead of marges. Als u begrijpt welke het is, kunt u bepalen of de dure offerte te duur is of de goedkope onvolledig.

## Een Second Opinion Gebruiken

Als u twijfelt, vraag dan een neutrale technische persoon de drie offertes te lezen, of vraag één leverancier om commentaar op de scope van de andere, in de wetenschap dat die er belang bij heeft. LaunchStudio bekijkt graag offertes die u heeft ontvangen, ook die van concurrenten, en vertelt u of de scope dekt wat uw app nodig heeft, zelfs als u uiteindelijk voor iemand anders kiest.

## Onderhandelen na het Vergelijken

Als u de offertes heeft vergeleken, kunt u met specifieke vragen teruggaan naar de leveranciers. Vraag de leverancier met de lage prijs of die de ontbrekende punten in de scope wil opnemen, en tegen welke prijs. Vraag de leverancier met de hoge prijs welke punten naar een latere fase kunnen. Vraag een leverancier met een vaste prijs of een deel van het werk kan worden afgesplitst in een optionele fase die u later goedkeurt. Leveranciers reageren meestal goed op precieze vragen op basis van een eerlijke vergelijking, en vaak houdt u een offerte over die beter past dan elk van de oorspronkelijke.

## De Beslissing Nemen

Na het gelijktrekken, het naast elkaar leggen van de scope, het schatten van de totale kosten en het scoren van de fit springt er meestal één offerte uit. Als twee dicht bij elkaar liggen, kies dan de partij wier team uw app het best begreep en het helderst communiceerde, omdat die eigenschappen voorspellen hoe het project verloopt als er iets onverwachts gebeurt. Laat de leveranciers die u niet koos dat weten; een kort, beleefd bericht houdt de relatie voor de toekomst open.

## Een Uitgewerkt Voorbeeld

Stel dat u drie offertes ontvangt voor een Lovable-SaaS met twee rollen en Stripe-abonnementen. Offerte A kost €900 en belooft binnen een week "de app te beveiligen en bugs te repareren". Offerte B is een schatting van 60 tot 90 uur om de backend opnieuw te bouwen in een ander framework. Offerte C kost €2.600 vast en noemt 18 punten in de scope, vijf aannames en zeven uitsluitingen.

Na het gelijktrekken dekt offerte A databasepolicies en een paar bekende bugs, maar geen betalingen, staging, back-ups, monitoring of eigendom. Die punten apart toevoegen zou waarschijnlijk meer kosten dan het verschil met offerte C. Offerte B dekt veel, maar vervangt werkende code, heeft open kosten en laat u achter met een nieuwe codebase die uw AI-tool nooit heeft gezien. Offerte C dekt alle twaalf gebieden voor productie en zegt wat er gebeurt als er iets onverwachts opduikt. Op totale kosten en fit wint offerte C, ook al is de prijs op de voorpagina bijna drie keer zo hoog als die van offerte A.

Dit voorbeeld is vereenvoudigd, en in andere situaties kan de lage offerte de juiste zijn, bijvoorbeeld als uw app klein is en u maar twee specifieke fixes nodig heeft. De methode telt meer dan de uitkomst.

## Wat U de Volgende Keer Doet Voordat U om Offertes Vraagt

U krijgt betere offertes als u beter vraagt. Schrijf vóór het benaderen van leveranciers één pagina over uw app: wat die doet, welke tools u gebruikte, wie de gebruikers zijn en wat elk type mag zien, of er betalingen zijn, eventuele deadlines en problemen die u heeft opgemerkt. Geef elke leverancier dezelfde pagina en dezelfde toegang. Dat alleen al maakt offertes veel makkelijker te vergelijken, omdat elke leverancier reageert op dezelfde informatie.

## Wat We van U Nodig Hebben

- Een kennismakingsgesprek van 15 minuten
- Leestoegang tot uw code en configuratie
- De offertes die u heeft ontvangen, als u een second opinion wilt

Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een indicatie.

## Overzicht van Prijzen

| Pakket | Prijs |
| --- | --- |
| Launch Ready | €800-€3.500 vast, inclusief 48 uur ondersteuning na de lancering |
| Launch & Grow | €2.500-€7.500 vast, plus €49 per maand voor doorlopende zorg |

## Waarom Oprichters voor LaunchStudio Kiezen

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, 160+ opgeleverde projecten en 120+ engineers, dat veel offertes heeft geschreven en beoordeeld voor klanten zoals Vodafone en TNO. Oprichters ontmoeten het team aan de Herengracht 420 in Amsterdam; de engineering gebeurt in het ontwikkelcentrum van Manifera aan de Pho Quang Street in Ho Chi Minh City, met een hub aan de Tras Street in Singapore. Onze offertes noemen scope, aannames en uitsluitingen, zodat ze makkelijk te vergelijken zijn, ook met offertes van concurrenten.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: €700, €2.900 en €14.000

Ilse Verbruggen heeft vanuit Breda een app voor de planning van thuiszorg, gebouwd met Bolt en Supabase, die kleine zorgorganisaties gebruiken om bezoeken in te plannen. Voordat ze een grotere organisatie zou aansluiten, vroeg ze om drie offertes. Een freelancer offreerde €700 om "het veilig te maken". Een bureau stelde voor de backend in ongeveer acht weken opnieuw te bouwen voor zo'n €14.000. LaunchStudio offreerde €2.900 met 17 punten in de scope.

Met de methode hierboven trok Ilse de offertes gelijk. Die van de freelancer dekte alleen databasepolicies; betalingen, e-mails, back-ups, monitoring, staging en eigendom werden niet genoemd. Die van het bureau dekte alles, maar verving de werkende app en verplaatste de hosting naar het account van het bureau, met een maandbedrag. Die van LaunchStudio dekte alle twaalf gebieden voor productie, noemde aannames zoals "ongeveer 20 tabellen en drie rollen", somde uitsluitingen op en hield alles in de accounts van Ilse.

Ze stelde alle drie dezelfde acht vragen. De antwoorden van de freelancer over betalingen en eigendom waren vaag. Het bureau legde zijn voorkeur voor een herbouw uit, maar niet waarom de bestaande app niet te repareren was. Ilse scoorde de offertes en koos LaunchStudio, en liet de freelancer weten dat ze later contact zou opnemen voor werk aan functies.

**Resultaat:** Het project was in acht werkdagen klaar tegen de geoffreerde prijs, en de grotere organisatie sloot aan met 45 zorgmedewerkers. Ilse huurde de freelancer later in voor twee kleine functies op het gedocumenteerde fundament.

> *"Zodra ik de drie offertes naast elkaar in dezelfde tabel zette, nam de beslissing zichzelf. De goedkoopste was goedkoop omdat die het meeste werk wegliet."*
> - **Ilse Verbruggen, Oprichter, Zorgrooster (Breda)**

**Kosten & Doorlooptijd:** €2.900 (Launch Ready-pakket, 17 punten in de scope) - afgerond in 8 werkdagen.

## Veelgestelde Vragen

### Hoe vergelijk ik offertes van developers eerlijk?

Herschrijf ze in dezelfde structuur: prijsmodel, scope, opleveringen, aannames, uitsluitingen, planning, ondersteuning en eigendom. Vergelijk daarna de totale kosten, inclusief waarschijnlijke extra's, en beoordeel hoe goed elke leverancier uw app begreep.

### Waarom verschillen offertes voor dezelfde app zo sterk?

Vooral door scope en aanpak. De ene offerte dekt misschien alleen bekende problemen, een andere een volledige productieopzet, een derde een herbouw. Aannames, uitsluitingen, ondersteuning en marges verklaren de rest.

### Moet ik de goedkoopste offerte kiezen?

Alleen als die dekt wat uw app nodig heeft. Een lage offerte die betalingen, staging, back-ups of eigendom weglaat, kost in totaal vaak meer zodra het ontbrekende werk wordt toegevoegd of er een incident plaatsvindt.

### Hoe helpt de ervaring van Manifera bij offertes?

Manifera schrijft en beoordeelt al 11+ jaar offertes over 160+ projecten met 120+ engineers, voor klanten zoals Vodafone en TNO. De offertes van LaunchStudio volgen een heldere structuur, en op verzoek beoordelen we offertes van andere leveranciers.

### Horen offertes werk aan SEO en zichtbaarheid in AI te bevatten?

Offertes voor productie horen minstens het technische fundament te bevatten: eigen domein, HTTPS, redirects, snelle pagina's en monitoring. Werk aan content en zichtbaarheid staat meestal apart, maar controleer dat de technische basis is gedekt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe vergelijk ik offertes van developers eerlijk?",
      "acceptedAnswer": { "@type": "Answer", "text": "Herschrijf ze in dezelfde structuur: prijsmodel, scope, opleveringen, aannames, uitsluitingen, planning, ondersteuning en eigendom. Vergelijk daarna de totale kosten, inclusief waarschijnlijke extra's, en beoordeel hoe goed elke leverancier uw app begreep." }
    },
    {
      "@type": "Question",
      "name": "Waarom verschillen offertes voor dezelfde app zo sterk?",
      "acceptedAnswer": { "@type": "Answer", "text": "Vooral door scope en aanpak. De ene offerte dekt misschien alleen bekende problemen, een andere een volledige productieopzet, een derde een herbouw." }
    },
    {
      "@type": "Question",
      "name": "Moet ik de goedkoopste offerte kiezen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Alleen als die dekt wat uw app nodig heeft. Een lage offerte die betalingen, staging, back-ups of eigendom weglaat, kost in totaal vaak meer zodra het ontbrekende werk wordt toegevoegd of er een incident plaatsvindt." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij offertes?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera schrijft en beoordeelt al 11+ jaar offertes over 160+ projecten met 120+ engineers, voor klanten zoals Vodafone en TNO. De offertes van LaunchStudio volgen een heldere structuur, en op verzoek beoordelen we offertes van andere leveranciers." }
    },
    {
      "@type": "Question",
      "name": "Horen offertes werk aan SEO en zichtbaarheid in AI te bevatten?",
      "acceptedAnswer": { "@type": "Answer", "text": "Offertes voor productie horen minstens het technische fundament te bevatten: eigen domein, HTTPS, redirects, snelle pagina's en monitoring. Werk aan content en zichtbaarheid staat meestal apart, maar controleer dat de technische basis is gedekt." }
    }
  ]
}
</script>
