---
Titel: "Hoe Maak Ik een Back-up van de Database van Mijn Lovable-App?"
Trefwoorden: back-up lovable database, supabase back-up, supabase terugzetten, lovable dataverlies, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Hoe Maak Ik een Back-up van de Database van Mijn Lovable-App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Maak Ik een Back-up van de Database van Mijn Lovable-App?",
  "description": "De data van uw Lovable-app staat in Supabase, en of er een back-up van wordt gemaakt hangt af van uw abonnement en instellingen. Deze gids legt beheerde back-ups uit, point-in-time recovery, uw eigen exports buiten de deur, bestandsopslag en de hersteltest die bewijst dat het allemaal werkt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-22",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-do-i-back-up-my-lovable-apps-database" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Database backups", "url": "https://supabase.com/docs/guides/platform/backups" },
    { "@type": "CreativeWork", "name": "GDPR Article 32: Security of processing", "url": "https://gdpr-info.eu/art-32-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 5: Principles", "url": "https://gdpr-info.eu/art-5-gdpr/" },
    { "@type": "CreativeWork", "name": "ENISA Threat Landscape", "url": "https://www.enisa.europa.eu/topics/cyber-threats/threat-landscape" }
  ]
}
</script>

**Kort antwoord:** de data van uw Lovable-app staat in Supabase (uw eigen project of Lovable Cloud). Bij betaalde abonnementen van Supabase worden dagelijkse back-ups voor u beheerd, en point-in-time recovery kan worden toegevoegd voor nauwkeuriger herstel. Voeg voor echte bescherming uw eigen geplande export naar aparte opslag toe, maak apart back-ups van geüploade bestanden en voer een hersteltest uit, zodat u weet hoe lang herstel werkelijk duurt. Een back-up die u nooit heeft teruggezet, is een hoop, geen plan.

## Belangrijkste Punten

- **De data van uw Lovable-app staat in Supabase,** en of er back-ups van worden gemaakt hangt af van uw abonnement en instellingen, niet van Lovable.
- **Gebruik drie lagen:** beheerde dagelijkse back-ups bij een betaald abonnement, point-in-time recovery voor recente fouten en uw eigen export buiten de deur voor onafhankelijkheid.
- **Bestanden in Supabase Storage maken geen deel uit van databaseback-ups** en hebben eigen bescherming nodig.
- **Een back-up die u nooit heeft teruggezet, is een hoop, geen plan.** Test elk kwartaal het terugzetten en meet hoe lang het duurt.
- **Back-ups bevatten persoonsgegevens,** dus bewaar ze in de EU, beperk de toegang en documenteer de bewaartermijn voor de AVG.

## Drie Lagen van Bescherming

| Laag | Waartegen het beschermt | Hoe |
| --- | --- | --- |
| Beheerde dagelijkse back-ups | Grote storingen, slechte migraties | Betaald Supabase-abonnement, controleer de instellingen |
| Point-in-time recovery (PITR) | Fouten in de afgelopen uren, zoals een verkeerde verwijdering | Uitbreiding bij ondersteunde abonnementen |
| Uw eigen export buiten de deur | Problemen met accounts, problemen bij de provider, archieven op lange termijn | Geplande `pg_dump` naar aparte opslag |

Controleer de functies en bewaartermijnen voor back-ups van uw huidige abonnement op de prijs- en back-uppagina's van Supabase, want details veranderen.

## Wat Back-ups Niet Dekken

- **Opslagbestanden.** Databaseback-ups bevatten geen bestanden in Supabase Storage. Geüploade documenten en afbeeldingen hebben een eigen back-up nodig.
- **Configuratie van authenticatie en geheimen.** Instellingen van providers, secrets van edge functions en e-mailsjablonen horen te worden gedocumenteerd.
- **Code van edge functions.** Die staat in uw repository, die uw back-up is als hij op GitHub staat.
- **Het gratis abonnement.** Gratis projecten hebben beperkte of geen garanties voor back-ups en kunnen na inactiviteit worden gepauzeerd. Productie-apps horen op een betaald abonnement.

## Uw Eigen Export Inrichten

Een eenvoudig, betrouwbaar patroon:

1. Een geplande taak (GitHub Actions, een kleine server of een geplande functie) voert elke nacht `pg_dump` uit op uw database
2. De dump wordt versleuteld en geüpload naar opslag in een ander account of bij een andere provider, in een EU-regio
3. Oude dumps worden na uw bewaartermijn verwijderd, bijvoorbeeld 30 dagen plus maandelijkse kopieën voor een jaar
4. Bij een mislukking ontvangt u een melding

Bewaar de verbindingsstring van de database als secret, nooit in de repository.

## De Hersteltest

Eén keer per kwartaal:

1. Maak een tijdelijk Supabase-project aan
2. Zet de nieuwste back-up daarin terug
3. Controleer het aantal rijen in belangrijke tabellen en neem steekproeven van recente records
4. Meet hoe lang het hele proces duurt

De tijd die u meet, is uw realistische hersteltijd. Als die langer is dan uw klanten zouden accepteren, verbeter het proces dan voordat u het nodig heeft.

## Back-ups en de AVG

Back-ups bevatten persoonsgegevens. Bewaar ze in de EU, beperk de toegang en leg een bewaartermijn vast. Wanneer een gebruiker om verwijdering vraagt, verdwijnen zijn gegevens binnen die termijn uit de back-ups; documenteer dit in uw privacyverklaring.

## Herstelnormen in Gewone Taal

Professionals beschrijven de behoeften rond back-ups met twee getallen. De **recovery point objective** (RPO) is hoeveel data u zich kunt permitteren te verliezen, gemeten in tijd: als uw RPO 24 uur is, is een dagelijkse back-up genoeg; als het minuten zijn, heeft u point-in-time recovery nodig. De **recovery time objective** (RTO) is hoe lang u het zich kunt permitteren plat te liggen terwijl u terugzet. Deze twee getallen voor uw app opschrijven, maakt van vage zorg concrete eisen. Een boekingsapp die betalingen verwerkt, heeft misschien een RPO van minuten en een RTO van een uur nodig; een interne tool kan voor beide een dag verdragen.

## Wat Meestal tot Dataverlies Leidt

Hardwarestoringen zijn zeldzaam op beheerde platforms. De gangbare oorzaken zijn menselijk en logisch:

- Een bulkverwijdering of -wijziging die op de verkeerde records wordt uitgevoerd
- Een migratie die een kolom verkeerd verwijdert of omzet
- Een bug die de data van veel gebruikers tegelijk overschrijft
- Een gecompromitteerde sleutel die wordt gebruikt om data te verwijderen of te versleutelen
- Het per ongeluk verwijderen van een project of bucket

Elk van deze gebeurt binnen uw eigen systeem, en daarom beschermt de redundantie van de provider u niet. U heeft back-ups nodig die teruggaan tot vóór de fout, en bij voorkeur één kopie buiten het account dat zou kunnen worden gecompromitteerd.

## Het 3-2-1-Principe, Aangepast

Een klassieke regel voor back-ups zegt: bewaar drie kopieën van uw data, op twee verschillende soorten opslag, met één kopie buiten de deur. Voor de Supabase-app van een oprichter is een praktische aanpassing: de live database, de beheerde back-ups van Supabase en uw eigen versleutelde export bij een andere provider of in een ander account. Die derde kopie beschermt u tegen problemen op accountniveau, zoals verloren toegang of een gecompromitteerde beheerder, waartegen beheerde back-ups binnen hetzelfde account niet beschermen.

## De Back-ups Zelf Beschermen

Back-ups zijn aantrekkelijke doelwitten: ze bevatten alles. Versleutel uw eigen exports, bewaar ze in een privébucket met beperkte toegang, gebruik aparte inloggegevens voor de back-uptaak en geef de identiteit die naar de back-upopslag schrijft geen rechten om daar te verwijderen. Ransomware-aanvallen richten zich steeds vaker eerst op back-ups, dus ze moeilijk te verwijderen maken hoort bij het ontwerp.

## Opslagbestanden: Een Apart Plan

Bestanden in Supabase Storage hebben een eigen aanpak nodig. Opties zijn belangrijke buckets periodiek synchroniseren naar aparte opslag, versiebeheer gebruiken waar dat wordt ondersteund, of voor kritieke documenten zoals getekende contracten en facturen bij het aanmaken een kopie naar een archiefbucket schrijven. Bepaal welke bestanden u echt niet kunt missen en bescherm die als eerste.

## Terugzetten Zonder Het Erger te Maken

Als er iets misgaat, is de neiging om direct over de live database heen terug te zetten. Dat kan bewijs en nieuwere geldige data vernietigen. Een veiliger patroon: zet terug in een apart project, vergelijk de getroffen tabellen met productie, en kopieer alleen de records terug die u nodig heeft. Oefen dit één keer onder rustige omstandigheden, zodat u het niet tijdens een incident hoeft te leren.

## Back-ups en de AVG in Detail

Back-ups bevatten persoonsgegevens en vallen onder dezelfde regels als uw live database: beveiliging die past bij het risico onder artikel 32, aandacht voor locatie bij doorgiften en opslagbeperking onder artikel 5. Bewaar back-ups in EU-regio's, stel een bewaartermijn vast, beperk de toegang en vermeld in uw privacyverklaring dat verwijderde data in back-ups kan blijven bestaan tot ze verlopen. Zorg bij het terugzetten dat data die op verzoek van een gebruiker was verwijderd, niet terug in productie komt.

## Kosten

Beheerde back-ups horen bij de betaalde abonnementen van Supabase; point-in-time recovery is een uitbreiding bij ondersteunde abonnementen; uw eigen exports kosten weinig aan opslag. Vergeleken met de kosten van het verliezen van klantgegevens behoren deze tot de goedkoopste beschermingen die er zijn.

## Een Hersteloefening die U Deze Week Kunt Doen

Blok een uur en volg deze stappen:

1. Noteer de tijd en kies een recente back-up of een tijdstip.
2. Maak een tijdelijk Supabase-project aan in dezelfde regio.
3. Zet de back-up daarin terug, of laad uw nieuwste eigen export met standaardtools van PostgreSQL.
4. Vergelijk het aantal rijen in uw vijf belangrijkste tabellen met productie.
5. Open drie recente records en controleer of ze kloppen.
6. Laat een lokale of stagingkopie van de app naar het tijdelijke project wijzen en log in als testgebruiker.
7. Noteer hoe lang het hele proces duurde en schrijf op wat onduidelijk was.
8. Verwijder het tijdelijke project en de data erin.

Dat uur maakt van uw back-up een geteste vaardigheid in plaats van een aanname, en de notities worden uw herstelhandleiding.

## Vragen die Klanten Stellen

Zakelijke klanten vragen vaak: Hoe vaak maakt u back-ups? Waar worden ze bewaard? Hoe lang worden ze bewaard? Wanneer heeft u voor het laatst een terugzetting getest? Hoe snel kunt u herstellen? Schriftelijke antwoorden hebben, onderbouwd met een echte hersteltest, geeft bij inkoop in de zorg, het onderwijs en B2B SaaS vaak de doorslag.

## Eigenaarschap van het Back-upproces

Iemand moet eigenaar zijn van de back-ups, ook in een bedrijf van twee personen. Die persoon controleert maandelijks of de back-ups draaien, elk kwartaal of een terugzetting werkt, en na elke grote wijziging of nieuwe tabellen en buckets worden gedekt. Schrijf zijn naam in uw beheerdocument. Back-ups zonder eigenaar stoppen vaak stilletjes; niemand merkt het tot de dag dat ze nodig zijn.

## Back-ups voor Apps op een Geïntegreerde Backend van een Builder

Als uw app draait op een geïntegreerde backend van een builder in plaats van op uw eigen Supabase-project, controleer dan welke opties voor back-ups en exports u heeft, hoe ver ze teruggaan en of u ze zelf kunt terugzetten. Als de antwoorden beperkt zijn en uw app belangrijke klantgegevens bevat, overweeg dan te verhuizen naar een project dat u zelf beheert, waar instellingen voor back-ups, point-in-time recovery en exports in uw handen liggen.

## Samenvatting

Ken uw RPO en RTO, gebruik beheerde back-ups plus uw eigen export, bescherm bestanden apart, houd back-ups veilig en in de EU, en test het terugzetten volgens een schema. Die vijf gewoonten dekken de overgrote meerderheid van de scenario's voor dataverlies waar oprichters mee te maken krijgen.

## Veelgemaakte Fouten bij Back-ups

- Productie draaien op een gratis abonnement zonder betekenisvolle garanties voor back-ups
- Aannemen dat databaseback-ups ook geüploade bestanden bevatten
- Uw eigen exports bewaren in hetzelfde account dat zou kunnen worden gecompromitteerd
- Nooit een back-up terugzetten tot er een noodgeval is
- Over live data heen terugzetten zonder eerst in een apart project te vergelijken
- Nieuwe tabellen of buckets vergeten die na het schrijven van het back-upplan zijn toegevoegd

## Het Resultaat

Een geteste back-up maakt van een mogelijke ramp een ongemak. Wanneer er een fout gebeurt - en in een groeiende app gebeurt dat uiteindelijk - zet u de getroffen records terug, informeert u wie dat moet weten en gaat u verder, in plaats van data opnieuw op te bouwen uit e-mails en geheugen.

## Nog Eén Gewoonte

Stel na elke grote release één vraag: als deze release de verkeerde data had verwijderd, hoe snel zouden we die dan terugkrijgen? Als het antwoord onduidelijk is, test het dan vóór de volgende release.

## Het Laten Regelen

LaunchStudio richt back-ups, exports buiten de deur en een hersteltest in als onderdeel van productielanceringen, en het Launch & Grow-pakket omvat beheerde hosting met automatische back-ups voor €49 per maand. Anders dan freelancers wordt LaunchStudio ondersteund door Manifera, vertrouwd door Vodafone, TNO en CFLW, waar getest herstel een contractuele verwachting is; zie [het portfolio van Manifera](https://www.manifera.com/portfolio/). Supabase documenteert [databaseback-ups](https://supabase.com/docs/guides/platform/backups) en PITR uitgebreid. Zie voor de rest van uw lancering onze [pagina over de productie-inrichting van Supabase](https://launchstudio.eu/nl/blog/supabase-developer-for-hire-production-setup-and-rls).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Volkstuinapp die een Seizoen Wiste

Henk Mol is voorzitter van een volkstuinvereniging in Zwolle en bouwde Tuinpad in Lovable: leden beheren tuinen, wachtlijsten, aanwezigheid bij werkdagen en jaarlijkse contributie. Terwijl hij voor het nieuwe seizoen testdata opruimde, vroeg hij Lovable "alle tuinen van vorig jaar te verwijderen". De gegenereerde SQL verwijderde elk tuinrecord, inclusief de huidige toewijzingen van 140 leden.

Het Supabase-project van Henk stond op het gratis abonnement. Er was geen back-up om terug te zetten. Hij besteedde drie weekenden aan het opnieuw opbouwen van de toewijzingen uit papieren administratie en e-mails van leden.

LaunchStudio zette het project over op een betaald abonnement met dagelijkse back-ups, voegde point-in-time recovery toe, richtte een nachtelijke versleutelde export in naar EU-opslag in een apart account, maakte back-ups van geüploade tuinfoto's en contributiebewijzen, en voerde samen met Henk een getimede hersteltest uit. Destructieve databaseacties werden verplaatst naar een beheerfunctie met bevestiging in plaats van vrije prompts.

**Resultaat:** Zes maanden later overschreef een vrijwilliger per ongeluk de wachtlijst. Die werd in minder dan twintig minuten teruggezet naar vijf minuten vóór de fout.

> *"Ik vroeg de AI op te ruimen en hij deed precies wat ik zei. Het probleem was dat niets het ongedaan kon maken."*
> - **Henk Mol, Oprichter, Tuinpad (Zwolle)**

**Kosten & Doorlooptijd:** €1.100 (Launch Ready-pakket: overstap naar een betaald abonnement, PITR, exports buiten de deur, back-ups van bestanden, hersteltest en veilige beheeracties) - afgerond in 4 werkdagen.

## Veelgestelde Vragen

### Maakt Lovable automatisch back-ups van mijn data?

Uw data staat in Supabase, dus back-ups hangen af van het Supabase-abonnement en de instellingen achter uw app. Gratis projecten bieden weinig bescherming. Controleer uw abonnement en richt back-ups in voordat echte gebruikers op de app vertrouwen.

### Wat is point-in-time recovery?

Met PITR zet u de database terug naar een specifiek moment, niet alleen naar de laatste dagelijkse back-up. Dat is waardevol als er overdag een fout gebeurt, zoals een bulkverwijdering of een foutieve migratie, en u minuten in plaats van uren wilt verliezen.

### Zitten geüploade bestanden in de databaseback-ups?

Nee. Bestanden in Supabase Storage staan los van de database. Maak er back-ups van met een eigen proces, of zorg in elk geval dat u de belangrijke bestanden kunt herstellen, zoals contracten of facturen.

### Hoe vaak moet ik het terugzetten van een back-up testen?

Minstens elk kwartaal, en na elke grote wijziging aan uw database-inrichting. De 11+ jaar beheer van Manifera laten zien dat ongeteste back-ups op het slechtste moment falen, vaak door ontbrekende rechten of onverwachte hersteltijden.

### Heeft dataverlies invloed op mijn online zichtbaarheid?

Dat kan. Verloren inhoud betekent kapotte pagina's, en een storing terwijl u opnieuw opbouwt betekent pagina's die zoekmachines en AI-assistenten niet kunnen bereiken. Snel herstel beperkt die schade.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Maakt Lovable automatisch back-ups van mijn data?",
      "acceptedAnswer": { "@type": "Answer", "text": "Back-ups hangen af van het Supabase-abonnement en de instellingen achter de app; gratis projecten bieden weinig bescherming." }
    },
    {
      "@type": "Question",
      "name": "Wat is point-in-time recovery?",
      "acceptedAnswer": { "@type": "Answer", "text": "De database terugzetten naar een specifiek moment, nuttig om na een fout minuten in plaats van uren te verliezen." }
    },
    {
      "@type": "Question",
      "name": "Zitten geüploade bestanden in de databaseback-ups?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. Bestanden in Supabase Storage hebben een eigen back-upproces nodig." }
    },
    {
      "@type": "Question",
      "name": "Hoe vaak moet ik het terugzetten van een back-up testen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Minstens elk kwartaal en na grote databasewijzigingen, omdat ongeteste back-ups vaak falen wanneer ze nodig zijn." }
    },
    {
      "@type": "Question",
      "name": "Heeft dataverlies invloed op mijn online zichtbaarheid?",
      "acceptedAnswer": { "@type": "Answer", "text": "Dat kan, via kapotte pagina's en storingen die crawlers niet kunnen bereiken; snel herstel beperkt de schade." }
    }
  ]
}
</script>
