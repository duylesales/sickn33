---
Titel: "Wat Er Gebeurt in Week Eén, Twee en Drie van een Productielancering"
Trefwoorden: tijdlijn productielancering, wat te verwachten bij app-lancering, werkwijze launchstudio per week, projectplan productiegereedheid, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Wat Er Gebeurt in Week Eén, Twee en Drie van een Productielancering

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wat Er Gebeurt in Week Eén, Twee en Drie van een Productielancering",
  "description": "Een beschrijving per week van een productielancering door LaunchStudio voor een app gebouwd met Lovable, Bolt, v0, Cursor of Claude Code: wat er vóór de start gebeurt, toegang en beoordeling in week één, reparaties en inrichting in week twee, testen, release en overdracht in week drie, wat de oprichter elke week doet, hoe updates en beslissingen werken en hoe kortere Launch Ready-projecten dezelfde stappen inkorten.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-10-18",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/what-happens-in-week-one-two-and-three-of-a-production-launch" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Production checklist", "url": "https://supabase.com/docs/guides/deployment/going-into-prod" },
    { "@type": "CreativeWork", "name": "Google SRE Book: Release Engineering", "url": "https://sre.google/sre-book/release-engineering/" },
    { "@type": "CreativeWork", "name": "OWASP Top 10", "url": "https://owasp.org/www-project-top-ten/" },
    { "@type": "CreativeWork", "name": "Agile Alliance: Definition of Done", "url": "https://www.agilealliance.org/glossary/definition-of-done/" }
  ]
}
</script>

Oprichters die nog nooit met een ontwikkelpartner hebben gewerkt, vragen zich vaak af hoe het project in de praktijk zal voelen. Krijgen ze technische vragen die ze niet kunnen beantwoorden? Is de app offline? Hoeveel van hun tijd kost het? Wanneer zien ze resultaat? Onzekerheid over het proces is een van de redenen waarom oprichters productiewerk uitstellen waarvan ze weten dat het nodig is.

Deze pagina beschrijft een gebruikelijk LaunchStudio-project van drie weken, de duur van veel Launch & Grow-projecten en de langere Launch Ready-projecten. Kortere Launch Ready-projecten van drie tot vijf werkdagen volgen dezelfde stappen in ingekorte vorm. Elk project is anders, maar het ritme is consistent, en dat vooraf kennen maakt de ervaring rustiger.

## Belangrijkste Punten

- **Uw app blijft de hele tijd live;** het werk gebeurt op staging tot de release.
- **Week één draait om toegang en beoordeling,** en eindigt met een geprioriteerde lijst met bevindingen.
- **Week twee draait om reparaties en inrichting,** met korte updates en af en toe een beslissing voor u.
- **Week drie draait om testen, release en overdracht,** gevolgd door ondersteuning na de lancering.
- **Uw tijdsinvestering is bescheiden:** een paar korte gesprekken, enkele beslissingen en een laatste controle.

## Vóór de Start

Vóór week één gebeuren er drie dingen. Eerst een kennismakingsgesprek van ongeveer 15 minuten, waarin we leren over uw app, gebruikers, plannen en deadline. Daarna een korte blik op het project met leestoegang, zodat de offerte op de werkelijkheid is gebaseerd. Ten slotte een schriftelijke vaste offerte met scope, aannames, uitsluitingen, planning en prijs, die u goedkeurt. Als er persoonsgegevens in het spel zijn, tekenen we een verwerkersovereenkomst. We spreken een startdatum af, en u ontvangt een korte lijst met accounts waarvoor u ons uitnodigt.

## Week Eén: Toegang en Beoordeling

**Dag 1 en 2: toegang en eigendom.** U nodigt ons team uit in uw accounts met individuele rollen. We maken het overzicht van accounts en controleren het eigendom. Als iets op naam van iemand anders staat, zoals een database in het account van een freelancer of een domein dat door een voormalige partner is geregistreerd, beginnen we het naar het eigendom van uw bedrijf over te brengen, omdat sommige overdrachten dagen duren. We richten ook een stagingomgeving in als die er nog niet is, zodat we nooit experimenteren op uw live app.

**Dag 2 tot 4: beoordeling.** We beoordelen de gebieden binnen de scope: databasepolicies getest met accounts in verschillende rollen, geheimen, authenticatie, opslag, betalingen, e-mails, prestaties, deployment, back-ups en monitoring, plus alles wat specifiek is voor uw sector. Bevindingen worden vastgelegd met hun ernst en bewijs. Als we iets urgents vinden, zoals een uitgelekte servicesleutel of klantgegevens die door iedereen te lezen zijn, vertellen we het u dezelfde dag en lossen we het meestal direct op.

**Dag 5: gesprek over de bevindingen.** In een gesprek van ongeveer 30 tot 45 minuten lopen we de bevindingen in begrijpelijke taal met u door, bevestigen we de prioriteiten en stellen we de zakelijke vragen die alleen u kunt beantwoorden, zoals "mag een teamlid facturen zien?" of "wat moet er gebeuren als een verlenging mislukt?". Als er iets buiten de oorspronkelijke scope opduikt, leggen we de opties en kosten uit; niets extra's gebeurt zonder uw goedkeuring.

**Uw betrokkenheid in week één:** ons uitnodigen in de accounts, een paar snelle vragen via berichten en het gesprek over de bevindingen.

## Week Twee: Reparaties en Inrichting

**Reparaties in volgorde van prioriteit.** De ernstigste problemen komen eerst: toegang tot gegevens, geheimen, betalingen. Daarna de productieopzet: omgevingen, pipeline, migraties, e-mailauthenticatie, back-ups met een hersteltest en monitoring. Daarna prestaties, opschonen en resterende punten. Alle wijzigingen komen binnen als pull requests in uw repository en worden naar staging uitgerold.

**Tests.** Terwijl we repareren, voegen we geautomatiseerde tests toe voor de regels die ertoe doen, zoals "een gebruiker van bedrijf A kan de facturen van bedrijf B niet zien" of "een betaalwebhook die twee keer wordt verwerkt, maakt één bestelling aan". Deze tests blijven na het project in uw repository.

**Korte updates.** U ontvangt om de één of twee dagen een schriftelijke update: wat er is gedaan, wat er volgt en of we iets van u nodig hebben. Updates zijn kort en in begrijpelijke taal, met links naar staging als u wilt kijken.

**Beslissingen.** Soms brengt een reparatie een keuze met zich mee die gebruikers raakt, zoals hoe lang gegevens van sollicitanten worden bewaard, wat klanten zien als een betaling mislukt of of bestaande gebruikers na een beveiligingswijziging opnieuw moeten inloggen. We leggen de opties uit en bevelen er een aan; u beslist.

**Uw betrokkenheid in week twee:** updates lezen, af en toe een vraag beantwoorden en, als u wilt, staging uitproberen.

## Week Drie: Testen, Release en Overdracht

**Dag 1 en 2: verificatie.** We herhalen de oorspronkelijke tests op de gerepareerde versie, draaien de geautomatiseerde tests, controleren de belangrijkste routes van begin tot eind op staging en voeren waar relevant belastings- of prestatietests uit. We vullen de checklist voor lanceringsgereedheid in met bewijs voor elk punt.

**Dag 2 of 3: uw controle op staging.** U besteedt ongeveer een uur aan het doorlopen van de belangrijkste routes van uw app op staging: registreren, inloggen, de kernacties, betalen indien relevant, e-mails. U bevestigt dat alles werkt en eruitziet zoals verwacht. Alles wat niet overeenkomt met de scope, wordt opgelost.

**Dag 3 of 4: release.** We brengen de release op een werkdag naar productie, vroeg genoeg om de rest van de dag te kunnen monitoren. Als er een migratie van gegevens of gebruikers bij komt kijken, spreken we een rustig moment af. Na de release lopen we samen met u de belangrijkste routes in productie door en bevestigen we dat monitoring en meldingen werken. Een rollback ligt klaar als dat nodig is.

**Dag 4 of 5: overdracht.** In een overdrachtsgesprek van ongeveer een uur lopen we de schriftelijke samenvatting, het overzicht van accounts, de procedures voor releases, rollback en herstel en de projectinstructies voor uw AI-tool door. Toegang die we niet meer nodig hebben, wordt ingetrokken of beperkt tot wat de doorlopende zorg vereist.

**Uw betrokkenheid in week drie:** de controle op staging, beschikbaar zijn op de dag van de release en het overdrachtsgesprek.

## Na Week Drie

Launch Ready-projecten bevatten 48 uur ondersteuning na de release, waarin we de monitoring nauwlettend volgen en problemen oplossen die met het werk samenhangen. Launch & Grow gaat verder met doorlopende zorg voor €49 per maand: monitoring, updates, controles van back-ups, platformtoezicht, een maandelijkse gezondheidsnotitie en kleine reparaties. Hoe dan ook blijven problemen die door ons werk zijn veroorzaakt ook na de ondersteuningsperiode onze verantwoordelijkheid.

## Hoe Kortere Projecten Dezelfde Stappen Inkorten

Een klein Launch Ready-project van drie tot vijf werkdagen volgt dezelfde volgorde in minder tijd. Toegang en beoordeling gebeuren op dag één, met de bevindingen aan het einde van de dag of de volgende ochtend. Reparaties en inrichting kosten één tot drie dagen. Testen, uw controle op staging, release en overdracht gebeuren op de laatste dag of twee. Het gesprek over de bevindingen en het overdrachtsgesprek kunnen worden gecombineerd of ingekort, maar de stappen blijven.

## Wat de Planning Kan Veranderen

- **Overdrachten van eigendom** die afhangen van derden, zoals een domeinregistrar of een voormalige freelancer
- **Externe goedkeuringen,** zoals beoordelingen door betaalpartners of indieningen in app stores
- **Beslissingen** die langer duren, bijvoorbeeld juridische input over bewaartermijnen
- **Onverwachte bevindingen** die u aan de scope wilt toevoegen
- **Uw lanceringsdatum,** als we terugplannen vanaf een vaste deadline

We melden deze punten vroeg en passen het plan samen met u aan. Als een vaste deadline in gevaar komt, bespreken we welke punten voorrang krijgen, zodat de belangrijkste risico's vóór de lancering zijn opgelost.

## Uw App Tijdens het Project

Uw productieapp blijft de hele tijd draaien. We werken op staging en brengen wijzigingen op een gepland moment uit. Als u tijdens het project met uw AI-tool blijft bouwen, spreken we af welke gebieden worden gewijzigd, zodat het werk niet botst. Veel oprichters pauzeren grotere wijzigingen gewoon twee of drie weken en richten zich op verkoop, klanten of het voorbereiden van hun lanceringscommunicatie.

## Communicatiekanalen

We spreken bij de start één kanaal af, zoals een gedeelde chat of e-mailwisseling, voor updates en vragen, met een vaste contactpersoon aan onze kant. Gesprekken worden ingepland tijdens Nederlandse kantooruren vanuit Amsterdam; de engineering in Ho Chi Minh City begint eerder op de dag, wat vaak betekent dat er al voortgang zichtbaar is wanneer u aan uw ochtend begint. Urgente zaken worden duidelijk gemarkeerd, zodat ze nooit verloren gaan tussen de gewone updates.

## Wat U aan het Einde Heeft

Aan het einde van week drie heeft u een app die veilig is, van u is, correct is uitgerold, wordt gemonitord en gedocumenteerd is; een testsuite die de belangrijkste regels beschermt; procedures die u zonder ons kunt volgen; instructies die uw AI-tool in lijn houden met het werk; en een ingevulde lanceringschecklist die laat zien wat er is gecontroleerd en hoe.

## Voorbereiden op een Soepele Start

U kunt de eerste week versnellen door vóór de startdatum een paar dingen voor te bereiden: een lijst met elke tool en dienst die de app gebruikt, inloggegevens voor de accounts die u bezit, zodat u ons snel kunt uitnodigen, een korte omschrijving van de soorten gebruikers en wat elk mag zien, eventuele vragen of eisen van klanten die u heeft ontvangen en een notitie van problemen die u heeft opgemerkt. Oprichters die dit voorbereiden, hebben hun gesprek over de bevindingen meestal een dag of twee eerder, omdat er minder tijd gaat zitten in het opsporen van accounts.

## Als het Niet Volgens Plan Loopt

Soms stuit een project op een obstakel: een voormalige leverancier draagt een account traag over, de beoordeling door een betaalpartner duurt langer dan verwacht of een beslissing hangt af van een advocaat die op vakantie is. We vertellen het u zodra we het zien, stellen opties voor, zoals een release in twee fasen of tijdelijk om de afhankelijkheid heen werken, en spreken met u een herzien plan af. De scope en prijs blijven zoals afgesproken; alleen de planning schuift, en alleen met uw instemming.

## Prijs

| Pakket | Gebruikelijke duur | Prijs |
| --- | --- | --- |
| Launch Ready | 3-10 werkdagen | €800-€3.500 vast, inclusief 48 uur ondersteuning na de lancering |
| Launch & Grow | 2-4 weken | €2.500-€7.500 vast, plus €49 per maand voor doorlopende zorg |

Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een indicatie.

## Waarom Oprichters voor LaunchStudio Kiezen

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, 160+ opgeleverde projecten en 120+ engineers, dat gestructureerde projecten uitvoert voor klanten zoals Vodafone en TNO. Oprichters ontmoeten het team aan de Herengracht 420 in Amsterdam; de engineering gebeurt in het ontwikkelcentrum van Manifera aan de Pho Quang Street in Ho Chi Minh City, met een hub aan de Tras Street in Singapore. We maken het proces voorspelbaar, zodat u zich op uw klanten kunt richten terwijl uw app voor hen gereed wordt gemaakt.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Drie Weken Vóór de Vakbeurs

Rob Jacobs runt vanuit Eindhoven een SaaS voor verhuurbedrijven van evenementenmateriaal, gebouwd met Cursor en Supabase, en wilde die presenteren op een landelijke vakbeurs. Drie weken vóór de beurs startte hij een Launch & Grow-project met LaunchStudio, geoffreerd op €5.100.

In week één bleek uit het overzicht van accounts dat het domein was geregistreerd door zijn voormalige zakenpartner, dus de overdracht begon op dag één. De beoordeling vond losse policies tussen verhuurbedrijven, Stripe-abonnementen die op de succespagina werden bijgewerkt en geen staging. De servicesleutel in een functie aan de clientkant werd dezelfde middag geroteerd. In het gesprek over de bevindingen besloot Rob dat medewerkers van bedrijven materiaal en boekingen mochten zien, maar geen facturen, tenzij ze een financiële rol hadden.

In week twee werden de policies herschreven met tests, werden een stagingomgeving en een pipeline ingericht, ging Stripe over op geverifieerde webhooks met een afstemming van eerdere abonnementen en werd de e-mailauthenticatie ingesteld. Rob ontving om de dag een update en beantwoordde twee vragen over de regels bij mislukte betalingen.

In week drie besteedde Rob een uur aan het controleren van staging, vond de release op een dinsdagochtend plaats en was het overdrachtsgesprek op donderdag. De overdracht van het domein was op woensdag rond, twee dagen vóór de beurs.

**Resultaat:** Rob demonstreerde het live product op de beurs en sloot tijdens en na het evenement negen verhuurbedrijven aan, zonder één technisch probleem tijdens de onboarding.

> *"Ik verwachtte drie weken chaos. Het werden drie weken met korte berichten, twee gesprekken en één uur klikken door staging. Daarna ging ik naar de beurs met een app die ik vertrouwde."*
> - **Rob Jacobs, Oprichter, Verhuurplanner (Eindhoven)**

**Kosten & Doorlooptijd:** €5.100 (Launch & Grow-pakket: overdracht van eigendom, policies met tests, staging en pipeline, Stripe-webhooks en afstemming, e-mailauthenticatie, monitoring en overdracht, plus €49 per maand) - afgerond in 15 werkdagen.

## Veelgestelde Vragen

### Hoe lang duurt een productielancering met LaunchStudio?

Launch Ready-projecten duren meestal drie tot tien werkdagen, en Launch & Grow-projecten twee tot vier weken. De exacte planning staat in uw vaste offerte en hangt af van de scope, overdrachten van eigendom en eventuele externe goedkeuringen.

### Is mijn app tijdens het project offline?

Nee. We werken op een stagingomgeving en brengen wijzigingen op een gepland moment op een werkdag uit. Migraties van gegevens of gebruikers kunnen een kort, afgesproken tijdvenster nodig hebben, meestal buiten drukke uren.

### Hoeveel van mijn tijd kost het project?

Doorgaans een paar uur, verspreid over het project: ons uitnodigen in de accounts, een gesprek over de bevindingen, af en toe een vraag beantwoorden, een uur staging controleren, beschikbaar zijn op de dag van de release en een overdrachtsgesprek.

### Hoe maakt de ervaring van Manifera het proces voorspelbaar?

Manifera voert al 11+ jaar gestructureerde softwareprojecten uit, over 160+ projecten met 120+ engineers, voor klanten zoals Vodafone en TNO. LaunchStudio past die ervaring toe in een herhaalbaar proces dat is afgestemd op apps gebouwd met AI.

### Bevat het project de basis voor SEO en zichtbaarheid in AI?

Ja. De productieopzet omvat een eigen domein, HTTPS, doorverwijzingen, metadata van pagina's, uitsluiting van staging van indexering en snelle openbare pagina's, die zoekmachines en AI-antwoordmachines helpen uw site vanaf de lancering goed te lezen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe lang duurt een productielancering met LaunchStudio?",
      "acceptedAnswer": { "@type": "Answer", "text": "Launch Ready-projecten duren meestal drie tot tien werkdagen, en Launch & Grow-projecten twee tot vier weken. De exacte planning staat in uw vaste offerte en hangt af van de scope, overdrachten van eigendom en eventuele externe goedkeuringen." }
    },
    {
      "@type": "Question",
      "name": "Is mijn app tijdens het project offline?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. We werken op een stagingomgeving en brengen wijzigingen op een gepland moment op een werkdag uit." }
    },
    {
      "@type": "Question",
      "name": "Hoeveel van mijn tijd kost het project?",
      "acceptedAnswer": { "@type": "Answer", "text": "Doorgaans een paar uur, verspreid over het project: ons uitnodigen in de accounts, een gesprek over de bevindingen, af en toe een vraag beantwoorden, een uur staging controleren, beschikbaar zijn op de dag van de release en een overdrachtsgesprek." }
    },
    {
      "@type": "Question",
      "name": "Hoe maakt de ervaring van Manifera het proces voorspelbaar?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera voert al 11+ jaar gestructureerde softwareprojecten uit, over 160+ projecten met 120+ engineers, voor klanten zoals Vodafone en TNO. LaunchStudio past die ervaring toe in een herhaalbaar proces dat is afgestemd op apps gebouwd met AI." }
    },
    {
      "@type": "Question",
      "name": "Bevat het project de basis voor SEO en zichtbaarheid in AI?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. De productieopzet omvat een eigen domein, HTTPS, doorverwijzingen, metadata van pagina's, uitsluiting van staging van indexering en snelle openbare pagina's, die zoekmachines en AI-antwoordmachines helpen uw site vanaf de lancering goed te lezen." }
    }
  ]
}
</script>
