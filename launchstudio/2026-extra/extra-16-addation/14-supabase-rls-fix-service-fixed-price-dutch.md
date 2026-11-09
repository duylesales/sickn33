---
Titel: "Supabase RLS-Fixservice: Row Level Security tegen een Vaste Prijs voor Apps Gebouwd met AI"
Trefwoorden: supabase rls fixservice, row level security repareren, supabase beveiligingsservice, rls lovable app repareren, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Supabase RLS-Fixservice: Row Level Security tegen een Vaste Prijs voor Apps Gebouwd met AI

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Supabase RLS-Fixservice: Row Level Security tegen een Vaste Prijs voor Apps Gebouwd met AI",
  "description": "Een dienst tegen een vaste prijs die gaten in de Supabase Row Level Security vindt en dicht in apps gebouwd met Lovable, Bolt, v0, Cursor of Claude Code. Deze pagina legt uit wat de dienst omvat, hoe het werk wordt gedaan, wat u ontvangt, gebruikelijke doorlooptijden en prijzen, hoe u weet of u de dienst nodig heeft en hoe LaunchStudio, ondersteund door Manifera, uw app werkend houdt terwijl blootstelling van data wordt gedicht.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-08-09",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/supabase-rls-fix-service-fixed-price" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" },
    { "@type": "CreativeWork", "name": "Supabase: Storage access control", "url": "https://supabase.com/docs/guides/storage/security/access-control" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A01 Broken Access Control", "url": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/" },
    { "@type": "CreativeWork", "name": "GDPR Article 32: Security of processing", "url": "https://gdpr-info.eu/art-32-gdpr/" }
  ]
}
</script>

Draait uw app op Supabase, dan is Row Level Security het slot op elke deur. De browser praat met een publieke sleutel rechtstreeks met uw database, en RLS-policies bepalen welke rijen elke gebruiker mag lezen, aanmaken, wijzigen of verwijderen. Ontbreken die policies, zijn ze te ruim of inconsistent, dan kan elke ingelogde gebruiker, en soms iedereen op internet, data opvragen die nooit voor hem bedoeld was.

AI-builders zoals Lovable, Bolt en v0 maken tabellen en policies aan om functies te laten werken. Ze ontwerpen zelden toegangsregels rond uw bedrijf: welke klant eigenaar is van welk record, wat een teamlid mag zien, wat een beheerder mag wijzigen. Het resultaat komt veel voor en is ernstig, en het blijft meestal onzichtbaar totdat een klant, een beveiligingsreviewer of een aanvaller het vindt.

De RLS-fixservice van LaunchStudio is een gerichte opdracht tegen een vaste prijs om elk gat in de toegangscontrole van uw Supabase-project te vinden en te dichten, zonder uw app opnieuw te bouwen of de functies te breken waar uw gebruikers op vertrouwen.

## Belangrijkste Punten

- **De dienst omvat elke tabel, view, functie en storagebucket** in uw Supabase-project, afgezet tegen de rollen in uw product.
- **Fixes worden geschreven als geteste policies,** geverifieerd met echte accounts voor elke rol via de API, niet alleen in het dashboard.
- **Uw app blijft werken:** we controleren na wijzigingen elk scherm en elke functie, en repareren queries die op kapotte policies leunden.
- **U ontvangt documentatie en geautomatiseerde tests,** zodat toekomstige wijzigingen met AI gaten niet ongemerkt weer kunnen openen.
- **Gebruikelijke prijs: €800-€3.500 binnen Launch Ready,** opgeleverd in drie tot tien werkdagen, afhankelijk van het aantal tabellen en rollen.

## Signalen Dat U Deze Dienst Nodig Heeft

- U heeft uw app nooit met twee aparte accounts via de API getest
- De security advisor van Supabase of de beveiligingsscan van Lovable meldt tabellen zonder RLS
- Policies bevatten voorwaarden als `true` of alleen `auth.uid() is not null`
- Uw app kent organisaties, teams of klanten, en u weet niet zeker of de data tussen hen gescheiden is
- Een zakelijke klant stuurde een beveiligingsvragenlijst met vragen over isolatie tussen tenants
- U gebruikt storagebuckets voor documenten, foto's of facturen en weet niet zeker wie ze kan lezen
- Er komt een technische review door een investeerder aan

Gelden er twee of meer, dan is het risico waarschijnlijk reëel. OWASP plaatst gebrekkige toegangscontrole bovenaan de risico's voor webapplicaties, en in Supabase-apps is het de meest voorkomende bevinding die we zien.

## Wat de Dienst Omvat

| Gebied | Wat we reviewen en repareren |
| --- | --- |
| Tabellen | RLS ingeschakeld op elke tabel met gebruikers- of bedrijfsdata; aparte policies voor select, insert, update en delete |
| Isolatie tussen tenants | Grenzen tussen organisaties, teams of klanten afgedwongen op elke rij |
| Rollen | Beheerder, lid, gast, klant en andere rollen gekoppeld aan precieze rechten |
| Views | Views die RLS omzeilen vervangen of beveiligd |
| Functies | Databasefuncties en RPC-endpoints gecontroleerd op escalatie van rechten, inclusief security definer-functies |
| Opslag | Bucketpolicies voor uploads en downloads, privébuckets en signed URL's |
| Edge functions | Gebruik van de service role key gereviewd, met afgedwongen gebruikerscontext waar nodig |
| Clientcode | Frontendqueries die op kapotte policies leunden, aangepast |
| Prestaties | Policies zo geschreven dat ze snel blijven met indexen en efficiënte patronen |
| Tests | Geautomatiseerde negatieve autorisatietests per rol |

## Hoe het Werk Wordt Gedaan

**1. Toegangsmodel.** We beginnen met een korte sessie om af te spreken wie wat mag zien en doen. U beschrijft uw gebruikers in zakelijke termen; wij vertalen dat naar een model van rollen en eigendom. Vaak is dit de eerste keer dat de toegangsregels van uw product op papier komen.

**2. Inventarisatie.** We brengen elke tabel, view, functie, bucket en edge function in kaart, met de huidige policies en hoe de app ze gebruikt.

**3. Test op blootstelling.** Met testaccounts voor elke rol, bij voorkeur in twee aparte organisaties, bevragen we de API rechtstreeks, zoals een aanvaller met uw publieke sleutel zou doen. Elke bevinding wordt vastgelegd met bewijs.

**4. Fixen op staging.** Policies worden herschreven op een stagingkopie van uw project, met migraties die in uw repository worden opgeslagen. Waar de app op te ruime toegang leunde, passen we de queries aan.

**5. Verifiëren.** Geautomatiseerde tests bevestigen dat elke rol kan wat hij moet kunnen en niets meer. We klikken voor elke rol door de belangrijkste journeys van de app om zeker te weten dat er niets kapot is.

**6. Uitbrengen.** Migraties worden via een gecontroleerde deployment in productie doorgevoerd, met monitoring tijdens en na de release.

**7. Documenteren.** U ontvangt een kort document over toegangscontrole en instructies voor uw AI-tools, zodat toekomstige prompts dezelfde regels volgen.

## Wat U Ontvangt

- Een bevindingenrapport in begrijpelijke taal, met elke gevonden blootstelling en hoe die is opgelost
- Row Level Security-policies en storagepolicies als migraties met versies in uw repository
- Negatieve autorisatietests die bij elke toekomstige wijziging draaien
- Een overzicht van de toegangscontrole met rollen en regels
- Projectinstructies voor Lovable, Cursor of Claude Code met de patronen voor policies die gevolgd moeten worden
- 48 uur support na de lancering

## Gebruikelijke Bevindingen

| Bevinding | Impact |
| --- | --- |
| Tabel zonder RLS | Iedereen met de publieke sleutel kan alle rijen lezen en wijzigen |
| Policy met `true` | Gelijk aan geen bescherming voor die bewerking |
| Policy die alleen inloggen vereist | Elke gebruiker kan de records van elke andere gebruiker lezen |
| Ontbrekende controle bij insert | Gebruikers kunnen records in andere organisaties aanmaken |
| Update zonder controle op eigendom | Gebruikers kunnen data van anderen wijzigen, ook rollen |
| Rol opgeslagen in een bewerkbare profielkolom | Gebruikers kunnen zichzelf tot beheerder promoveren |
| Openbare storagebucket | Privébestanden bereikbaar via een URL |
| Security definer-functie zonder controles | Omzeilt alle policies wanneer hij wordt aangeroepen |
| Service role key in de frontend | Volledige databasetoegang voor iedereen |

Elk van deze punten is te repareren zonder uw interface te veranderen.

## Wat We van U Nodig Hebben

De dienst is zo opgezet dat hij weinig van uw tijd vraagt. Doorgaans hebben we nodig:

- **Een kennismakingsgesprek van 15 minuten** om het product en de gebruikers te begrijpen
- **Leestoegang** tot het Supabase-project en de coderepository, verleend via uitnodigingen
- **Dertig tot zestig minuten** om het toegangsmodel af te spreken: wie wat mag zien en doen
- **Testaccounts** of toestemming om ze op staging aan te maken
- **Een korte controle** van de belangrijkste journeys op staging vóór de release, bij voorkeur door u of iemand die het product goed kent

Al het andere, waaronder de inventarisatie, het testen, de fixes, migraties en documentatie, nemen onze engineers voor hun rekening.

## Vragen van Zakelijke Klanten, en Hoe U Ze Kunt Beantwoorden

Na de fix kunt u veelgestelde beveiligingsvragen met vertrouwen en bewijs beantwoorden:

| Vraag van de klant | Antwoord dat u kunt geven |
| --- | --- |
| Hoe is onze data gescheiden van die van andere klanten? | Elke tabel dwingt in de database Row Level Security per organisatie af, geverifieerd met geautomatiseerde tests |
| Kunnen uw medewerkers onze data zien? | Alleen gedefinieerde rollen, en toegang wordt vastgelegd waar auditlogging is ingericht |
| Wie kan onze documenten downloaden? | Bestanden staan in privéopslag en zijn alleen toegankelijk voor geautoriseerde gebruikers via kortlevende signed links |
| Hoe voorkomt u regressies? | Autorisatietests draaien bij elke wijziging vóór de deployment |
| Waar wordt onze data opgeslagen? | In de Supabase-regio van uw project, bijvoorbeeld Frankfurt |

Dit is vaak het verschil tussen een vastgelopen inkoopproces en een getekend contract.

## Policies Correct Houden na de Fix

De meeste RLS-problemen komen terug via nieuwe functies: een nieuwe tabel zonder policies, een prompt die een policy versoepelt om een functie te laten werken, een nieuwe functie die de service role key gebruikt. De tests en projectinstructies die we leveren beschermen hiertegen, maar een paar gewoonten helpen:

- **Review elke migratie** die tabellen aanmaakt of policies wijzigt voordat die productie bereikt.
- **Draai de security advisor van Supabase** na grote wijzigingen.
- **Vraag uw AI-tool om policies en tests toe te voegen** voor elke nieuwe tabel, zoals beschreven in de projectinstructies.
- **Herhaal de test met twee accounts** vóór belangrijke releases.

Blijft uw team snel bouwen, dan vangt een periodieke review, bijvoorbeeld elk kwartaal, afwijkingen vroeg af.

## Prijs en Doorlooptijd

| Omvang van het project | Gebruikelijke scope | Indicatieve prijs | Gebruikelijke duur |
| --- | --- | --- | --- |
| Klein | Tot ongeveer 10 tabellen, 2-3 rollen, één bucket | Onderkant van €800-€3.500 | 3-5 werkdagen |
| Middel | 10-25 tabellen, organisaties en teams, meerdere buckets | Midden van de range | 5-8 werkdagen |
| Groter | Veel tabellen, complexe rollen, functies en integraties | Bovenkant, of binnen Launch & Grow | 8-10 werkdagen |

U ontvangt een vaste offerte na een gesprek van 15 minuten en een korte blik met alleen leestoegang op uw project. De prijs verandert halverwege niet. Heeft u ook betalingen, beheerde hosting, back-ups en doorlopende support nodig, dan past het werk in **Launch & Grow** (€2.500-€7.500 plus €49 per maand). Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een eerste indicatie.

## Waarom Niet Gewoon de AI-Tool Vragen het te Repareren?

AI-tools kunnen policies schrijven als ze precies te horen krijgen wat ze moeten doen. De moeilijkheid zit in weten wat u ze moet vertellen: welke tabellen welke regels nodig hebben, hoe rollen op elkaar inwerken, welke functies policies omzeilen en hoe u het resultaat via de API test. De prompt "beveilig mijn database" levert vaak policies op die redelijk lijken maar nog steeds toegang tussen tenants toestaan, of functies breken zodat de volgende prompt ze weer versoepelt. Een gestructureerde review met tests geeft u regels waarop u kunt vertrouwen, en instructies die uw AI-tool daarna beter maken.

## Wat Niet Is Inbegrepen

Om de prijs vast te houden, is de scope expliciet. De RLS-fixservice omvat geen herontwerp van uw interface, geen nieuwe functies, geen migratie naar een andere database en geen formele penetratietest door een onafhankelijke tester. Brengt de review andere ernstige problemen aan het licht, zoals blootgestelde sleutels of kapotte betaalwebhooks, dan melden we die en offreren we de fixes apart, of nemen we ze met uw akkoord op in een bredere Launch Ready-scope.

## Waarom Oprichters voor LaunchStudio Kiezen

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, 160+ opgeleverde projecten en 120+ engineers, met diepgaande PostgreSQL-ervaring op enterprisesystemen. Herre Roelevink, oprichter van Manifera en CEO van LaunchStudio, was medeoprichter van het cybersecuritybedrijf dat nu CFLW Cyber Strategies heet, en daarom is toegangscontrole het eerste wat we in elk project controleren. Oprichters ontmoeten het team aan de Herengracht 420 in Amsterdam; de engineering gebeurt in het ontwikkelcentrum van Manifera aan de Pho Quang Street in Ho Chi Minh City, met een hub aan de Tras Street in Singapore.

We werken in uw repository en uw Supabase-project, met toegang die u verleent en kunt intrekken. Uw frontend blijft intact, en uw app blijft compatibel met de AI-tools die u gebruikt. Zie voor achtergrond over veelgemaakte fouten onze [gids voor een Supabase RLS-audit](https://launchstudio.eu/nl/blog/supabase-rls-audit-the-policy-mistakes-we-find-most), en voor prestaties onze gids over [prestaties van Row Level Security](https://launchstudio.eu/nl/blog/row-level-security-performance-in-supabase).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Het Klantportaal Waar Elke Klant op Eén Query Afstand Was

Joyce Vermeulen heeft een klein administratiekantoor in Hoorn en bouwde Klantmap met Lovable en Supabase: een portaal waar ongeveer 180 klanten bonnetjes en bankafschriften uploaden, en haar team de btw-aangiften per kwartaal voorbereidt. Een nieuwe klant die in de IT werkte, stelde tijdens de onboarding een eenvoudige vraag: "Hoe zorgt u ervoor dat andere klanten mijn documenten niet kunnen zien?" Joyce besefte dat ze het niet wist.

De test op blootstelling gaf snel antwoord. De documententabel had een select-policy waarmee elke ingelogde gebruiker alle rijen kon lezen, zodat een klant via de API de documentnamen en metadata van elke andere klant kon opvragen. De storagebucket voor uploads was openbaar, met bestandspaden op basis van klantnamen. In de profielentabel konden gebruikers hun eigen rolkolom bijwerken, en een databasefunctie voor de kwartaaloverzichten draaide als security definer zonder de aanroeper te controleren.

LaunchStudio sprak met Joyce een toegangsmodel af: klanten zien alleen hun eigen documenten en berichten, medewerkers zien de klanten die aan hen zijn toegewezen, en Joyce als eigenaar ziet alles. Policies werden voor alle elf tabellen herschreven met aparte regels per bewerking, rollen verhuisden naar een beschermde tabel, de overzichtsfunctie kreeg een expliciete rechtencontrole, en de bucket werd privé met policies per klantmap en signed URL's. Negatieve autorisatietests dekten elke rol, de frontendqueries die op ruime toegang leunden werden aangepast, en projectinstructies legden de patronen vast voor toekomstige Lovable-sessies.

**Resultaat:** De fixes gingen vijf werkdagen na het eerste gesprek live, zonder wijziging aan de interface van het portaal. Joyce stuurde haar IT-klant een beschrijving van één pagina van de toegangsregels, en gebruikte hetzelfde document later om de beveiligingsvragenlijst van een grotere klant te beantwoorden.

> *"Ik kon eindelijk de vraag beantwoorden die elke klant zou moeten stellen. En ik kon het antwoord bewijzen met tests."*
> - **Joyce Vermeulen, Oprichter, Klantmap (Hoorn)**

**Kosten & Doorlooptijd:** €1.850 (Launch Ready-pakket: toegangsmodel, RLS- en storagepolicies, fixes in functies, tests en documentatie) - afgerond in 5 werkdagen.

## Veelgestelde Vragen

### Wat kost een Supabase RLS-fix?

De meeste projecten vallen binnen de Launch Ready-range van €800 tot €3.500, afhankelijk van het aantal tabellen, rollen, functies en storagebuckets. U ontvangt een vaste offerte na een gesprek van 15 minuten en een korte blik op uw project, voordat er werk begint.

### Breekt het repareren van RLS mijn app?

Dat kan als het slordig gebeurt, omdat sommige functies op te ruime toegang leunen. Daarom repareren we eerst op staging, passen we getroffen queries aan, draaien we geautomatiseerde tests voor elke rol en klikken we door de belangrijkste journeys voordat we naar productie gaan.

### Moet ik u toegang geven tot mijn productiedatabase?

We beginnen met leestoegang om het project te reviewen en werken op een stagingkopie voor de fixes. Wijzigingen in productie lopen via migraties in uw repository en een gecontroleerde deployment. Toegang wordt via uw accounts verleend en kan op elk moment worden ingetrokken.

### Waarom doet de cybersecurityachtergrond van Manifera ertoe bij RLS?

Toegangscontrole is een beveiligingsdiscipline, niet alleen een database-instelling. De CEO van Manifera komt uit de cybersecurity en het bedrijf beveiligt al 11+ jaar enterprisesystemen, dus LaunchStudio test policies zoals een aanvaller dat zou doen, via de API, niet alleen in het dashboard.

### Helpt het repareren van RLS bij vertrouwen van klanten en zichtbaarheid?

Ja. Als u isolatie tussen tenants kunt beschrijven en bewijzen, verkort dat beveiligingsreviews en inkoopprocessen, en een openbare pagina over beveiliging die uw aanpak uitlegt, helpt zakelijke kopers, zoekmachines en AI-antwoordmachines uw product als betrouwbaar te herkennen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat kost een Supabase RLS-fix?",
      "acceptedAnswer": { "@type": "Answer", "text": "De meeste projecten vallen binnen €800-€3.500, afhankelijk van tabellen, rollen, functies en buckets, met een vaste offerte na een gesprek van 15 minuten." }
    },
    {
      "@type": "Question",
      "name": "Breekt het repareren van RLS mijn app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Niet met fixes op staging, aangepaste queries, geautomatiseerde tests per rol en handmatige controles vóór de release." }
    },
    {
      "@type": "Question",
      "name": "Moet ik u toegang geven tot mijn productiedatabase?",
      "acceptedAnswer": { "@type": "Answer", "text": "Leestoegang voor de review; fixes op staging en wijzigingen in productie via migraties en een gecontroleerde deployment, op elk moment in te trekken." }
    },
    {
      "@type": "Question",
      "name": "Waarom doet de cybersecurityachtergrond van Manifera ertoe bij RLS?",
      "acceptedAnswer": { "@type": "Answer", "text": "Toegangscontrole is een beveiligingsdiscipline; LaunchStudio test policies via de API zoals een aanvaller zou doen." }
    },
    {
      "@type": "Question",
      "name": "Helpt het repareren van RLS bij vertrouwen van klanten en zichtbaarheid?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja; aantoonbare isolatie tussen tenants verkort reviews en helpt kopers en AI-machines het product te vertrouwen." }
    }
  ]
}
</script>
