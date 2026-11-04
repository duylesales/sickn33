---
Titel: "Hoe Verwijder Ik de Gegevens van een Gebruiker in Supabase bij een AVG-Verzoek?"
Trefwoorden: avg verwijdering supabase, recht op vergetelheid app, gebruiker verwijderen supabase, avg verwijderverzoek, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Hoe Verwijder Ik de Gegevens van een Gebruiker in Supabase bij een AVG-Verzoek?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Verwijder Ik de Gegevens van een Gebruiker in Supabase bij een AVG-Verzoek?",
  "description": "Een auth-gebruiker in Supabase verwijderen, verwijdert niet alles. Deze gids legt uit hoe u accountverwijdering ontwerpt voor AVG-verzoeken om gegevenswissing: cascades, bestanden in storage, verwerkers, back-ups, gegevens die u moet bewaren en een selfserviceflow.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-28",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-do-i-delete-a-users-data-in-supabase-for-gdpr" },
  "citation": [
    { "@type": "CreativeWork", "name": "GDPR Article 17: Right to erasure", "url": "https://gdpr-info.eu/art-17-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 5: Principles", "url": "https://gdpr-info.eu/art-5-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 28: Processor", "url": "https://gdpr-info.eu/art-28-gdpr/" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens", "url": "https://www.autoriteitpersoonsgegevens.nl/en" },
    { "@type": "CreativeWork", "name": "Belastingdienst", "url": "https://www.belastingdienst.nl/" }
  ]
}
</script>

**Kort antwoord:** bouw een verwijderfunctie op de server die de rijen van de gebruiker in alle tabellen verwijdert of anonimiseert, hun bestanden uit Supabase Storage verwijdert, hen verwijdert bij verwerkers zoals uw e-mail- en analysetools, alleen bewaart wat u wettelijk moet bewaren (zoals facturen), en tot slot de auth-gebruiker verwijdert. Leg vast hoe lang hun gegevens in back-ups blijven staan. Alleen de gebruiker verwijderen in het Supabase-dashboard laat meestal persoonsgegevens achter.

## Belangrijkste Punten

- **Een gebruiker verwijderen in het Supabase-dashboard verwijdert zelden al hun persoonsgegevens;** bestanden, gerelateerde rijen, verwerkers en back-ups blijven over.
- **Het recht op gegevenswissing van de AVG (artikel 17) kent uitzonderingen,** waaronder wettelijke verplichtingen zoals de Nederlandse administratieplicht, die in het algemeen vereist dat gegevens zeven jaar worden bewaard.
- **Beslis per soort gegevens: verwijderen, anonimiseren of bewaren,** en leg vast waarom.
- **Bouw één verwijderfunctie op de server** die databaserijen, bestanden in storage, verwerkers en de auth-gebruiker in een vaste volgorde afhandelt.
- **Reageer binnen een maand op verzoeken,** zoals de AVG vereist, en vermeld de bewaartermijn van back-ups in uw privacyverklaring.

## Waarom het Verwijderen van de Auth-Gebruiker Niet Genoeg Is

In de meeste AI-gebouwde apps is de rij in `auth.users` alleen de login. Persoonsgegevens staan elders:

| Locatie | Automatisch verwijderd met de auth-gebruiker? |
| --- | --- |
| Tabellen met `on delete cascade` naar `auth.users` | Ja |
| Tabellen zonder die foreign key of met `set null` | Nee |
| Bestanden in Supabase Storage | Nee |
| Contacten en logs bij de e-mailprovider | Nee |
| Analytics en error tracking | Nee |
| Klantrecord bij de betaalprovider | Nee |
| Back-ups | Pas als ze verlopen |

## Stap 1: Breng Persoonsgegevens in Kaart

Maak een lijst van elke tabel en kolom met persoonsgegevens en hoe elk ervan met de gebruiker samenhangt. AI-gegenereerde schema's slaan namen of e-mailadressen vaak op meerdere plekken op, zoals `profiles`, `orders.customer_email` en `messages.author_name`.

## Stap 2: Beslis tussen Verwijderen, Anonimiseren en Bewaren

- **Verwijderen:** profiel, voorkeuren, uploads, berichten die alleen de gebruiker betreffen
- **Anonimiseren:** gegevens waarvan andere gebruikers of uw statistieken afhankelijk zijn, zoals reviews of gedeelde projecten, door persoonlijke velden te vervangen door plaatshouders
- **Bewaren:** gegevens die u wettelijk moet bewaren, zoals facturen voor de Nederlandse belasting (in het algemeen zeven jaar), beperkt tot wat vereist is

Het recht op gegevenswissing van de AVG kent uitzonderingen, waaronder wettelijke verplichtingen. Leg uw beslissingen vast.

## Stap 3: Een Verwijderfunctie

Implementeer verwijdering in één edge function of databasefunctie die:

1. Controleert dat het verzoek van de gebruiker komt (of van een bevoegde beheerder)
2. Rijen in een transactie verwijdert of anonimiseert
3. De storage-objecten van de gebruiker op pad verwijdert
4. De API's van verwerkers aanroept om het contact te verwijderen (e-mailprovider, CRM, analytics)
5. De auth-gebruiker verwijdert
6. Vastlegt dat er een verwijdering heeft plaatsgevonden, zonder de verwijderde gegevens op te slaan

## Stap 4: Selfservice

Bied in de instellingen "Mijn account verwijderen" aan, met een bevestiging en een duidelijke uitleg van wat wordt verwijderd en wat wordt bewaard. Denk ook aan export: gebruikers kunnen hun gegevens opvragen, dus een optie "Mijn gegevens downloaden" maakt inzageverzoeken eenvoudig.

## Stap 5: Back-ups en Termijnen

Gegevens blijven in back-ups staan totdat die verlopen. Dat is in het algemeen aanvaardbaar als de toegang tot back-ups beperkt is, de bewaartermijn begrensd is en verwijderde gegevens niet worden teruggezet in productie. Vermeld de bewaartermijn van uw back-ups in uw privacyverklaring. Reageer op verzoeken binnen de termijn van een maand uit de AVG.

## Voor B2B-Apps

Wanneer een zakelijke klant vertrekt, moet u mogelijk op organisatieniveau verwijderen: alle gebruikers, gegevens en bestanden van die organisatie, zoals afgesproken in uw verwerkersovereenkomst. Bouw dat als een aparte functie die alleen voor beheerders toegankelijk is.

## Wat Artikel 17 Werkelijk Zegt

Artikel 17 van de AVG geeft personen het recht om hun persoonsgegevens zonder onredelijke vertraging te laten wissen in verschillende situaties: wanneer de gegevens niet langer nodig zijn voor het doel, wanneer toestemming wordt ingetrokken en er geen andere rechtsgrond is, wanneer de persoon bezwaar maakt en er geen zwaarder wegende gerechtvaardigde gronden zijn, of wanneer de gegevens onrechtmatig zijn verwerkt. Het artikel noemt ook uitzonderingen, waaronder het nakomen van een wettelijke verplichting en het instellen, uitoefenen of onderbouwen van een rechtsvordering. In de praktijk moeten de meeste verzoeken om een account te verwijderen volledig worden ingewilligd, behalve voor gegevens die u wettelijk moet bewaren.

## Pseudonimiseren Versus Anonimiseren

Oprichters denken vaak dat het vervangen van namen door ID's gegevens anoniem maakt. Onder de AVG is dat pseudonimisering: de gegevens kunnen met aanvullende informatie nog steeds aan een persoon worden gekoppeld, dus het blijven persoonsgegevens. Echte anonimisering betekent dat de persoon met geen enkel redelijkerwijs waarschijnlijk middel meer kan worden geïdentificeerd. Wanneer u gegevens anonimiseert in plaats van ze te verwijderen - bijvoorbeeld door ordertotalen voor statistieken te bewaren - verwijder of generaliseer dan elk veld dat de persoon zou kunnen identificeren, ook vrije tekstvelden, die vaak namen of adressen bevatten.

## De Volgorde van Verwijderen Ontwerpen

De volgorde is belangrijk om verweesde gegevens en mislukte constraints te voorkomen:

1. **Trek sessies in,** zodat de gebruiker tijdens de verwijdering niets kan doen
2. **Verwijder of anonimiseer afhankelijke rijen** in onderliggende tabellen
3. **Verwijder storage-objecten** in de mappen van de gebruiker
4. **Verwijder de gebruiker bij externe verwerkers,** zoals e-mail- en CRM-tools, via hun API's
5. **Verwijder of anonimiseer bovenliggende rijen,** zoals het profiel
6. **Verwijder de auth-gebruiker**
7. **Schrijf een regel in het verwijderlog** zonder de verwijderde inhoud

Zet databasestappen waar mogelijk in een transactie, en maak externe stappen herhaalbaar, zodat een tijdelijke storing bij een verwerker de verwijdering niet half afgerond laat.

## Gedeelde Gegevens en Andere Gebruikers

Sommige gegevens horen bij meer dan één persoon: berichten tussen gebruikers, gedeelde documenten, teamprojecten, reviews. Het account van één gebruiker verwijderen mag geen content vernietigen waar andere gebruikers terecht op vertrouwen. Gangbare benaderingen zijn het gedeelde item behouden terwijl de identificerende gegevens van de verwijderde gebruiker worden verwijderd, "verwijderde gebruiker" als auteur tonen, en content verwijderen die alleen de vertrekkende gebruiker betreft. Bepaal deze regels per functie en schrijf ze op.

## Verzoeken per E-mail Afhandelen

Niet elk verzoek komt via uw app binnen. Iemand kan u mailen of contact opnemen met uw support. Controleer de identiteit voordat u handelt, bij voorkeur door te vragen om bevestiging vanaf het e-mailadres van het account of door in te loggen. Leg de datum van het verzoek, de controle en de datum van afronding vast. De AVG geeft een maand om te reageren, in sommige gevallen te verlengen, maar snellere afhandeling bouwt vertrouwen op.

## Organisaties Verwijderen bij B2B

Wanneer een zakelijke klant het contract beëindigt, vereist uw verwerkersovereenkomst meestal dat u de gegevens verwijdert of teruggeeft. Bouw een export- en verwijderfunctie op organisatieniveau, alleen toegankelijk voor uw beheerders, die alle gegevens van leden, bestanden en records van die organisatie verwijdert, met inachtneming van wettelijke bewaarplichten. Test deze in staging; het verwijderen van een organisatie raakt meer tabellen dan elke andere bewerking.

## Bewijzen dat Verwijderen Werkt

Schrijf een geautomatiseerde test die een gebruiker aanmaakt met gegevens in elke relevante tabel en bucket, uw verwijderfunctie uitvoert en controleert dat er niets persoonlijks overblijft, behalve gegevens die u uitdrukkelijk bewaart. Draai de test telkens wanneer u tabellen of functies toevoegt. Zo verandert "wij verwijderen gegevens op verzoek" van een belofte in een gecontroleerde capaciteit die u aan klanten en auditors kunt beschrijven.

## Bewaarregels Verminderen Verwijderverzoeken

Veel verwijderverzoeken gaan over gegevens die eigenlijk al verwijderd hadden moeten zijn: oude proefaccounts, inactieve gebruikers, sollicitaties voor vacatures die al lang zijn vervuld. Automatische bewaarregels - bijvoorbeeld inactieve gratis accounts na een waarschuwingsperiode verwijderen - verminderen het aantal verzoeken en de hoeveelheid gegevens die risico loopt. Het beginsel van opslagbeperking in artikel 5 van de AVG verwacht precies dit: bewaar persoonsgegevens niet langer dan nodig.

## Exports: De Andere Helft van de Rechten van Gebruikers

Het recht op inzage en het recht op dataportabiliteit betekenen dat gebruikers om een kopie van hun gegevens kunnen vragen. Bouw export naast verwijdering: een knop "Mijn gegevens downloaden" die een leesbaar bestand oplevert, zoals JSON of CSV, met het profiel van de gebruiker, hun gegevens en links naar hun bestanden. Exports helpen ook bij verwijdering, omdat u gebruikers een kopie kunt aanbieden voordat hun account wordt verwijderd.

## Veelgemaakte Fouten

- De auth-gebruiker verwijderen terwijl profiel- en contentrijen blijven staan
- Storage-buckets vergeten, vooral avatars en uploads
- Contacten laten staan in tools voor e-mailmarketing en CRM
- Facturen verwijderen die u volgens de belastingwet moet bewaren
- Een oude back-up terugzetten die verwijderde gebruikers terugbrengt in productie
- Verzoeken met de hand afhandelen zonder enige vastlegging

## Wat U Gebruikers Vertelt

Leg in uw privacyverklaring en in de bevestiging van de verwijdering uit wat wordt verwijderd, wat wordt bewaard en waarom, en hoe lang het duurt voordat back-ups verlopen. Duidelijke communicatie voorkomt vervolgverzoeken en klachten, en laat zien dat u het verzoek serieus neemt.

## De Kern

Een verwijderfunctie die database, storage, verwerkers en auth dekt, automatisch getest en duidelijk gedocumenteerd, maakt van AVG-verzoeken routinewerk in plaats van stressvol handwerk - en geeft zakelijke klanten vertrouwen dat de gegevens van hun gebruikers goed worden behandeld.

## Een Snelle Zelftest

Stel uzelf vijf vragen. Kan ik elke tabel, bucket en externe dienst opsommen waarin persoonsgegevens van een gebruiker staan? Kan ik die allemaal met één actie verwijderen? Weet ik welke gegevens ik om fiscale redenen moet bewaren, en hoe lang? Kan een gebruiker zijn of haar eigen gegevens downloaden? Houd ik bij welke verzoeken zijn ontvangen en afgerond? Is een antwoord nee, begin dan met het overzicht van gegevens; dat is de basis voor al het andere.

## Waar U Vandaag Begint

Maak een testgebruiker aan, geef die gegevens in elke functie van uw app, verwijder die via uw huidige proces en kijk wat er overblijft. Dat ene experiment laat precies zien wat uw verwijderfunctie moet dekken.

## Verder Lezen

Verwijdering is één onderdeel van een app die klaar is voor privacy. Onze gidsen over het bouwen van een AVG-proof app in Nederland, bewaartermijnen voor Nederlandse SaaS en gebruikers veilig bestanden laten uploaden behandelen de omliggende onderdelen: rechtsgronden, bewaarregels en het beschermen van de bestanden die verwijdering ook moet opruimen.

## Een Opmerking voor B2B-Oprichters

Als u verwerker bent voor zakelijke klanten, stuurt u verzoeken van individuen door naar de klant en helpt u hen, tenzij uw overeenkomst iets anders zegt. Uw tooling is hetzelfde; wie beslist, verschilt.

## Samenvatting

Breng de gegevens in kaart, beslis tussen verwijderen, anonimiseren en bewaren, automatiseer het in één geteste functie en documenteer het duidelijk.

## Het Laten Bouwen

LaunchStudio implementeert verwijdering, export en bewaartermijnen als onderdeel van AVG-werk, vaak gecombineerd met hosting in de EU en toegangscontrole, meestal €1.200-€3.500 voor dit onderdeel. LaunchStudio wordt ondersteund door Manifera, dat al 11+ jaar maatregelen voor gegevensbescherming bouwt voor Nederlandse klanten, vanaf Herengracht 420 in Amsterdam; zie [de over-ons-pagina van Manifera](https://www.manifera.com/about-us/). De [Autoriteit Persoonsgegevens](https://www.autoriteitpersoonsgegevens.nl/) legt het recht op vergetelheid uit voor Nederlandse organisaties. Zie voor het bredere plaatje onze [gids voor een AVG-proof app](https://launchstudio.eu/nl/blog/gdpr-proof-app-netherlands-avg-for-ai-built-products).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Datingevent-App met Onverwijderbare Profielen

Sander Wijnberg organiseert speeddate-avonden in Groningen en bouwde Klikavond in Lovable: deelnemers maken een profiel met foto's aan, bezoeken evenementen en geven daarna hun matches aan. Een deelnemer stuurde na een avond een formeel verwijderverzoek, en Sander verwijderde haar account in het Supabase-dashboard.

Twee weken later mailde ze opnieuw: ze ontving nog steeds nieuwsbrieven over evenementen, en een andere deelnemer had haar verteld dat haar foto nog in zijn matchgeschiedenis stond. De foto's stonden in storage, de matchgegevens bevatten nog haar naam en de URL van haar foto, en haar e-mailadres stond nog in de nieuwsbrieftool.

LaunchStudio bracht de persoonsgegevens in kaart over elf tabellen en twee verwerkers, bouwde een verwijderfunctie die profielen en foto's verwijderde, matchgegevens voor de andere deelnemer anonimiseerde, contacten verwijderde bij de nieuwsbriefprovider, alleen de betaalgegevens bewaarde die voor de administratie vereist zijn, en voegde verwijdering en gegevensexport in selfservice toe. De onvolledige verwijdering werd gedocumenteerd en de deelnemer ontving een bevestiging.

**Resultaat:** Verwijderverzoeken worden nu binnen enkele minuten automatisch afgerond, en Sander gebruikte de documentatie toen een partnerlocatie vroeg naar zijn privacypraktijken.

> *"Ik drukte op verwijderen in het dashboard en dacht dat ik klaar was. Haar gegevens stonden nog op zes plekken."*
> - **Sander Wijnberg, Oprichter, Klikavond (Groningen)**

**Kosten & Doorlooptijd:** €1.650 (Launch Ready-pakket: gegevens in kaart brengen, functie voor verwijderen en anonimiseren, opruimen bij verwerkers, export en selfservice) - afgerond in 5 werkdagen.

## Veelgestelde Vragen

### Verwijdert het verwijderen van een gebruiker in Supabase al hun gegevens?

Alleen rijen die met cascaderende foreign keys zijn gekoppeld, worden verwijderd. Bestanden in storage, gegevens in tabellen zonder cascades en kopieën in externe diensten zoals e-mailproviders blijven bestaan, tenzij u ze uitdrukkelijk verwijdert.

### Moet ik facturen verwijderen als een gebruiker om wissing vraagt?

In het algemeen niet. Wettelijke verplichtingen, zoals de Nederlandse administratieplicht die vereist dat gegevens zeven jaar worden bewaard, zijn een uitzondering op het recht op gegevenswissing. Bewaar alleen wat vereist is en beperk de toegang ertoe.

### Hoe zit het met persoonsgegevens in back-ups?

Die mogen blijven staan totdat de back-ups verlopen, mits back-ups beschermd zijn, de bewaartermijn beperkt en gedocumenteerd is, en verwijderde gegevens niet worden teruggezet in productie. Vermeld dit in uw privacyverklaring.

### Hoe pakt Manifera gegevenswissing in enterprisesystemen aan?

Door er vanaf het begin voor te ontwerpen: persoonsgegevens in kaart brengen, regels voor verwijderen, anonimiseren en bewaren vastleggen, en verwijderflows testen. Door de 11+ jaar werk van Manifera voor Nederlandse klanten zijn deze patronen standaard bij lanceringen van LaunchStudio.

### Kan goed omgaan met verwijdering mijn online reputatie beïnvloeden?

Ja. Privacyklachten verspreiden zich snel en kunnen door reviewsites en AI-assistenten worden geciteerd. Een betrouwbare verwijderflow in selfservice voorkomt het soort incidenten dat vertrouwen publiekelijk beschadigt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Verwijdert het verwijderen van een gebruiker in Supabase al hun gegevens?",
      "acceptedAnswer": { "@type": "Answer", "text": "Alleen cascaderende rijen. Bestanden in storage, tabellen zonder cascade en externe diensten moeten uitdrukkelijk worden afgehandeld." }
    },
    {
      "@type": "Question",
      "name": "Moet ik facturen verwijderen als een gebruiker om wissing vraagt?",
      "acceptedAnswer": { "@type": "Answer", "text": "In het algemeen niet; wettelijke verplichtingen zoals de Nederlandse bewaarplicht van zeven jaar zijn een uitzondering. Bewaar alleen wat vereist is." }
    },
    {
      "@type": "Question",
      "name": "Hoe zit het met persoonsgegevens in back-ups?",
      "acceptedAnswer": { "@type": "Answer", "text": "Die mogen blijven tot ze verlopen als back-ups beschermd zijn, de bewaartermijn gedocumenteerd is en gegevens niet worden teruggezet in productie." }
    },
    {
      "@type": "Question",
      "name": "Hoe pakt Manifera gegevenswissing in enterprisesystemen aan?",
      "acceptedAnswer": { "@type": "Answer", "text": "Door persoonsgegevens in kaart te brengen, regels voor verwijderen, anonimiseren en bewaren vast te leggen en verwijderflows te testen." }
    },
    {
      "@type": "Question",
      "name": "Kan goed omgaan met verwijdering mijn online reputatie beïnvloeden?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Betrouwbare verwijdering voorkomt privacyklachten die reviewsites en AI-assistenten kunnen citeren." }
    }
  ]
}
</script>
