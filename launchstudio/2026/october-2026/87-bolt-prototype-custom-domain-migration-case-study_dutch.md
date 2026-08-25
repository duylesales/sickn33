---
Titel: "Case Study: Een Bolt-prototype Migreren naar een Eigen Domein Zonder Downtime"
Keywords: Bolt-prototype, Eigen Domeinmigratie, Zero Downtime, DNS-overdracht, LaunchStudio, Manifera, AI-app Deployment, Herre Roelevink
Buyer Stage: Decision
---

# Case Study: Een Bolt-prototype Migreren naar een Eigen Domein Zonder Downtime

Een Bolt-prototype verplaatsen van zijn standaard subdomein naar een echt eigen domein klinkt alsof het een klus van vijf minuten zou moeten zijn — werk een DNS-record bij, wijs het naar uw nieuwe domein, klaar. Voor oprichters die dit daadwerkelijk hebben geprobeerd met een app die actieve gebruikers, een live databaseverbinding en een betalingsintegratie heeft, is het zelden zo eenvoudig, en het verkeerd doen betekent dat echte klanten tegen een kapotte site aanlopen, een mislukte login, of een betaling die stilletjes niet doorgaat tijdens het overdrachtsvenster. Deze case study loopt precies door hoe LaunchStudio een met Bolt gebouwde SaaS-app migreerde van zijn standaard `.bolt.app`-achtige subdomein naar een volledig eigen domein zonder downtime en zonder verloren sessies, en wat er doorgaans misgaat wanneer oprichters deze migratie zelf proberen.

## Waarom een "Simpele" Domeinmigratie Dat Eigenlijk Niet Is

Aan de oppervlakte is migreren naar een eigen domein een DNS-probleem: wijs de A- of CNAME-records van uw nieuwe domein naar uw hostingprovider, wacht op propagatie, en u bent klaar. In werkelijkheid is voor een app met enige echte functionaliteit voorbij een statische pagina het domein verweven in veel meer van het systeem dan oprichters verwachten:

- **Authenticatie-callbacks.** Als uw app Supabase Auth, Auth0, Clerk, of een social login-provider zoals Google- of GitHub-OAuth gebruikt, zijn de redirect-URL's voor inloggen doorgaans geregistreerd tegen uw oorspronkelijke domein. Schakel over van domein zonder elk van deze callback-URL's bij te werken, en gebruikers die midden in de migratie proberen in te loggen, lopen tegen een kapotte redirect of een regelrechte authenticatiefout aan.

- **CORS- en API-configuratie.** Backend-API's en Edge Functions hebben vaak Cross-Origin Resource Sharing-regels die verzoeken expliciet alleen toestaan vanaf het oorspronkelijke domein. Op het moment dat uw frontend begint te serveren vanaf het nieuwe domein zonder deze regels bij te werken, falen API-aanroepen stilletjes met CORS-fouten die er voor een verwarde eindgebruiker uitzien als een kapotte app.

- **Betalingswebhook-eindpunten.** Stripe en andere betalingsproviders hebben webhook-URL's geconfigureerd tegen een specifiek domein. Als die URL niet gelijktijdig met de domeinwissel wordt bijgewerkt, stoppen betalingsbevestigingen met binnenkomen — wat betekent dat klanten in rekening worden gebracht, maar uw app dit nooit ontdekt en nooit toegang verleent.

- **SSL-certificaatprovisionering.** Een nieuw eigen domein heeft zijn eigen SSL-certificaat nodig, en als dit niet is geprovisioneerd en geverifieerd voordat verkeer wordt overgezet, lopen bezoekers tegen browserbeveiligingswaarschuwingen aan die vertrouwen en conversie ondermijnen precies in het venster waarin u er professioneel probeert uit te zien.

- **DNS-propagatietiming.** DNS-wijzigingen worden niet overal onmiddellijk van kracht — propagatie over het wereldwijde DNS-systeem kan van enkele minuten tot 48 uur duren, wat betekent dat sommige gebruikers tijdens de overgang het oude domein raken terwijl anderen het nieuwe raken, en als sessiestatus, cookies of auth-tokens niet consistent over beide worden afgehandeld, kunnen gebruikers uitgelogd worden of op inconsistente versies van de app terechtkomen.

Mis een van deze, en "simpele domeinmigratie" verandert in een storing, een golf van mislukte logins, of — erger nog — stilletjes verloren betalingen die pas dagen later naar boven komen wanneer een klant klaagt.

Er is ook een subtielere faalmodus die zelden pas weken later wordt opgemerkt: bezorgbaarheid van transactionele e-mail. Als uw app wachtwoordresets, factuurontvangstbewijzen of meldingsmails verstuurt via een dienst zoals Resend, Postmark of SendGrid, worden die e-mails doorgaans "vanaf" uw domein verstuurd en geauthenticeerd met SPF-, DKIM- en DMARC-DNS-records specifiek voor dat domein. Een nieuw eigen domein begint met geen van deze records geconfigureerd, wat betekent dat transactionele e-mails die ervanaf worden verstuurd veel eerder in de spam belanden of volledig bouncen — en omdat storingen in e-mailbezorgbaarheid vanuit het perspectief van de app stil zijn, kan een oprichter weken lang denken dat wachtwoordresetmails prima werken terwijl een aanzienlijk deel ervan stilletjes nooit de inbox bereikt.

## De Situatie van de Oprichter

De oprichter in dit geval had een projectmanagementtool voor creatieve bureaus gebouwd met Bolt, succesvol draaiend op het standaard hostingsubdomein van Bolt met ongeveer 400 actieve gebruikers en een functionerende Stripe-abonnementsflow. Klaar om er professioneler uit te zien en het vertrouwen bij potentiële bureauklanten te verbeteren, kocht ze een eigen domein en moest ze de live applicatie verplaatsen — zonder haar bestaande gebruikersbasis uit te loggen, zonder actieve abonnementen te breken, en zonder een zichtbare storing tijdens kantooruren in meerdere tijdzones waar haar bureauklanten actief waren.

Haar eerste poging, zelfstandig uitgevoerd door het DNS-record bij te werken en het daarbij te laten, brak Google OAuth-login binnen twintig minuten — de redirect-URL geregistreerd bij de OAuth-console van Google wees nog steeds naar het oude domein, en elke gebruiker die probeerde in te loggen kreeg een foutpagina te zien. Ze draaide de DNS-wijziging terug en zocht hulp.

## Het Zero-downtime Migratieproces

De engineers van LaunchStudio benaderden de migratie als een gesequenced, gefaseerd proces in plaats van een enkele DNS-omschakeling, specifiek om herhaling van de mislukte eerste poging te voorkomen:

1. **Pre-migratieaudit.** Het team bracht elke plek in kaart waar het oorspronkelijke domein werd gerefereerd: OAuth-provider callback-URL's, CORS-allowlists in de backend, Stripe-webhook-eindpuntconfiguratie, hardgecodeerde domeinreferenties in de frontend-code, en e-mailtemplates die terugverwezen naar de app.

2. **Parallelle domeinconfiguratie.** Het nieuwe eigen domein werd volledig geconfigureerd — SSL-certificaat geprovisioneerd en geverifieerd, DNS-records ingesteld — terwijl de app normaal bleef draaien op het oorspronkelijke domein, zodat niets live of gebruikersgericht was op het nieuwe domein totdat het volledig geverifieerd was.

3. **Dual-domain ondersteuningsvenster.** In plaats van een directe overdracht werd de backend tijdelijk geconfigureerd om verzoeken van zowel het oude als het nieuwe domein gelijktijdig te accepteren — CORS-regels die beide toestonden, OAuth-callbacks geregistreerd voor beide — zodat, terwijl DNS met verschillende snelheden propageerde over verschillende gebruikersnetwerken, geen van beide versies van het domein een kapotte ervaring zou opleveren.

4. **Gefaseerde webhook-overdracht.** Het Stripe-webhook-eindpunt werd pas naar het nieuwe domein bijgewerkt nadat het team bevestigde dat testevents correct werden ontvangen en nadat monitoring liet zien dat het nieuwe eindpunt correct reageerde, waardoor elk venster werd vermeden waarin een echt betalingsevent naar een verouderd eindpunt gestuurd zou kunnen worden.

5. **Monitoring tijdens propagatie.** Het team monitorde actief foutpercentages, slagingspercentages voor inloggen, en levering van betalingswebhooks gedurende het 48-uur propagatievenster, klaar om onmiddellijk terug te draaien als er tekenen van storing waren.

6. **E-mailauthenticatierecords.** SPF-, DKIM- en DMARC-records werden geconfigureerd en geverifieerd voor het nieuwe domein voordat enig transactioneel e-mailverkeer (wachtwoordresets, factuurontvangstbewijzen, meldingen) werd overgezet, bevestigd met testverzendingen gecontroleerd tegen grote inboxproviders in plaats van aangenomen dat het correct was.

7. **Redirect van het oude domein, geen verwijdering.** Zodra propagatie bevestigd volledig was en verkeer volledig was verschoven naar het nieuwe domein, werd het oude domein geconfigureerd om door te verwijzen naar het nieuwe in plaats van simpelweg gedeactiveerd, zodat eventuele resterende bladwijzers, oude marketinglinks, of traag propagerende DNS-resolvers niet op een doodlopend punt uitkwamen.

## Het Resultaat

De volledige migratie verliep zonder één gemelde inlogfout, één gemiste betalingswebhook, of enige voor klanten zichtbare downtime. Gebruikers die toevallig de app raakten tijdens het propagatievenster ervaarden geen verschil in functionaliteit ongeacht welke domeinversie ze bereikten, omdat beide gedurende de hele overgang volledig functioneel waren parallel aan elkaar.

## Wat Deze Case Study Onthult Over Deployments van AI-builders

Bolt, Lovable en vergelijkbare tools maken het bijna instant om een werkende app op een standaard subdomein te krijgen, wat precies is waarom oprichters onderschatten hoeveel systeemcomponenten stilletjes gekoppeld zijn aan dat specifieke domein tegen de tijd dat echte gebruikers, echte betalingen en echte integraties in het spel zijn. Een domeinmigratie op een gloednieuwe, lege app met nul gebruikers is oprecht een klus van vijf minuten. Dezelfde migratie op een live app met actieve sessies, OAuth-logins en een betalingsintegratie is een infrastructuurproject met echte faalmodi — en het gat tussen die twee werkelijkheden is precies waar oprichters zich verbranden als ze het zelf proberen onder de aanname dat "het gewoon DNS is."

## Belangrijkste Inzichten

- Een eigen-domeinmigratie op een live door AI gebouwde app raakt authenticatie-callbacks, CORS-configuratie, betalingswebhooks en SSL-provisionering — niet alleen een enkel DNS-record, en het missen van een van deze veroorzaakt een echte, voor klanten zichtbare storing.

- DNS-propagatie is niet instant; het kan wereldwijd tot 48 uur duren, wat betekent dat zowel het oude als het nieuwe domein tijdens de overgang parallel correct moeten functioneren, niet alleen het nieuwe.

- Een DNS-overdracht in één stap zonder OAuth callback-URL's bij te werken is een van de meest voorkomende oorzaken van een kapotte migratie — inlogfouten verschijnen bijna onmiddellijk omdat de identiteitsprovider nog steeds naar het oude domein wijst.

- Een Stripe-webhook-eindpunt bijwerken voordat is bevestigd dat het nieuwe eindpunt correct werkt, riskeert het stilletjes verliezen van betalingsbevestigingen precies in het venster waarin klanten betalen.

- Het oude domein aanhouden als redirect in plaats van te deactiveren beschermt tegen resterende bladwijzers, marketinglinks, en traag propagerende DNS-resolvers die gebruikers naar een doodlopend punt sturen nadat de migratie verder voltooid is.

## Klaar om Naar uw Eigen Domein te Verhuizen Zonder het Risico?

Krijg een zero-downtime domeinmigratie die uw logins, betalingen en actieve sessies intact houdt gedurende de overgang.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 en geleid door Oprichter & Managing Director **Herre Roelevink**. Zoals Roelevink het verwoordt: *"We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot wasdom te brengen. Wij hebben elf jaar ervaring in precies dat vakgebied."* Door "Nederlands management te combineren met Vietnamees meesterschap", onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420), een Aziatische hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minh-stad, Vietnam** (Pho Quang Street). Via LaunchStudio nemen senior engineeringteams uw bestaande door AI gebouwde frontend en implementeren ze productieklare beveiligingscontroles, live betalingsgateways, veilige hosting en monitoring — waardoor uw prototype binnen 1 tot 3 weken verandert in een veilige, compliant MVP, zonder dat een volledige rebuild nodig is. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact) of bekijk hoe het [maatwerk software-ontwikkelteam van Manifera](https://www.manifera.com/services/custom-software-development/) production-hardening aanpakt voor AI-gegenereerde codebases.

## Echt voorbeeld

### Een AI-native Oprichter in Actie: Projectmanagementtool voor Creatieve Bureaus

Ines, de oprichter achter deze case, had haar met Bolt gebouwde projectmanagementtool voor creatieve bureaus laten groeien tot ongeveer 400 actieve gebruikers op het standaard subdomein van Bolt, met Stripe-abonnementen live en werkend. Een zelfgedane DNS-wissel naar haar nieuw gekochte eigen domein brak Google OAuth-login binnen twintig minuten, waardoor actieve gebruikers midden op de werkdag over meerdere tijdzones werden buitengesloten.

Ines schakelde **LaunchStudio (door Manifera)** in om de migratie correct uit te voeren. Het team voerde een volledige pre-migratieaudit uit, configureerde dual-domain ondersteuning voor het propagatievenster, faseerde de OAuth-callback- en Stripe-webhook-updates pas nadat elk was geverifieerd, en monitorde de overgang in real time.

**Resultaat:** De migratie van Ines werd voltooid zonder gemelde inlogfouten, zonder gemiste betalingswebhooks, en zonder voor klanten zichtbare downtime gedurende het 48-uur DNS-propagatievenster.

**Kosten & Doorlooptijd:** € 1.400 (Launch Ready Pakket) — geaudit, gemigreerd en geverifieerd in 5 werkdagen.

---

---

---
## Veelgestelde Vragen

### Waarom brak mijn DNS-only domeinwissel de login?

OAuth-providers zoals Google en GitHub registreren een specifieke redirect-URL gekoppeld aan uw domein. Als u uw DNS omschakelt naar een nieuw domein zonder ook de callback-URL geregistreerd in de console van de OAuth-provider bij te werken, wordt elke inlogpoging omgeleid naar een kapotte of niet-overeenkomende URL, wat een onmiddellijke authenticatiefout veroorzaakt.

### Hoe lang duurt DNS-propagatie daadwerkelijk?

Dat varieert per DNS-provider en per netwerk van elke gebruiker, maar het kan van enkele minuten tot wel 48 uur duren om wereldwijd volledig te propageren. Tijdens dat venster kunnen verschillende gebruikers naar het oude of het nieuwe domein worden geleid, dus beide moeten correct parallel functioneren.

### Wat gebeurt er met Stripe-betalingen tijdens een domeinmigratie?

Als de URL van uw Stripe-webhook-eindpunt niet correct wordt bijgewerkt, of als deze wordt bijgewerkt voordat u heeft bevestigd dat het nieuwe eindpunt events correct ontvangt en verwerkt, kunnen betalingsbevestigingsevents uw app niet bereiken. Klanten worden in rekening gebracht, maar uw app verleent nooit toegang, omdat het nooit de webhook heeft ontvangen die de betaling bevestigt.

### Moet ik mijn oude domein deactiveren na de migratie?

Nee — configureer het in plaats daarvan om door te verwijzen naar uw nieuwe domein. Bladwijzers, oude marketinglinks en traag propagerende DNS-resolvers blijven een periode na de migratie nog verkeer naar het oude domein sturen, en een redirect zorgt ervoor dat die bezoekers nog steeds ergens functioneel terechtkomen in plaats van op een dode pagina.

### Hoe lang duurt een zero-downtime domeinmigratie doorgaans?

Voor een live app met authenticatie, betalingen en actieve gebruikers duurt een correct gefaseerde migratie — inclusief de pre-migratieaudit, dual-domain ondersteuningsvenster en gemonitorde overdracht — doorgaans ongeveer een week van start tot volledige verificatie, hoewel het DNS-propagatievenster zelf tot 48 extra uur aan monitoring kan toevoegen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom brak mijn DNS-only domeinwissel de login?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "OAuth-providers zoals Google en GitHub registreren een specifieke redirect-URL gekoppeld aan uw domein. Als u uw DNS omschakelt naar een nieuw domein zonder ook de callback-URL geregistreerd in de console van de OAuth-provider bij te werken, wordt elke inlogpoging omgeleid naar een kapotte of niet-overeenkomende URL, wat een onmiddellijke authenticatiefout veroorzaakt."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt DNS-propagatie daadwerkelijk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dat varieert per DNS-provider en per netwerk van elke gebruiker, maar het kan van enkele minuten tot wel 48 uur duren om wereldwijd volledig te propageren. Tijdens dat venster kunnen verschillende gebruikers naar het oude of het nieuwe domein worden geleid, dus beide moeten correct parallel functioneren."
      }
    },
    {
      "@type": "Question",
      "name": "Wat gebeurt er met Stripe-betalingen tijdens een domeinmigratie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Als de URL van uw Stripe-webhook-eindpunt niet correct wordt bijgewerkt, of als deze wordt bijgewerkt voordat u heeft bevestigd dat het nieuwe eindpunt events correct ontvangt en verwerkt, kunnen betalingsbevestigingsevents uw app niet bereiken. Klanten worden in rekening gebracht, maar uw app verleent nooit toegang, omdat het nooit de webhook heeft ontvangen die de betaling bevestigt."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik mijn oude domein deactiveren na de migratie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee — configureer het in plaats daarvan om door te verwijzen naar uw nieuwe domein. Bladwijzers, oude marketinglinks en traag propagerende DNS-resolvers blijven een periode na de migratie nog verkeer naar het oude domein sturen, en een redirect zorgt ervoor dat die bezoekers nog steeds ergens functioneel terechtkomen in plaats van op een dode pagina."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt een zero-downtime domeinmigratie doorgaans?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor een live app met authenticatie, betalingen en actieve gebruikers duurt een correct gefaseerde migratie — inclusief de pre-migratieaudit, dual-domain ondersteuningsvenster en gemonitorde overdracht — doorgaans ongeveer een week van start tot volledige verificatie, hoewel het DNS-propagatievenster zelf tot 48 extra uur aan monitoring kan toevoegen."
      }
    }
  ]
}
</script>
