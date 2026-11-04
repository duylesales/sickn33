---
Titel: "Is de Anon Key van Supabase Veilig om in Mijn App te Tonen?"
Trefwoorden: is supabase anon key veilig, supabase anon key openbaar, supabase publishable key, supabase service role key, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Is de Anon Key van Supabase Veilig om in Mijn App te Tonen?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Is de Anon Key van Supabase Veilig om in Mijn App te Tonen?",
  "description": "De anon key (publishable key) van Supabase is ontworpen om openbaar te zijn, maar is alleen veilig als Row Level Security correct is. Dit artikel legt het verschil uit tussen anon-, publishable-, service role- en secret keys, wat een aanvaller met elk ervan kan, en hoe u uw app controleert.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-05",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/is-the-supabase-anon-key-safe" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: API keys", "url": "https://supabase.com/docs/guides/api/api-keys" },
    { "@type": "CreativeWork", "name": "Supabase: Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" },
    { "@type": "CreativeWork", "name": "OWASP Secrets Management Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A01 Broken Access Control", "url": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/" },
    { "@type": "CreativeWork", "name": "GDPR Article 33", "url": "https://gdpr-info.eu/art-33-gdpr/" }
  ]
}
</script>

**Kort antwoord:** ja, de anon key van Supabase is ontworpen om openbaar te zijn, en het is normaal dat u hem in de frontendcode van uw app ziet. Maar hij is alleen veilig als uw Row Level Security-policies correct zijn. Met de anon key kan iedereen als anonieme of ingelogde gebruiker met uw database praten; RLS bepaalt wat ze werkelijk kunnen doen. De sleutel die nooit mag worden blootgesteld, is de **service role key** (of de nieuwere **secret key**), die RLS volledig omzeilt.

## Belangrijkste Punten

- **De anon key (of publishable key) van Supabase is ontworpen om openbaar te zijn.** Hem in uw frontend zien is normaal.
- **Hij is alleen veilig als Row Level Security correct is,** omdat iedereen er uw database mee kan bevragen als anonieme of ingelogde gebruiker, binnen wat uw policies toestaan.
- **De service role key (of secret key) omzeilt RLS volledig** en mag nooit in een browser, mobiele app, repository of log verschijnen.
- **De anon key "verbergen" in omgevingsvariabelen verbergt hem niet;** frontendvariabelen worden in de browsercode gebundeld.
- **Als een service role key is blootgesteld, behandel het dan als incident:** direct vervangen, bevoorrechte code naar de server verplaatsen, logs nakijken en de meldplicht onder de AVG beoordelen.

## De Sleutels Naast Elkaar

Supabase heeft twee generaties namen voor sleutels gebruikt. Beide komen in huidige projecten voor:

| Sleutel | Ook bekend als | Waar hij hoort | Wat hij kan |
| --- | --- | --- | --- |
| anon key | publishable key (`sb_publishable_...`) | Browser, mobiele apps | Wat uw RLS-policies toestaan voor anonieme of ingelogde gebruikers |
| service role key | secret key (`sb_secret_...`) | Alleen de server: edge functions, backend, CI | Alles, met omzeiling van RLS |

De anon key is als de voordeur van een gebouw met een receptie. Iedereen kan naar binnen; de receptie (RLS) bepaalt waar ze heen mogen. De service role key is een loper die elke deur opent zonder het aan de receptie te vragen.

## Wat Iemand met Uw Anon Key Kan

Met uw project-URL en anon key, die iedereen in uw frontend kan vinden, kan iemand:

- Uw database-API rechtstreeks aanroepen, zonder de interface van uw app
- Zich registreren en inloggen als gebruiker, als registratie openstaat
- Rijen lezen, toevoegen, wijzigen of verwijderen, **precies zo ver als uw RLS-policies toestaan**
- Databasefuncties aanroepen die beschikbaar zijn voor de rollen anon of authenticated
- Opslagobjecten openen die de storage policies toestaan

Als RLS correct is, is dit onschuldig: ze kunnen doen wat elke gebruiker van uw app kan. Als RLS ontbreekt of te ruim is, wordt de anon key de weg naar binnen. Daarom is "de anon key is gelekt" bijna nooit het echte probleem. Het echte probleem is RLS.

## Wat Iemand met de Service Role Key Kan

Alles. Elke tabel lezen, elke rij wijzigen, data verwijderen, adminusers aanmaken, alle opslag openen. Als deze sleutel in uw frontend, uw repository of uw logs verschijnt, behandel het dan als incident:

1. Vervang of trek de sleutel direct in via de projectinstellingen van Supabase
2. Verplaats elke bewerking die hem nodig had naar een edge function of backend
3. Controleer de logs op ongebruikelijke activiteit sinds de blootstelling
4. Overweeg of een melding van een datalek onder de AVG nodig is

## Hoe U Uw App in Vijf Minuten Controleert

1. **Zoek de sleutel in uw frontend.** Open de ontwikkelaarstools en doorzoek de geladen scripts op `supabase` of uw project-URL. Noteer welke sleutel daar staat.
2. **Decodeer hem als het een JWT is.** Oudere sleutels zijn JWT's; plak hem in een JWT-decoder en controleer de claim `role`. `anon` is prima. `service_role` is een noodgeval.
3. **Als hij begint met `sb_`,** controleer dan het voorvoegsel: `sb_publishable_` is prima in de browser, `sb_secret_` niet.
4. **Controleer de status van RLS.** In het Supabase-dashboard hoort elke tabel in blootgestelde schema's RLS ingeschakeld te hebben.
5. **Test als gebruiker.** Log in als twee verschillende gebruikers en probeer elkaars data te lezen. Onze [zelftest voor de beveiliging van Lovable](https://launchstudio.eu/nl/blog/is-my-lovable-app-secure) loopt dit stap voor stap door.

## Veelvoorkomende Misverstanden

**"Ik verberg de anon key in een omgevingsvariabele."** Omgevingsvariabelen met een frontendvoorvoegsel, zoals `VITE_` of `NEXT_PUBLIC_`, worden in de browsercode gebundeld. Ze zijn configuratie, geen geheimen. Dat is prima voor de anon key en fout voor alles wat geheim is.

**"Ik zet de service role key alleen voor de adminpagina in de frontend."** De code van de adminpagina wordt door elke bezoeker gedownload. Gebruik een edge function die controleert of de aanroeper admin is en voer daarna de bevoorrechte actie op de server uit.

**"RLS staat aan, dus ik ben veilig."** Ingeschakeld met een policy `using (true)` beschermt niets. Wat telt, is wat de policies zeggen.

## Hoe de Architectuur van Supabase het Ontwerp van de Sleutels Verklaart

Supabase stelt uw PostgreSQL-database beschikbaar via een automatisch gegenereerde REST- en GraphQL-API. Verzoeken bevatten een sleutel die aangeeft welke Postgres-rol wordt gebruikt. De anon- of publishable key hoort bij beperkte rollen: `anon` voor bezoekers en `authenticated` voor ingelogde gebruikers, waarvan de toegang wordt gefilterd door Row Level Security-policies. De service role- of secret key hoort bij een rol die RLS omzeilt, bedoeld voor vertrouwde servercode. De documentatie van Supabase over API-sleutels beschrijft dit model en legt de nieuwere formaten voor publishable en secret keys uit.

Dit ontwerp is bewust. Het laat frontends met de database praten zonder eigen backend, terwijl de beveiliging in de database blijft, waar die niet kan worden omzeild door frontendcode aan te passen. De prijs is dat RLS goed moet zijn.

## Een Korte Geschiedenis van de Twee Sleutelformaten

Supabase gaf sleutels oorspronkelijk uit als JSON Web Tokens, met de rol erin gecodeerd: `anon` of `service_role`. Nieuwere projecten kunnen publishable keys (beginnend met `sb_publishable_`) en secret keys (beginnend met `sb_secret_`) gebruiken, die makkelijker onafhankelijk te vervangen en in te trekken zijn. Veel projecten gebruiken tijdens de overgang beide formaten. De regel is voor beide generaties hetzelfde: de openbare mag in clients, de geheime niet.

## Wat Aanvallers Werkelijk Doen met een Anon Key

Geautomatiseerde scanners doorzoeken routinematig websites, halen Supabase-URL's en anon keys uit JavaScript-bundels en tasten de API af. Gangbare pogingen zijn tabellen opvragen, alle rijen opvragen van veelgebruikte tabelnamen zoals `users`, `profiles`, `orders` of `messages`, en inserts proberen. Als RLS op een van deze is uitgeschakeld of te ruim is, is data binnen minuten blootgesteld, zonder dat een menselijke aanvaller specifiek aandacht aan uw app besteedt. Daarom biedt "niemand kent mijn app nog" geen bescherming.

## Gelaagde Verdediging Naast RLS

RLS is de belangrijkste maatregel, maar een paar extra lagen verkleinen het risico verder:

- **Beperk blootgestelde schema's,** zodat interne tabellen helemaal niet via de API bereikbaar zijn
- **Gebruik views met `security_invoker`** of beperkte functies om alleen de kolommen beschikbaar te maken die clients nodig hebben
- **Schakel CAPTCHA in bij registratie,** zodat aanvallers niet vrij geauthenticeerde accounts kunnen aanmaken om policies te testen
- **Beperk gevoelige bewerkingen met rate limits** via edge functions
- **Monitor logs** op ongebruikelijke querypatronen, zoals grote leesacties op tabellen die normale gebruikers zelden raken

## Sleutels Veilig Vervangen

Vervangen is het makkelijkst als het is gepland. Bewaar geheime sleutels alleen in opslag voor geheimen op de server, zodat ze op één plek kunnen worden vervangen, gebruik aparte sleutels voor staging en productie, en documenteer welke diensten welke sleutel gebruiken. Met het nieuwere sleutelformaat kunt u een nieuwe secret key aanmaken, uitrollen en daarna de oude intrekken, zonder downtime. Vervang sleutels wanneer iemand met toegang vertrekt, na elke vermoedelijke blootstelling, en periodiek als gewoonte.

## Een Mobiele App of Koppeling met een Derde Partij Controleren

Dezelfde regels gelden buiten uw webfrontend. Mobiele apps kunnen worden uitgepakt, dus beschouw alles erin als openbaar. Automatiseringstools zoals Zapier of Make horen nooit de secret key te krijgen; geef ze in plaats daarvan een speciaal, beperkt endpoint. Vraag u, voordat u een tool koppelt, af: als het account van deze tool werd gecompromitteerd, wat zou iemand dan kunnen met de inloggegevens die erin staan?

## Een Patroon uit de Praktijk: De "Tijdelijke" Servicesleutel

Een terugkerend verhaal in AI-gebouwde apps gaat zo: een functie moet rijen bijwerken die de policies van de huidige gebruiker niet toestaan, zoals een gebruiker die de dienstruil van een ander accepteert of een beheerder die een verzoek goedkeurt. De snelste manier om het te laten werken, is de service role key "tijdelijk" in de frontend te gebruiken. De functie werkt, de deadline wordt gehaald, en de sleutel blijft. Weken later staat de sleutel nog steeds in de bundel en geeft hij iedereen volledige toegang tot de database.

Het juiste patroon kost iets meer tijd, maar is standaard: maak een edge function die de aanroeper controleert, nagaat of de actie voor hem is toegestaan, de wijziging uitvoert met inloggegevens op de server en het vastlegt in een log. De frontend roept de functie aan met de normale sessie van de gebruiker. De sleutel verlaat de server nooit.

## Uw Eigen App in de Praktijk Controleren

Open uw app in een browser, open de ontwikkelaarstools, ga naar het netwerktabblad en herlaad de pagina. Klik op een verzoek naar uw Supabase-URL en bekijk de headers van het verzoek: u ziet de sleutel die wordt meegestuurd. Kopieer hem naar een JWT-decoder als het een oudere sleutel is en controleer de rol. Doorzoek daarna alle geladen JavaScript-bestanden op `service_role` en `sb_secret_`. Dit kost vijf minuten en geeft een definitief antwoord over de gevaarlijkste fout. Als u niets geheims vindt, gaat u verder met het testen van uw policies met twee gebruikersaccounts.

## De Regel in Eén Zin

Als u één ding onthoudt: de publishable- of anon key is een deur waar iedereen doorheen kan lopen, dus uw Row Level Security-policies zijn de sloten op elke kamer; de secret- of service role key is een loper, dus die mag uw server nooit verlaten. Al het andere in dit artikel volgt daaruit.

## De Productie-Inrichting die We Aanraden

- Anon- of publishable key in de frontend, service role- of secret key alleen in serveromgevingen
- RLS ingeschakeld op elke blootgestelde tabel, met policies getest met echte gebruikerssessies
- Bevoorrechte acties in edge functions die de aanroeper controleren
- Sleutels vervangen wanneer een teamlid met toegang vertrekt
- Geheimen uit de git-historie verwijderd

LaunchStudio richt dit in als onderdeel van productiewerk aan Supabase, meestal binnen een Launch Ready-pakket tussen €800 en €3.500. LaunchStudio wordt aangedreven door Manifera, een softwareontwikkelbedrijf met 11+ jaar ervaring en een ontwikkelcentrum in Ho Chi Minh City, gecoördineerd met klanten vanuit Amsterdam. Meer over het team op [de over-ons-pagina van Manifera](https://www.manifera.com/about-us/). De eigen uitleg van Supabase over [API-sleutels](https://supabase.com/docs/guides/api/api-keys) is de gezaghebbende bron.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Vrijwilligersapp voor een Festival met een Loper in de Bundel

Olivier Maes coördineert de vrijwilligers van een muziekfestival bij Leuven en bouwde Shiftwissel met Bolt en Supabase: vrijwilligers kiezen diensten, ruilen ze met elkaar en ontvangen de gegevens van hun polsbandje. Binnen twee weken meldden zich ongeveer 600 vrijwilligers aan.

Een vrijwilliger met een achtergrond in ontwikkeling stuurde Olivier een bericht: het JavaScript van de app bevatte een sleutel waarvan de gedecodeerde rol `service_role` was. Bolt had die gebruikt om de functie "dienst ruilen" te laten werken, omdat de policies van de anon key niet toestonden dat de ene vrijwilliger de dienst van een andere bijwerkte. Met die sleutel kon iedereen het telefoonnummer en adres van elke vrijwilliger lezen, of het volledige dienstrooster verwijderen.

LaunchStudio verving de sleutel binnen het uur en controleerde de logs op ongebruikelijke toegang, waarbij niets werd gevonden behalve de eigen test van de vrijwilliger. Engineers verplaatsten daarna de ruillogica naar een edge function die controleerde dat beide vrijwilligers akkoord waren, schakelden RLS in op alle tabellen met policies waarmee vrijwilligers alleen hun eigen gegevens en het openbare dienstrooster konden lezen, en richtten een stagingproject in voor verdere wijzigingen.

**Resultaat:** Shiftwissel verwerkte tijdens het festival ongeveer 1.100 dienstruilen zonder incidenten. Olivier informeerde de vrijwilligers transparant over de oplossing, en de organisatoren van het festival namen de app over voor het jaar daarop.

> *"De anon key stond in de code omdat hij daar hoort. De andere sleutel stond in de code omdat de AI een shortcut nodig had. Ik wist niet dat er een verschil was."*
> - **Olivier Maes, Oprichter, Shiftwissel (Leuven)**

**Kosten & Doorlooptijd:** €1.350 (vervanging van de sleutel, controle van de logs, edge function voor ruilen, RLS en staging) - afgerond in 4 werkdagen.

## Veelgestelde Vragen

### Moet ik de anon key van Supabase verbergen?

Nee, u kunt hem niet zinvol verbergen, en dat hoeft ook niet. Elke sleutel die door browsercode wordt gebruikt, is zichtbaar voor gebruikers. De anon- of publishable key is daarvoor ontworpen. Besteed de moeite in plaats daarvan aan correcte Row Level Security.

### Wat is het verschil tussen de anon key en de publishable key?

Ze dienen hetzelfde doel. De publishable key (`sb_publishable_...`) is het nieuwere sleutelformaat van Supabase, en de anon key is het oudere equivalent op basis van JWT. Beide zijn veilig in de browser met correcte RLS. Hun geheime tegenhangers zijn de service role key en de secret key.

### Wat moet ik doen als mijn service role key is blootgesteld?

Vervang of trek hem direct in via het Supabase-dashboard, verplaats code die hem gebruikte naar een serveromgeving, controleer de logs op verdachte activiteit en beoordeel of persoonsgegevens zijn ingezien. Onder de AVG moet een meldplichtig datalek binnen 72 uur worden gemeld.

### Waarom geeft Manifera prioriteit aan het omgaan met sleutels in AI-gebouwde apps?

Omdat blootgestelde geheime sleutels elke andere beveiligingsmaatregel tot decoratie maken. De 11+ jaar enterpriselevering van Manifera en de cybersecurity-achtergrond van Herre Roelevink zetten het beheer van geheimen bovenaan elke review, nog voor enig functiewerk.

### Kan een blootgestelde sleutel invloed hebben op hoe zoekmachines mijn site behandelen?

Indirect. Een gecompromitteerde database kan worden gebruikt om spam of kwaadaardige inhoud in uw pagina's te injecteren, waardoor uw site kan worden gemarkeerd of uit de index verdwijnt. Geheime sleutels buiten de frontend houden helpt dat te voorkomen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik de anon key van Supabase verbergen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. Sleutels in de browser zijn altijd zichtbaar en de anon- of publishable key is daarvoor ontworpen. Richt u op correcte Row Level Security." }
    },
    {
      "@type": "Question",
      "name": "Wat is het verschil tussen de anon key en de publishable key?",
      "acceptedAnswer": { "@type": "Answer", "text": "Hetzelfde doel: de publishable key is het nieuwere formaat, de anon key de oudere JWT. Hun geheime tegenhangers zijn de service role- en secret keys." }
    },
    {
      "@type": "Question",
      "name": "Wat moet ik doen als mijn service role key is blootgesteld?",
      "acceptedAnswer": { "@type": "Answer", "text": "Vervang hem direct, verplaats code die hem gebruikt naar de server, controleer de logs en beoordeel de toegang tot persoonsgegevens; meldplichtige datalekken onder de AVG moeten binnen 72 uur worden gemeld." }
    },
    {
      "@type": "Question",
      "name": "Waarom geeft Manifera prioriteit aan het omgaan met sleutels in AI-gebouwde apps?",
      "acceptedAnswer": { "@type": "Answer", "text": "Blootgestelde geheime sleutels maken andere beveiligingsmaatregelen waardeloos. De 11+ jaar levering van Manifera en de cybersecurity-achtergrond van Herre Roelevink zetten het beheer van geheimen voorop." }
    },
    {
      "@type": "Question",
      "name": "Kan een blootgestelde sleutel invloed hebben op hoe zoekmachines mijn site behandelen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirect. Een gecompromitteerde database kan spam of kwaadaardige inhoud injecteren, wat leidt tot markering of verwijdering uit de index." }
    }
  ]
}
</script>
