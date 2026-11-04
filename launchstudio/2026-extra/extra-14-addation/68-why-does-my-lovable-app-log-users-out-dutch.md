---
Titel: "Waarom Logt Mijn Lovable-App Gebruikers Steeds Uit?"
Trefwoorden: lovable logt gebruikers uit, supabase sessie verlopen, lovable login-lus, supabase refresh token, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Waarom Logt Mijn Lovable-App Gebruikers Steeds Uit?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Waarom Logt Mijn Lovable-App Gebruikers Steeds Uit?",
  "description": "Gebruikers die willekeurig worden uitgelogd, login-lussen en foutmeldingen over verlopen sessies in apps met Lovable en Supabase komen meestal voort uit een handvol oorzaken. Dit artikel legt elk ervan uit: domeinen, meerdere clients, het vernieuwen van tokens, opslag, privacy in de browser en sessie-instellingen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-16",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/why-does-my-lovable-app-log-users-out" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: User sessions", "url": "https://supabase.com/docs/guides/auth/sessions" },
    { "@type": "CreativeWork", "name": "Supabase: Redirect URLs", "url": "https://supabase.com/docs/guides/auth/redirect-urls" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A07 Identification and Authentication Failures", "url": "https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/" }
  ]
}
</script>

**Kort antwoord:** meestal is het een van zes dingen: gebruikers die wisselen tussen domeinen (preview, met en zonder www), meerdere Supabase-clients in de code die vechten om dezelfde sessie, het vernieuwen van tokens dat mislukt omdat de app offline was of op de achtergrond draaide, sessieopslag die door browsers of in-app-webviews wordt gewist, redirect-URL's die na het inloggen naar de verkeerde plek wijzen, of instellingen voor de sessieduur die strenger zijn dan u bedoelde. Elk heeft een specifieke oorzaak die te verhelpen is.

## Belangrijkste Punten

- **Willekeurige uitlogs in apps met Lovable en Supabase hebben meestal zes oorzaken:** meerdere domeinen, meerdere Supabase-clients, mislukte tokenvernieuwingen, gewiste opslag, verkeerde redirects en strenge sessie-instellingen.
- **Sessies worden per domein opgeslagen,** dus met www, zonder www en preview-URL's gedragen zich als afzonderlijke apps.
- **Maak één Supabase-client en gebruik die overal;** meerdere clients kunnen elkaars sessies overschrijven.
- **Mobiele browsers en in-app-browsers** pauzeren tabbladen en beperken opslag, waardoor vernieuwingen vaker mislukken.
- **Omgaan met sessies is ook een beveiligingskwestie:** OWASP rekent fouten in identificatie en authenticatie tot de grootste risico's voor webapplicaties.

## Oorzaak 1: Meer dan Eén Domein

Sessies worden per domein opgeslagen. Een gebruiker die inlogt op `uwapp.nl` en later op `www.uwapp.nl` of de preview van Lovable belandt, lijkt uitgelogd. Oplossing: kies één canoniek domein, stuur alle andere daarnaartoe door, en werk de site-URL en de redirectlijst in Supabase bij.

## Oorzaak 2: Meerdere Supabase-Clients

AI-gegenereerde code maakt soms in meerdere bestanden een nieuwe Supabase-client aan. Meerdere clients kunnen onafhankelijk van elkaar tokens vernieuwen en elkaars sessie overschrijven, wat schijnbaar willekeurige uitlogs veroorzaakt. Oplossing: maak één client in één module en importeer die overal.

## Oorzaak 3: Mislukte Tokenvernieuwingen

Supabase gebruikt kortlevende access tokens die met een refresh token worden vernieuwd. Als een tabblad op een telefoon slaapt, het netwerk wegvalt op het moment van vernieuwen, of twee tabbladen tegelijk vernieuwen, kan de vernieuwing mislukken. Oplossing: gebruik de automatische vernieuwing van de officiële client, handel de events `TOKEN_REFRESHED` en `SIGNED_OUT` af, en vermijd eigen omgang met tokens.

## Oorzaak 4: Opslag Gewist of Geblokkeerd

Sessies worden in de browseropslag bewaard. Privé browsen, strenge privacy-instellingen, sommige in-app-browsers (zoals bij het openen van links vanuit sociale apps) en extensies die opslag wissen, kunnen die leegmaken. Oplossing: detecteer wanneer opslag niet beschikbaar is en toon een duidelijke melding; moedig voor belangrijke flows aan om de gewone browser te gebruiken.

## Oorzaak 5: Verkeerde Redirects na het Inloggen

Magic links, OAuth en wachtwoordherstel kunnen gebruikers naar een ander domein of pad sturen dan waar hun sessie staat, wat een login-lus veroorzaakt. Oplossing: breng de site-URL van Supabase, de lijst met toegestane redirects en de waarden van `redirectTo` in uw code met elkaar in lijn.

## Oorzaak 6: Sessie-Instellingen

Met Supabase kunt u op ondersteunde abonnementen het gedrag van sessies instellen, zoals tijdslimieten en time-outs bij inactiviteit. Een strenge instelling die tijdens de ontwikkeling is gekozen, kan gebruikers in productie verrassen. Oplossing: kies limieten die passen bij uw beveiligingsbehoeften en leg ze uit aan gebruikers.

## Snelle Diagnose

| Symptoom | Waarschijnlijke oorzaak |
| --- | --- |
| Uitgelogd na het klikken op een link in een e-mail | Verschil in redirect-URL of domein |
| Willekeurig uitgelogd tijdens het gebruik van de app | Meerdere clients of mislukte vernieuwingen |
| Alleen uitgelogd op de iPhone of via links in Instagram/Facebook | Beperkingen van opslag in webviews |
| Login-lus: inloggen, dan terug naar het inlogscherm | Redirectconfiguratie of sessie die niet wordt bewaard |
| Elke ochtend uitgelogd | Tijdslimiet van de sessie of time-out bij inactiviteit |

## Hoe Sessies in Supabase Werken

Wanneer een gebruiker inlogt, geeft Supabase Auth twee tokens uit: een kortlevend access token, een JSON Web Token dat bij elk verzoek de identiteit van de gebruiker bewijst, en een langer geldig refresh token waarmee nieuwe access tokens worden opgehaald. De Supabase-client bewaart beide, standaard in de browseropslag, en vernieuwt het access token automatisch voordat het verloopt. De documentatie van Supabase over sessies beschrijft deze levenscyclus en de instellingen die erop van invloed zijn. De meeste problemen met uitloggen zijn fouten ergens in deze cyclus: tokens die zijn opgeslagen waar de app ze niet kan vinden, die door concurrerende clients worden vernieuwd of die verloren gaan wanneer de opslag wordt gewist.

## Waarom Dubbele Clients Problemen Geven

AI-gegenereerde code maakt vaak een nieuwe Supabase-client aan binnen afzonderlijke componenten of pagina's. Elke client kan een eigen timer voor vernieuwing starten. Wanneer twee clients vrijwel tegelijk vernieuwen, kan de ene een refresh token gebruiken dat de andere al heeft geroteerd, waardoor de server het weigert en de gebruiker uitlogt. De oplossing is eenvoudig en blijvend: maak één client in één module, exporteer die en importeer die overal. Een zoektocht naar `createClient` in uw codebase laat het probleem meestal binnen enkele minuten zien.

## Domeinen, Cookies en Opslag

Browsers scheiden opslag per origin: protocol, domein en poort. `https://uwapp.nl`, `https://www.uwapp.nl` en een preview-URL zijn verschillende origins met aparte sessies. Gebruikers die daartussen wisselen, lijken uitgelogd. Kies één canoniek domein, stuur alle andere daar met permanente redirects naartoe en gebruik dat domein overal: in de site-URL van Supabase, de lijst met toegestane redirects, e-mailsjablonen en links in uw app.

## De Werkelijkheid op Mobiel

Op telefoons pauzeren browsers tabbladen op de achtergrond om de batterij te sparen, wisselen netwerken tussen wifi en mobiele data, en kunnen in-app-browsers binnen sociale media de opslag beperken. Elk daarvan kan het vernieuwen van een token onderbreken. Een robuuste aanpak betekent luisteren naar de wijzigingen in de authenticatiestatus van de client, vernieuwingen opnieuw proberen zodra de verbinding terug is in plaats van direct uit te loggen, en invoer van de gebruiker lokaal opslaan, zodat een zeldzame uitlog geen werk in uitvoering vernietigt. Moedig gebruikers voor belangrijke flows, zoals betalingen, aan om uw app in hun gewone browser te openen.

## Sessie-Instellingen en Beveiliging

De duur van een sessie is een afweging tussen gemak en beveiliging. Lange sessies betekenen minder vaak inloggen; korte sessies beperken de schade als een apparaat wordt gestolen. Met Supabase kunt u op ondersteunde abonnementen onderdelen van het sessiegedrag instellen. Denk aan uw doelgroep: een consumentenapp kan gebruikers meestal lang ingelogd houden, terwijl een app met financiële of medische gegevens na inactiviteit opnieuw om authenticatie kan vragen en MFA kan vereisen voor gevoelige acties. De richtlijnen van OWASP over fouten in authenticatie benadrukken het correct beëindigen van sessies bij uitloggen en time-outs die bij het risico passen.

## Uitloggen dat Echt Uitlogt

Het omgekeerde probleem doet er ook toe. Wanneer een gebruiker op "uitloggen" klikt, moet de sessie zowel op de server als in de browser eindigen, zodat refresh tokens niet opnieuw kunnen worden gebruikt. Op gedeelde apparaten is dat belangrijk. De methoden voor uitloggen van Supabase kunnen sessies intrekken; gebruik voor functies als "overal uitloggen" de optie voor globaal uitloggen. Test dat na het uitloggen de terugknop van de browser geen privégegevens uit de cache toont.

## Uitlogs Systematisch Diagnosticeren

Vraag betrokken gebruikers welk apparaat en welke browser ze gebruikten en hoe ze in de app kwamen (link in een e-mail, bladwijzer, sociale media). Controleer in de logs van Supabase Auth of er rond het gemelde tijdstip vernieuwingen zijn mislukt. Reproduceer het probleem in hetzelfde type browser. Koppel het bewijs daarna aan de zes oorzaken hierboven. De meeste gevallen zijn binnen een dag opgelost zodra het patroon duidelijk is.

## Een Checklist voor de Oplossing

- Zoek naar `createClient` en breng alles terug tot één gedeelde Supabase-client
- Kies één canoniek domein en stuur alle andere door
- Stel de site-URL en de redirectlijst van Supabase in op productie en legitieme omgevingen
- Werk e-mailsjablonen en links bij zodat ze het canonieke domein gebruiken
- Handel wijzigingen in de authenticatiestatus af zonder uit te loggen bij tijdelijke fouten in de vernieuwing
- Sla concepten lokaal op bij formulieren waarin gebruikers tijd steken
- Beoordeel de instellingen voor time-outs van sessies tegen uw beveiligingsbehoeften
- Test op Safari voor iOS, Chrome voor Android en minstens één in-app-browser

## De Gezondheid van Sessies Monitoren

Houd het aantal uitlogs en mislukte vernieuwingen bij via de logs van Supabase Auth en error tracking. Een plotselinge stijging na een release wijst meestal op een codewijziging die een extra client heeft toegevoegd of redirects heeft veranderd. Meldingen bij ongebruikelijke pieken helpen u regressies op te merken voordat klanten uw supportinbox overspoelen.

## Veelgemaakte Fouten

- Uitlogs oplossen door sessies extreem lang te maken zonder aan beveiliging te denken
- Clients aanmaken binnen componenten die vaak opnieuw renderen
- Preview- en productie-URL's door elkaar gebruiken in e-mails
- Tokens op eigen plekken bewaren in plaats van de client ze te laten beheren
- Het gedrag van in-app-browsers negeren voor gebruikers die via sociale media binnenkomen

## De Opbrengst

Betrouwbare sessies zijn onzichtbaar voor gebruikers, en dat is precies het doel. Door ze te herstellen, verdwijnt een van de meest frustrerende ervaringen in elke app, daalt de supportdruk en wordt het werk beschermd dat gebruikers in uw product steken.

## Gerelateerde Onderwerpen

Onze gidsen over inloggen met Google in Lovable-apps, e-mails van Supabase die niet aankomen en tweestapsverificatie behandelen de verwante onderdelen van authenticatie uitgebreider.

## Wanneer Uitloggen Bewust Gebeurt

Niet elke uitlog is een bug. Apps waarin beveiliging zwaar weegt, kunnen gebruikers na inactiviteit uitloggen, opnieuw om authenticatie vragen voor gevoelige acties of sessies beëindigen wanneer een wachtwoord verandert. Maak dit gedrag expliciet: toon een melding die uitlegt waarom de gebruiker is uitgelogd en wat die moet doen, waarschuw vóór een time-out bij inactiviteit en bewaar niet-opgeslagen werk. Gebruikers accepteren beveiligingsmaatregelen die ze begrijpen; ze ergeren zich aan maatregelen die op fouten lijken.

## Wijzigingen Uitleggen aan Gebruikers

Als u een langlopend probleem met uitloggen oplost, laat het betrokken gebruikers dan weten. Een kort bericht - "We hebben een probleem opgelost waardoor sommige gebruikers onverwacht werden uitgelogd" - herstelt vertrouwen en maakt van gefrustreerde gebruikers vaak weer actieve gebruikers.

## Vragen aan Betrokken Gebruikers

Wanneer gebruikers uitlogs melden, beperken een paar vragen de oorzaak snel: welk apparaat en welke browser gebruikte u? Opende u de app vanuit een e-mail, een bladwijzer of een app voor sociale media? Werd u uitgelogd tijdens het gebruik van de app of toen u later terugkwam? Gebeurde het op wifi of op mobiele data? Verzamel de antwoorden in een eenvoudig formulier of supportsjabloon; na een handvol meldingen verschijnen meestal patronen.

## Samenvatting

Eén client, één domein, correcte redirects, robuuste omgang met vernieuwingen en verstandige sessie-instellingen lossen bijna elk probleem met uitloggen in apps met Lovable en Supabase op.

## Waar U Vandaag Begint

Zoek in uw project naar `createClient`. Komt het meer dan één keer voor, breng het dan eerst terug tot één; die ene wijziging lost een groot deel van de onverklaarde uitlogs in Lovable-apps op. Controleer daarna of uw app op precies één domein bereikbaar is.

## De Kern

De meeste "willekeurige" uitlogs zijn niet willekeurig. Volg de levenscyclus van de sessie, los de problemen met de gedeelde client en het domein op, en gebruikers merken helemaal niets meer van authenticatie.

## Verder Lezen

Zie onze gids over het verhuizen van een Lovable-app naar uw eigen hosting voor het instellen van één canoniek domein met redirects.

## Het Laten Oplossen

Problemen met sessies zijn een veelvoorkomende oplossing van LaunchStudio, meestal een tot twee dagen binnen een Launch Ready-pakket, samen met het opruimen van redirects en domeinen. LaunchStudio wordt ondersteund door Manifera, waarvan de engineers al 11+ jaar authenticatieflows implementeren vanuit Ho Chi Minh-stad en Amsterdam; zie [de webappontwikkeling van Manifera](https://www.manifera.com/services/web-app-develop/). Supabase legt [sessies](https://supabase.com/docs/guides/auth/sessions) uitgebreid uit. Verwante problemen behandelen we in ons artikel over [veelvoorkomende problemen in Lovable-apps oplossen](https://launchstudio.eu/nl/blog/fix-my-lovable-app-the-problems-founders-bring-us-most).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Het Verkoopteam dat Twintig Keer per Dag Werd Uitgelogd

Ruud Koopman bouwde Klantbezoek in Lovable: een lichte CRM voor buitendienstmedewerkers van een groothandel in bouwmaterialen, gebruikt op telefoons tussen klantbezoeken door. Vertegenwoordigers klaagden dat ze voortdurend werden uitgelogd, vaak tijdens het invoeren van bezoeknotities, die daarna verloren gingen.

LaunchStudio vond drie oorzaken tegelijk. De code maakte in vier verschillende componenten een Supabase-client aan, die elk volgens een eigen schema tokens vernieuwden. De app was bereikbaar op zowel `klantbezoek.nl` als `www.klantbezoek.nl`, en links in e-mails met meldingen gebruikten de versie met www. En wanneer telefoons tussen bezoeken op slot gingen, mislukte het vernieuwen van tokens op zwakke mobiele verbindingen, waardoor gebruikers werden uitgelogd in plaats van dat het opnieuw werd geprobeerd.

De engineers brachten alles terug tot één clientmodule, stuurden www door naar het canonieke domein en werkten de redirectinstellingen bij, voegden afhandeling toe die het vernieuwen opnieuw probeerde zodra de verbinding terug was in plaats van uit te loggen, en sloegen concepten van bezoeknotities lokaal op, zodat er niets verloren ging als een sessie toch verliep.

**Resultaat:** Onverwachte uitlogs gingen van een dagelijkse klacht naar vrijwel nul, en het aantal vastgelegde bezoeknotities per vertegenwoordiger per week steeg merkbaar zodra vertegenwoordigers de app vertrouwden.

> *"Elke uitlog kostte een vertegenwoordiger zijn notities en zijn geduld. De oorzaak bleek vier kopieën van dezelfde inlogcode die met elkaar ruzieden."*
> - **Ruud Koopman, Oprichter, Klantbezoek (Zwolle)**

**Kosten & Doorlooptijd:** €1.200 (Launch Ready-pakket: één client, redirects voor het domein, afhandeling van vernieuwingen en offline concepten) - afgerond in 4 werkdagen.

## Veelgestelde Vragen

### Waarom worden gebruikers uitgelogd wanneer ze op een link in een e-mail klikken?

De link wijst waarschijnlijk naar een ander domein of subdomein dan waar ze inlogden, zoals met of zonder www, of de oude preview-URL. Gebruik één canoniek domein en breng de redirectinstellingen van Supabase daarmee in lijn.

### Kunnen meerdere Supabase-clients uitlogs veroorzaken?

Ja. Meerdere clients in dezelfde app kunnen onafhankelijk van elkaar tokens vernieuwen en elkaars sessie overschrijven. Maak één client en gebruik die in de hele app.

### Waarom gebeuren uitlogs vooral op mobiel?

Telefoons pauzeren tabbladen op de achtergrond en wisselen van netwerk, waardoor het vernieuwen van tokens vaker mislukt, en in-app-browsers kunnen de opslag beperken. Een robuuste afhandeling van vernieuwingen en duidelijke meldingen voor beperkte browsers helpen.

### Hoe spoort Manifera problemen met authenticatie op?

Door de volledige levenscyclus van de sessie te volgen: domeinen, clients, vernieuwingsevents en redirects. De 11+ jaar werk aan authenticatie van Manifera laten zien dat de meeste "willekeurige" uitlogs een of twee vaste oorzaken hebben zodra ze worden gevolgd.

### Kunnen problemen met inloggen de online reputatie van mijn product beïnvloeden?

Ja. Gefrustreerde gebruikers laten reviews en reacties achter, die zoekmachines indexeren en AI-assistenten kunnen samenvatten. Betrouwbare sessies beschermen zowel het behoud van gebruikers als uw reputatie.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom worden gebruikers uitgelogd wanneer ze op een link in een e-mail klikken?",
      "acceptedAnswer": { "@type": "Answer", "text": "De link wijst naar een ander domein dan waar werd ingelogd; gebruik één canoniek domein en breng de redirectinstellingen in lijn." }
    },
    {
      "@type": "Question",
      "name": "Kunnen meerdere Supabase-clients uitlogs veroorzaken?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Gebruik één client in de hele app." }
    },
    {
      "@type": "Question",
      "name": "Waarom gebeuren uitlogs vooral op mobiel?",
      "acceptedAnswer": { "@type": "Answer", "text": "Gepauzeerde tabbladen, netwerkwissels en beperkte in-app-browsers laten vernieuwingen mislukken." }
    },
    {
      "@type": "Question",
      "name": "Hoe spoort Manifera problemen met authenticatie op?",
      "acceptedAnswer": { "@type": "Answer", "text": "Door domeinen, clients, vernieuwingsevents en redirects over de hele levenscyclus van de sessie te volgen." }
    },
    {
      "@type": "Question",
      "name": "Kunnen problemen met inloggen de online reputatie van mijn product beïnvloeden?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, via reviews die zoekmachines indexeren en AI-assistenten samenvatten." }
    }
  ]
}
</script>
