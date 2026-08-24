---
Titel: "Case Study: Hoe een Fintech-oprichter Stripe-betalingen in 9 Dagen Beveiligde"
Keywords: Fintech Beveiliging, Stripe Connect, Webhook Handtekeningverificatie, Row Level Security, B2B Facturatie SaaS, LaunchStudio, Manifera, Herre Roelevink, Bolt, Betalingsbeveiliging
Buyer Stage: Decision
---

# Case Study: Hoe een Fintech-oprichter Stripe-betalingen in 9 Dagen Beveiligde

Toen Daniel Osei begon met het bouwen van een B2B-facturatie- en betalingsplatform, bouwde hij geen to-do-lijst-app of een contenttool. Hij bouwde iets dat echt geld zou verplaatsen tussen echte bedrijven, echte bankgegevens zou bevatten, en precies in een categorie viel — fintech — waar één enkel beveiligingsfalen niet alleen gênant is voor een founder, maar een bedrijf kan beëindigen en gebruikers blootstelt aan reëel financieel nadeel. Dit is het verhaal van wat er mis was met zijn door AI gebouwde prototype, waarom dat specifiek gevaarlijk was gezien wat het product daadwerkelijk deed, en het gerichte engineeringtraject van negen dagen dat het veranderde in iets dat veilig genoeg was om aan betalende klanten voor te leggen.

## Het probleem

Daniel gebruikte Bolt om de kern van zijn platform te bouwen: een facturatietool waarmee kleine bedrijven facturen konden opstellen, betalingen van klanten konden ontvangen en — cruciaal — uitbetalingen konden splitsen over meerdere partijen met behulp van Stripe Connect, zodat een bureau een klant kon factureren en automatisch een percentage kon doorsluizen naar een onderaannemer zonder handmatige bankoverschrijvingen. In een demo zag het er naadloos uit. Eronder werd het bij elkaar gehouden door precies het patroon dat keer op keer opduikt in door AI gegenereerde fintech-prototypes.

De logica voor betalingsbevestiging draaide volledig op de frontend. Wanneer een klant een factuur betaalde, stuurde de browser onmiddellijk door naar een scherm "betaling ontvangen" zodra de Stripe-checkout aan de kant van de klant was voltooid — maar niets op Daniels server verifieerde onafhankelijk of de betaling daadwerkelijk was verwerkt, of dat de fondsen daadwerkelijk waren geïnd in plaats van slechts geautoriseerd. Er was helemaal geen webhook-listener, laat staan een die de handtekening van Stripe verifieerde om te bevestigen dat het event daadwerkelijk van Stripe afkomstig was en niet van een vervalst verzoek. Iedereen die de URL-structuur begreep, kon in theorie het "succes"-endpoint rechtstreeks aanroepen en een factuur als betaald markeren zonder ook maar iets te betalen.

Daaronder zat iets nog ergers. Row Level Security op de Supabase-database was wel opgezet in het schema, maar nooit ingeschakeld — precies het patroon dat opduikt in een groot deel van de door AI gegenereerde backends. Elke factuur, elk gekoppeld bankgegeven en elk klantcontact was technisch opvraagbaar door elke geauthenticeerde gebruiker, niet alleen het account waaraan het toebehoorde. Voor een notitie-app is dat een privacyblunder. Voor een platform dat de bank- en uitbetalingsgegevens van bedrijven bevat, was het een directe route waarlangs de ene klant de financiële gegevens van een andere klant kon inzien.

En in de client-side JavaScript-bundel, zichtbaar voor iedereen die de developer console van zijn browser opende, stonden de geheime Stripe-sleutel en de API-credentials die Daniels app gebruikte om namens gebruikers de Connect-API van Stripe aan te roepen. Een sleutel met dat toegangsniveau, blootgesteld in de browser, is geen theoretisch risico — het is een openstaande uitnodiging voor iemand om programmatisch uitbetalingen aan te maken of data op te halen met Daniels eigen live credentials.

## Het risico van fintech verkeerd doen

Elk door AI gebouwd prototype heeft baat bij goede beveiligingsverharding, maar de inzet schaalt rechtstreeks mee met wat de app daadwerkelijk aanraakt. Een kapot RLS-beleid op een app voor het delen van recepten is slechte praktijk. Een kapot RLS-beleid op een platform met gekoppelde bankrekeningnummers, uitbetalingsgeschiedenissen en fiscale bedrijfsgegevens is een geheel andere categorie probleem — één die kan leiden tot regelgevende blootstelling, het vertrouwen kan vernietigen waar een financieel product op leunt om überhaupt te kunnen bestaan, en in het slechtste geval kan resulteren in echt geld dat naar de verkeerde partij gaat zonder mogelijkheid tot terugdraaien.

Daniel begreep dit instinctief, en precies daarom wachtte hij niet af. Hij had acht weken runway gepland om zijn eerste groep bureauklanten aan boord te krijgen, die allemaal vanaf week één echte bankrekeningen zouden koppelen en echte klantbetalingen zouden verwerken. Lanceren met blootgestelde Stripe-sleutels en uitgeschakelde RLS was geen risico dat hij bereid was te nemen met het geld van anderen, en hij nam contact op met LaunchStudio voordat er ook maar één betalende klant het platform had aangeraakt.

## De oplossing in 9 dagen

De engineers van LaunchStudio begonnen met het precies in kaart brengen van wat Daniels met Bolt gebouwde frontend aanriep en verwachtte, zodat het verhardingswerk eronder kon plaatsvinden zonder dat hij het facturatiedashboard, de klantgerichte betalingspagina's of enige van de workflows die zijn ontwerp al goed afhandelde, opnieuw hoefde te bouwen.

**Dag 1–2: Audit en dreigingsinventarisatie.** Het team volgde elk pad waarlangs geld of gevoelige financiële data door de app bewoog — de factuuraanmaakflow, de Stripe Connect-onboarding voor onderaannemers, de logica voor het splitsen van uitbetalingen en elke Supabase-tabel die bankgegevens of klantgegevens aanraakte. Dit leverde een precieze lijst op van wat er moest worden gerepareerd, nog voordat er een enkele regel nieuwe code werd geschreven.

**Dag 3–5: Row Level Security, correct afgebakend.** Engineers implementeerden RLS-beleid dat niet alleen was gekoppeld aan `auth.uid()`, maar ook aan de accountrol — want Daniels platform had meerdere gebruikerstypen (bureau-eigenaren, onderaannemers en klanten) die elk verschillende, deels overlappende delen van dezelfde factuurdata moesten kunnen zien. Een onderaannemer moest inzicht hebben in zijn eigen uitbetalingsgeschiedenis maar verder niets; een bureau-eigenaar moest inzicht hebben in facturen die hij had uitgegeven, maar niet in de boeken van een ander bureau. Dit goed doen betekende beleidsregels schrijven die zowel identiteit als rol controleerden bij elke query, getest tegen realistische scenario's waarin een verkeerd beleid ofwel data zou lekken ofwel stilletjes een legitieme functie zou breken.

**Dag 6–7: Ondertekende Stripe-webhooks met idempotentie.** Het team bouwde een speciaal, server-side webhook-endpoint dat bij elk binnenkomend event de handtekening van Stripe verifieert, zodat vervalste verzoeken worden geweigerd voordat ze de database ooit bereiken. De betalingsstatus wordt nu alleen bijgewerkt wanneer Stripe's eigen servers bevestigen dat een betaling is verwerkt — nooit door een client-side redirect. Er werd idempotentie-afhandeling toegevoegd zodat, wanneer Stripe een webhook-aflevering opnieuw probeert (wat routinematig gebeurt als onderdeel van Stripe's eigen betrouwbaarheidsgaranties), de app een uitbetaling of betaling niet dubbel verwerkt.

**Dag 8: Geheimenbeheer via Edge Functions.** De blootgestelde geheime Stripe-sleutel en de Connect API-credentials werden volledig uit de client-side bundel gehaald en verplaatst naar Supabase Edge Functions, waar ze nooit naar de browser worden verzonden. Alle aanroepen naar de Stripe Connect-API — het aanmaken van uitbetalingssplitsingen, het controleren van accountstatus, het uitvoeren van transfers — verlopen nu via deze server-side functies in plaats van rechtstreeks vanuit client-code te worden aangeroepen.

**Dag 9: Monitoring en eindverificatie.** Sentry werd gekoppeld aan zowel de frontend als de nieuwe backend-functies, zodat elke storing in de webhook-pipeline, een uitbetalingssplitsing of een RLS-gescopede query onmiddellijk zichtbaar wordt met een volledige stacktrace, in plaats van stilletjes te falen op een manier die niemand opmerkt totdat een klant klaagt. Het team voerde een volledige testronde uit met testtransacties voor elke gebruikersrol om te bevestigen dat het nieuwe RLS-beleid exact zo functioneerde als bedoeld, voordat het platform aan Daniel werd teruggegeven.

## Het resultaat

Negen werkdagen nadat Daniel voor het eerst contact opnam, verwerkte zijn facturatieplatform zijn eerste live batch echte transacties van zijn startgroep bureauklanten — waarbij elke betalingsbevestiging afkomstig was van een geverifieerde Stripe-webhook, elke factuur en elk bankgegeven alleen zichtbaar was voor het account waartoe het behoorde, en er nergens credentials te vinden waren die de dev-tools van een browser konden bereiken. Het onboardingproces verliep precies zoals gepland, waarbij bureaus vanaf week één echte Stripe Connect-accounts koppelden en echte facturen uitgaven, zonder een enkel incident van datablootstelling of uitbetalingsfout in de weken die volgden.

Net zo belangrijk: Daniel kon zijn beveiligingsniveau nu accuraat beschrijven aan potentiële klanten — een niet te onderschatten voordeel bij fintech-verkoop, waar zakelijke inkopers routinematig scherpe vragen stellen over hoe hun bankgegevens worden beschermd voordat ze zich aanmelden. Verifieerbare antwoorden hebben, onderbouwd door daadwerkelijke server-side handhaving in plaats van beloftes, verkortte zijn verkoopgesprekken aanzienlijk.

## Belangrijkste inzichten

- Fintech-producten hebben een categorisch hogere inzet dan typische SaaS-apps — een uitgeschakeld RLS-beleid of een niet-geverifieerde webhook is niet zomaar een bug, het is een directe route naar blootstelling van financiële data of betalingsfraude.

- Betalingsbevestiging aan de frontend alleen is nooit voldoende voor het verplaatsen van echt geld; een ondertekende, idempotente, server-side Stripe-webhook is de enige betrouwbare bron van waarheid over of een betaling daadwerkelijk is verwerkt.

- Row Level Security moet zowel op identiteit als op rol worden afgebakend bij platforms met meerdere partijen — een beleid dat alleen `auth.uid()` controleert, volstaat niet wanneer verschillende accounttypen verschillende, overlappende zichtbaarheid nodig hebben op dezelfde data.

- Blootgestelde API-sleutels in client-side code zijn bijzonder gevaarlijk voor platforms die Stripe Connect gebruiken, omdat een gelekte sleutel kan worden gebruikt om programmatisch uitbetalingen te initiëren, niet alleen om data te lezen.

- Een gericht engineeringtraject van negen dagen was genoeg om Daniels platform te verplaatsen van een lanceringsblokkerend risico naar productieklaar, zonder dat zijn bestaande met Bolt gebouwde frontend opnieuw hoefde te worden gebouwd.

## Maak uw fintech-prototype productieklaar

Laat gaten in betalingslogica of data-isolatie niet de reden zijn dat uw fintech-lancering misgaat.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 en geleid door Oprichter & Managing Director **Herre Roelevink**. Zoals Roelevink het verwoordt: *"We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot wasdom te brengen. Wij hebben elf jaar ervaring in precies dat vakgebied."* Door "Nederlands management te combineren met Vietnamees meesterschap", onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420), een Aziatische hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minh-stad, Vietnam** (Pho Quang Street). Via LaunchStudio nemen senior engineeringteams uw bestaande door AI gebouwde frontend en implementeren ze productieklare beveiligingscontroles, ondertekende betalingswebhooks, veilige hosting en monitoring — waardoor uw prototype binnen 1 tot 3 weken verandert in een veilige, audit-klare MVP, zonder rebuild. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact) of bekijk hoe het [maatwerk software-ontwikkelteam van Manifera](https://www.manifera.com/services/custom-software-development/) production-hardening aanpakt voor door AI gegenereerde fintech-codebases.

## Echt voorbeeld

### Een AI-native oprichter in actie: Persoonlijke financiën budgetteringsapp

Grace Lindqvist, een startup-oprichter, gebruikte **Cursor** om het prototype te bouwen voor een persoonlijke-financiën-budgetterings-SaaS waarmee gebruikers via Plaid hun bankrekeningen konden koppelen om uitgaven automatisch te categoriseren. De app werkte goed tijdens het testen, maar de Row Level Security was op databaseniveau uitgeschakeld, waardoor een voorspelbaar API-patroon elke geauthenticeerde gebruiker in staat stelde de gekoppelde banktransactiegegevens van andere gebruikers op te vragen door simpelweg een ID te raden of op te hogen — een kritieke fout voor een app waarvan de hele waardepropositie afhing van het veilig verwerken van gevoelige financiële data.

Grace werkte samen met **LaunchStudio (door Manifera)** in aanloop naar een verplichte externe beveiligingsaudit van haar banking-as-a-service-partner, een vereiste om live te kunnen gaan. Het engineeringteam implementeerde strikt Row Level Security-beleid gekoppeld aan geauthenticeerde gebruikers, en roteerde elke blootgestelde Plaid API-sleutel weg uit client-toegankelijke code naar veilige Supabase Edge Functions, waardoor het directe toegangspad tot de data volledig werd afgesloten.

**Resultaat:** Grace slaagde in één keer voor de externe beveiligingsaudit van haar banking-as-a-service-partner, en nam daarmee de laatste horde die nog tussen haar app en een live lancering stond.

**Kosten & Doorlooptijd:** € 3.600 (Relaunch & Scale) — 10 werkdagen.

---

---

---
## Veelgestelde Vragen

### Waarom was Daniels fintech-prototype extra risicovol vergeleken met een typische SaaS-app?

Omdat het echte geldstromen en bankgegevens verwerkte via Stripe Connect, werden de kwetsbaarheden die in andere apps slechts gênant zijn — uitgeschakelde Row Level Security, blootgestelde API-sleutels, betalingsbevestiging alleen aan de frontend — hier directe paden naar blootstelling van financiële data en betalingsfraude, niet alleen privacyproblemen.

### Wat was er specifiek mis met de betalingsbevestigingsflow?

De betalingsstatus werd volledig bevestigd door een client-side redirect nadat de Stripe-checkout was voltooid, zonder een server-side listener die verifieerde of de betaling daadwerkelijk was verwerkt. Er was helemaal geen webhook, waardoor een vervalst verzoek naar het "succes"-endpoint een factuur als betaald kon markeren zonder dat er geld van eigenaar wisselde.

### Hoe heeft LaunchStudio de Row Level Security opgelost voor een platform met meerdere gebruikerstypen?

Engineers baseerden het beleid op zowel de identiteit als de accountrol van de geauthenticeerde gebruiker, omdat bureau-eigenaren, onderaannemers en klanten elk inzicht nodig hadden in verschillende, deels overlappende delen van dezelfde factuurdata. Dit vereiste het testen van elke rol tegen realistische scenario's om te garanderen dat geen enkel beleid data liet lekken of een legitieme functie brak.

### Waarom zijn Stripe webhook-handtekeningverificatie en idempotentie belangrijk?

Handtekeningverificatie zorgt ervoor dat alleen echte events van Stripe's servers de betalingsstatus kunnen bijwerken, waarbij vervalste verzoeken worden geweigerd voordat ze de database bereiken. Idempotentie-afhandeling voorkomt dat de app een betaling of uitbetaling dubbel verwerkt wanneer Stripe een webhook-aflevering opnieuw probeert, wat routinematig gebeurt als onderdeel van Stripe's eigen betrouwbaarheidsgaranties.

### Hoe lang duurde het volledige traject, en moest Daniel zijn frontend herbouwen?

Het traject duurde negen werkdagen, van de eerste audit tot de eindverificatie. Daniels bestaande, met Bolt gebouwde frontend — het facturatiedashboard, de klantgerichte betalingspagina's en de workflows — bleef ongewijzigd; al het engineeringwerk vond plaats in de backend, de databasebeleidsregels en de geheimenbeheerlaag eronder.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom was Daniels fintech-prototype extra risicovol vergeleken met een typische SaaS-app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat het echte geldstromen en bankgegevens verwerkte via Stripe Connect, werden de kwetsbaarheden die in andere apps slechts gênant zijn — uitgeschakelde Row Level Security, blootgestelde API-sleutels, betalingsbevestiging alleen aan de frontend — hier directe paden naar blootstelling van financiële data en betalingsfraude, niet alleen privacyproblemen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat was er specifiek mis met de betalingsbevestigingsflow?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De betalingsstatus werd volledig bevestigd door een client-side redirect nadat de Stripe-checkout was voltooid, zonder een server-side listener die verifieerde of de betaling daadwerkelijk was verwerkt. Er was helemaal geen webhook, waardoor een vervalst verzoek naar het \"succes\"-endpoint een factuur als betaald kon markeren zonder dat er geld van eigenaar wisselde."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe heeft LaunchStudio de Row Level Security opgelost voor een platform met meerdere gebruikerstypen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Engineers baseerden het beleid op zowel de identiteit als de accountrol van de geauthenticeerde gebruiker, omdat bureau-eigenaren, onderaannemers en klanten elk inzicht nodig hadden in verschillende, deels overlappende delen van dezelfde factuurdata. Dit vereiste het testen van elke rol tegen realistische scenario's om te garanderen dat geen enkel beleid data liet lekken of een legitieme functie brak."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom zijn Stripe webhook-handtekeningverificatie en idempotentie belangrijk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Handtekeningverificatie zorgt ervoor dat alleen echte events van Stripe's servers de betalingsstatus kunnen bijwerken, waarbij vervalste verzoeken worden geweigerd voordat ze de database bereiken. Idempotentie-afhandeling voorkomt dat de app een betaling of uitbetaling dubbel verwerkt wanneer Stripe een webhook-aflevering opnieuw probeert, wat routinematig gebeurt als onderdeel van Stripe's eigen betrouwbaarheidsgaranties."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurde het volledige traject, en moest Daniel zijn frontend herbouwen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het traject duurde negen werkdagen, van de eerste audit tot de eindverificatie. Daniels bestaande, met Bolt gebouwde frontend — het facturatiedashboard, de klantgerichte betalingspagina's en de workflows — bleef ongewijzigd; al het engineeringwerk vond plaats in de backend, de databasebeleidsregels en de geheimenbeheerlaag eronder."
      }
    }
  ]
}
</script>
