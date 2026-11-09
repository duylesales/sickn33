---
Titel: "Hoe Herstel Ik Verwijderde Data in Supabase?"
Trefwoorden: verwijderde data herstellen supabase, supabase back-up terugzetten, supabase point-in-time recovery, verwijderde tabel supabase terughalen, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Hoe Herstel Ik Verwijderde Data in Supabase?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Herstel Ik Verwijderde Data in Supabase?",
  "description": "Per ongeluk verwijderde rijen, een gedropte tabel of een slechte migratie kunnen in elke met AI gebouwde app gebeuren. Deze gids legt uit wat u direct moet doen, welke hersteloptie Supabase biedt via back-ups en point-in-time recovery, waarom het terugzetten van een heel project riskant is, hoe u specifieke records veilig herstelt, wat er met bestanden in opslag gebeurt en hoe u dataverlies voorkomt met soft delete, waarborgen en geteste herstelprocedures.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-08-02",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-do-i-recover-deleted-data-in-supabase" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Database backups", "url": "https://supabase.com/docs/guides/platform/backups" },
    { "@type": "CreativeWork", "name": "Supabase: Point-in-time recovery", "url": "https://supabase.com/docs/guides/platform/backups#point-in-time-recovery" },
    { "@type": "CreativeWork", "name": "PostgreSQL: Backup and restore", "url": "https://www.postgresql.org/docs/current/backup.html" },
    { "@type": "CreativeWork", "name": "GDPR Article 32: Security of processing", "url": "https://gdpr-info.eu/art-32-gdpr/" }
  ]
}
</script>

**Kort antwoord:** voorkom eerst verdere schade en controleer daarna welke back-ups u heeft. Op betaalde Supabase-plannen kunt u met dagelijkse back-ups en, met de add-on, point-in-time recovery de database terugzetten naar een eerder moment, maar het terugzetten van het hele project draait ook elke legitieme wijziging sinds dat moment terug. Bij per ongeluk verwijderde specifieke records is het meestal veiliger om een back-up terug te zetten in een apart project, de ontbrekende rijen daaruit te halen en ze opnieuw in productie in te voegen. Bestanden in Supabase Storage worden apart van databaseback-ups behandeld. Voorkom het volgende incident met soft delete, beperkte verwijderrechten, gereviewde migraties en regelmatig geteste herstelprocedures.

## Belangrijkste Punten

- **Handel snel maar zorgvuldig:** stop het proces dat de schade veroorzaakt, noteer het tijdstip en voorkom dat haastige fixes het erger maken.
- **Ken uw back-upsituatie voordat u haar nodig heeft:** op welk plan u zit, hoe ver back-ups teruggaan en of point-in-time recovery aanstaat.
- **Een volledige projectrestore draait alles terug,** inclusief nieuwe bestellingen, gebruikers en wijzigingen sinds het herstelpunt.
- **Selectief herstel** vanuit een teruggezette kopie is meestal de juiste aanpak voor verwijderde records.
- **Voorkomen is beter dan herstellen:** soft delete, beperkte verwijderrechten, reviews van migraties en geteste back-ups.

## Stap 1: Stop de Schade

Dataverlies gaat vaak door nadat het is begonnen: een bug die bij elke run records verwijdert, een synchronisatietaak die data overschrijft, een AI-agent die een destructief script herhaalt.

- **Stop de bron:** schakel de functie uit, pauzeer de taak, draai de deployment terug of trek de toegang in die het veroorzaakte.
- **Noteer het tijdstip** waarop het probleem begon, zo precies mogelijk. Logs, auditregels en meldingen van gebruikers helpen.
- **Informeer uw team** en spreek af dat niemand zonder afstemming handmatige wijzigingen in productie doet.
- **Voer geen extra "fixes"** direct in productie uit totdat u begrijpt wat er gebeurd is.

## Stap 2: Begrijp Wat Er Verloren Is

- Welke tabellen en records zijn getroffen?
- Is data verwijderd, overschreven of beschadigd?
- Wanneer is het precies gebeurd?
- Welke legitieme wijzigingen zijn er sindsdien gedaan?
- Zijn bestanden in opslag ook getroffen?

Logs, audittabellen en de migratiegeschiedenis helpen deze vragen te beantwoorden. Als uw app een auditlog heeft, kunnen verwijderde records en hun waarden daar zelfs zichtbaar zijn.

## Stap 3: Bekijk Uw Hersteloptie

| Optie | Wat het biedt | Aandachtspunten |
| --- | --- | --- |
| Soft-deleted records | Records die als verwijderd zijn gemarkeerd maar nog in de tabel staan | Direct herstel, als uw app soft delete gebruikt |
| Auditlog of historietabellen | Eerdere waarden vastgelegd door triggers | Kan specifieke records herbouwen |
| Dagelijkse back-ups | Momentopname van de database eens per dag, bewaard gedurende een periode die afhangt van het plan | Herstelpunt kan vele uren vóór het incident liggen |
| Point-in-time recovery | Terugzetten naar een specifiek moment binnen de bewaartermijn | Beschikbaar als add-on op betaalde plannen; zeer precies |
| Uw eigen exports | Logische dumps die u heeft gemaakt, bijvoorbeeld vóór migraties | Alleen zo actueel als de laatste export |

Supabase beschrijft back-ups en point-in-time recovery in de platformdocumentatie, inclusief welke plannen dagelijkse back-ups bevatten en hoe lang ze worden bewaard. Controleer de actuele details voor uw plan en project, bij voorkeur vóór een incident.

## Waarom een Volledige Restore Riskant Is

De hele database terugzetten naar een moment vóór het incident klinkt als een schone oplossing. Het verwijdert echter ook alles wat daarna is gebeurd: nieuwe aanmeldingen, bestellingen, betalingen die via webhooks zijn geregistreerd, berichten en bewerkingen. Voor een app met actieve gebruikers kan dat erger zijn dan het oorspronkelijke probleem, en het veroorzaakt inconsistenties met externe systemen zoals uw betaalprovider.

Een volledige restore is gepast wanneer de hele database beschadigd is, het incident heel recent is en er sindsdien weinig legitieme activiteit was, of de schade zo omvangrijk is dat selectief herstel niet praktisch is. Herstel anders selectief.

## Selectief Herstel

De veiligere aanpak voor de meeste per ongeluk verwijderde data:

1. **Zet een back-up of point-in-time-kopie terug in een apart project,** of verkrijg een databasedump uit de back-up, zonder productie aan te raken. Controleer de actuele opties van Supabase om naar een nieuw project terug te zetten of back-ups te downloaden.
2. **Zoek de ontbrekende data** in de teruggezette kopie: de verwijderde rijen, met hun ID's en gerelateerde records.
3. **Exporteer die rijen,** inclusief onderliggende records die via cascades zijn verwijderd.
4. **Controleer op conflicten** met data die sindsdien is aangemaakt, zoals hergebruikte unieke waarden.
5. **Voeg ze gecontroleerd opnieuw in productie in,** bij voorkeur via een script dat door iemand anders is gereviewd, binnen een transactie.
6. **Verifieer** met tellingen en steekproeven, en bevestig bij getroffen gebruikers.
7. **Verwijder de tijdelijke kopie** als u klaar bent, want die bevat productiedata.

Zo blijft alle legitieme activiteit behouden terwijl wat verloren was, wordt hersteld.

## Cascaderende Verwijderingen

Veel door AI gegenereerde schema's gebruiken `on delete cascade`, waardoor het verwijderen van één record stilletjes alle gerelateerde records verwijdert: een klant verwijderen verwijdert ook zijn projecten, facturen en documenten. Zoek bij herstel alle getroffen onderliggende records in de teruggezette kopie, niet alleen het bovenliggende record. En bekijk de cascades daarna opnieuw, zoals beschreven in onze gids over [soft delete versus hard delete](https://launchstudio.eu/nl/blog/soft-delete-vs-hard-delete-in-saas).

## Bestanden in Opslag

Databaseback-ups dekken de data in de database. Bestanden in Supabase Storage, zoals geüploade documenten en afbeeldingen, worden apart opgeslagen, en hun herstel hangt af van hoe opslag is ingericht en geback-upt. Metadata over bestanden staat in de database, maar de inhoud van de bestanden niet. Als er bestanden zijn verwijderd, controleer dan of u eigen kopieën of opslag met versies heeft, en plan back-ups van bestanden expliciet als bestanden belangrijk zijn voor uw bedrijf.

## Na het Herstel: Leren en Voorkomen

Zodra de data is hersteld, zoekt u de grondoorzaak en voorkomt u herhaling:

- **Soft delete** voor belangrijke bedrijfsrecords, met een prullenbak en herstelfunctie
- **Beperk verwijderrechten** in Row Level Security, zodat gewone gebruikers belangrijke data niet definitief kunnen verwijderen
- **Bevestigingen voor destructieve acties,** met een samenvatting van wat erdoor wordt geraakt
- **Review migraties,** vooral die door AI-tools zijn gegenereerd, voordat ze in productie draaien; let op `drop table`, `drop column` en brede `delete`-statements
- **Gescheiden omgevingen,** zodat experimenten en sessies van AI-agents tegen staging draaien, niet tegen productie
- **Auditlogs** die verwijderingen vastleggen met de uitvoerder en de waarden
- **Point-in-time recovery** ingeschakeld voor productiedatabases met belangrijke data
- **Geteste herstelprocedures:** oefen selectief herstel minstens één keer, zodat u de stappen kent vóór een noodgeval

## Een Restore Oefenen Voordat U Hem Nodig Heeft

Het slechtste moment om te leren hoe een restore werkt, is tijdens een incident. Een hersteloefening, een of twee keer per jaar, maakt herstel tot routine:

1. **Kies een realistisch scenario,** zoals "het project van een klant en alle bijbehorende taken zijn gisteren om 14.00 uur verwijderd".
2. **Zet een back-up of point-in-time-kopie terug** in een apart project, volgens de gedocumenteerde stappen van Supabase.
3. **Zoek de data op** en exporteer de getroffen rijen, inclusief gerelateerde records.
4. **Voeg ze opnieuw in staging in,** niet in productie, met een gereviewd script.
5. **Meet de tijd van elke stap** en schrijf op wat onduidelijk of traag was.
6. **Werk uw runbook bij** met de precieze stappen, commando's en contactpersonen.
7. **Verwijder het tijdelijke project** na afloop.

Oprichters die één keer hebben geoefend, herstellen echte incidenten meestal binnen uren in plaats van dagen, en maken onder druk minder fouten.

## Eigen Exports Bewaren

Back-ups van het platform zijn essentieel, maar een onafhankelijke kopie voegt weerbaarheid toe: regelmatige logische exports van de database naar opslag die u zelf beheert, versleuteld en bewaard gedurende een vastgestelde periode, en kopieën van belangrijke bestanden. Die beschermen tegen scenario's zoals problemen met toegang tot accounts of fouten die pas worden ontdekt nadat de bewaartermijn van de back-ups van het platform is verstreken. Behandel deze exports als gevoelige data, met dezelfde discipline voor toegangscontrole en bewaartermijnen als productie.

## Communiceren met Gebruikers

Als gebruikers data zijn kwijtgeraakt, vertel hun dan wat er is gebeurd, wat u heeft hersteld, wat niet kon worden hersteld en wat u heeft veranderd om herhaling te voorkomen. Als bij het incident persoonsgegevens verloren zijn gegaan of onbeschikbaar zijn geworden, overweeg dan of het onder de AVG een inbreuk in verband met persoonsgegevens is, wat ook verlies van beschikbaarheid omvat, en of er meldplichten gelden. Onze gids over [reageren op een datalek onder de AVG](https://launchstudio.eu/nl/blog/gdpr-data-breach-response-the-72-hours-for-a-small-saas) legt de beoordeling uit.

## Herstellen van Overschreven Data

Niet alle dataverlies is verwijdering. Soms worden waarden overschreven: een bulkupdate zonder filter zet de status van elke klant op inactief, of een synchronisatietaak vervangt adressen door lege waarden. Herstel volgt hetzelfde principe: zet een kopie van vóór het incident terug in een apart project, vergelijk de getroffen kolommen met productie en schrijf alleen de gewijzigde waarden voor getroffen rijen terug, zodat latere legitieme wijzigingen intact blijven. Audit- of historietabellen, als uw app eerdere waarden vastlegt, kunnen dit veel sneller maken.

## Veelvoorkomende Oorzaken van Dataverlies in Apps Gebouwd met AI

| Oorzaak | Voorbeeld |
| --- | --- |
| Door AI gegenereerde migratie | Een agent dropt en herschept een tabel om het schema te "vereenvoudigen" |
| Cascaderende verwijdering | Het verwijderen van een dubbele klant verwijdert al zijn projecten |
| Bug in een bulkactie | Een knop "geselecteerde verwijderen" verwijdert alles als er niets is geselecteerd |
| Fout in een synchronisatietaak | Een integratie overschrijft lokale data met lege waarden uit een extern systeem |
| Ontbrekend filter | Een update zonder filter wijzigt elke rij |
| Handmatige SQL in productie | Een snelle fix in de SQL-editor met een onbedoeld bereik |
| Seed- of testscript | Een resetscript draait tegen productie in plaats van staging |

De meeste hiervan zijn te voorkomen met omgevingen, reviews en minimale toegangsrechten.

## Wie Zou Mogen Herstellen

Productiedata terugzetten is een krachtige actie. Beperk het tot een klein aantal mensen met accounts die met MFA zijn beveiligd, laat een tweede persoon scripts voor restore en heropname reviewen, en leg elke restore vast in een operationeel logboek met de reden en de uitkomst.

## Hoe LaunchStudio Helpt

LaunchStudio helpt oprichters om dataverlies te herstellen en te voorkomen: het incident beoordelen, back-ups of point-in-time-kopieën terugzetten in aparte projecten, specifieke records herstellen inclusief data die via cascades verdween, veilig opnieuw invoegen, en daarna soft delete, beperkte rechten, auditlogs, reviews van migraties, gescheiden omgevingen, strategieën voor back-ups van bestanden en geteste herstelprocedures implementeren.

Het **Launch Ready**-pakket (€800-€3.500) omvat ondersteuning bij herstel en preventieve waarborgen; **Launch & Grow** (€2.500-€7.500 plus €49 per maand) omvat beheerde hosting met back-ups, monitoring en prioriteitssupport, zodat incidenten snel worden afgehandeld. Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een schatting.

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, 160+ opgeleverde projecten en 120+ engineers, dat productiedatabases beheert en herstelt voor enterpriseklanten. Oprichters ontmoeten het team aan de Herengracht 420 in Amsterdam; de engineering gebeurt in het ontwikkelcentrum aan de Pho Quang Street in Ho Chi Minh City, met een hub aan de Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Migratie Die de Bestellingentabel Dropte

Thomas Brink bouwde Bloemenabonnement met Cursor en Supabase: een abonnementsdienst die wekelijks verse bloemen bezorgt bij kantoren en huishoudens in Utrecht. Toen hij een agent vroeg een veld voor een bezorgnotitie toe te voegen, besloot de agent de bestellingentabel te herstructureren en genereerde een migratie die de tabel dropte en opnieuw aanmaakte. Thomas draaide die op een dinsdagmiddag direct tegen productie. Ongeveer 14.000 eerdere bestellingen en de leveringen van die week verdwenen.

Hij zat op een betaald plan met dagelijkse back-ups, maar zonder point-in-time recovery. De laatste back-up was van die ochtend vroeg. Een volledige restore zou de nieuwe bestellingen sindsdien, de via Mollie-webhooks geregistreerde betalingen en verschillende nieuwe abonnementen hebben verwijderd. Thomas' eerste neiging was om alles meteen terug te zetten.

LaunchStudio raadde een volledige restore af. De laatste dagelijkse back-up werd teruggezet in een apart project, en de bestellingentabel werd daaruit geëxporteerd, samen met de via een cascade verwijderde orderregels. Bestellingen die na de back-up waren aangemaakt, werden gereconstrueerd uit betalingsgegevens van Mollie en webhooklogs, die in een aparte tabel waren opgeslagen. De data werd in een gereviewde transactie opnieuw in productie ingevoegd, met tellingen per dag gecontroleerd en steekproeven tegen de bezorglijsten. Het nieuwe veld voor de bezorgnotitie werd toegevoegd met een correcte, additieve migratie. Daarna werd point-in-time recovery ingeschakeld, gingen migraties via een gereviewde pipeline met staging, werden destructieve statements automatisch gemarkeerd, en werd een herstelprocedure gedocumenteerd en getest.

**Resultaat:** Alle historische bestellingen en de leveringen van die week waren de volgende ochtend hersteld, en geen enkele klant miste een bezorging. Thomas heeft sindsdien tientallen migraties zonder incident door de gereviewde pipeline laten lopen.

> *"De agent probeerde behulpzaam te zijn. Ik heb geleerd dat de database een poort nodig heeft tussen een goed idee en productie."*
> - **Thomas Brink, Oprichter, Bloemenabonnement (Utrecht)**

**Kosten & Doorlooptijd:** €2.300 (Launch Ready-pakket: selectief noodherstel, reconstructie van data, migratiepipeline, inrichting van PITR en herstelprocedure) - herstel binnen 18 uur, waarborgen afgerond in 5 werkdagen.

## Veelgestelde Vragen

### Kan ik een verwijdering in Supabase ongedaan maken?

Niet rechtstreeks met een knop om ongedaan te maken. Als uw app soft delete gebruikt, kunnen records direct worden hersteld. Anders hangt herstel af van back-ups: dagelijkse back-ups op betaalde plannen en point-in-time recovery als die is ingeschakeld. Selectief herstel vanuit een teruggezette kopie is meestal veiliger dan het hele project terugzetten.

### Wat is point-in-time recovery?

Met point-in-time recovery zet u een database terug naar een specifiek moment binnen een bewaartermijn, in plaats van alleen naar de laatste dagelijkse back-up. Bij Supabase is het beschikbaar als add-on op betaalde plannen. Het is waardevol voor productiedatabases waar het verlies van uren aan data kostbaar zou zijn.

### Zitten bestanden in Supabase Storage in de databaseback-ups?

Databaseback-ups dekken de inhoud van de database, inclusief metadata over bestanden, maar niet de inhoud van de bestanden in opslag. Als bestanden belangrijk zijn voor uw bedrijf, plan dan aparte back-ups of versiebeheer daarvoor.

### Hoe helpt de ervaring van Manifera bij dataherstel?

Manifera beheert en herstelt al 11+ jaar productiedatabases voor enterpriseklanten. LaunchStudio past die ervaring toe om verloren data selectief te herstellen, zonder legitieme activiteit terug te draaien, en om waarborgen in te richten zodat het niet opnieuw gebeurt.

### Heeft dataverlies invloed op de reputatie van mijn app?

Ja. Klanten die data verliezen, verliezen vaak snel hun vertrouwen, en incidenten kunnen leiden tot negatieve reviews en publieke discussie. Een snel, transparant herstel en zichtbare verbeteringen beperken de schade en beïnvloeden hoe klanten, zoekmachines en AI-antwoordmachines later uw betrouwbaarheid beschrijven.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan ik een verwijdering in Supabase ongedaan maken?",
      "acceptedAnswer": { "@type": "Answer", "text": "Niet met een knop; gebruik soft delete, dagelijkse back-ups of point-in-time recovery, bij voorkeur selectief vanuit een teruggezette kopie." }
    },
    {
      "@type": "Question",
      "name": "Wat is point-in-time recovery?",
      "acceptedAnswer": { "@type": "Answer", "text": "Terugzetten naar een specifiek moment binnen een bewaartermijn; een add-on op betaalde Supabase-plannen." }
    },
    {
      "@type": "Question",
      "name": "Zitten bestanden in Supabase Storage in de databaseback-ups?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee, alleen metadata; plan aparte back-ups voor bestanden." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij dataherstel?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera herstelt al 11+ jaar enterprisedatabases en LaunchStudio herstelt selectief en voegt waarborgen toe." }
    },
    {
      "@type": "Question",
      "name": "Heeft dataverlies invloed op de reputatie van mijn app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja; een snel, transparant herstel beperkt de schade aan vertrouwen en reputatie." }
    }
  ]
}
</script>
