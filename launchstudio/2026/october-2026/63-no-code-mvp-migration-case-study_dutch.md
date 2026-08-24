---
Titel: "Case Study: Een No-Code MVP Migreren naar Productie-architectuur in 12 Dagen"
Keywords: no-code MVP migratie, Bubble naar productie, productie-architectuur, LaunchStudio, Manifera, Row Level Security, Stripe webhooks, databasemigratie, Herre Roelevink
Buyer Stage: Decision
---

# Case Study: Een No-Code MVP Migreren naar Productie-architectuur in 12 Dagen

Noor had 340 betalende gebruikers op een abonnementsapp voor maaltijdplanning, volledig gebouwd in Bubble, en ze durfde er niet meer aan te komen. Elke paginalading duurde vier seconden langer dan zou moeten. Haar Bubble-workflow-logs toonden database-query's die tijdens de drukke avonduren — precies wanneer maaltijdplanners de app daadwerkelijk openen — een time-out gaven. Supporttickets over "de app blijft maar draaien" waren veranderd van incidenteel naar dagelijks. Ze wist dat het platform zijn fundament was ontgroeid, maar ze wist ook dat "van no-code af" het soort project was dat gemakkelijk drie maanden kon duren en alles kon breken wat op dat moment werkte. Hier is precies hoe een migratie van 12 dagen, van een no-code MVP naar productie-architectuur, er stap voor stap uitziet, en waarom het niet nodig was het product dat haar gebruikers al kenden weg te gooien.

## Waarom no-code MVP's tegen een muur aanlopen bij schaal

Bubble is, net als andere no-code- en low-code-platforms, oprecht uitstekend in waar het voor gebouwd is: een idee omzetten in een werkend, testbaar product zonder code te schrijven. Noor had haar hele businessmodel — het genereren van maaltijdplannen, boodschappenlijst-exports, een abonnementsbetaalmuur — binnen ongeveer zes weken gevalideerd in Bubble, sneller dan bijna elke maatwerkbouw had kunnen bereiken. De muur waar ze bij 340 gebruikers tegenaan liep, was geen falen van Bubble; het was het voorspelbare plafond dat no-code-platforms bereiken zodra echt gelijktijdig verkeer, complexe relationele data en aangepaste bedrijfslogica ontgroeien wat een visuele workflow-builder is ontworpen te optimaliseren. De database van Bubble is een algemene objectopslag, afgestemd op flexibiliteit, niet op het soort geïndexeerde, relationele query's die een maaltijdplanningsapp nodig heeft zodra deze recepten, dieetbeperkingen en weekplannen voor honderden gelijktijdige gebruikers kruisverwijst. Workflows die milliseconden kostten bij 20 testgebruikers begonnen seconden te kosten bij 340 echte gebruikers, en er was geen voor de hand liggende hendel meer binnen het platform om aan te trekken.

## Dag 1–2: Audit en architectuurplan

De engineers van LaunchStudio begonnen met het volledig in kaart brengen van Noors Bubble-datastructuur — elk datatype, elk veld, elke workflow die de database aanraakte — in plaats van te gokken naar wat belangrijk was. Deze stap is belangrijker dan hij klinkt: een overhaaste migratie die één workflow-afhankelijkheid mist, is hoe founders eindigen met een "succesvolle" migratie die stilletjes een functie breekt die niemand heeft getest. De audit bracht drie specifieke knelpunten aan het licht: niet-geïndexeerde lookups in de receptmatching-workflow, een checkout-flow die de ingebouwde Stripe-plugin van Bubble gebruikte zonder server-side webhook die de betaling bevestigde, en nul toegangscontrole op databaseniveau — elke ingelogde gebruiker kon in principe de opgeslagen maaltijdplannen van een andere gebruiker opvragen via een gemanipuleerde API-aanroep, omdat Bubbles privacyregels losjes waren geconfigureerd op typeniveau in plaats van per record.

Met de audit voltooid, bepaalde het team de doelarchitectuur: een PostgreSQL-database op Supabase om Bubbles interne dataopslag te vervangen, Row Level Security-beleid om databasegebonden data-isolatie per gebruiker af te dwingen, een ondertekende Stripe-webhook om de plugin-gebaseerde checkout te vervangen, en een Next.js-frontendlaag om de pagina's te vervangen die het zwaarst leunden op databaseprestaties — terwijl Noors bestaande ontwerp, paginalay-outs en gebruikersstromen precies behouden bleven zoals haar 340 gebruikers ze al kenden.

## Dag 3–6: De databasemigratie

Dit was de fase met het hoogste risico, en degene die de meeste no-code-migraties verkeerd doen door te haasten. Engineers exporteerden Noors volledige Bubble-dataset — recepten, gebruikersprofielen, maaltijdplannen, abonnementsgegevens — en koppelden elk Bubble-datatype aan een correct genormaliseerd PostgreSQL-schema, waarbij foreign keys en indexen werden toegevoegd op plekken waar Bubbles platte structuur die niet had. De receptmatching-workflow, die bij elk verzoek een niet-geïndexeerde volledige scan draaide over elk recept in de database, ging van een gemiddelde responstijd van 4,2 seconden naar minder dan 200 milliseconden zodra hij tegen geïndexeerde Postgres-tabellen draaide.

De migratie liep parallel met de live Bubble-app in plaats van als een harde overstap: een staging-Supabase-instantie ontving een volledige datasynchronisatie, en het team valideerde rijenaantallen, relatie-integriteit, en controleerde steekproefsgewijs individuele gebruikersaccounts tegen de live app voordat er iets aan de productie werd geraakt. Dit is de stap die van een risicovolle migratie een saaie migratie maakt — parallel valideren betekent dat een fout wordt opgevangen op een staging-database, niet voor de ogen van 340 betalende gebruikers midden in de migratie.

## Dag 7–9: Beveiliging en betalingen verharden

Met het datamodel op zijn plaats implementeerden engineers Row Level Security-beleid, gekoppeld aan `auth.uid()`, op elke tabel met gebruikersdata, waardoor het toegangscontrolehiaat dat de audit had gevonden werd gedicht. Een query voor de maaltijdplannen van één gebruiker wordt nu geweigerd op databaseniveau als deze niet overeenkomt met de geauthenticeerde sessie — niet weggefilterd door applicatielogica die een bug zou kunnen omzeilen, maar structureel onmogelijk, ongeacht wat de frontend verstuurt.

De Stripe-integratie werd herbouwd rond een ondertekende backend-webhook met idempotentie-afhandeling, ter vervanging van Bubbles plugin-gebaseerde checkout, die geen server-side bevestigingsstap had. Noors abonnementsfacturatie was stilletjes kwetsbaar geweest voor hetzelfde falen dat Bubble-apps vaak treft: de kaart van een gebruiker wordt succesvol belast, maar als de browser zijn retourtraject naar de servers van Bubble niet voltooit, wordt het abonnementsrecord nooit geactiveerd. De nieuwe webhook luistert rechtstreeks naar het server-to-server-event van Stripe, zodat een weggevallen verbinding een betalende klant niet langer kan scheiden van de toegang waarvoor hij heeft betaald.

## Dag 10–12: Frontendintegratie, testen en overstap

In plaats van Noors UI te herbouwen, herbouwden engineers alleen de datafetch-laag eronder — waarbij de interne API-aanroepen van Bubble werden vervangen door aanroepen naar de nieuwe Supabase-backend, terwijl haar bestaande paginalay-outs, branding en gebruikersstromen onaangeroerd bleven. Sentry werd geïnstalleerd over de volledige nieuwe stack, zodat elke fout na de migratie onmiddellijk zichtbaar zou worden met een stacktrace, niet als een stille storing. Het team voerde een volledige regressietest uit over elke kernworkflow — het genereren van maaltijdplannen, boodschappenlijst-export, abonnementscheckout, accountinstellingen — voordat de overstap werd gepland voor een periode met weinig verkeer, waarbij de oude Bubble-instantie 48 uur na livegang live en ongewijzigd bleef staan als terugvaloptie.

## Het resultaat

Noors app draait nu op productieklare architectuur: geïndexeerde PostgreSQL in plaats van Bubbles interne opslag, door RLS afgedwongen data-isolatie in plaats van privacyregels op typeniveau, een ondertekende Stripe-webhook in plaats van een client-side plugin-flow, en Sentry-monitoring in plaats van stille storingen. De gemiddelde paginalaadtijd tijdens drukke avonduren daalde van 4,8 seconden naar 640 milliseconden. Supporttickets over trage laadtijden of blijvend draaiende schermen daalden naar nul in de eerste twee weken na de migratie. En omdat de frontendlaag werd herbouwd rond haar bestaande ontwerp in plaats van vervangen, hoefden haar 340 bestaande gebruikers het product nooit opnieuw te leren — voor hen werd de app gewoon plotseling snel.

## Wat deze migratie niet vereiste

Het is de moeite waard om expliciet te benoemen wat een productiemigratie zoals deze niét nodig heeft, omdat de angst om "alles weg te gooien" meestal is wat founders ervan weerhoudt om te beginnen. Noor hoefde haar UI niet te herbouwen, haar gebruikers niet opnieuw te trainen, geen parallelle productlancering te draaien, of nieuwe aanmeldingen te pauzeren tijdens de overgang. Ze hoefde zelf geen PostgreSQL, RLS-beleidssyntax of webhook-handtekeningverificatie te leren. De volledige migratie liep onder het product dat haar gebruikers al open hadden staan in hun browser, met een ingebouwd terugvalvenster, juist zodat "in productie" nooit "onomkeerbaar" betekende.

## Belangrijkste inzichten

- No-code-platforms zoals Bubble zijn oprecht effectief voor het valideren van een MVP, maar hun algemene dataopslag loopt tegen een prestatiemuur zodra echt gelijktijdig verkeer en relationele query's verder schalen dan waarvoor een visuele workflow-builder is geoptimaliseerd.
- Een overhaaste migratie die een volledige workflow-audit overslaat, is hoe founders eindigen met een "succesvolle" migratie die stilletjes een ongeteste functie breekt — eerst elk datatype en elke afhankelijkheid in kaart brengen is wat de rest van de tijdlijn voorspelbaar maakt.
- Parallel migreren — synchroniseren naar een staging-database en rijenaantallen en relaties valideren vóór de overstap — maakt van een risicovolle migratie een saaie, waarbij fouten worden opgevangen voordat ze betalende gebruikers bereiken.
- Row Level Security en ondertekende Stripe-webhooks dichten de twee meest voorkomende productiehiaten in zowel no-code- als AI-gegenereerde apps: data-isolatie op databaseniveau en betalingsbevestiging die niet afhankelijk is van een verbonden blijvende browser van de klant.
- Een volledige migratie van een no-code-platform vereist, mits correct uitgevoerd, geen herbouw van de frontend of het pauzeren van het bedrijf — Noors migratie van 12 dagen liep onder een live product met 340 betalende gebruikers en een ingebouwd terugvalvenster van 48 uur.

## Klaar om van No-Code af te stappen zonder opnieuw te beginnen

Als uw no-code MVP zijn fundament is ontgroeid, is de oplossing een migratieplan met een terugvalvenster — geen herbouw van drie maanden.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 en geleid door Oprichter & Managing Director **Herre Roelevink**. Zoals Roelevink het verwoordt: *"We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot wasdom te brengen. Wij hebben elf jaar ervaring in precies dat vakgebied."* Door "Nederlands management te combineren met Vietnamees meesterschap", onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420), een Aziatische hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minh-stad, Vietnam** (Pho Quang Street). Via LaunchStudio migreren senior engineeringteams uw no-code- of AI-gegenereerde MVP naar productieklare architectuur — geïndexeerde databases, afgedwongen Row Level Security, ondertekende betalingswebhooks en echte monitoring — doorgaans binnen 1 tot 3 weken, zonder een herontwerp af te dwingen dat uw bestaande gebruikers opnieuw zouden moeten leren. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact) of bekijk hoe het [maatwerk software-ontwikkelteam van Manifera](https://www.manifera.com/services/custom-software-development/) grootschaligere platformmigraties plant.

## Echt voorbeeld

### Een AI-native oprichter in actie: De fitnesscoaching-marktplaats

Elin bouwde een marktplaats die freelance fitnesscoaches koppelt aan klanten met **Replit Agent**, met daarbovenop AI-gegenereerde matching van trainingsplannen op een Supabase-backend. Het prototype werkte goed genoeg om in de eerste maand 60 coaches aan boord te krijgen, maar Elin merkte een patroon op in haar Stripe-dashboard: coaches werden uitbetaald voor sessies die klanten hadden geannuleerd, omdat haar annuleringslogica volledig client-side draaide en geen server-side controle had tegen de daadwerkelijke belastingstatus van Stripe voordat een uitbetaling werd geactiveerd.

Ze nam contact op met **LaunchStudio (door Manifera)** voordat de discrepantie groot genoeg werd om haar marges te bedreigen. Engineers ontdekten dat Replit Agent de uitbetalingslogica had opgezet om alleen te activeren op basis van een database-vlag, zonder webhook die verifieerde dat de onderliggende belasting daadwerkelijk was afgehandeld en niet was terugbetaald. Het team herbouwde de flow rond een ondertekende Stripe-webhook die de live belastingstatus controleert voordat een uitbetaling plaatsvindt, en voegde een reconciliatietaak toe die elke discrepantie tussen geregistreerde sessies en daadwerkelijke Stripe-events markeert voor handmatige controle.

**Resultaat:** Geen enkele onjuiste uitbetaling in de acht weken na de fix, en Elin heeft nu een geautomatiseerd reconciliatierapport in plaats van wekelijks handmatig haar Stripe-dashboard te controleren.

**Kosten & Doorlooptijd:** €1.900 (Launch & Grow Pakket) — voltooid in 7 werkdagen.

---

---

---
## Veelgestelde Vragen

### Waarom werd een Bubble-app langzamer naarmate het meer gebruikers kreeg?
De interne database van Bubble is een algemene objectopslag, geoptimaliseerd voor flexibiliteit tijdens snelle prototyping, niet voor de geïndexeerde, relationele query's die een data-intensieve app op schaal nodig heeft. Workflows die instant draaien tegen een handvol testrecords, kunnen veranderen in meerdere-seconden-durende volledige tabelscans zodra echte gebruikersdata en gelijktijdig verkeer toenemen, omdat er binnen de ingebouwde datalaag van het platform geen equivalent bestaat voor aangepaste indexering of query-optimalisatie.

### Betekent overstappen van Bubble dat de hele app vanaf nul moet worden herbouwd?
Nee. In Noors geval werden alleen de datalaag en de backendlogica herbouwd — haar paginalay-outs, branding en gebruikersstromen bleven precies zoals haar bestaande gebruikers ze kenden. De migratie verving wat zich onder de interface bevond (de database, betalingsbevestiging en toegangscontrole) zonder een herontwerp te vereisen of gebruikers te dwingen het product opnieuw te leren.

### Hoe risicovol is het migreren van de database van een live app met betalende gebruikers?
Het risico komt bijna volledig voort uit het overslaan van validatiestappen, niet uit de migratie zelf. Het parallel draaien van de nieuwe database met de live app, het eerst synchroniseren en valideren van data op een staging-omgeving, en het live houden van het oude systeem als terugvaloptie gedurende een bepaalde periode na de overstap zijn wat een live databasemigratie verandert van een hoogrisico-gebeurtenis in een routinematige.

### Wat is het verschil tussen dit soort migratie en wat LaunchStudio doet voor AI-builder-prototypes zoals Lovable of Bolt?
Het onderliggende doel is hetzelfde — productieklare beveiliging, betrouwbare betalingen en echte monitoring — maar het uitgangspunt verschilt. Een Lovable- of Bolt-prototype heeft al een echte codebase en vaak een Supabase-database die alleen verharding nodig heeft (RLS, webhooks, geheimen). Een no-code-platform zoals Bubble vereist eerst een extra stap: het migreren van de data en logica uit de proprietaire omgeving van het no-code-platform naar een standaard, codegebaseerde architectuur voordat hetzelfde hardingswerk kan plaatsvinden.

### Hoe lang duurt een no-code-migratie zoals deze doorgaans?
Noors migratie duurde 12 werkdagen, inclusief audit, databasemigratie, beveiligings- en betalingsverharding en frontendintegratie met een ingebouwd terugvalvenster. Doorlooptijden variëren met de complexiteit van het bestaande datamodel en het aantal workflows dat de database aanraakt, maar de meeste no-code-naar-productie-migraties voor een app in MVP-fase vallen binnen een bereik van 1 tot 3 weken onder het Launch & Grow-pakket van LaunchStudio.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom werd een Bubble-app langzamer naarmate het meer gebruikers kreeg?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De interne database van Bubble is een algemene objectopslag, geoptimaliseerd voor flexibiliteit tijdens snelle prototyping, niet voor de geïndexeerde, relationele query's die een data-intensieve app op schaal nodig heeft. Workflows die instant draaien tegen een handvol testrecords, kunnen veranderen in meerdere-seconden-durende volledige tabelscans zodra echte gebruikersdata en gelijktijdig verkeer toenemen, omdat er binnen de ingebouwde datalaag van het platform geen equivalent bestaat voor aangepaste indexering of query-optimalisatie."
      }
    },
    {
      "@type": "Question",
      "name": "Betekent overstappen van Bubble dat de hele app vanaf nul moet worden herbouwd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. In Noors geval werden alleen de datalaag en de backendlogica herbouwd — haar paginalay-outs, branding en gebruikersstromen bleven precies zoals haar bestaande gebruikers ze kenden. De migratie verving wat zich onder de interface bevond (de database, betalingsbevestiging en toegangscontrole) zonder een herontwerp te vereisen of gebruikers te dwingen het product opnieuw te leren."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe risicovol is het migreren van de database van een live app met betalende gebruikers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het risico komt bijna volledig voort uit het overslaan van validatiestappen, niet uit de migratie zelf. Het parallel draaien van de nieuwe database met de live app, het eerst synchroniseren en valideren van data op een staging-omgeving, en het live houden van het oude systeem als terugvaloptie gedurende een bepaalde periode na de overstap zijn wat een live databasemigratie verandert van een hoogrisico-gebeurtenis in een routinematige."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het verschil tussen dit soort migratie en wat LaunchStudio doet voor AI-builder-prototypes zoals Lovable of Bolt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het onderliggende doel is hetzelfde — productieklare beveiliging, betrouwbare betalingen en echte monitoring — maar het uitgangspunt verschilt. Een Lovable- of Bolt-prototype heeft al een echte codebase en vaak een Supabase-database die alleen verharding nodig heeft (RLS, webhooks, geheimen). Een no-code-platform zoals Bubble vereist eerst een extra stap: het migreren van de data en logica uit de proprietaire omgeving van het no-code-platform naar een standaard, codegebaseerde architectuur voordat hetzelfde hardingswerk kan plaatsvinden."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt een no-code-migratie zoals deze doorgaans?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Noors migratie duurde 12 werkdagen, inclusief audit, databasemigratie, beveiligings- en betalingsverharding en frontendintegratie met een ingebouwd terugvalvenster. Doorlooptijden variëren met de complexiteit van het bestaande datamodel en het aantal workflows dat de database aanraakt, maar de meeste no-code-naar-productie-migraties voor een app in MVP-fase vallen binnen een bereik van 1 tot 3 weken onder het Launch & Grow-pakket van LaunchStudio."
      }
    }
  ]
}
</script>
