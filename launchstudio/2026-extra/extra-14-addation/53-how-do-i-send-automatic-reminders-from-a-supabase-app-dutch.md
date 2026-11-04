---
Titel: "Hoe Verstuur Ik Automatische Herinneringen vanuit een Supabase-App?"
Trefwoorden: automatische herinneringen supabase, pg_cron supabase, geplande taken lovable, e-mailherinneringen ai-app, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Hoe Verstuur Ik Automatische Herinneringen vanuit een Supabase-App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Verstuur Ik Automatische Herinneringen vanuit een Supabase-App?",
  "description": "Afspraakherinneringen, verlengingsberichten en opvolgmails vragen om geplande taken. Deze gids laat zien hoe u betrouwbare herinneringen bouwt in een Lovable- of Bolt-app met Supabase, met pg_cron, edge functions, een tabel voor herinneringen, tijdzones en bescherming tegen dubbele berichten.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-01",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-do-i-send-automatic-reminders-from-a-supabase-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase Cron", "url": "https://supabase.com/docs/guides/cron" },
    { "@type": "CreativeWork", "name": "PostgreSQL documentation", "url": "https://www.postgresql.org/docs/current/ddl-rowsecurity.html" },
    { "@type": "CreativeWork", "name": "GDPR Article 28: Processor", "url": "https://gdpr-info.eu/art-28-gdpr/" },
    { "@type": "CreativeWork", "name": "Google SRE Book: Monitoring Distributed Systems", "url": "https://sre.google/sre-book/monitoring-distributed-systems/" }
  ]
}
</script>

**Kort antwoord:** plan met Supabase Cron (gebouwd op de extensie `pg_cron`) een taak die om de paar minuten draait en een edge function aanroept. Die functie zoekt de herinneringen op die verstuurd moeten worden, verstuurt ze via uw e-mail- of sms-provider en markeert elke herinnering als verzonden, zodat er nooit een twee keer uitgaat. Sla tijden op in UTC, reken om naar de tijdzone van de gebruiker voor weergave en planningslogica, en monitor dat de taak blijft draaien.

## Belangrijkste Punten

- **Betrouwbare herinneringen vragen om een outboxtabel, een planner en een idempotente verzender,** niet om een functie die binnen een webverzoek draait.
- **Supabase Cron, gebouwd op de extensie pg_cron van PostgreSQL,** kan edge functions volgens een schema starten.
- **Sla tijdstempels op in UTC en plan in de tijdzone van de gebruiker;** de wisseling naar zomer- en wintertijd in maart en oktober is een klassieke oorzaak van herinneringen die een uur verkeerd zitten.
- **Markeer herinneringen als in verwerking vóór het versturen,** om dubbelingen door overlappende runs of herhaalpogingen te voorkomen.
- **Monitor de planner zelf,** omdat geplande taken geruisloos falen.

## De Bouwstenen

| Onderdeel | Rol |
| --- | --- |
| Tabel `reminders` | Wat er verstuurd moet worden, aan wie, wanneer en of het verstuurd is |
| Supabase Cron-taak | Start de verwerking om de paar minuten |
| Edge function | Kiest herinneringen die aan de beurt zijn, verstuurt ze en legt de resultaten vast |
| E-mail-/sms-provider | Bezorgt het bericht |
| Monitoring | Waarschuwt als de taak stopt of mislukkingen zich opstapelen |

## Stap 1: Een Tabel voor Herinneringen

Kolommen zoals `id`, `user_id`, `type`, `send_at` (tijdstempel met tijdzone), `payload`, `status` (pending, sent, failed), `attempts` en `sent_at`. Wanneer een boeking wordt aangemaakt, voegt u de bijbehorende herinneringen toe, bijvoorbeeld 24 uur en 2 uur vooraf. Wordt de boeking geannuleerd of verplaatst, dan werkt u ze bij of annuleert u ze.

Deze "outbox"-aanpak is makkelijker te overzien dan herinneringen ter plekke berekenen, en geeft u een geschiedenis van wat er verstuurd is.

## Stap 2: Plan de Taak

Maak een cron-taak die elke vijf minuten draait en uw edge function aanroept. Bewaar de URL van de functie en een geheime header in de configuratie, zodat alleen de planner hem kan starten.

## Stap 3: Verwerk Veilig

De edge function:

1. Selecteert herinneringen met status pending waarvoor `send_at <= now()` geldt, in kleine batches
2. Markeert ze in dezelfde stap als in verwerking, zodat een parallelle run ze niet opnieuw oppakt
3. Verstuurt elk bericht via de provider, met een idempotentiesleutel waar die wordt ondersteund
4. Legt succes of mislukking vast, verhoogt het aantal pogingen en plant een nieuwe poging bij tijdelijke storingen

## Stap 4: Krijg Tijdzones Goed

Sla tijdstempels op met tijdzone, in UTC. Bepaal herinneringstijden in de tijdzone van de gebruiker ("9:00 de dag ervoor" betekent 9:00 in Amsterdam, niet in UTC). De wisseling naar zomer- en wintertijd in maart en oktober is een klassieke oorzaak van herinneringen die een uur verkeerd zitten.

## Stap 5: Respecteer de Ontvanger

- Neem alleen noodzakelijke details op; vermijd gevoelige informatie in sms'jes
- Bied een afmeldmogelijkheid voor herinneringen die niet essentieel zijn
- Verstuur 's nachts niets, tenzij de gebruiker daarom heeft gevraagd

## Stap 6: Monitor de Planner

Geplande taken falen geruisloos. Stuur een melding als er in de afgelopen 30 minuten geen taak heeft gedraaid of als het aantal mislukte herinneringen een drempel overschrijdt. Onze gids over [weten wanneer uw app uitvalt](https://launchstudio.eu/nl/blog/how-do-i-know-when-my-ai-built-app-goes-down) behandelt dit soort controles op stille storingen.

## Waarom Herinneringen Falen in AI-Gebouwde Apps

Gegenereerde code voor herinneringen neemt vaak shortcuts die in een demo werken: een timer in de browser, een controle die draait wanneer een pagina laadt, of een functie die elke minuut start en opnieuw berekent wie een bericht moet krijgen. Deze aanpakken breken in productie. Browsers worden gesloten, pagina's worden niet op het juiste moment geladen, functies overlappen elkaar, en niets legt vast wat al verstuurd is. Het resultaat is gemiste herinneringen, dubbele berichten of allebei. Een beetje structuur - een outbox, een planner en een verzender - lost alle drie op.

## Het Outbox-Patroon

Het outbox-patroon scheidt het bepalen van wat er verstuurd moet worden van het daadwerkelijke versturen. Wanneer er iets gebeurt, zoals het aanmaken van een boeking, schrijft u een of meer rijen naar een tabel met herinneringen, met het beoogde verzendtijdstip. Een apart proces verstuurt de herinneringen die aan de beurt zijn en legt het resultaat vast. Dit patroon heeft verschillende voordelen:

- Herinneringen overleven herstarts en deployments, omdat ze in de database staan
- U ziet precies wat er gepland staat en wat er verstuurd is
- Annuleren of verzetten is een update in de database
- Herhaalpogingen zijn expliciet en veilig
- Rapportages en audits krijgt u er gratis bij

## Tijdzones op de Juiste Manier

Sla alle tijdstempels op als `timestamp with time zone` in UTC. Sla de tijdzone van elke gebruiker of organisatie op, zoals `Europe/Amsterdam`. Wanneer u een herinnering berekent als "9:00 de dag vóór de afspraak", rekent u die uit in de tijdzone van de gebruiker en zet u hem voor opslag om naar UTC. De tijdzonefuncties van PostgreSQL gaan correct om met zomer- en wintertijd als u benoemde tijdzones gebruikt in plaats van vaste verschuivingen. Test herinneringen die vallen op de datums waarop de klok verzet wordt; daar zitten de bugs verstopt.

## Plannen met Supabase Cron

Met Supabase Cron plant u SQL of aanroepen van edge functions met bekende cron-expressies, zoals elke vijf minuten. Voor herinneringen is een gangbare opzet een taak elke vijf minuten die een verzendfunctie aanroept, die de herinneringen die aan de beurt zijn in kleine batches verwerkt. Bescherm de functie met een geheim, zodat alleen de planner hem kan aanroepen, en leg het schema vast in een migratie, zodat het in elke omgeving bestaat.

## Betrouwbaar Versturen

De verzendfunctie moet:

1. Een batch herinneringen selecteren die aan de beurt zijn en de status pending hebben
2. Ze in dezelfde transactie als in verwerking markeren, zodat een parallelle run ze overslaat
3. Elk bericht versturen via de e-mail- of sms-provider
4. Succes vastleggen met een tijdstempel, of mislukking met een foutmelding en het aantal pogingen
5. Tijdelijke mislukkingen met vertraging opnieuw inplannen, en na een vast aantal pogingen opgeven

Het gebruik van de idempotentiefuncties van de provider, waar beschikbaar, biedt extra bescherming tegen dubbelingen wanneer een netwerkfout een geslaagde verzending verbergt.

## Inhoud en Toestemming

Herinneringen zijn meestal transactioneel - ze gaan over een dienst waar de gebruiker om heeft gevraagd - en hebben daarom in het algemeen geen toestemming voor marketing nodig. Respecteer gebruikers toch: laat ze waar zinvol kanalen kiezen, vermijd gevoelige informatie in sms'jes, verstuur op redelijke tijden en bied afmeldmogelijkheden voor herinneringen die niet essentieel zijn. Onder de AVG zijn de telefoonnummers en e-mailadressen die u voor herinneringen gebruikt persoonsgegevens; neem uw berichtenproviders op in uw lijst van verwerkers.

## Sms Versus E-mail Versus Pushberichten

| Kanaal | Sterke punten | Aandachtspunten |
| --- | --- | --- |
| E-mail | Goedkoop, rijke inhoud, makkelijk te loggen | Wordt mogelijk laat gelezen of belandt in spam |
| Sms | Hoge openingspercentages, goed voor tijdkritische herinneringen | Kosten per bericht, beperkte inhoud, telefoonnummers zijn persoonsgegevens |
| Pushberichten | Direct, gratis per bericht | Vereist installatie van de app en toestemming |

Veel apps combineren ze: e-mail voor bevestigingen en samenvattingen, sms of pushberichten voor tijdkritische herinneringen.

## Gepland Werk Monitoren

Leg elke run van de planner vast met een tijdstempel. Stuur een melding als er in de afgelopen 30 minuten geen run was, als het aantal mislukkingen een drempel overschrijdt of als herinneringen met status pending zich opstapelen na hun verzendtijd. Zonder deze controles kan een kapotte planner onopgemerkt blijven tot klanten klagen over gemiste afspraken.

## Een Schema voor Herinneringen dat U Kunt Aanpassen

Een praktische tabel voor herinneringen bevat vaak: `id`, `organisation_id`, `user_id`, `related_type` en `related_id` (bijvoorbeeld een boeking), `channel` (e-mail, sms, push), `template`, `send_at` (UTC), `status` (pending, processing, sent, failed, cancelled), `attempts`, `last_error`, `sent_at` en `created_at`. Bescherm de tabel met Row Level Security, zodat gebruikers hun eigen geplande herinneringen kunnen zien als u die toont, terwijl alleen servercode de status kan wijzigen. Indexeer `status` en `send_at` samen, zodat de planner herinneringen die aan de beurt zijn snel vindt.

## Verzetten en Annuleren

Wanneer een boeking wordt verzet, werkt u de bijbehorende herinneringen met status pending bij in plaats van nieuwe aan te maken; wordt hij geannuleerd, dan markeert u ze als geannuleerd. Door dit in dezelfde transactie te doen als de wijziging van de boeking, blijven herinneringen in lijn met de werkelijkheid. Een veelvoorkomende bug in gegenereerde code is bij elke wijziging nieuwe herinneringen aanmaken, zodat klanten er een krijgen voor elke versie van de boeking.

## Herinneringen Testen

Test in staging met herinneringen die een paar minuten vooruit zijn gepland, waaronder één op een datum waarop de klok wordt verzet, één voor een geannuleerde boeking en één waarbij de provider tijdelijk onbereikbaar is. Controleer dat voor elk geldig geval precies één bericht op de juiste lokale tijd aankomt, geen enkel voor de geannuleerde boeking, en een geslaagde nieuwe poging na de storing.

## De Kern

Herinneringen lijken eenvoudig en falen geruisloos in veel AI-gebouwde apps. Een outboxtabel, een geplande verzender, correcte tijdzones, idempotent versturen en monitoring maken er een betrouwbare functie van waar klanten op kunnen rekenen.

## Verder dan Herinneringen: Ander Gepland Werk

Hetzelfde patroon werkt voor andere geplande taken: maandrapportages, berichten over aflopende proefperiodes, het opruimen van gegevens volgens bewaartermijnen, waarschuwingen voor verlengingen en nachtelijke synchronisaties. Gebruik één planner, één log voor taken en consistente monitoring voor al deze taken, in plaats van een ander mechanisme per functie. Wanneer iets stopt met draaien, weet u het direct en weet u waar u moet kijken.

## Kosten

Geplande functies en databaseopslag voor herinneringen kosten weinig. De grootste kosten zijn sms-tarieven, die per land en provider verschillen, en de tijd om het systeem goed in te richten. Vergeleken met de omzet die verloren gaat door gemiste afspraken of de supporttijd die opgaat aan dubbele berichten, verdient de investering zich voor de meeste boekings- en dienstverlenende bedrijven snel terug.

## Gerelateerde Onderwerpen

Herinneringen zijn afhankelijk van betrouwbare e-mailbezorging en van weten wanneer er iets kapotgaat. Onze gidsen over e-mails van Supabase die niet aankomen en over het monitoren van AI-gebouwde apps behandelen allebei.

## Vragen Voordat U Herinneringen Bouwt

Welke gebeurtenissen leiden tot herinneringen, en hoeveel per gebeurtenis? In welke tijdzones wonen uw gebruikers? Welke kanalen hebben klanten liever, en wat kost elk kanaal? Wat moet er gebeuren als een afspraak verandert of wordt geannuleerd? Hoe weet u het als herinneringen stoppen? Door deze vijf vragen eerst te beantwoorden, wordt de implementatie eenvoudig.

## Een Opmerking over Belasting

Als u duizenden herinneringen op hetzelfde moment verstuurt, zoals elke ochtend om 9:00, spreid ze dan over een paar minuten en verwerk ze in batches, om de rate limits van providers te respecteren en uw database responsief te houden.

## Samenvatting

Outboxtabel, geplande verzender, opslag in UTC, planning in lokale tijd, idempotent versturen en monitoring: zes ingrediënten voor herinneringen waar klanten op kunnen rekenen.

## Het Laten Bouwen

Herinneringen zijn een veelvoorkomende toevoeging van LaunchStudio aan boekings- en SaaS-apps, meestal twee tot vier dagen binnen een opdracht tegen vaste prijs. LaunchStudio wordt ondersteund door Manifera, dat al 11+ jaar planningssystemen bouwt voor enterprise- en logistieke klanten, met engineers in Ho Chi Minh-stad en klantcontact in Amsterdam; zie [het portfolio van Manifera](https://www.manifera.com/portfolio/). Supabase documenteert [Cron](https://supabase.com/docs/guides/cron) en het plannen van edge functions.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Rijschoolherinneringen die een Uur te Laat Kwamen

Kees Bakkenes runt een rijschool in Emmen met zes instructeurs en bouwde Rijlesrooster in Bolt: leerlingen boeken lessen, instructeurs beheren hun beschikbaarheid en iedereen ontvangt herinneringen per sms. In de winter werkten de herinneringen. Nadat de klok in maart was verzet, kwam elke herinnering een uur te laat, en sommige leerlingen misten hun les.

Bolt had een geplande functie gegenereerd die lokale tijden, opgeslagen als tekst, vergeleek met de UTC-tijd van de server. De functie draaide bovendien elke minuut en verstuurde herinneringen opnieuw als de sms-provider traag reageerde, waardoor sommige leerlingen hetzelfde bericht drie keer ontvingen. Toen de functie na een storing bij de provider faalde, merkte twee dagen lang niemand iets.

LaunchStudio maakte een tabel voor herinneringen met tijdstempels in UTC en planningslogica in Europe/Amsterdam, verplaatste de planning naar Supabase Cron met een run elke vijf minuten, maakte het versturen idempotent met het bijhouden van de status, en voegde nieuwe pogingen bij tijdelijke storingen en meldingen bij vastgelopen taken toe.

**Resultaat:** Tijdens de wisseling naar wintertijd in oktober en het jaar daarna kwamen herinneringen op tijd en zonder dubbelingen aan, en het aantal gemiste lessen daalde merkbaar volgens de rapportages van de instructeurs van Kees.

> *"De herinneringen werkten vijf maanden perfect. Toen werd de klok verzet, en de opkomst van mijn leerlingen ook."*
> - **Kees Bakkenes, Oprichter, Rijlesrooster (Emmen)**

**Kosten & Doorlooptijd:** €1.400 (Launch Ready-pakket: outbox voor herinneringen, planning met cron, oplossingen voor tijdzones, idempotentie, nieuwe pogingen en meldingen) - afgerond in 5 werkdagen.

## Veelgestelde Vragen

### Hoe plan ik taken in Supabase?

Gebruik Supabase Cron, dat voortbouwt op de Postgres-extensie `pg_cron`, om SQL uit te voeren of edge functions volgens een schema aan te roepen. Voor het versturen van e-mails of sms'jes roept de cron-taak meestal een edge function aan die het werk doet.

### Waarom worden mijn herinneringen twee keer verstuurd?

Meestal omdat overlappende runs dezelfde herinneringen oppakken, of omdat herhaalpogingen berichten opnieuw versturen die eigenlijk al waren bezorgd. Herinneringen als in verwerking markeren vóór het versturen en idempotentiesleutels gebruiken voorkomt dubbelingen.

### Waarom zitten mijn herinneringen een uur verkeerd?

Door de omgang met tijdzones. Lokale tijden opslaan zonder tijdzone-informatie, of UTC en lokale tijd door elkaar gebruiken, gaat mis rond de wisseling naar zomer- en wintertijd. Sla UTC op en plan in de tijdzone van de gebruiker.

### Hoe maakt Manifera geplande taken betrouwbaar?

Door ze te behandelen als gemonitorde infrastructuur: een outboxtabel, idempotente verwerking, nieuwe pogingen en meldingen bij vastgelopen taken. De 11+ jaar logistieke en planningssystemen van Manifera hebben deze patronen gevormd.

### Kunnen herinneringsmails mijn e-mailreputatie beïnvloeden?

Ja, positief of negatief. Gewenste herinneringen op het juiste moment vanaf een geauthenticeerd domein bouwen reputatie op. Dubbele berichten, berichten 's nachts en ontbrekende afmeldmogelijkheden leiden tot klachten die de reputatie schaden.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe plan ik taken in Supabase?",
      "acceptedAnswer": { "@type": "Answer", "text": "Gebruik Supabase Cron, gebouwd op pg_cron, om SQL uit te voeren of edge functions volgens een schema aan te roepen." }
    },
    {
      "@type": "Question",
      "name": "Waarom worden mijn herinneringen twee keer verstuurd?",
      "acceptedAnswer": { "@type": "Answer", "text": "Overlappende runs of herhaalpogingen versturen opnieuw; markeer herinneringen als in verwerking en gebruik idempotentiesleutels." }
    },
    {
      "@type": "Question",
      "name": "Waarom zitten mijn herinneringen een uur verkeerd?",
      "acceptedAnswer": { "@type": "Answer", "text": "Door de omgang met tijdzones rond zomer- en wintertijd; sla UTC op en plan in de tijdzone van de gebruiker." }
    },
    {
      "@type": "Question",
      "name": "Hoe maakt Manifera geplande taken betrouwbaar?",
      "acceptedAnswer": { "@type": "Answer", "text": "Met een outboxtabel, idempotente verwerking, nieuwe pogingen en meldingen bij vastgelopen taken." }
    },
    {
      "@type": "Question",
      "name": "Kunnen herinneringsmails mijn e-mailreputatie beïnvloeden?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Goed getimede, geauthenticeerde herinneringen bouwen reputatie op; dubbelingen en ontbrekende afmeldmogelijkheden schaden die." }
    }
  ]
}
</script>
