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
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-deployment-day-checklist" }
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

Manifera brengt 11+ jaar aan productie-engineeringervaring naar precies dit soort kloof, met technici gevestigd in Singapore die oprichters in de regio ondersteunen met deploymentbeoordelingen vóór de lancering, niet erna. Als u toewerkt naar uw eigen deploymentdag, kunt u [praten met een engineer die door AI gegenereerde code begrijpt](https://launchstudio.eu/nl/#contact) voordat u pusht, of bekijken hoe Manifera [offshore softwareontwikkeling](https://www.manifera.com/services/offshore-software-development/) structureert voor teams die dit soort beoordeling ingebouwd willen hebben in hun proces in plaats van er achteraf aan vast te plakken.

## Als U Zojuist een Gelekte Sleutel Heeft Gevonden: Het Eerste Uur, Stap voor Stap

De eerdere checklist was bedoeld om een lek te voorkomen. Dit stappenplan is voor de oprichter die die fase helaas al voorbij is — die zojuist een API-sleutel heeft ontdekt in een publieke git-commit of in een door de browser gedownloade JavaScript-bundel. Blijf kalm en voer binnen het eerste uur deze vier stappen uit:

**Minuut 0-15: Roteer de Sleutel Onmiddellijk (Niet Eerst Code Bewerken).** Ga direct naar het dashboard van de betreffende provider (bijvoorbeeld Stripe, OpenAI of Supabase) en trek de gelekte sleutel in ('Revoke' of 'Roll Key'). Maak een nieuwe sleutel aan. Begin *niet* met het bewerken van uw broncode of het pushen van nieuwe commits; zolang de oude sleutel actief is bij de provider, kan iedereen die hem heeft gekopieerd er misbruik van maken.

**Minuut 15-30: Inspecteer de Verbruiks- en Toegangslogs.** Controleer in het dashboard van de provider direct de activiteitslogs sinds het moment van de git-push. Zijn er ongebruikelijke pieken in API-aanroepen, zijn er data-exports uitgevoerd of zijn er onbekende IP-adressen actief geweest? Zo weet u direct of het lek daadwerkelijk is geëxploiteerd of dat u op tijd was.

**Minuut 30-45: Verwijder het Geheim uit de Git-Geschiedenis.** Een nieuwe commit maken waarin u de sleutel verwijdert, volstaat *niet* — de sleutel blijft immers voor altijd zichtbaar in eerdere commits. Gebruik tools zoals `git-filter-repo` of BFG Repo-Cleaner om het geheim definitief uit de volledige commit-historie te wissen, of vraag een ervaren engineer om de repository op te schonen.

**Minuut 45-60: Verplaats het Geheim naar een Veilige Omgevingsvariabele.** Plaats de nieuwe sleutel uitsluitend in uw lokale `.env`-bestand (dat in `.gitignore` staat) en in het beveiligde configuratiedashboard van uw hostingprovider (zoals Vercel). Verifieer dat de sleutel aan de serverzijde blijft en nooit meer met een `NEXT_PUBLIC_` prefix in de frontend belandt.

Door snel en methodisch te handelen, beperkt u een potentieel catastrofaal incident tot een beheersbare operationele verstoring.
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
    {
      "@type": "Question",
      "name": "Waarom komen API-sleutels zo vaak blootgesteld te liggen in de frontend?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat ontwikkelomgevingen vaak client-side en server-side configuratie op één plek mengen, en tenzij dit expliciet wordt gescheiden vóór deployment, kunnen geheimen die voor de server bedoeld zijn, terechtkomen in code die naar de browser wordt verzonden."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe kan ik nu controleren of mijn eigen app dit probleem heeft?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Open uw gedeployde app in een browser, open devtools, en doorzoek de netwerkverzoeken en geladen scripts op elke API-sleuteltekenreeks — als deze ergens in die weergave verschijnt, is deze blootgesteld."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet ik doen als ik een blootgestelde sleutel vind?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Roteer deze onmiddellijk bij de provider, en verplaats vervolgens de code die deze gebruikt naar een server-side eindpunt, zodat de sleutel nooit uw eigen infrastructuur hoeft te verlaten."
      }
    },
    {
      "@type": "Question",
      "name": "Beoordeelt LaunchStudio deployments voordat ze live gaan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja — dit is een standaardonderdeel van onze pre-launch beoordeling, en onze technici, waaronder het team gevestigd in Singapore, controleren specifiek op precies dit soort blootstelling voordat een oprichter naar productie pusht."
      }
    },
    {
      "@type": "Question",
      "name": "Is dit alleen een risico bij Cursor?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, het is een deploymentprocesrisico dat geldt ongeacht welke AI-codeertool de app heeft gebouwd — de oplossing is in beide gevallen hetzelfde: scheid omgevingen, en laat geheimen nooit client-side code bereiken."
      }
    }
  ]
}
</script>
