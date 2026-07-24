---
Titel: "De AI-Deploymentdag Die Verkeerd Gaat (En de Checklist Die Het Voorkomt)"
Trefwoorden: ai deployment, deploy ai generated app, environment variables production, ai app launch checklist
Koperfase: Overweging
Doelgroep: Technische solo-oprichter
---
# De AI-Deploymentdag Die Verkeerd Gaat (En de Checklist Die Het Voorkomt)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "De AI-Deploymentdag Die Verkeerd Gaat (En de Checklist Die Het Voorkomt)",
  "description": "Een stap-voor-stap verslag van hoe een AI-deployment misgaat wanneer omgevingsvariabelen niet per omgeving worden gescheiden, plus de checklist die dit opvangt vóór de lancering.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-deployment-day-checklist" }
}
</script>

9:14 uur: u pusht naar productie. 9:16 uur: de app laadt, de demo werkt, u maakt een screenshot voor het teamkanaal. 9:52 uur: iemand opent uit nieuwsgierigheid de devtools en vindt de API-sleutel van uw AI-provider in platte tekst in de frontend JavaScript-bundel, zichtbaar voor iedereen die hetzelfde tabblad opent dat u zojuist vierde. Dit is geen hypothetisch scenario. Het is de meest voorkomende manier waarop een AI-deployment omslaat van "we hebben gelanceerd" naar "we hebben een probleem", en het gebeurt omdat een deploymentdag honderd kleine beslissingen bevat, en precies één daarvan — waar een geheim leeft — degene is die niet met een snelle oplossing ongedaan kan worden gemaakt.

## Waarom deze specifieke fout precies op deploymentdag optreedt

Het bouwen van een app met Cursor, Bolt of vergelijkbare tools gebeurt doorgaans in één ononderbroken omgeving: één project, één set configuratiewaarden, één mentaal model van "de app". Deployment is het eerste moment waarop dat mentale model in ten minste twee realiteiten moet splitsen — ontwikkeling en productie — die elk hun eigen, gescheiden configuratie zouden moeten hebben, zeker voor alles wat op een geheim lijkt. Als die splitsing nooit expliciet plaatsvindt, worden de waarden die lokaal prima werkten ongewijzigd doorgezet, inclusief elke API-sleutel die alleen ooit op een server had mogen leven, niet in code die naar de browser van elke bezoeker wordt verzonden.

Dit is precies de fout die makkelijk één keer wordt gemaakt en nooit wordt opgemerkt, omdat er op het moment van deployen niets vreemds aan lijkt. De app werkt. De functie die de API van de AI-provider aanroept, werkt. Pas wanneer iemand daadwerkelijk inspecteert wat er naar de browser is verzonden, blijkt de sleutel in het volle zicht te staan — en tegen die tijd heeft hij al net zo lang live gestaan, en mogelijk buit te maken, als de deployment openbaar toegankelijk is geweest.

## De checklist die het opvangt vóór de lancering

- **Aparte omgevingsbestanden voor ontwikkeling en productie** — laat nooit één `.env`-bestand beide dienen; productiegeheimen mogen alleen bestaan waar productiecode draait.
- **Bevestig welke variabelen frontend-blootgesteld zijn en welke server-only** — alles met een prefix voor client-side bundling (een veelvoorkomend patroon in moderne frameworks) wordt naar de browser van elke bezoeker verzonden; alles dat privé moet blijven, mag nooit die prefix dragen.
- **Doorzoek de gebuilde frontendbundel op de letterlijke tekenreeks van elke API-sleutel** voordat u de deployment als voltooid beschouwt — niet de broncode, maar de daadwerkelijk gecompileerde output die naar browsers wordt verzonden.
- **Roteer elke sleutel die een publieke repository of een client-gebundelde build heeft aangeraakt**, ook al was het maar kort, in plaats van aan te nemen dat niemand het heeft opgemerkt.
- **Bevestig de ratelimieten en quota van elke externe API-sleutel** — een gelekte sleutel is niet alleen een privacykwestie, het is ook een facturatiekwestie als iemand anders hem begint te gebruiken.
- **Test de gedeployde app vanuit een incognitobrowser met geopende devtools**, specifiek gericht op netwerkverzoeken en gebundelde scripts, niet alleen de gerenderde pagina.

## Waarom deze specifieke kloof zo vaak voorkomt in door AI gebouwde apps

AI-codeerassistenten zijn uitstekend in het end-to-end koppelen van een functie — roep deze API aan, render deze respons — maar de tool heeft geen zelfstandig besef van welke waarden in die koppeling geheimen zijn en welke publieke configuratie. Als een prompt zegt "verbind met de AI-provider met deze sleutel", doet de tool precies dat, in welk bestand dan ook waarmee de functie werkt, zonder noodzakelijkerwijs te signaleren dat dat bestand uiteindelijk wordt gebundeld en naar de browser verzonden. Het onderscheid tussen server-side en client-side code is een architecturaal concept waarvan de tool aanneemt dat u het al begrijpt — en voor oprichters die snel bewegen richting hun eerste productiedeployment, is dat vaak het ene ding dat niemand expliciet heeft gecontroleerd.

Manifera brengt 11+ jaar aan productie-engineeringervaring naar precies dit soort kloof, met technici gevestigd in Singapore die oprichters in de regio ondersteunen met deploymentbeoordelingen vóór de lancering, niet erna. Als u toewerkt naar uw eigen deploymentdag, kunt u [praten met een engineer die door AI gegenereerde code begrijpt](https://launchstudio.eu/en/#contact) voordat u pusht, of bekijken hoe Manifera [offshore softwareontwikkeling](https://www.manifera.com/services/offshore-software-development/) structureert voor teams die dit soort beoordeling ingebouwd willen hebben in hun proces in plaats van er achteraf aan vast te plakken.

## Echt voorbeeld

### Een AI-native oprichter in actie: de sleutel in het volle zicht

Vincent Voskuil, een oprichter uit Enkhuizen, bouwde "MeldStroom" — een incidentmeldingstool voor kleine operationele teams — met Cursor. De app gebruikte een API van een AI-provider om binnenkomende meldingen automatisch te helpen categoriseren, een functie die Vincent al vroeg had gekoppeld en uitgebreid had getest tijdens de ontwikkeling. Toen de deploymentdag aanbrak, pushte hij dezelfde configuratie rechtstreeks naar productie, zonder te scheiden welke omgevingsvariabelen waar hoorden.

De API-sleutel van de AI-provider, die alleen ooit vanaf de server had hoeven worden aangeroepen, kwam rechtstreeks terecht in de openbare frontend JavaScript — zichtbaar voor iedereen die de devtools van zijn browser opende en naar het netwerktabblad of de gecompileerde scripts keek. Niemand had iets kwaadaardigs gedaan om dit te veroorzaken; de sleutel leefde simpelweg in een configuratiebestand dat op dezelfde manier in de client-side build terechtkwam als tijdens de lokale ontwikkeling, omdat niets in de deploymentstap de twee had gescheiden.

Het werd ontdekt toen een technisch nieuwsgierige vroege gebruiker, die uit algemene interesse in de app rondneusde, de sleutel in het volle zicht opmerkte in een scriptbestand. Vincent bracht MeldStroom direct naar LaunchStudio. Onze technici roteerden de blootgestelde sleutel, herstructureerden de app zodat alle aanroepen naar de AI-provider via een server-side eindpunt lopen in plaats van rechtstreeks vanuit de browser, en stelden voortaan correct gescheiden omgevingsconfiguraties in voor ontwikkeling en productie.

**Resultaat:** De API-aanroepen van MeldStroom naar de AI-provider gebeuren nu volledig server-side, waarbij de sleutel nooit aanwezig is in code die naar een browser wordt verzonden, met ratelimietmonitoring op zijn plaats om toekomstig misbruik van die sleutel op te vangen.

> *"Ik heb de functie honderd keer getest in ontwikkeling en hij werkte elke keer perfect. Het kwam nooit bij mij op dat 'werkend' en 'veilig om te deployen' verschillende vragen waren."*
> — **Vincent Voskuil, oprichter, MeldStroom (Enkhuizen)**

**Kosten en tijdlijn:** € 1.100 (sleutelrotatie, server-side API-routering, scheiding van omgevingen) — voltooid in 4 werkdagen.

---

## Veelgestelde vragen

### Waarom komen API-sleutels zo vaak blootgesteld te liggen in de frontend?

Omdat ontwikkelomgevingen vaak client-side en server-side configuratie op één plek mengen, en tenzij dit expliciet wordt gescheiden vóór deployment, kunnen geheimen die voor de server bedoeld zijn, terechtkomen in code die naar de browser wordt verzonden.

### Hoe kan ik nu controleren of mijn eigen app dit probleem heeft?

Open uw gedeployde app in een browser, open devtools, en doorzoek de netwerkverzoeken en geladen scripts op elke API-sleuteltekenreeks — als deze ergens in die weergave verschijnt, is deze blootgesteld.

### Wat moet ik doen als ik een blootgestelde sleutel vind?

Roteer deze onmiddellijk bij de provider, en verplaats vervolgens de code die deze gebruikt naar een server-side eindpunt, zodat de sleutel nooit uw eigen infrastructuur hoeft te verlaten.

### Beoordeelt LaunchStudio deployments voordat ze live gaan?

Ja — dit is een standaardonderdeel van onze pre-launch beoordeling, en onze technici, waaronder het team gevestigd in Singapore, controleren specifiek op precies dit soort blootstelling voordat een oprichter naar productie pusht.

### Is dit alleen een risico bij Cursor?

Nee, het is een deploymentprocesrisico dat geldt ongeacht welke AI-codeertool de app heeft gebouwd — de oplossing is in beide gevallen hetzelfde: scheid omgevingen, en laat geheimen nooit client-side code bereiken.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Why do API keys end up exposed in the frontend so often?", "acceptedAnswer": { "@type": "Answer", "text": "Because development environments frequently mix client-side and server-side configuration in one place, and unless that's explicitly split before deployment, secrets meant for the server can get bundled into code that ships to the browser." } },
    { "@type": "Question", "name": "How can I check if my own app has this issue right now?", "acceptedAnswer": { "@type": "Answer", "text": "Open your deployed app in a browser, open dev tools, and search the network requests and loaded scripts for any API key string — if it appears anywhere in that view, it's exposed." } },
    { "@type": "Question", "name": "What should I do if I find an exposed key?", "acceptedAnswer": { "@type": "Answer", "text": "Rotate it immediately with the provider, then move the code that uses it to a server-side endpoint so the key never needs to leave your own infrastructure." } },
    { "@type": "Question", "name": "Does LaunchStudio review deployments before they go live?", "acceptedAnswer": { "@type": "Answer", "text": "Yes — this is a standard part of our pre-launch review, and our engineers, including the team based in Singapore, specifically check for exactly this class of exposure before a founder pushes to production." } },
    { "@type": "Question", "name": "Is this only a risk with Cursor?", "acceptedAnswer": { "@type": "Answer", "text": "No, it's a deployment-process risk that applies regardless of which AI coding tool built the app — the fix is the same either way: separate environments, and never let secrets reach client-side code." } }
  ]
}
</script>
