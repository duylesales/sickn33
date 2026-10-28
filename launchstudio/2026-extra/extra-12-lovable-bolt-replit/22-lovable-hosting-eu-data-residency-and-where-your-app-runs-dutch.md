---
Titel: "Lovable Hosting: EU-Datalocatie en Waar Uw App Echt Draait"
Trefwoorden: lovable hosting, EU-datalocatie, AVG-doorgiften, regio's, subverwerkers, datalocatie, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Lovable Hosting: EU-Datalocatie en Waar Uw App Echt Draait

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting: EU-Datalocatie en Waar Uw App Echt Draait",
  "description": "Nederlandse zakelijke klanten vragen waar hun data is opgeslagen, en de meeste door AI gebouwde apps kunnen dat niet beantwoorden. Hoe u het uitzoekt, waarom de databaseregio maar een deel van het antwoord is, en wat u doet als het eerlijke antwoord het verkeerde is.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-hosting-eu-data-residency-and-where-your-app-runs" }
}
</script>

De vraag komt binnen in een e-mail van de IT- of privacyfunctionaris van een klant, meestal terwijl een contract wordt beoordeeld, en ze is eenvoudig geformuleerd: waar wordt onze data opgeslagen?

Voor de meeste oprichters die met Lovable bouwden, is het eerlijke eerste antwoord dat ze het niet weten. De database werd aangemaakt door een standaardinstelling te accepteren. Het hostingplatform deployt naar waar het naartoe deployt. E-mail loopt via een provider waarvan niemand ooit naar de infrastructuur heeft gekeken. En de AI-functie die in het voorjaar werd toegevoegd, stuurt klanttekst naar een model-API die overal kan draaien.

Dit is te beantwoorden, en het goed beantwoorden is vaak het verschil tussen het binnenhalen van een Nederlandse zakelijke klant en niet. Het is ook, zodra u hebt gekeken, af en toe een reden om iets te veranderen.

## Begin met de Lijst, Niet met het Antwoord

Schrijf, voordat u iets beslist, elke dienst op die klantdata raakt. In een typisch door AI gebouwd product is die lijst langer dan verwacht.

De database en haar back-ups. Objectopslag voor geüploade bestanden. De applicatiehosting zelf, inclusief serverless functies, die in een andere regio kunnen draaien dan uw database. De e-mailprovider. Error tracking, dat verzoekdata vastlegt en soms persoonsgegevens in stacktraces. Analytics. De betaalprovider. Elke AI-model-API. Supporttools. Sessie-opnames, als u die hebt toegevoegd en vergeten.

Per dienst drie feiten: waar de data wordt verwerkt, waar ze wordt opgeslagen, en waar de back-ups staan. Elke betrouwbare provider publiceert ze, en geen ervan kost veel tijd om te vinden.

Deze lijst is nuttig buiten de vraag over datalocatie - het is het register van subverwerkers waar uw zakelijke klanten toch om zullen vragen, en het is inhoudelijk vereist door de AVG, ongeacht wie erom vraagt.

## De Databaseregio Is Niet het Hele Antwoord

Oprichters die hiernaar kijken, controleren meestal de database, zien dat die in Frankfurt of Amsterdam staat, en stoppen.

Drie dingen worden vaak gemist. Back-ups kunnen naar een andere regio worden gerepliceerd dan de primaire database, wat een bewuste veerkrachtfunctie is en een vraag over datalocatie. Serverless functies draaien vaak in de regio die het dichtst bij de bezoeker ligt, tenzij vastgezet, dus uw Europese database wordt bevraagd door code die in Virginia draait. En CDN-randknooppunten houden gecachete content per definitie wereldwijd vast - wat prima is voor publieke pagina's en niet prima als er ooit een gepersonaliseerd antwoord is gecachet.

Het punt over functies veroorzaakt ook echte vertraging: een applicatie die wereldwijd is uitgerold met een database in één regio, betekent dat elk verzoek een trage heen-en-terugreis maakt. Functies vastzetten in de regio van de database is meestal zowel het compliant antwoord als het snellere.

## Doorgiften Buiten de EU Zijn Niet Verboden

Het is de moeite waard precies te zijn, want oprichters denken vaak dat de regels strenger zijn dan ze zijn.

Persoonsgegevens mogen de Europese Economische Ruimte verlaten, mits er een rechtmatige grondslag is voor de doorgifte - een adequaatheidsbesluit voor het land van bestemming, modelcontractbepalingen (standard contractual clauses) met aanvullende maatregelen waar nodig, of een van de smalle uitzonderingen. De meeste grote providers bieden de relevante contractvoorwaarden standaard aan.

Dus "onze error tracking wordt verwerkt in de Verenigde Staten onder modelcontractbepalingen, waarbij persoonsgegevens vóór verzending worden verwijderd" is een legitiem antwoord. Wat niet legitiem is, is het niet weten, en wat contracten kost is niet de doorgifte maar het onvermogen haar te beschrijven.

Twee praktische posities zijn het onderscheiden waard. Een wettelijke eis om data in de EU te houden, is buiten specifieke sectoren zeldzaam. Een contractuele eis van een klant - een ziekenhuis, een gemeente, een bank - komt veel voor, en daarover wordt onderhandeld in plaats van dat ze wettelijk is vastgelegd. Weten met welke van de twee u te maken hebt, verandert wat u eraan moet doen.

## Verminder Wat U Verstuurt Voordat U Verplaatst Waar U Het Naartoe Stuurt

De goedkoopste verbetering is meestal niet een dienst verhuizen. Het is er minder naartoe sturen.

Error tracking die is ingesteld om persoonsgegevens vóór verzending te verwijderen, neemt het grootste deel van de zorg weg zonder van provider te wisselen. Analytics zonder persoonlijke identificaties wordt een veel kleinere vraag. Een AI-functie die alleen de tekst verstuurt die voor de taak nodig is, in plaats van een heel record inclusief namen en adressen, geeft minder door en kost minder.

Dit is goede praktijk, los van geografie, en het maakt het gesprek over subverwerkers korter, omdat de eerlijke beschrijving "gepseudonimiseerde technische data" wordt in plaats van "klantgegevens".

## Wanneer U Toch Iets Moet Veranderen

Soms is het antwoord echt onvoldoende voor de klant die voor u staat, en moet er iets verhuizen.

Volgorde van moeilijkheid, goedkoopste eerst. Serverless functies vastzetten in een regio is meestal één configuratieregel. Een e-mail- of error-trackingprovider vervangen door een in de EU gehoste tegenhanger is een dag. Objectopslag verhuizen is kopiëren plus herschrijven hoe URL's worden gemaakt. De database verhuizen is een migratie met een onderhoudsvenster. De AI-modelprovider omzetten naar een deployment in een EU-regio is meestal een configuratiewijziging met een ander endpoint, al kan het beïnvloeden welke modellen beschikbaar zijn.

Doe ze in die volgorde, en controleer na elke stap of aan de eis van de klant is voldaan. Vaak is dat na twee stappen al zo, en is de dure migratie overbodig.

## Schrijf het Antwoord Op Voordat Erom Wordt Gevraagd

Maak een pagina - een echte pagina op uw website, geen alinea in een e-mail - die beschrijft waar data wordt opgeslagen, welke subverwerkers u gebruikt, wat elk ontvangt, en welke contractuele grondslag een doorgifte buiten de EU dekt.

Drie voordelen. Het verkoopgesprek wordt drastisch korter, omdat de inkoopfunctionaris het kan lezen in plaats van ernaar te vragen. Het toont een niveau van serieusheid dat de meeste kleine concurrenten niet bereiken. En het schrijven ervan dwingt de inventarisatie accuraat te zijn, en dat is het deel dat ertoe doet.

Houd haar actueel. Een subverwerkerspagina die een provider noemt die u twee jaar geleden niet meer gebruikte en de AI-API weglaat die u in het voorjaar toevoegde, is erger dan geen pagina, omdat het een uitspraak is die u hebt gedaan en waaraan u kunt worden gehouden.

## De Vragen Achter de Vraag

Datalocatie is zelden het enige wat een inkoopbeoordeling wil, en de andere punten komen in dezelfde e-mail binnen. Ze kennen laat u één keer voorbereiden in plaats van drie keer.

**Wie heeft aan uw kant toegang tot de data?** Oftewel: hoeveel mensen in uw bedrijf kunnen de gegevens van een klant lezen, onder welke controles, en wordt die toegang gelogd. Voor een eenmanszaak is het eerlijke antwoord kort, en kunnen zeggen "één persoon, met vastgelegde toegang, en hier is het logboek" is sterker dan een vage geruststelling.

**Wat gebeurt er als het contract eindigt?** Exportformaat, termijn voor verwijdering, en de bevestiging dat back-ups uiteindelijk verlopen. Klanten vragen het omdat ze eerder vast hebben gezeten.

**Wat is uw beschikbaarheidstoezegging en uw incidentproces?** Niet per se een formele SLA voor een klein product, maar een genoemd doel en een geschreven beschrijving van hoe u reageert en meldt.

**Gebruikt u klantdata om modellen te trainen?** Steeds vaker de eerste vraag in plaats van de laatste, en het verwachte antwoord is nee, duidelijk gezegd, met de voorwaarden van de leverancier als onderbouwing - sommige model-API's gedragen zich op verschillende niveaus anders, dus controleer het in plaats van het aan te nemen.

Geen van deze vereist een groot bedrijf om goed te beantwoorden. Ze vereisen dat u erover hebt nagedacht voordat erom wordt gevraagd, en dat is het hele verschil tussen een inkoopproces van twee weken en een van twee maanden.

De praktische stap is alle vijf de antwoorden in één intern document te zetten en de klantgerichte helft op uw website te houden. Inkoopfunctionarissen zijn geen tegenstanders; het zijn mensen met een checklist die die liever snel afvinken. Geef ze iets om af te vinken.

## Dit Inrichten

Voor een bestaand product kost dit doorgaans één tot twee dagen: een inventarisatie van elke dienst die klantdata raakt, met locaties voor verwerking, opslag en back-ups per dienst; serverless functies vastgezet in de regio van de database; gecachete content gecontroleerd zodat niets gepersonaliseerds op randknooppunten staat; error tracking en analytics ingesteld om persoonsgegevens te verwijderen of weg te laten; AI-functies beoordeeld op wat ze werkelijk versturen; contractuele grondslagen bevestigd voor doorgiften buiten de EER; een gepubliceerde pagina over subverwerkers en datalocatie; en een notitie in de repository zodat de lijst wordt bijgewerkt wanneer er een dienst bijkomt.

LaunchStudio doet dit als onderdeel van het klaarmaken van een product voor zakelijke klanten, en het is meestal het stuk dat een contract met een groot bedrijf of de publieke sector deblokkeert. Achter het werk staat Manifera - elf jaar, klanten als Vodafone, TNO en CFLW, met Europese activiteiten vanaf de Herengracht 420 in Amsterdam en ontwikkeling in Singapore en Ho Chi Minh-stad.

[Stuur ons de vragenlijst die u kreeg](https://launchstudio.eu/nl/#contact) en wij vertellen u welke antwoorden u al hebt.

## Echt voorbeeld

### De Vragenlijst van de Gemeente

Hidde Vermaas bouwde Meldpunt in Lovable: een systeem waarmee gemeenten meldingen van inwoners ontvangen en volgen over straatmeubilair, verlichting en groenonderhoud. Elf kleinere gemeenten gebruikten het toen een grotere gemeente een aanbesteding startte.

Hun vragenlijst vroeg waar persoonsgegevens - namen, adressen en e-mailadressen van melders en vrije-tekstomschrijvingen - werden opgeslagen en verwerkt. Hiddes eerlijke antwoord vergde twee weken onderzoek en was minder comfortabel dan hij verwachtte.

De Supabase-database stond in Frankfurt, en dat was prima. Maar zijn serverless functies draaiden in de regio die het dichtst bij de bezoeker lag, dus queries kwamen binnen vanaf drie continenten. Zijn error tracking legde volledige verzoeken vast, inclusief namen en adressen van melders, verwerkt in de Verenigde Staten, zonder opschoning. Geüploade foto's van gemelde problemen stonden in een opslagbucket in een Amerikaanse regio, gekozen door een standaardinstelling waar niemand naar had gekeken. En een functie voor het samenvatten van omschrijvingen, in het voorjaar toegevoegd, stuurde de volledige meldingstekst - inclusief namen - naar een model-API zonder dat er een verwerkersovereenkomst was.

Zes werkdagen: de volledige inventarisatie van diensten met locaties voor verwerking, opslag en back-ups gedocumenteerd; functies vastgezet in de regio Frankfurt, wat ook de gemiddelde responstijd met 240 milliseconden verlaagde; error tracking verplaatst naar een in de EU gehoste provider met opschoning van verzoeken ingesteld, zodat persoonsgegevens nooit worden verstuurd; 34.000 foto's gemigreerd naar een EU-opslagregio, met het genereren van URL's herschreven en bestaande links omgeleid; de samenvattingsfunctie omgezet naar een modelendpoint in een EU-regio met een verwerkersovereenkomst, en aangepast om alleen de omschrijving te versturen in plaats van het hele record; een gepubliceerde pagina over subverwerkers en datalocatie; en een gedocumenteerd proces dat een controle op datalocatie vereist voordat er een nieuwe dienst bijkomt.

**Resultaat:** de vragenlijst werd beantwoord vanaf de gepubliceerde pagina met twee verduidelijkende zinnen, en het contract werd gegund. Drie van de elf bestaande gemeenten vroegen binnen een maand om hetzelfde document, en Hidde stuurt de link nu mee voordat erom wordt gevraagd.

> *"Elk van die standaardinstellingen werd gekozen door op een middag door een installatiescherm te klikken. Geen ervan was een beslissing, en alle vier stonden ze op de vragenlijst."*
> - **Hidde Vermaas, Oprichter, Meldpunt (Deventer)**

**Kosten & Doorlooptijd:** €4.200 (inventarisatie van diensten, functies vastgezet in een regio, migratie van error tracking met opschoning, opslagmigratie met omleiden van links, wijziging van AI-endpoint en overeenkomst met kleinere payload, gepubliceerde documentatie, procesdefinitie) - afgerond in 6 werkdagen.

## Veelgestelde vragen

### Is het illegaal om persoonsgegevens uit de EU buiten de EU op te slaan?

Nee. Doorgiften zijn toegestaan met een rechtmatige grondslag - een adequaatheidsbesluit, modelcontractbepalingen met passende maatregelen, of een uitzondering. Wat problemen veroorzaakt, is niet weten wat u doet of het niet kunnen beschrijven.

### Is het controleren van mijn databaseregio genoeg?

Nee. Back-ups kunnen elders worden gerepliceerd, serverless functies draaien vaak dicht bij de bezoeker in plaats van bij de database, en CDN-knooppunten cachen wereldwijd. Alle drie moeten worden gecontroleerd.

### Wat wordt er meestal gemist in de inventarisatie?

Error tracking die volledige verzoeken vastlegt, analytics met identificaties, later toegevoegde AI-model-API's, en objectopslag die is aangemaakt met een standaardregio die niemand bewust koos.

### Moet ik alles naar de EU verhuizen?

Meestal niet. Verminder eerst wat u verstuurt - verwijder persoonsgegevens uit error tracking, stuur AI-functies alleen wat ze nodig hebben - en verhuis daarna diensten in volgorde van kosten, waarbij u na elke stap controleert of aan de eis is voldaan.

### Moet ik een lijst van subverwerkers publiceren?

Ja. Het verkort verkoopgesprekken met zakelijke klanten, toont serieusheid, en dwingt uw eigen inventarisatie accuraat te zijn. Houd haar actueel, anders wordt ze een risico.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is het illegaal om persoonsgegevens uit de EU buiten de EU op te slaan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee - doorgiften zijn rechtmatig met een adequaatheidsbesluit, modelcontractbepalingen of een uitzondering. Het probleem is niet kunnen beschrijven wat u doet."
      }
    },
    {
      "@type": "Question",
      "name": "Is het controleren van de databaseregio voldoende?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Back-ups kunnen naar een andere regio repliceren, serverless functies draaien vaak dicht bij de bezoeker, en CDN-knooppunten cachen wereldwijd."
      }
    },
    {
      "@type": "Question",
      "name": "Wat wordt meestal gemist bij het opsommen waar data naartoe gaat?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Error tracking die verzoeken vastlegt, analytics-identificaties, later toegevoegde AI-model-API's, en opslagbuckets aangemaakt met een standaardregio."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik elke dienst naar de EU verhuizen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Meestal niet. Verminder eerst wat u verstuurt, verhuis dan diensten in volgorde van kosten, en controleer na elke stap of aan de eis is voldaan."
      }
    },
    {
      "@type": "Question",
      "name": "Moet een klein product een lijst van subverwerkers publiceren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. Het verkort inkoopgesprekken en dwingt uw eigen inventarisatie accuraat te blijven - mits u haar actueel houdt."
      }
    }
  ]
}
</script>
