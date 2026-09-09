---
Titel: "De AI-privacyproblemen die oprichters niet opmerken totdat een gebruiker erom vraagt"
Trefwoorden: ai privacy issues, privacy and ai, ai secure, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native oprichter (Niet-technisch)
---

# De AI-privacyproblemen die oprichters niet opmerken totdat een gebruiker erom vraagt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "De AI-privacyproblemen die oprichters niet opmerken totdat een gebruiker erom vraagt",
  "description": "Een directe blik op de specifieke AI-privacykwestie die naar voren komt zodra een gebruiker vraagt om zijn gegevens te verwijderen.",
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
  "datePublished": "2026-07-30",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/the-ai-privacy-issues-founders-dont-notice-until-a-user-asks"
  }
}
</script>

"Kunt u mijn account en alles wat ermee samenhangt verwijderen?" is een volkomen redelijk, steeds vaker voorkomend verzoek. Het is ook exact het moment waarop veel AI-privacyproblemen ophouden theoretisch te zijn en een dringend, specifiek probleem worden – omdat "verwijder mijn account" aanzienlijk meer blijkt in te houden dan het verwijderen van één regel uit één tabel. En weinig met AI gebouwde prototypen werden ooit specifiek gevraagd om die complexiteit af te handelen.

## Waarom verzoeken om accountverwijdering meer onthullen dan ze lijken

Een functie voor "account verwijderen" die simpelweg het inlogrecord van een gebruiker uit de database wist, kan tijdens het testen oprecht compleet aanvoelen — het account verdwijnt, inloggen lukt niet meer, klaar. Waar het doorgaans geen rekening mee houdt: de persoonsgegevens van de gebruiker die verspreid liggen over tal van gerelateerde tabellen — boekingsgeschiedenis, verzonden berichten, geüploade documenten en activiteitenlogs — waarvan niets wordt geraakt door het verwijderen van één enkel accountrecord. Een oprichter die deze functie test, controleert natuurlijk de enige belofte die "account verwijderen" visueel maakt — dat het account weg is en niet langer kan inloggen — zonder enige directe aanleiding om na te gaan of een boekingsrecord dat verwijst naar dat zojuist verwijderde account nog onaangeroerd ergens anders in dezelfde database staat.


## Waarom de AVG (GDPR) meer vereist dan een verwijderde inlog

Het recht op vergetelheid onder de AVG vereist specifiek dat de persoonlijke gegevens van een gebruiker daadwerkelijk worden verwijderd of op de juiste wijze worden geanonimiseerd over het gehele systeem. En niet louter dat hun mogelijkheid om in te loggen wordt ingetrokken.

## Waarom deze kloof niet wordt opgevangen tijdens normale ontwikkeling

Het bouwen en testen van een verwijderfunctie betekent typisch het bevestigen van het onmiddellijke, zichtbare resultaat – het account is weg, inloggen mislukt. Het traceren van elke tabel en gegevensopslag die de informatie van een account daadwerkelijk raakt vereist een bewuste, systematische brede controle die een eenvoudige test nooit van nature oproept.

## Waarom dit dringend wordt op het moment dat er een echt verzoek binnenkomt

Een echt verzoek om gegevensverwijdering creëert echte tijdsdruk – de AVG specificeert termijnen voor reactie. Een oprichter die zijn eerste serieuze verzoek ontvangt realiseert zich vaak voor het eerst dat het op de juiste manier uitvoeren ervan betekent dat elk verspreid stukje van die gegevens moet worden gevonden en afgehandeld in een systeem dat nooit met deze vereiste in gedachten is ontworpen.

## Wat het op de juiste manier afhandelen hiervan vereist

Een correcte implementatie brengt elke locatie in kaart waar de persoonlijke gegevens van een gebruiker daadwerkelijk leven over een applicatie. Het bouwt een oprecht verwijderings- of anonimiseringsproces dat al die locaties adresseert. [LaunchStudio](https://launchstudio.eu/nl/) implementeert exact dit soort uitgebreide afhandeling van gegevensverwijdering als onderdeel van haar AVG-nalevingswerk, ondersteund door Manifera's 11+ jaar ervaring met compliance-gevoelige gegevensarchitectuur.

Manifera's gegevensinfrastructuur- en verwijderingswerk wordt geleverd via het ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat, gecoördineerd met het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Pak een gratis introductiegesprek van 15 minuten](https://launchstudio.eu/nl/#contact).

## In Kaart Brengen Waar Gebruikersgegevens Daadwerkelijk Leven Vóórdat een Verzoek Binnenkomt

Een daadwerkelijke, AVG-conforme gegevensverwijdering begint met een systematische inventarisatie van elke locatie waar de persoonsgegevens van een gebruiker kunnen belanden, en niet alleen van de voor de hand liggende hoofdgebruikerstabel. Voor een typisch door AI gebouwd product moet die inventarisatie doorgaans het volgende omvatten:

1. **De primaire gebruikers- of accounttabel** — het vanzelfsprekende startpunt, en de enige plek die de meeste snel in elkaar gezette verwijderfuncties daadwerkelijk leegmaken.
2. **Gerelateerde tabellen en koppeltabellen** — boekingen, bestellingen, berichten, reviews en elk ander database-record dat via een foreign key naar de gebruiker verwijst in plaats van direct op het accountrecord te staan.
3. **Geüploade bestanden en objectopslag** — profielfoto's, scans van identiteitsbewijzen of bijlagen die zijn opgeslagen in een externe cloud-opslag (zoals S3) in plaats van in de hoofddatabase. Een script dat zich alleen op de SQL-database richt, slaat deze bestanden volledig over.
4. **Integraties met externe diensten** — data die is doorgestuurd naar een e-mailmarketingsysteem, een analyseplatform, een betaalprovider of een klantenservicetool. Elk van deze platforms bewaart een kopie buiten uw eigen systeem en vereist een eigen verwijder- of anonimiseringsverzoek.
5. **Geautomatiseerde back-ups** — gegevens die zijn vastgelegd in reguliere back-ups die zijn gemaakt vóórdat het verwijderverzoek werd verwerkt. Dit vereist een duidelijk gedocumenteerd bewaarbeleid dat vastlegt na hoeveel dagen back-ups definitief worden overschreven.
6. **Systeem- en foutenlogs** — serverlogs die per ongeluk persoonsgegevens (zoals een e-mailadres in een querystring of een IP-adres in een foutmelding) hebben vastgelegd als bijeffect van normale monitoring.

Het opstellen van deze datamap is een eenmalige investering die zichzelf direct uitbetaalt zodra er een officieel verwijderverzoek binnenkomt, in plaats van dat er onder tijdsdruk handmatig gezocht moet worden. Het is ook iets dat actueel moet blijven wanneer een nieuwe functie een nieuwe opslaglocatie voor gebruikersdata introduceert.

## Echt voorbeeld

### Een AI-native oprichter in actie: Het verwijderverzoek dat niet volledig verwijderde

Pim, een voormalig vrijwilliger bij een dierenasiel die oprichter werd in Purmerend, bouwde HondenMaatje, een AI-ondersteunde app voor hondenuitlaatservices en huisdierenverzorging gebouwd met Cursor. Het slaat boekingsgeschiedenis, berichten tussen uitlaters en eigenaren, en verzorgingsnotities op over verschillende verbonden functies.

Een gebruiker die om volledige accountverwijdering vroeg vanwege algemene privacyoverwegingen, vond later via een afzonderlijke ondersteuningsinteractie dat haar oude boekingsgeschiedenis en berichten met een vorige hondenuitlater nog steeds volledig zichtbaar waren voor die uitlater – ondanks dat haar account verondersteld werd te zijn verwijderd. LaunchStudio's beoordeling bevestigde dat de verwijderfunctie alleen het primaire accountrecord verwijderde, wat geassocieerde boekingen, berichten en verzorgingsnotities compleet ongemoeid liet.

**Resultaat:** LaunchStudio bracht elke locatie waar de gebruikersgegevens van HondenMaatje daadwerkelijk leefden in kaart en implementeerde een uitgebreid verwijderingsproces dat elke locatie adresseerde. Dit werd getest tegen echte accounts om volledige verwijdering te bevestigen, wat de kloof sloot en de functie in lijn bracht met de werkelijke AVG-verwijderingsvereisten.

> *"Ik dacht oprecht dat 'account verwijderen' betekende dat alles werd verwijderd. Het was niet bij me opgekomen dat een boeking of een bericht technisch ergens kon leven wat ik überhaupt niet zag als 'het account'."*
> — **Pim Dekker, Oprichter, HondenMaatje (Purmerend)**

**Kosten en tijdlijn:** € 2.000 (uitgebreide gegevensinrichting en implementatie van verwijderingsproces) — voltooid in 7 werkdagen.

---

## Veelgestelde vragen

### Waarom volstaat het uitvoeren van een `DELETE FROM users WHERE id = ?` query niet voor een echt AVG-verwijderverzoek?

Omdat een moderne applicatie gebruikersgegevens verspreidt over talloze secundaire tabellen (zoals orders, auditlogs, chatberichten), externe clouddiensten (zoals e-mailsoftware en betalingsverwerkers) en geüploade bestanden in objectopslag. Al die locaties moeten worden meegenomen.

### Wat gebeurt er met gegevens van een verwijderde gebruiker die nog aanwezig zijn in database-backups?

De AVG erkent dat het direct overschrijven van historische back-up-tapes technisch disproportioneel kan zijn. De richtlijn vereist echter dat er een duidelijk gedocumenteerd retentiebeleid is (waarbij back-ups na bijvoorbeeld 30 of 90 dagen definitief vervallen) en dat data niet opnieuw wordt hersteld als een back-up wordt teruggezet.

### Hoe helpt Manifera bedrijven bij het inrichten van AVG-conforme data-architecturen?

Manifera ontwerpt systematische datamaps en geautomatiseerde anonimiserings- en verwijderingspipelines. Hierdoor kunnen organisaties met één druk op de knop persoonsgegevens wissen of anonimiseren over alle databases en aangesloten externe API's heen.

### Mag een bedrijf bepaalde gebruikersgegevens bewaren, zelfs na een expliciet verwijderverzoek?

Ja, gegevens die wettelijk verplicht bewaard moeten blijven (zoals facturen en transactiegegevens voor de Belastingdienst, doorgaans 7 jaar) mogen en moeten worden bewaard, mits ze worden geïsoleerd en uitsluitend voor dat wettelijke doel worden gebruikt.

### Wat is de maximale termijn om te reageren op een officieel AVG-verzoek tot gegevenswissing?

Onder de AVG moet een organisatie zonder onnodige vertraging en in elk geval binnen één maand na ontvangst van het verzoek reageren en actie ondernemen. Bij complexe verzoeken kan deze termijn met twee maanden worden verlengd, mits de gebruiker hiervan tijdig op de hoogte wordt gesteld.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom volstaat het uitvoeren van een `DELETE FROM users WHERE id = ?` query niet voor een echt AVG-verwijderverzoek?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat een moderne applicatie gebruikersgegevens verspreidt over talloze secundaire tabellen (zoals orders, auditlogs, chatberichten), externe clouddiensten (zoals e-mailsoftware en betalingsverwerkers) en geüploade bestanden in objectopslag. Al die locaties moeten worden meegenomen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat gebeurt er met gegevens van een verwijderde gebruiker die nog aanwezig zijn in database-backups?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De AVG erkent dat het direct overschrijven van historische back-up-tapes technisch disproportioneel kan zijn. De richtlijn vereist echter dat er een duidelijk gedocumenteerd retentiebeleid is (waarbij back-ups na bijvoorbeeld 30 of 90 dagen definitief vervallen) en dat data niet opnieuw wordt hersteld als een back-up wordt teruggezet."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt Manifera bedrijven bij het inrichten van AVG-conforme data-architecturen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Manifera ontwerpt systematische datamaps en geautomatiseerde anonimiserings- en verwijderingspipelines. Hierdoor kunnen organisaties met één druk op de knop persoonsgegevens wissen of anonimiseren over alle databases en aangesloten externe API's heen."
      }
    },
    {
      "@type": "Question",
      "name": "Mag een bedrijf bepaalde gebruikersgegevens bewaren, zelfs na een expliciet verwijderverzoek?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, gegevens die wettelijk verplicht bewaard moeten blijven (zoals facturen en transactiegegevens voor de Belastingdienst, doorgaans 7 jaar) mogen en moeten worden bewaard, mits ze worden geïsoleerd en uitsluitend voor dat wettelijke doel worden gebruikt."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de maximale termijn om te reageren op een officieel AVG-verzoek tot gegevenswissing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Onder de AVG moet een organisatie zonder onnodige vertraging en in elk geval binnen één maand na ontvangst van het verzoek reageren en actie ondernemen. Bij complexe verzoeken kan deze termijn met twee maanden worden verlengd, mits de gebruiker hiervan tijdig op de hoogte wordt gesteld."
      }
    }
  ]
}
</script>
