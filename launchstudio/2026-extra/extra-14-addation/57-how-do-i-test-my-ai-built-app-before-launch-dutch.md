---
Titel: "Hoe Test Ik Mijn AI-Gebouwde App Vóór de Lancering?"
Trefwoorden: ai-gebouwde app testen, lovable-app testen, testen voor de lancering, playwright supabase testen, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Hoe Test Ik Mijn AI-Gebouwde App Vóór de Lancering?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Test Ik Mijn AI-Gebouwde App Vóór de Lancering?",
  "description": "AI-gebouwde apps worden meestal alleen getest door erdoorheen te klikken. Deze gids geeft een praktisch testplan voor de lancering: scenario's voor kritieke paden, rechtentests met meerdere gebruikers, betaaltests, geautomatiseerde end-to-end-tests en een generale repetitie van de lancering.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-05",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-do-i-test-my-ai-built-app-before-launch" },
  "citation": [
    { "@type": "CreativeWork", "name": "Perry et al., Do Users Write More Insecure Code with AI Assistants?", "url": "https://arxiv.org/abs/2211.03622" },
    { "@type": "CreativeWork", "name": "DORA 2024 Accelerate State of DevOps Report", "url": "https://dora.dev/research/2024/dora-report/" },
    { "@type": "CreativeWork", "name": "Playwright documentation", "url": "https://playwright.dev/docs/intro" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A01 Broken Access Control", "url": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/" },
    { "@type": "CreativeWork", "name": "web.dev: Web Vitals", "url": "https://web.dev/articles/vitals" }
  ]
}
</script>

**Kort antwoord:** test de paar dingen die het meeste pijn zouden doen als ze kapotgaan, in een stagingomgeving, met meer dan één gebruiker. Schrijf uw kritieke paden op (registratie, inloggen, de kernactie, betaling, zichtbaarheid van gegevens), test elk pad met minstens twee accounts en verschillende rollen, doorloop betalingen in testmodus met geslaagde, mislukte en geannuleerde betalingen, automatiseer de belangrijkste paden met end-to-end-tests, en houd een generale repetitie op de productieopzet voordat u iets aankondigt.

## Belangrijkste Punten

- **Test wat het meeste pijn zou doen als het kapotgaat:** registratie en inloggen, de kernactie, betalingen, zichtbaarheid van gegevens, wachtwoordherstel en verwijdering.
- **Test altijd met meer dan één gebruiker en rol;** fouten in toegangscontrole verschijnen pas als er een tweede account bestaat.
- **Code die met AI is geschreven, vraagt meer testen, niet minder.** Onderzoekers van Stanford ontdekten dat ontwikkelaars met AI-hulp meer vertrouwen hadden in minder veilige code, en het DORA-onderzoek van Google koppelt geautomatiseerd testen aan stabiele oplevering.
- **Automatiseer de belangrijkste drie of vier paden** met end-to-end-tests zoals Playwright, die bij elke deployment draaien.
- **Repeteer de lancering op productie:** een echte kleine betaling, echte e-mails, meldingen, terugdraaien en het terugzetten van een back-up.

## Waarom Doorklikken Niet Genoeg Is

Wanneer u uw eigen app test, gebruikt u één account, het ideale pad en een snelle verbinding. Echte gebruikers brengen veel accounts, verkeerde invoer, trage telefoons en slechte timing mee. AI-gegenereerde code is extra gevoelig voor perfect werken op het pad waarvoor u een prompt schreef en breken op paden waarvoor u dat niet deed.

## Stap 1: Maak een Lijst van Uw Kritieke Paden

Meestal vijf tot tien. Voor een boekings-SaaS bijvoorbeeld:

1. Registreren, e-mailadres bevestigen, inloggen
2. Een boeking maken
3. Een boeking betalen
4. Een boeking annuleren of wijzigen
5. Overzicht van boekingen voor medewerkers
6. Wachtwoordherstel
7. Account verwijderen

## Stap 2: Test Rechten met Echte Accounts

Maak gebruikers aan in verschillende rollen en organisaties. Controleer voor elk kritiek pad wat elke gebruiker kan zien en doen. Probeer directe URL's en gewijzigde ID's. Hier falen AI-gebouwde apps het vaakst; onze [beveiligingszelftest voor Lovable](https://launchstudio.eu/nl/blog/is-my-lovable-app-secure) loopt de methode door.

## Stap 3: Test Betalingen Grondig

| Scenario | Verwacht resultaat |
| --- | --- |
| Geslaagde betaling | Toegang verleend via een webhook |
| Klant sluit de browser na het betalen | Toegang wordt nog steeds verleend |
| Betaling geannuleerd of mislukt | Geen toegang, duidelijke melding, opnieuw proberen mogelijk |
| Dubbelklik op betalen | Eén afschrijving |
| Verlenging mislukt (abonnementen) | Respijtperiode en e-mail |

## Stap 4: Test Slechte Invoer en Slechte Omstandigheden

- Zeer lange teksten, emoji's, speciale tekens in namen
- Lege verplichte velden, verkeerde formaten
- Traag netwerk (de ontwikkelaarstools van de browser kunnen dat simuleren)
- Mobiele browsers op iOS en Android
- Twee mensen die hetzelfde record bewerken

## Stap 5: Automatiseer de Belangrijkste Paden

Tools voor end-to-end-tests zoals Playwright kunnen inloggen als testgebruikers en bij elke deployment automatisch door kritieke paden klikken. Begin met drie tests: registreren en inloggen, de kernactie, en een rechtencontrole dat de ene gebruiker de gegevens van een andere niet kan zien. AI-tools kunnen helpen deze tests te schrijven, maar controleer wat ze toetsen.

## Stap 6: Generale Repetitie

Op de productieopzet, voordat u iets aankondigt:

- Een echte betaling van een klein bedrag, daarna terugbetalen
- Een echte e-mail bezorgd bij Gmail en Outlook
- Monitoringmeldingen getest
- Terugdraaien getest
- Het terugzetten van een back-up getest

## Waarom AI-Gebouwde Apps Bewust Testen Vragen

Wanneer code snel wordt gegenereerd, is het makkelijk om aan te nemen dat die is gecontroleerd. In de praktijk optimaliseerde de AI voor het scenario dat u beschreef, niet voor de scenario's die u niet noemde. De studie van Perry en collega's aan Stanford liet zien dat deelnemers die AI-assistenten gebruikten minder veilige code schreven en vaker dachten dat die veilig was. Het DORA-onderzoek van Google koppelt geautomatiseerd testen en continuous delivery al lang aan betere resultaten, en het rapport van 2024 verbond meer gebruik van AI aan minder stabiele oplevering wanneer zulke praktijken ontbraken. Testen is hoe u gegenereerd vertrouwen omzet in verdiend vertrouwen.

## Een Testplan op Basis van Risico

U kunt niet alles testen, dus test op basis van risico. Stel voor elke functie twee vragen: hoe waarschijnlijk is het dat die kapotgaat, en hoe erg zou dat zijn? Functies met geld, persoonsgegevens of toegangscontrole hebben altijd een grote impact. Functies die onlangs via prompts zijn gewijzigd, gaan altijd eerder kapot. Combineer de twee om te bepalen waar u testtijd aan besteedt:

| Impact / waarschijnlijkheid | Lage waarschijnlijkheid | Hoge waarschijnlijkheid |
| --- | --- | --- |
| Grote impact | Testen vóór elke grote release | Testen vóór elke release, automatiseren |
| Kleine impact | Af en toe steekproefsgewijs controleren | Testen bij wijziging |

## Goede Testscenario's Schrijven

Een goed scenario is concreet: wie de gebruiker is, wat die doet en wat er moet gebeuren. Bijvoorbeeld: "Een lid van Organisatie A opent een factuur-URL die bij Organisatie B hoort en ziet een foutmelding, niet de factuur." Schrijf scenario's eerst in gewone taal; ze zijn nuttig voor handmatig testen, voor het briefen van ontwikkelaars en voor het genereren van geautomatiseerde tests. Twintig goed gekozen scenario's dekken het meeste van wat ertoe doet voor een gemiddelde oprichtersapp.

## Toegangscontrole Goed Testen

Toegangscontrole verdient een eigen sessie. Maak twee organisaties aan met elk twee gebruikers - een beheerder en een lid - en probeer:

- Records van de andere organisatie op te vragen via de interface en de API
- Een record van een andere organisatie te openen door een ID in de URL te wijzigen
- Een record van een andere organisatie bij te werken of te verwijderen
- Als lid acties die alleen voor beheerders zijn direct aan te roepen
- Bestanden van een andere organisatie te downloaden door links te raden of te hergebruiken

Elke poging moet op de server mislukken. Slaagt er een, los die dan op vóór de lancering; OWASP rangschikt gebrekkige toegangscontrole als het grootste risico voor webapplicaties.

## End-to-End-Tests met Playwright

Playwright bestuurt een echte browser door uw app en controleert de resultaten. Begin voor een oprichtersapp met drie tests: registreren en inloggen, de kernactie voor een betalende klant, en een controle op toegang tussen organisaties. Draai ze bij elke deployment via uw CI-pipeline tegen staging. AI-tools kunnen eerste versies van deze tests schrijven; controleer dat de assertions het juiste gedrag toetsen en niet simpelweg wat de app nu doet.

## Betalingen van Begin tot Eind Testen

Gebruik de testmodus van uw betaalprovider om een geslaagde betaling, annulering, mislukking, dubbelklik en het sluiten van de browser vóór de redirect te dekken. Gebruik voor abonnementen tools zoals de test clocks van Stripe om verlengingen, mislukte verlengingen en opzeggingen te simuleren zonder weken te wachten. Controleer dat uw database elke uitkomst correct weergeeft en dat klanten de juiste e-mails ontvangen.

## Prestaties en Mobiel Testen

Test belangrijke schermen op een middenklasse telefoon met een vertraagde verbinding. Vul staging met realistische hoeveelheden gegevens, want een lijst die met tien rijen direct laadt, kan met tienduizend rijen seconden duren. De Web Vitals van Google geven bruikbare doelen voor laadsnelheid en responsiviteit op openbare pagina's.

## Basis van Toegankelijkheid

Controleer dat formulieren labels hebben, knoppen met het toetsenbord bereikbaar zijn, het contrast voldoende is en afbeeldingen een alternatieve tekst hebben. Naast goede praktijk gelden onder de Europese Toegankelijkheidswet toegankelijkheidseisen voor veel digitale diensten voor consumenten in de EU, met uitzonderingen voor micro-ondernemingen.

## Een Testsprint van Twee Dagen Vóór de Lancering

Dag één: schrijf uw twintig scenario's, maak testgebruikers en organisaties aan in staging, voer alle scenario's voor toegangscontrole en betalingen handmatig uit en leg elk probleem vast. Dag twee: los de blokkades voor de lancering op, test ze opnieuw, schrijf de eerste drie Playwright-tests en voeg ze toe aan CI, en test daarna de belangrijkste flows op twee telefoons en twee browsers. Twee gerichte dagen vangen de meeste problemen op die anders in uw eerste week met klanten zouden opduiken.

## Vroege Gebruikers Betrekken

Nodig vóór een openbare lancering een paar vertrouwde gebruikers uit voor een bèta op staging of productie, met duidelijke verwachtingen. Echte gebruikers vinden problemen die bouwers nooit zouden vinden, omdat ze niet weten op welke knoppen ze geacht worden te drukken. Geef ze een eenvoudige manier om problemen te melden en reageer snel; vroege gebruikers die zien dat er iets met hun feedback gebeurt, worden vaak uw sterkste ambassadeurs.

## Tests Levend Houden

Tests die niemand onderhoudt, worden ruis. Wanneer een functie bewust verandert, werkt u de tests in dezelfde wijziging bij. Wanneer een test faalt, behandel het als informatie: of de app is kapot, of de test is verouderd, en beide verdienen aandacht. Een kleine set betrouwbare tests is veel meer waard dan een grote set die niemand gelooft.

## Wat U met de Resultaten Doet

Verdeel elk probleem over drie groepen. Blokkades voor de lancering: alles wat te maken heeft met toegang tot gegevens, betalingen, inloggen of gegevensverlies - oplossen vóór de lancering. Oplossingen voor de eerste week: kapotte lay-outs op sommige apparaten, verwarrende meldingen, trage schermen - direct na de lancering oplossen. Backlog: afwerking en leuke extra's. Schrijf de lijst op en deel die met wie u helpt bouwen; een lijst met prioriteiten is veel nuttiger dan een lange, ongesorteerde lijst.

## Testen na de Lancering

Testen stopt niet bij de lancering. Voeg voor elke bug die klanten melden een test toe, zodat die niet onopgemerkt terug kan komen. Voer de scenario's voor toegangscontrole opnieuw uit na elke functie die gegevens of rollen raakt. En bekijk uw geautomatiseerde tests wanneer een test faalt om een andere reden dan een echte bug; onbetrouwbare tests ondermijnen het vertrouwen in de hele set.

## Gerelateerde Onderwerpen

Testen werkt het best met staging en CI. Onze gidsen over het inrichten van een stagingomgeving en automatische deployments voor Lovable- of Bolt-apps laten zien hoe u deze tests bij elke wijziging draait.

## Testchecklist

- Twintig uitgeschreven scenario's die de kritieke paden dekken
- Toegangscontrole getest met twee organisaties en twee rollen per organisatie
- Uitkomsten van betalingen getest in testmodus, inclusief dubbelklik en gesloten browser
- Belangrijkste flows getest op twee telefoons en twee browsers
- Drie geautomatiseerde end-to-end-tests die bij elke deployment draaien
- Generale repetitie op productie met een echte kleine betaling en terugbetaling

## De Opbrengst

Een paar dagen bewust testen beschermt de eerste indruk die uw product maakt, en een eerste indruk is moeilijk te herstellen.

## Verder Lezen

Onze checklist van 25 punten voor een vibe code-audit vult dit plan aan met de beveiligings- en beheercontroles die u naast functioneel testen uitvoert.

## Een Buglijst die Echt Helpt

Per probleem: wat u deed, wat er gebeurde, wat u verwachtte, welke gebruiker en welk apparaat. Los blokkades voor de lancering (gegevens, betalingen, inloggen) op vóór de lancering; plan de rest in.

## Het Laten Regelen

LaunchStudio test elke app vóór de lancering, inclusief rechtentests met meerdere rollen en betaalscenario's, en kan geautomatiseerde end-to-end-tests aan uw pipeline toevoegen. LaunchStudio wordt ondersteund door Manifera, waarvan de QA-praktijken voortkomen uit 11+ jaar en 160+ projecten voor klanten waaronder Vodafone en Xpar Vision; zie [de maatwerksoftwareontwikkeling van Manifera](https://www.manifera.com/services/custom-software-development/). [De documentatie van Playwright](https://playwright.dev/docs/intro) is een goed startpunt voor geautomatiseerde tests.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Het Cursusplatform dat door Eén Persoon Werd Getest

Marloes Vink, fotografiedocent in Haarlem, bouwde Lichtlessen in Lovable: een online cursusplatform met videolessen, opdrachten en feedback van de docent. Ze testte het wekenlang, altijd ingelogd als zichzelf, de beheerder. Twee dagen voor de lancering probeerde een vriendin het als cursist.

Binnen een uur ontdekte de vriendin dat cursisten de ingeleverde opdrachten van andere cursisten konden openen door een getal in de URL te wijzigen, dat de knop "markeren als voltooid" werkte bij lessen die de cursist niet had gekocht, dat geannuleerde iDEAL-betalingen de cursus toch ontgrendelden, en dat de videospeler niet werkte in Safari op de iPhone.

Marloes stelde de lancering een week uit. LaunchStudio herstelde de RLS op ingeleverde opdrachten en lesvoortgang, verplaatste de toegangscontroles voor cursussen naar de server, koppelde toegang aan geverifieerde betaalwebhooks, loste het afspelen van video op met een compatibele streamingopzet, en voegde drie Playwright-tests toe (registratie en aankoop, rechten van cursisten, feedback van de docent) die bij elke deployment draaien.

**Resultaat:** De lancering ging een week later door met 120 cursisten in de eerste groep. De geautomatiseerde tests vingen in de maanden daarna twee regressies op voordat cursisten ze zagen.

> *"Ik heb mijn app een maand getest. Alleen nooit als iemand anders dan degene die hem had gebouwd."*
> - **Marloes Vink, Oprichter, Lichtlessen (Haarlem)**

**Kosten & Doorlooptijd:** €2.400 (Launch Ready-pakket: RLS-herstel, toegang op de server, betaalwebhooks, videoherstel voor Safari en geautomatiseerde tests) - afgerond in 6 werkdagen.

## Veelgestelde Vragen

### Wat moet ik als eerste testen in een AI-gebouwde app?

Rechten, betalingen en inloggen. Test dat gebruikers elkaars gegevens niet kunnen zien of wijzigen, dat betalingen alleen toegang geven als ze slagen, en dat registreren, inloggen en wachtwoordherstel werken op echte apparaten.

### Heb ik geautomatiseerde tests nodig voor een kleine app?

Een paar wel. Drie tot vijf end-to-end-tests die uw kritieke paden dekken, vangen regressies op wanneer AI-tools code opnieuw genereren. U heeft geen volledige testdekking nodig om er profijt van te hebben.

### Kan AI mijn tests schrijven?

AI-tools kunnen snel eerste versies van tests maken, wat nuttig is. Controleer wat elke test toetst, want gegenereerde tests toetsen soms het huidige gedrag in plaats van het juiste gedrag, inclusief bugs.

### Hoe pakt Manifera testen aan bij lanceringen tegen vaste prijs?

Door te focussen op risico: kritieke paden, rechten en betalingen worden vóór de lancering altijd getest met meerdere rollen. De 11+ jaar QA-praktijk van Manifera geeft voorrang aan tests die incidenten voorkomen boven tests die alleen dekkingscijfers verhogen.

### Heeft testen invloed op SEO of zichtbaarheid in AI?

Indirect. Openbare pagina's testen op mobiel en trage verbindingen brengt problemen met renderen en prestaties aan het licht die anders de paginabeleving zouden schaden en content moeilijker te crawlen en te citeren zouden maken.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat moet ik als eerste testen in een AI-gebouwde app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Rechten, betalingen en inloggen, op echte apparaten en met meerdere gebruikers." }
    },
    {
      "@type": "Question",
      "name": "Heb ik geautomatiseerde tests nodig voor een kleine app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Een paar end-to-end-tests op kritieke paden vangen regressies op door code die AI opnieuw genereert." }
    },
    {
      "@type": "Question",
      "name": "Kan AI mijn tests schrijven?",
      "acceptedAnswer": { "@type": "Answer", "text": "Het kan eerste versies maken; controleer de assertions, want gegenereerde tests kunnen bestaande bugs vastleggen." }
    },
    {
      "@type": "Question",
      "name": "Hoe pakt Manifera testen aan bij lanceringen tegen vaste prijs?",
      "acceptedAnswer": { "@type": "Answer", "text": "Testen op basis van risico van kritieke paden, rechten en betalingen met meerdere rollen." }
    },
    {
      "@type": "Question",
      "name": "Heeft testen invloed op SEO of zichtbaarheid in AI?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirect, door problemen met mobiel renderen en prestaties op openbare pagina's op te sporen." }
    }
  ]
}
</script>
