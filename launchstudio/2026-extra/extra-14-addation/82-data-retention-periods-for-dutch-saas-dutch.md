---
Titel: "Bewaartermijnen voor Nederlandse SaaS: Wat U Bewaart en Wat U Verwijdert"
Trefwoorden: bewaartermijnen saas, bewaren van gegevens nederland, fiscale bewaarplicht 7 jaar, bewaarbeleid avg app, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelgroep: SaaS-Oprichter Scale-Up
---

# Bewaartermijnen voor Nederlandse SaaS: Wat U Bewaart en Wat U Verwijdert

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bewaartermijnen voor Nederlandse SaaS: Wat U Bewaart en Wat U Verwijdert",
  "description": "AI-gebouwde apps bewaren meestal alles voor altijd. De AVG vereist dat persoonsgegevens niet langer worden bewaard dan nodig, terwijl de Nederlandse fiscale regels vereisen dat de administratie jarenlang wordt bewaard. Deze gids laat zien hoe u bewaartermijnen vastlegt en automatiseert.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-30",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/data-retention-periods-for-dutch-saas" },
  "citation": [
    { "@type": "CreativeWork", "name": "GDPR Article 5: Principles", "url": "https://gdpr-info.eu/art-5-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 17: Right to erasure", "url": "https://gdpr-info.eu/art-17-gdpr/" },
    { "@type": "CreativeWork", "name": "Belastingdienst", "url": "https://www.belastingdienst.nl/" },
    { "@type": "CreativeWork", "name": "IBM Cost of a Data Breach Report", "url": "https://www.ibm.com/reports/data-breach" },
    { "@type": "CreativeWork", "name": "Supabase Cron", "url": "https://supabase.com/docs/guides/cron" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens", "url": "https://www.autoriteitpersoonsgegevens.nl/en" }
  ]
}
</script>

Twee regels trekken in tegengestelde richtingen. De AVG zegt dat persoonsgegevens niet langer mogen worden bewaard dan nodig is voor hun doel. Het Nederlandse belastingrecht zegt dat de administratie in het algemeen zeven jaar moet worden bewaard. De meeste AI-gebouwde apps lossen die spanning op door niets te doen: alles wordt voor altijd bewaard. Een bewaarbeleid, geautomatiseerd in uw database, is hoe u beide regels respecteert en de schade van een toekomstig incident beperkt. Dit artikel is algemene informatie; laat specifieke termijnen bevestigen door uw accountant of advocaat.

## Belangrijkste Punten

- **Het beginsel van opslagbeperking in de AVG (artikel 5) vereist dat persoonsgegevens niet langer dan nodig worden bewaard;** het Nederlandse belastingrecht vereist in het algemeen dat de administratie zeven jaar wordt bewaard.
- **De meeste AI-gebouwde apps bewaren alles voor altijd,** wat het risico, de kosten en de impact van een incident vergroot.
- **Leg per categorie gegevens een bewaartermijn vast,** documenteer de redenen en automatiseer verwijdering of anonimisering met geplande taken.
- **Bij B2B bepalen klanten een deel van de bewaartermijnen** via uw verwerkersovereenkomst, inclusief verwijdering bij het einde van het contract.
- **Ook back-ups en logs hebben bewaarregels nodig,** en uw privacyverklaring hoort die te beschrijven.

## Gangbare Categorieën Gegevens en Uitgangspunten

| Gegevens | Gangbare aanpak | Reden |
| --- | --- | --- |
| Facturen, betalingen, administratie | 7 jaar bewaren | Nederlandse fiscale bewaarplicht (in het algemeen) |
| Gegevens van actieve klantaccounts | Bewaren zolang het account actief is | Nodig om de dienst te leveren |
| Gesloten accounts | Na een korte periode verwijderen of anonimiseren, bijv. 30-90 dagen | Niet langer nodig, met ruimte om te heractiveren |
| Inactieve gratis of proefaccounts | Na een vaste periode verwijderen, bijv. 12 maanden, met een waarschuwingsmail | Minimalisatie |
| Supportgesprekken | 1-2 jaar bewaren | Nuttig voor de supportgeschiedenis, daarna niet meer nodig |
| Applicatielogs met persoonsgegevens | Weken tot een paar maanden | Foutopsporing en beveiliging |
| Beveiligings- en toegangslogs | Langer, bijv. 6-12 maanden, of zoals afgesproken met klanten | Onderzoek bij incidenten |
| Vastlegging van toestemming voor marketing | Zolang u de toestemming gebruikt, plus een periode als bewijs | Toestemming aantonen |
| Geüploade bestanden | Gekoppeld aan het record waar ze bij horen | Verwijderen samen met het record |
| Back-ups | Doorlopende bewaartermijn, bijv. 30 dagen | Herstel, met een gedocumenteerde vertraging voor verwijderingen |

Dit zijn uitgangspunten, geen wettelijke regels. Uw doelen, contracten en sector kunnen andere termijnen vereisen.

## B2B: Uw Klanten Bepalen een Deel

Voor gegevens die u namens zakelijke klanten verwerkt, legt de verwerkersovereenkomst meestal vast wat er gebeurt: teruggeven of verwijderen bij het einde van het contract, soms met bewaartermijnen die de klant zelf kan instellen. Bouw export en verwijdering op organisatieniveau, en houd u aan de afgesproken termijnen.

## Bewaartermijnen Automatiseren

1. Voeg tijdstempels toe waar u op kunt vertrouwen: `created_at`, `last_active_at`, `closed_at`
2. Schrijf geplande taken (Supabase Cron die databasefuncties of edge functions aanroept) die gegevens na hun termijn verwijderen of anonimiseren
3. Stuur waarschuwingsmails voordat u inactieve accounts verwijdert
4. Verwijder gerelateerde bestanden in storage, niet alleen databaserijen
5. Leg vast wat er is verwijderd, zonder de verwijderde inhoud te bewaren
6. Test bewaartaken eerst in staging

Onze gids over [geplande taken en herinneringen in Supabase](https://launchstudio.eu/nl/blog/how-do-i-send-automatic-reminders-from-a-supabase-app) legt de kant van het plannen uit, en onze [gids over AVG-verwijdering](https://launchstudio.eu/nl/blog/how-do-i-delete-a-users-data-in-supabase-for-gdpr) behandelt de werking van verwijdering.

## Documenteer het

Leg uw bewaartermijnen vast in uw verwerkingsregister en vat ze samen in uw privacyverklaring. Wanneer klanten of toezichthouders ernaar vragen, overtuigt een duidelijke tabel meer dan "we verwijderen gegevens wanneer ze niet meer nodig zijn".

## Waarom Bewaartermijnen een Beveiligingsmaatregel Zijn

Gegevens die u niet meer heeft, kunnen niet uitlekken. Elk oud account, verouderd cv, verlopen proefabonnement en vergeten upload vergroot de mogelijke impact van een datalek. Het Cost of a Data Breach-onderzoek van IBM koppelt de kosten van datalekken steeds weer aan de hoeveelheid en gevoeligheid van de betrokken records. Bewaarregels zijn daarom niet alleen een compliance-oefening; ze verkleinen uw aanvalsoppervlak en de gevolgen van een incident. Ze verlagen ook de opslagkosten en maken uw database sneller en makkelijker te beheren.

## Het Juridische Kader in het Kort

Artikel 5 van de AVG legt de opslagbeperking vast: persoonsgegevens moeten worden bewaard in een vorm die identificatie niet langer mogelijk maakt dan nodig is voor de doelen. Het artikel schrijft geen specifieke termijnen voor; u legt ze per doel vast en moet ze kunnen onderbouwen. Artikel 17 geeft personen in veel situaties het recht op gegevenswissing, met uitzonderingen zoals wettelijke verplichtingen om gegevens te bewaren. Aan de andere kant vereisen de Nederlandse fiscale regels in het algemeen dat bedrijven hun administratie, inclusief facturen en bijbehorende stukken, zeven jaar bewaren, met langere termijnen voor bepaalde gegevens zoals die over onroerend goed. De Belastingdienst en uw accountant kunnen bevestigen wat er voor u geldt.

## Een Bewaarschema Opstellen

Een bewaarschema is een tabel met per categorie gegevens het doel, de bewaartermijn, de gebeurtenis waarmee de termijn begint, de actie aan het einde en de reden. Begin met uw overzicht van gegevens en loop elke categorie door:

| Categorie | Begin van de termijn | Termijn | Actie |
| --- | --- | --- | --- |
| Facturen en betalingen | Factuurdatum | 7 jaar | Verwijderen |
| Gesloten klantaccounts | Sluiting van het account | 30-90 dagen | Verwijderen of anonimiseren |
| Inactieve proefaccounts | Laatste activiteit | 12 maanden, met waarschuwing | Verwijderen |
| Supporttickets | Ticket gesloten | 1-2 jaar | Verwijderen |
| Applicatielogs | Logdatum | 30-90 dagen | Verwijderen |
| Beveiligings- en auditlogs | Logdatum | 6-12 maanden of zoals afgesproken | Verwijderen |
| Geüploade documenten | Gerelateerd record verwijderd | Direct | Bestanden verwijderen |

Deze termijnen zijn voorbeelden; kies uw eigen termijnen op basis van uw doelen en juridisch advies.

## Anonimiseren in Plaats van Verwijderen

Soms wilt u statistieken bewaren zonder persoonsgegevens, zoals het totaal aantal bestellingen per maand. Anonimisering moet de mogelijkheid wegnemen om een persoon met enig redelijkerwijs waarschijnlijk middel te identificeren. Namen en e-mailadressen weghalen, maar exacte adressen, geboortedatums of vrije notities laten staan, laat gegevens vaak herleidbaar, wat betekent dat het onder de AVG nog steeds persoonsgegevens zijn. Aggregeer waar mogelijk: bewaar maandtotalen in plaats van afzonderlijke records zodra gedetailleerde gegevens niet meer nodig zijn.

## Bewaartermijnen Automatiseren in een Supabase-App

Implementeer bewaartermijnen als geplande taken. Supabase Cron kan dagelijks databasefuncties of edge functions draaien die records na hun bewaartermijn vinden en verwijderen of anonimiseren, inclusief gerelateerde bestanden in storage. Leg elke run vast met aantallen, niet met inhoud. Stuur waarschuwingsmails voordat u inactieve accounts verwijdert die gebruikers misschien willen houden. Test elke taak in staging met testgegevens die randgevallen dekken, zoals accounts met recente facturen die moeten worden bewaard terwijl andere gegevens worden verwijderd.

## Bewaartermijnen in B2B-Contracten

Als verwerker voor zakelijke klanten volgt u hun instructies over bewaartermijnen, meestal beschreven in uw verwerkersovereenkomst. Gangbare bepalingen vereisen dat u bij het einde van het contract alle gegevens van de klant teruggeeft of verwijdert, soms na een korte overgangsperiode, en staan klanten toe de bewaartermijnen voor bepaalde gegevens in te stellen. Bouw verwijdering op organisatieniveau en instelbare bewaartermijnen waar klanten daarom vragen, en leg vast wanneer verwijderingen plaatsvinden, voor het geval klanten om een bevestiging vragen.

## Back-ups en Logs

Back-ups bevatten alle gegevens op het moment dat ze zijn gemaakt. Gebruik een doorlopende bewaartermijn voor back-ups, zoals 30 dagen, zodat verwijderde gegevens uiteindelijk ook uit de back-ups verdwijnen, en vermeld die vertraging in uw privacyverklaring. Logs bevatten vaak persoonsgegevens zoals e-mailadressen en IP-adressen; stel bewaartermijnen in voor applicatielogs, error tracking en analytics, en log niet meer persoonsgegevens dan u nodig heeft.

## Bewaartermijnen Uitleggen aan Gebruikers

Beschrijf bewaartermijnen in uw privacyverklaring op een manier die gebruikers begrijpen, bijvoorbeeld: "We bewaren uw accountgegevens zolang uw account actief is en verwijderen ze binnen 90 dagen nadat u uw account opheft. Facturen bewaren we zeven jaar, omdat de Nederlandse belastingwet dat vereist. Back-ups bewaren we 30 dagen." Duidelijke uitspraken bouwen vertrouwen op en voorkomen vragen. Stuur bij het verwijderen van inactieve accounts vooraf een waarschuwingsmail met een eenvoudige manier om het account te behouden.

## Bewaartermijnen Regelmatig Herzien

Bewaarschema's lopen uit de pas naarmate producten groeien. Elke nieuwe functie kan nieuwe categorieën gegevens opleveren: chatberichten, de geschiedenis van gesprekken met AI, geüploade media, analytics-events. Neem beslissingen over bewaartermijnen op in uw checklist voor nieuwe functies, herzie het schema minstens jaarlijks en controleer of geplande taken draaien en verwijderen wat ze moeten verwijderen. Een bewaartaak die maanden geleden ongemerkt is gestopt, is een veelvoorkomende bevinding bij audits.

## Veelgemaakte Fouten

- Alle gegevens voor altijd bewaren omdat verwijderen riskant voelt
- Facturen verwijderen die u volgens de belastingwet moet bewaren
- Databaserecords verwijderen, maar bestanden in storage laten staan
- Anonimisering waarbij mensen herleidbaar blijven
- Geen waarschuwing vóór het verwijderen van inactieve accounts
- Bewaartaken zonder monitoring

## De Opbrengst

Een duidelijk, geautomatiseerd bewaarbeleid vermindert het risico, de opslagkosten en de moeite om privacyvragen te beantwoorden. Het laat zakelijke klanten ook volwassenheid zien, en die vragen steeds vaker hoe lang u hun gegevens bewaart en hoe u ze verwijdert.

## Samenvatting

Breng uw gegevens in kaart, leg per categorie een bewaartermijn met een reden vast, automatiseer verwijdering en anonimisering met gemonitorde taken, stem af op de verwerkersovereenkomsten van klanten, neem back-ups en logs mee en leg alles duidelijk uit in uw privacyverklaring.

## Waar U Vandaag Begint

Maak een lijst van uw vijf grootste tabellen en uw storage-buckets. Schrijf bij elk op waarom u de gegevens bewaart en hoe lang u ze werkelijk nodig heeft. Waar het antwoord "voor altijd" is zonder reden, heeft u de eerste bewaarregel gevonden die u moet implementeren.

## Gerelateerde Onderwerpen

Bewaartermijnen gaan hand in hand met verwijdering, back-ups en geplande taken. Onze gidsen over AVG-verwijdering in Supabase, het maken van back-ups van de database van een Lovable-app en automatische herinneringen vanuit een Supabase-app behandelen de bouwstenen.

## Vragen die Klanten over Bewaartermijnen Stellen

Zakelijke klanten en privacy officers vragen vaak: hoe lang bewaart u onze gegevens? Wat gebeurt er wanneer we het contract beëindigen? Hoe lang duurt het voordat verwijderde gegevens uit back-ups verdwijnen? Kunnen we de bewaartermijnen voor de gegevens van onze gebruikers zelf instellen? Bereid korte, accurate antwoorden voor die worden onderbouwd door uw bewaarschema en geplande taken; ze komen vaak terug in beveiligingsvragenlijsten en bijlagen bij verwerkersovereenkomsten.

## De Kern

Bewaar wat de wet of uw doel vereist, verwijder de rest automatisch en leg beide duidelijk uit.

## Het Laten Inrichten

LaunchStudio implementeert bewaartaken, anonimisering, het opruimen van bestanden en documentatie als onderdeel van AVG-werk, meestal twee tot vijf dagen. LaunchStudio wordt ondersteund door Manifera, dat al 11+ jaar de levenscyclus van gegevens ontwerpt voor Nederlandse klanten vanuit Amsterdam en Ho Chi Minh-stad; zie [de over-ons-pagina van Manifera](https://www.manifera.com/about-us/). De [Belastingdienst](https://www.belastingdienst.nl/) publiceert de fiscale bewaarregels, en de [Autoriteit Persoonsgegevens](https://www.autoriteitpersoonsgegevens.nl/) legt opslagbeperking uit.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Vacaturesite die Elk Cv voor Altijd Bewaarde

Robin Geerts bouwde Horecabaan in Lovable: een vacaturesite voor werk in de horeca in Brabant, waar kandidaten cv's uploaden en werkgevers sollicitanten bekijken. Na drie jaar bevatte de database zo'n 18.000 cv's, veel daarvan van mensen die jaren geleden voor het laatst hadden ingelogd, waaronder cv's van minderjarigen die solliciteerden op weekendbaantjes.

Een adviseur gegevensbescherming die was ingehuurd door een grote hotelketen die klant was, vroeg naar de bewaartermijnen. Robin had geen beleid, verwijderde geen inactieve kandidaten en had geen manier om cv's te verwijderen wanneer werkgevers vacatures sloten.

LaunchStudio legde samen met Robin en zijn advocaat de bewaartermijnen vast: inactieve kandidaataccounts krijgen na 11 maanden een waarschuwing en worden na 12 maanden verwijderd; sollicitaties worden 6 maanden na het sluiten van een vacature verwijderd, tenzij de kandidaat instemt met langere opslag; logs worden 60 dagen bewaard; facturen voor werkgevers 7 jaar. Geplande taken voerden deze regels uit, inclusief cv-bestanden in storage, en de privacyverklaring en het verwerkingsregister werden bijgewerkt.

**Resultaat:** De eerste run verwijderde ongeveer twee derde van de opgeslagen cv's. De hotelketen tekende, en als bijeffect daalden Robins opslagkosten.

> *"Ik bewaarde alles omdat verwijderen riskant voelde. Alles bewaren was het echte risico."*
> - **Robin Geerts, Oprichter, Horecabaan (Eindhoven)**

**Kosten & Doorlooptijd:** €1.900 (implementatie van het bewaarbeleid, waarschuwingsmails, geplande verwijdering van records en bestanden, logging en bijgewerkte documentatie) - afgerond in 6 werkdagen.

## Veelgestelde Vragen

### Hoe lang moet ik facturen in Nederland bewaren?

De administratie, inclusief facturen, moet volgens de Nederlandse fiscale regels in het algemeen zeven jaar worden bewaard, met langere termijnen voor bepaalde gegevens zoals die over onroerend goed. Laat dit bevestigen door uw accountant.

### Hoe lang mag ik persoonsgegevens bewaren onder de AVG?

Niet langer dan nodig is voor het doel waarvoor u ze heeft verzameld. U legt de termijn per categorie vast en onderbouwt die, documenteert hem en voert verwijdering of anonimisering uit wanneer hij verloopt.

### Gelden bewaartermijnen ook voor back-ups?

Ja, maar back-ups volgen een eigen doorlopende bewaartermijn. Verwijderde gegevens blijven in back-ups staan totdat die verlopen; documenteer dat en zorg dat verwijderde gegevens niet worden teruggezet in productie.

### Hoe pakt Manifera de levenscyclus van gegevens aan?

Door bewaartermijnen vanaf het begin te ontwerpen: tijdstempels, geplande taken, anonimisering en documentatie. De 11+ jaar van Manifera met Nederlandse klanten laten zien dat bewaartermijnen die vroeg worden ingebouwd veel eenvoudiger zijn dan jarenlange gegevens later opruimen.

### Kan het bewaren van te veel gegevens mijn reputatie schaden?

Ja. Bij een incident bepaalt de hoeveelheid blootgestelde gegevens de impact. Kleinere, goed beheerde gegevensverzamelingen beperken de schade en de publieke aandacht die op datalekken volgt, ook in samenvattingen die door AI worden gegenereerd.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe lang moet ik facturen in Nederland bewaren?",
      "acceptedAnswer": { "@type": "Answer", "text": "In het algemeen zeven jaar, langer voor sommige gegevens; laat dit bevestigen door een accountant." }
    },
    {
      "@type": "Question",
      "name": "Hoe lang mag ik persoonsgegevens bewaren onder de AVG?",
      "acceptedAnswer": { "@type": "Answer", "text": "Niet langer dan nodig voor het doel; leg termijnen vast, documenteer ze en voer ze uit." }
    },
    {
      "@type": "Question",
      "name": "Gelden bewaartermijnen ook voor back-ups?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, via een doorlopende bewaartermijn; documenteer de vertraging en zet verwijderde gegevens niet terug." }
    },
    {
      "@type": "Question",
      "name": "Hoe pakt Manifera de levenscyclus van gegevens aan?",
      "acceptedAnswer": { "@type": "Answer", "text": "Bewaartermijnen vanaf het ontwerp, met tijdstempels, geplande taken, anonimisering en documentatie." }
    },
    {
      "@type": "Question",
      "name": "Kan het bewaren van te veel gegevens mijn reputatie schaden?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja; grotere blootgestelde gegevensverzamelingen vergroten de impact van en de aandacht voor incidenten." }
    }
  ]
}
</script>
