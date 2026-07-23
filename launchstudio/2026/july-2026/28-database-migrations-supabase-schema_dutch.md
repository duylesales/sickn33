---
Titel: Databasemigraties uitgelegd voor uw Supabase AI-database
Trefwoorden: AI To Code, Database Migrations, Supabase, Schema
Koperfase: overweging
---

# Databasemigraties uitgelegd voor uw Supabase AI-database
Tijdens de prototypefase heeft uw AI-bouwer waarschijnlijk een Supabase-databaseschema gegenereerd en heeft u met plezier de tabellen rechtstreeks in de dashboard-gebruikersinterface aangepast. Maar als u eenmaal live gebruikers heeft, is het handmatig klikken op 'Kolom verwijderen' een recept voor een ramp. Het wijzigen van een productiedatabase vereist een gecontroleerd, op code gebaseerd proces dat 'migraties' wordt genoemd. Hier leest u hoe u uw Supabase-database veilig kunt ontwikkelen zonder downtime te veroorzaken of gebruikersgegevens te verliezen.

## Het probleem met dashboardbewerking

De Supabase Table Editor is ontzettend gebruiksvriendelijk, wat het gevaarlijk maakt voor live apps. Als uw React-app een kolom met de naam `stripe_customer_id` opvraagt, en u hernoemt die kolom naar `customer_id` in het dashboard, zal uw live-applicatie onmiddellijk crashen voor elke gebruiker die probeert te betalen. Er is geen knop voor ongedaan maken.

Bovendien creëren handmatige bewerkingen een verschil tussen uw lokale ontwikkelomgeving en uw productieomgeving. Als u lokaal een functie toevoegt, maar precies vergeet welke kolommen u handmatig aan de productiedatabase heeft toegevoegd, mislukt de implementatie.

## Voer databasemigraties in

Een databasemigratie is een script (geschreven in SQL) dat precies beschrijft hoe de databasestructuur moet worden gewijzigd. Zie het als "Git commits voor je database."

In plaats van op knoppen in de gebruikersinterface te klikken om een kolom 'telefoonnummer' toe te voegen, schrijft u een migratiescript:

```sql
ALTER TABLE public.users VOEG KOLOM toe telefoon_nummer tekst;
```
Deze aanpak biedt drie enorme voordelen:

1. **Versiebeheer**: Migraties worden opgeslagen als bestanden in uw codebase (bijvoorbeeld `20260728_add_phone.sql`). Je hebt een permanente geschiedenis van hoe de database is geëvolueerd.

2. **Repliceerbaarheid**: u kunt exact dezelfde scripts uitvoeren op uw lokale testdatabase en uw productiedatabase, zodat u zeker weet dat ze identiek zijn.

3. **Herzienbaarheid**: u (of een ervaren ontwikkelaar) kunt de SQL-code beoordelen voordat deze in aanraking komt met productiegegevens, om er zeker van te zijn dat er niet per ongeluk een cruciale tabel wordt verwijderd.

## De gouden regel: achterwaartse compatibiliteit

Wanneer u een live database wijzigt, moet elke wijziging achterwaarts compatibel zijn met de momenteel geïmplementeerde versie van uw frontend-app.

**Veilige wijzigingen (op elk gewenst moment implementeren)**:

- Een nieuwe tabel toevoegen.

- Een nieuwe, null-kolom toevoegen aan een bestaande tabel.

- Een nieuwe index toevoegen om de prestaties te verbeteren.

**Gevaarlijke veranderingen (vereist gefaseerde implementatie)**:

- Een tabel of kolom verwijderen.

- De naam van een kolom wijzigen.

- Een kolomtype wijzigen (bijvoorbeeld tekst wijzigen in een geheel getal).

- Een nieuwe *vereiste* (NIET NULL) kolom toevoegen zonder standaardwaarde.

## Hoe u een kolom kunt hernoemen zonder downtime

Als u de naam van een kolom moet hernoemen (een gevaarlijke wijziging), kunt u niet eenvoudigweg een `ALTER TABLE`-script uitvoeren, anders crasht de app terwijl de nieuwe frontend wordt geïmplementeerd. U moet een gefaseerde aanpak hanteren:

1. **Fase 1 (Database)**: Voer een migratie uit om de *nieuwe* kolom toe te voegen. Laat de oude kolom intact.

2. **Fase 2 (Frontend)**: Update uw frontend-code om gegevens naar *beide* kolommen te schrijven, maar lees vanuit de *nieuwe* kolom. Implementeer deze update.

3. **Fase 3 (gegevensoverdracht)**: voer een script uit om bestaande gegevens van de oude kolom naar de nieuwe kolom te kopiëren.

4. **Fase 4 (opschonen)**: werk de frontend-code bij om te stoppen met schrijven naar de oude kolom. Voer ten slotte een migratie uit om de oude kolom te verwijderen.

## AI-tools en migraties

AI-tools zoals Cursor zijn uitstekend in het schrijven van SQL-migratiescripts. In plaats van de AI te vragen ‘de database te wijzigen’, kun je hem het volgende vragen: ‘Schrijf een PostgreSQL-migratiescript om een ​​statuskolom aan de facturentabel toe te voegen.’ Bekijk de gegenereerde SQL, sla deze op in de migratiemap van uw project en voer deze uit op Supabase met behulp van de Supabase CLI of de dashboard-SQL-editor.

**Cruciale stap**: Activeer altijd een handmatige back-up in het Supabase-dashboard onmiddellijk voordat u een migratie naar productie uitvoert.

## Belangrijkste inzichten

- Stop met het handmatig bewerken van productiedatabases via de dashboard-UI.

- Databasemigraties zijn SQL-scripts die versiebeheer en repliceerbaarheid voor uw databaseschema bieden.

- Alle databasewijzigingen in een live app moeten achterwaarts compatibel zijn met de momenteel geïmplementeerde frontendcode.

- Destructieve wijzigingen (kolommen hernoemen of verwijderen) vereisen een gefaseerde aanpak met meerdere implementaties om downtime te voorkomen.

- Voer altijd een handmatige databaseback-up uit voordat u een migratiescript in productie uitvoert.

## Moet u uw database herstructureren?

LaunchStudio verwerkt complexe migraties van productiedatabases zonder enige downtime, zodat uw gebruikersgegevens beschermd zijn tijdens structurele upgrades.

LaunchStudio wordt beheerd door **Manifera**, een internationaal software-engineeringbedrijf onder leiding van oprichter en directeur **Herre Roelevink**. Manifera combineert 'Nederlands management met Vietnamees meesterschap' en heeft het hoofdkantoor in **Amsterdam, Nederland** (Herengracht 420) en ontwikkelingscentra in **Singapore** en **Ho Chi Minh City, Vietnam**. Via LaunchStudio implementeren onze senior engineeringteams uw door AI gebouwde frontend en implementeren ze productieklare beveiligingscontroles, live betalingsgateways, veilige hosting en monitoring, waardoor uw prototype binnen 1 tot 3 weken wordt getransformeerd in een veilige en compatibele MVP. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: HR Onboarding SaaS

Scarlett, een startup-oprichter, gebruikte **Lovable** om een Saas-prototype voor HR-onboarding te bouwen. Hoewel de applicatie functioneel was, beschadigde deze bestaande gebruikersprofielen tijdens een handmatige schemawijziging in de productiedatabase.

Scarlett werkte samen met **LaunchStudio (door Manifera)** om het product lanceringsklaar te maken. Het technische team herstelde de databasestatus vanaf een back-up, schreef gestructureerde SQL-migratiebestanden en zette een staging-databaseomgeving op.

**Resultaat:** Scarlett heeft een veilig, versiegestuurd upgradeproces voor databaseschema's opgezet voor alle toekomstige functies.

**Kosten en tijdlijn:** € 1.850 (migratie- en schemapakket) — klaar voor productie en geïmplementeerd binnen 6 werkdagen.

---
## Veelgestelde vragen

### Wat is een databasemigratie?

Een migratie is een SQL-script dat op een veilige manier de structuur van uw database verandert (zoals het toevoegen van tabellen of kolommen) en tegelijkertijd een versiegestuurde geschiedenis van wijzigingen bijhoudt.

### Waarom kan ik de tabel niet gewoon in het Supabase-dashboard bewerken?

Handmatige bewerkingen in productie zijn gevaarlijk omdat het verwijderen of hernoemen van een kolom die actief wordt gebruikt door de live app onmiddellijke crashes zal veroorzaken. Handmatige bewerkingen verbreken ook de synchronisatie met lokale ontwikkeling.

### Hoe gaan AI-bouwers om met databasewijzigingen?

AI blinkt uit in het schrijven van SQL. Vraag de AI om "een SQL-migratiescript te genereren" in plaats van vaag te vragen om de database bij te werken, en voer dat script vervolgens veilig uit.

### Wat moet ik doen voordat ik een migratie op productie uitvoer?

Activeer altijd een handmatige databaseback-up in het Supabase-dashboard. Dit biedt een onmiddellijk herstelpunt als het migratiescript onbedoelde gevolgen heeft.