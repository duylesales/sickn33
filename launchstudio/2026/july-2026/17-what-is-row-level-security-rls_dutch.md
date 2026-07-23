---
Titel: "AI en beveiliging: Waarom uw app Row Level Security (RLS) nodig heeft"
Trefwoorden: AI And Security, Row Level Security, RLS, AI-app, Database
Koperfase: Bewustzijn
---

# AI en beveiliging: Waarom uw app Row Level Security (RLS) nodig heeft
Als je een AI-tool zoals Lovable hebt gebruikt om een ​​SaaS-prototype te bouwen dat is verbonden met Supabase, is de kans 80% dat je database fundamenteel onveilig is. De dader? Ontbrekende beveiliging op rijniveau (RLS). Zonder RLS kan elke ingelogde gebruiker mogelijk de gegevens van elke andere gebruiker in uw systeem openen, wijzigen of verwijderen. Hier volgt een uitleg van wat RLS is, waarom AI het negeert en hoe u dit kunt oplossen.

## De onzichtbare dreiging: een openbare database

Stel je voor dat je een hotel bouwt waar elke gast een sleutelkaart ontvangt. De sloten op de deuren controleren echter niet bij welke kamer de kaart hoort; ze controleren alleen of het een geldige hotelsleutel is. Elke gast kan elke deur openen.

Dit is precies hoe een Supabase-database werkt als Row Level Security is uitgeschakeld. Uw frontend-applicatie is mogelijk geprogrammeerd om de database alleen om 'gegevens van gebruiker A' te vragen, waardoor de app er bij normaal gebruik veilig uitziet. Maar als een kwaadwillende gebruiker het netwerkverkeer inspecteert en het API-verzoek wijzigt om te vragen naar "gegevens van gebruiker B", zal de database deze graag overhandigen. Het verifieerde dat de gebruiker was ingelogd, maar er werd niet gecontroleerd of hij of zij de gegevens bezat.

## Wat is beveiliging op rijniveau (RLS)?

Row Level Security is een functie van PostgreSQL (de database-engine die Supabase aandrijft) die de toegangscontrole van uw applicatiecode rechtstreeks naar de database-engine zelf verplaatst. Het fungeert als een onoverkomelijke uitsmijter.

Wanneer RLS is ingeschakeld, wordt elke afzonderlijke query die naar de database wordt verzonden, geëvalueerd op basis van een reeks beleidsregels die u definieert. Het meest voorkomende beleid ziet er als volgt uit:

> "Sta een gebruiker alleen toe deze rij te SELECTEREN (lezen) als de kolom `user_id` in deze rij overeenkomt met de ID van de gebruiker die het verzoek doet."
Met dit beleid zal de database, zelfs als een hacker de database expliciet om de gegevens van een andere gebruiker vraagt, een leeg resultaat retourneren. De beveiliging wordt op het laagst mogelijke niveau gehandhaafd.

## Waarom AI-bouwers RLS uit laten staan

Als RLS zo cruciaal is, waarom laten AI-tools zoals Lovable of Cursor het dan vaak uitgeschakeld?

AI-tools optimaliseren voor een functioneel prototype. Voor het configureren van RLS zijn specifieke regels nodig voor wie gegevens in verschillende tabellen (CRUD) kan maken, lezen, bijwerken en verwijderen. Als de AI de regels verkeerd raadt, breekt de applicatie: gebruikers klikken op een knop en er gebeurt niets omdat de database het verzoek heeft afgewezen. Om ervoor te zorgen dat het prototype een onmiddellijke ‘wauw’-factor biedt zonder wrijving, kiezen AI-bouwers vaak voor de weg van de minste weerstand: de database open laten.

## Hoe u uw RLS-status kunt controleren

U kunt uw kwetsbaarheidsstatus in minder dan twee minuten verifiëren:

1. Log in op uw Supabase Dashboard.

2. Navigeer naar de **Tabeleditor**.

3. Bekijk de lijst met uw tabellen. Als u naast een tabelnaam een ​​klein, ontgrendeld hangslotpictogram ziet, is RLS uitgeschakeld. Die tafel is kwetsbaar.

4. Als het hangslot vergrendeld is, klikt u erop om het actieve beleid te bekijken. Zorg ervoor dat er afzonderlijk beleid is voor SELECT-, INSERT-, UPDATE- en DELETE-bewerkingen.

## De oplossing implementeren

Het repareren van RLS omvat twee stappen voor elke tabel die gevoelige of gebruikersspecifieke gegevens bevat:

1. **RLS inschakelen**: Klik in Supabase op het ontgrendelingspictogram en schakel "RLS inschakelen" in.

2. **Schrijfbeleid**: u moet SQL-beleid maken dat het authenticatietoken van de gebruiker aan de gegevens koppelt. Een updatebeleid vereist bijvoorbeeld meestal dat `auth.uid() = user_id` wordt gecontroleerd.

Wees voorzichtig: slecht geschreven beleid kan legitieme gebruikers de toegang tot hun eigen gegevens ontzeggen of onbedoeld openbare toegang verlenen.

## Belangrijkste inzichten

- Row Level Security (RLS) beperkt de toegang tot de database, zodat gebruikers alleen hun eigen gegevens kunnen zien en wijzigen.

- AI-bouwers laten RLS vaak uitgeschakeld om ervoor te zorgen dat prototypes soepel werken zonder configuratiefouten.

- Zonder RLS kan elke geauthenticeerde gebruiker mogelijk de gegevens van andere gebruikers stelen of verwijderen door API-verzoeken te manipuleren.

- U moet RLS inschakelen en specifiek toegangsbeleid voor elke tabel schrijven voordat u deze voor echte gebruikers lanceert.

- RLS dwingt beveiliging af op het niveau van de database-engine, waardoor deze niet te omzeilen is door frontend-manipulatie.

## Beveilig uw database vóór de lancering

LaunchStudio controleert en implementeert robuust Row Level Security-beleid voor uw gehele Supabase-database, zodat de gegevens van uw gebruikers ondoordringbaar zijn.

LaunchStudio wordt beheerd door **Manifera**, een internationaal software-engineeringbedrijf onder leiding van oprichter en directeur **Herre Roelevink**. Manifera combineert 'Nederlands management met Vietnamees meesterschap' en heeft het hoofdkantoor in **Amsterdam, Nederland** (Herengracht 420) en ontwikkelingscentra in **Singapore** en **Ho Chi Minh City, Vietnam**. Via LaunchStudio implementeren onze senior engineeringteams uw door AI gebouwde frontend en implementeren ze productieklare beveiligingscontroles, live betalingsgateways, veilige hosting en monitoring, waardoor uw prototype binnen 1 tot 3 weken wordt getransformeerd in een veilige en compatibele MVP. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: Fitness Trainer CRM

Mason, de oprichter van een startup, gebruikte **Cursor** om een crm-prototype voor fitnesstrainers te bouwen. Hoewel de applicatie functioneel was, draaide deze zonder Row Level Security (RLS) op Supabase, wat betekent dat elke ingelogde trainer de klantnotities van andere trainers kon lezen en wijzigen.

Mason werkte samen met **LaunchStudio (door Manifera)** om het product lanceringsklaar te maken. Het technische team schakelde RLS in op alle databasetabellen en creëerde een strikt beleid dat overeenkomt met door de gebruiker geverifieerde UUID's.

**Resultaat:** Mason heeft alle klantgegevens beveiligd en strikte gegevensisolatie geverifieerd onder strenge tests met meerdere gebruikers.

**Kosten en tijdlijn:** € 1.200 (Security Hardening Package) — productieklaar en binnen 4 werkdagen geïmplementeerd.

---
## Veelgestelde vragen

### Wat is Row Level Security (RLS) precies?

Row Level Security beperkt de databasetoegang per rij. Het fungeert als uitsmijter op databaseniveau en zorgt ervoor dat de gebruiker die een verzoek indient, toestemming heeft om met die specifieke rij gegevens te communiceren.

### Waarom schakelen AI-bouwers RLS meestal uit?

AI-tools geven prioriteit aan het snel functioneel krijgen van uw applicatie. Het schrijven van complex beleid vereist context over uw bedrijfslogica. Om databasetoestemmingsfouten te voorkomen die de demo verbreken, laten AI-generatoren RLS uitgeschakeld.

### Hoe weet ik of RLS is ingeschakeld voor mijn Supabase-project?

Log in op Supabase, ga naar de Tabeleditor en zoek naar een hangslotpictogram naast uw tafels. Ontgrendeld betekent dat RLS is uitgeschakeld. Vergrendeld betekent dat het is ingeschakeld (maar u moet verifiëren dat het beleid correct is).

### Wat gebeurt er als ik start zonder RLS?

Lanceren zonder RLS is een ernstige kwetsbaarheid. Elke gebruiker kan API-verzoeken manipuleren om toegang te krijgen tot de gegevens van andere gebruikers of deze te verwijderen, waardoor u wordt blootgesteld aan datalekken en juridische straffen.