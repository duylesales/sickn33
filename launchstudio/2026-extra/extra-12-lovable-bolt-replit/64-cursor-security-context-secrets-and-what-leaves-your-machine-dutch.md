---
Titel: "Beveiliging in Cursor: Context, Geheimen en Wat Uw Machine Verlaat"
Trefwoorden: cursor beveiliging, privacy AI-editor, codeprivacy, .cursorignore, klantdata, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Beveiliging in Cursor: Context, Geheimen en Wat Uw Machine Verlaat

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Beveiliging in Cursor: Context, Geheimen en Wat Uw Machine Verlaat",
  "description": "Een AI-editor stuurt delen van uw project naar een model om te kunnen antwoorden. Wat dat omvat, wat de verwerkersovereenkomsten van uw klanten erover zeggen, en de instellingen en gewoonten die het verdedigbaar houden.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-19",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/cursor-security-context-secrets-and-what-leaves-your-machine" }
}
</script>

Een AI-editor werkt door context naar een model te sturen. Uw geopende bestand, gerelateerde bestanden, soms een index van het hele project, plus alles wat u in een gesprek plakt.

Dat is het product dat werkt zoals bedoeld, en het is ook een datastroom uit uw ontwikkelomgeving die de meeste oprichters nooit in kaart hebben gebracht. Voor een solo-developer zonder klantdata op de machine is het risico bescheiden. Voor iemand met een export van de productiedatabase in een map, of een verwerkersovereenkomst van een klant in een la, verdient het tien minuten nadenken.

## Wat Er Werkelijk Weggaat

Drie categorieën, oplopend in de mate waarin mensen het verwachten.

**Code waaraan u werkt.** Het huidige bestand en bestanden die de editor relevant acht. Dit is de kern van het product en de reden dat het nuttig is.

**Context van het hele project.** Veel editors indexeren de repository zodat de assistent vragen kan beantwoorden over code waar u niet naar kijkt. Die index is afgeleid van uw hele project, inclusief bestanden die u nooit opent.

**Alles wat u plakt.** Een foutmelding met een stack trace en requestdata. Een rij uit de database om een bug uit te leggen. Een configuratiebestand. Dit is de categorie met het hoogste risico, omdat hier klantdata het vaakst opduikt, en ze ligt volledig in uw handen.

## Instellingen Die Eén Keer Controleren Waard Zijn

Editors verschillen en veranderen, dus controleer in plaats van aan te nemen - het gaat erom het te weten, niet om op een herinnering te vertrouwen.

**Of uw code wordt bewaard of gebruikt voor training.** Er is meestal een privacymodus die garandeert dat dat niet gebeurt. Zet die aan, en controleer wat de instelling werkelijk belooft in plaats van wat de naam suggereert.

**Wat is uitgesloten van indexering.** De meeste editors ondersteunen een ignore-bestand. Gebruik het voor alles wat geheimen of data bevat: omgevingsbestanden, sleutelmateriaal, databasedumps, exports, alles in een map met klantvoorbeelden.

**Waar de verwerking plaatsvindt.** Welke aanbieder, welke regio. Dit is het antwoord dat u nodig hebt als een klant ernaar vraagt, en het hoort op de lijst van subverwerkers die elders in deze reeks wordt besproken als het iets van hen raakt.

**Of een zakelijk abonnement betere voorwaarden geeft.** Voor een bedrijf met verplichtingen jegens klanten is dat vaak zo, en het verschil is contractueel in plaats van technisch.

## Bewaar Geen Klantdata op Uw Machine

Dit is de aanbeveling die het grootste deel van het probleem wegneemt, en ze gaat eigenlijk helemaal niet over AI-editors.

Een productie-export op een laptop is een risico ongeacht wat er verder is geïnstalleerd: de laptop raakt kwijt, de map wordt gesynchroniseerd naar een cloudaccount, een back-up neemt haar mee, een ignore-regel wordt gemist. De editor is één pad meer, niet de oorzaak.

Werk met seeddata zoals eerder in deze reeks beschreven. Waar u echt de data van een klant nodig hebt om een probleem te reproduceren, haal het minimum eruit, anonimiseer het, bewaar het voor het onderzoek en verwijder het daarna.

Hebt u tijdelijk toch een echte export, bewaar die dan volledig buiten de projectmap - niet alleen genegeerd - zodat geen enkele indexeringsbeslissing erbij kan.

## De Plakgewoonte Is het Echte Risico

De meeste blootstelling via deze tools komt niet door de index. Ze komt door iemand die iets plakt om hulp te krijgen.

Een stack trace met een request body met de naam en het adres van een klant. Een databaserij om uit te leggen waarom een berekening fout is. Een configuratiebestand met een live sleutel om te vragen waarom een verbinding faalt. Elk is iets redelijks om hulp bij te willen, en elk stuurt echte data naar een derde partij.

Twee gewoonten dekken het. Anonimiseer vóór het plakken - vervang namen, adressen, identificatoren en sleutels door placeholders, wat vijftien seconden kost en het antwoord bijna nooit verandert. En vraag naar de vorm in plaats van de inhoud: "waarom zou deze query niets teruggeven terwijl de rij bestaat" is te beantwoorden zonder de rij.

Specifiek voor sleutels: plak er nooit een, om welke reden ook. Is er een sleutel geplakt, roteer hem dan, zoals beschreven in het artikel over het roteren van geheimen in deze reeks.

## Wat de Overeenkomsten van Uw Klanten Zeggen

Verwerkt u persoonsgegevens voor zakelijke klanten, dan vereist uw verwerkersovereenkomst vrijwel zeker dat u uw subverwerkers vermeldt en vooraf meldt voordat u er een toevoegt.

De vraag die dit oproept is smal en het eerlijk beantwoorden waard: verwerkt uw ontwikkeltooling de persoonsgegevens van uw klanten? Werkt u alleen met seeddata, dan is het antwoord nee en is de tool geen subverwerker - hij verwerkt uw code, en die is van u.

Plakt u routinematig productiedata in een assistent, dan is het antwoord ja, en is dat een subverwerker die u niet hebt opgegeven. Het juiste antwoord is meestal niet om hem op te geven; het is ermee stoppen, wat zowel makkelijker als beter is.

Schrijf op welke van de twee op u van toepassing is. Het is de vraag die een grondige klant uiteindelijk zal stellen, en erover hebben nagedacht voordat ernaar wordt gevraagd, is het hele goede antwoord.

## Wanneer de Assistent Commando's Kan Uitvoeren

De nieuwere mogelijkheid die een aparte gedachte waard is: editors en agents die commando's uitvoeren, bestanden in het hele project bewerken, packages installeren en diensten namens u aanroepen.

Dit is echt nuttig en het verandert het risico van openbaarmaking in handelen. Een model dat een commando kan uitvoeren, kan het verkeerde uitvoeren, en de faalwijzen zijn bekend voor iedereen die met een capabele maar onbegeleide helper heeft gewerkt: een destructief commando uitgevoerd tegen de verkeerde omgeving, een migratie toegepast op productie omdat de inloggegevens in de omgeving daarheen wezen, een package geïnstalleerd zonder dat iemand de naam las.

Vier maatregelen houden het comfortabel.

**Keur commando's goed in plaats van ze integraal toe te staan**, in elk geval totdat u weet hoe een bepaalde agent zich gedraagt. De bevestigingsstap is waar u opmerkt dat de database-URL in die terminal de live is.

**Geef de ontwikkelomgeving nooit productie-inloggegevens.** Dit is de maatregel die het meest uitmaakt, omdat ze een hele klasse aan rampen omzet in een foutmelding.

**Werk in een branch**, zodat bestandswijzigingen in het hele project in één actie kunnen worden weggegooid.

**Houd destructieve operaties buiten bereik.** Een databaseaccount voor ontwikkeling dat geen tabellen kan verwijderen, kan er ook niet toe worden overgehaald.

Niets hiervan is een argument tegen de mogelijkheid, die echt tijd bespaart. Het is hetzelfde argument dat het artikel over AI-beveiliging in deze reeks maakt over tools en modellen in het algemeen: de vraag is nooit of het ding kan worden misleid, maar wat het kan doen als dat gebeurt.

## De Machine Zelf

Een stap terug van de editor is de ontwikkelmachine de zwakste schakel in de meeste kleine softwarebedrijven, en ze bevat meer dan welke tool ook: toegang tot de repository, deployment-inloggegevens, dashboards van aanbieders, wachtwoordmanager, e-mail.

Vijf maatregelen, geen ervan kost lang, en allemaal komen ze uiteindelijk terug in de beveiligingsvragenlijst van een klant.

**Volledige schijfversleuteling**, wat een instelling is op elk huidig besturingssysteem en een gestolen laptop van een incident verandert in een ongemak.

**Een wachtwoordmanager** met unieke inloggegevens per dienst, en tweefactorauthenticatie op alles wat het aanbiedt - te beginnen met uw repositoryhost, uw hostingplatform, uw databaseaanbieder en uw domeinregistrar, omdat die vier de sleutels tot het product zijn.

**Automatische updates van besturingssysteem en browser**, omdat de realistische dreiging voor de laptop van een oprichter gewone malware is in plaats van iets gericht.

**Aparte accounts of profielen** voor werk en al het andere, wat beperkt waar een gecompromitteerde browsersessie bij kan.

**Een back-up van de machine zelf**, zodat een laptop die op een dinsdag uitvalt niet ook een dataverlies is.

Dit is onopvallend en het is het eerlijke antwoord op een vraag die onder alles in dit artikel ligt: de meest waarschijnlijke manier waarop de data van uw klanten wordt blootgesteld, is geen subtiele fout in uw applicatie, en niet het bewaarbeleid van een modelaanbieder. Het is het apparaat waarop al uw toegang staat.

## Dit Inrichten

Voor een oprichter die een AI-editor gebruikt, is dit doorgaans een halve dag: privacy- en bewaarinstellingen bevestigd in plaats van aangenomen, een ignore-bestand voor omgevingsbestanden, sleutels, dumps en exports, productiedata buiten de projectmap en bij voorkeur helemaal van de machine, seeddata gebruikt voor ontwikkeling, een gewoonte van anonimiseren vóór plakken met een absolute regel tegen het plakken van sleutels, de verwerkingslocatie vastgelegd, voorwaarden van een zakelijk abonnement geëvalueerd als u verplichtingen jegens klanten hebt, en een geschreven standpunt over of uw tooling klantdata raakt.

LaunchStudio behandelt praktijken in de ontwikkelomgeving als onderdeel van het klaarmaken van een product voor zakelijke klanten, waar de vraag bij inkoop opduikt. Daarachter staat Manifera - elf jaar, 120+ engineers, klanten waaronder Vodafone, TNO en CFLW.

[Vraag ons hoe uw ontwikkelopzet eruit zou zien voor de auditor van een klant](https://launchstudio.eu/nl/#contact).

## Echt voorbeeld

### Een Database-export in de Projectmap

Marnix Bouwhuis bouwde Debiteurenbeheer in Cursor: debiteuren- en betalingsherinneringsadministratie voor accountantskantoren, 29 kantoren die namens hun klanten zo'n 18.000 debiteuren beheren.

Bij het debuggen van een afstemmingsprobleem had hij een productietabel naar een CSV-bestand geëxporteerd en dat in de projectmap laten staan, waar het vier maanden bleef. De projectindex van de editor nam het mee, en hij had twee keer rijen eruit in een gesprek geplakt om te vragen waarom bedragen niet overeenkwamen.

De data bestond uit namen, adressen, openstaande bedragen en betalingsgeschiedenissen van bedrijven die de klanten van zijn klanten waren - data die hij als verwerker verwerkte, onder overeenkomsten die zijn subverwerkers noemden en geen enkele AI-tooling bevatten.

Hij vond het bij het voorbereiden van antwoorden voor de audit van een accountantsgroep.

Twee werkdagen: de export verwijderd en een regel ingevoerd dat productiedata nooit in de projectmap komt; een ignore-bestand voor omgevingsbestanden, sleutelmateriaal, exports en dumps; privacy-instellingen van de editor bevestigd met bewaring uitgeschakeld, en een zakelijk abonnement genomen voor de contractuele voorwaarden die het biedt; een geseede ontwikkeldataset gebouwd met een realistische vorm zodat productiedata niet nodig is voor gewoon werk; een gedocumenteerde procedure voor de gevallen waarin data van een klant echt moet worden gereproduceerd - minimale extractie, geanonimiseerd, daarna verwijderd, vastgelegd; een anonimiseergewoonte ingevoerd met een absolute regel tegen het plakken van inloggegevens; een geschreven beoordeling die concludeerde dat de periode van vier maanden verwerking door een niet-opgegeven subverwerker vormde, wat aan de betrokken kantoren werd gemeld met een beschrijving van het herstel; en de voorwaarden voor gegevensverwerking van de aanbieder gearchiveerd bij de documentatie over subverwerkers.

**Resultaat:** de accountantsgroep accepteerde de melding en ging door, wat Marnix toeschrijft aan het feit dat hij het zelf had gevonden en volledig had uitgelegd in plaats van ernaar te worden gevraagd. Hij merkt op dat de geseede dataset de reden wegnam waarom hij überhaupt productiedata exporteerde.

> *"Het bestand stond vier maanden in mijn project en ik heb er twee keer rijen uit geplakt. Er werd niets gehackt. Ik had gewoon de data van de klanten van mijn klanten naar een bedrijf gestuurd waarmee niemand had ingestemd."*
> - **Marnix Bouwhuis, Oprichter, Debiteurenbeheer (Amersfoort)**

**Kosten & Doorlooptijd:** €2.400 (dataverwijdering en regels voor projecthygiëne, ignore-bestand, privacyconfiguratie van de editor en zakelijk abonnement, geseede ontwikkeldataset, reproductieprocedure, anonimiseerpraktijken, meldingsbeoordeling en documentatie) - afgerond in 2 werkdagen.

## Veelgestelde vragen

### Wat stuurt een AI-editor naar het model?

Het bestand waaraan u werkt, bestanden die hij relevant acht, vaak een index van het hele project, en alles wat u in een gesprek plakt. Dat laatste is waar klantdata meestal opduikt.

### Wordt mijn code gebruikt voor training?

De meeste editors hebben een privacymodus die bewaring en training voorkomt. Zet die aan en controleer wat de instelling werkelijk belooft in plaats van op de naam te vertrouwen.

### Moet ik een ignore-bestand toevoegen?

Ja - voor omgevingsbestanden, sleutelmateriaal, databasedumps en exports. Beter nog: bewaar productiedata volledig buiten de projectmap, zodat geen enkele indexeringsbeslissing erbij kan.

### Is mijn AI-editor een subverwerker?

Alleen als hij de persoonsgegevens van uw klanten verwerkt. Werkt u met seeddata, dan verwerkt hij uw code, en die is van u. Routinematig productierijen plakken maakt hem er een, en de oplossing is stoppen in plaats van hem op te geven.

### Wat als ik een sleutel heb geplakt?

Roteer hem. Genereer een vervanging, deploy die, trek de oude in, en controleer daarna of hij is gebruikt. Hem uit het gesprek verwijderen verandert niets.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat stuurt een AI-editor naar het model?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het geopende bestand, gerelateerde bestanden, vaak een index van het hele project, en alles wat u plakt - dat laatste is waar klantdata meestal opduikt."
      }
    },
    {
      "@type": "Question",
      "name": "Wordt mijn code gebruikt om modellen te trainen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De meeste editors bieden een privacymodus die bewaring en training voorkomt. Zet die aan en controleer wat de instelling werkelijk toezegt."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik een ignore-bestand gebruiken met een AI-editor?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, voor omgevingsbestanden, sleutels, dumps en exports - en houd productiedata volledig buiten de projectmap."
      }
    },
    {
      "@type": "Question",
      "name": "Is een AI-editor een subverwerker onder mijn klantovereenkomsten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Alleen als hij persoonsgegevens van klanten verwerkt. Met seeddata verwerkt hij uw eigen code; productierijen plakken maakt hem er een."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet ik doen als ik een API-sleutel heb geplakt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Roteer hem - genereer een vervanging, deploy, trek de oude in, en controleer daarna de logs van de aanbieder. Het gesprek verwijderen verandert niets."
      }
    }
  ]
}
</script>
