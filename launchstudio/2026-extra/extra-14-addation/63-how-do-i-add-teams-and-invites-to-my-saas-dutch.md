---
Titel: "Hoe Voeg Ik Teams en Uitnodigingen Toe aan Mijn AI-Gebouwde SaaS?"
Trefwoorden: teams toevoegen aan saas, teamuitnodigingen supabase, organisaties lovable-app, b2b saas-accounts, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: SaaS-Oprichter Scale-Up
---

# Hoe Voeg Ik Teams en Uitnodigingen Toe aan Mijn AI-Gebouwde SaaS?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Voeg Ik Teams en Uitnodigingen Toe aan Mijn AI-Gebouwde SaaS?",
  "description": "De stap van losse gebruikers naar teams maakt van een tool een B2B-SaaS. Deze gids behandelt het datamodel, de uitnodigingsflow, rollen, facturering per organisatie en de migratie van bestaande accounts voor één gebruiker in een app met Supabase.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-11",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-do-i-add-teams-and-invites-to-my-saas" },
  "citation": [
    { "@type": "CreativeWork", "name": "OWASP Authorization Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html" },
    { "@type": "CreativeWork", "name": "Supabase: Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A01 Broken Access Control", "url": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/" },
    { "@type": "CreativeWork", "name": "GDPR Article 28: Processor", "url": "https://gdpr-info.eu/art-28-gdpr/" }
  ]
}
</script>

**Kort antwoord:** voer drie tabellen in (organisaties, lidmaatschappen met een rol, en uitnodigingen), verplaats het eigendom van bedrijfsgegevens van gebruikers naar organisaties, herschrijf Row Level Security zodat die lidmaatschap controleert in plaats van `user_id`, bouw een uitnodigingsflow met verlopende tokens die door een serverfunctie wordt afgehandeld, en koppel facturering aan de organisatie in plaats van aan de gebruiker. Migreer daarna elke bestaande gebruiker naar een persoonlijke organisatie, zodat er niets breekt.

## Belangrijkste Punten

- **Teams toevoegen maakt van een tool voor één gebruiker een B2B-SaaS:** gegevens gaan van gebruikers naar organisaties.
- **Drie tabellen doen het meeste werk:** organisaties, lidmaatschappen met rollen en uitnodigingen met verlopende tokens.
- **Elke Row Level Security-policy verandert** van `user_id = auth.uid()` naar controles op lidmaatschap via een hulpfunctie.
- **Facturering wordt aan de organisatie gekoppeld,** met limieten op het aantal plaatsen die in de uitnodigingsflow worden afgedwongen.
- **Bestaande gebruikers migreren naar persoonlijke organisaties,** zodat er voor huidige klanten niets breekt.

## Waarom Dit een Grotere Wijziging Is dan het Lijkt

De meeste AI-gebouwde apps beginnen met "elke gebruiker bezit de eigen gegevens" (`user_id = auth.uid()`). Teams veranderen de vraag in "welke organisatie bezit deze gegevens, en is deze gebruiker lid met de juiste rol?" Dat raakt het datamodel, elke policy, de facturering en de interface. Het is goed te doen; het moet alleen als één wijziging worden gepland, niet functie voor functie met prompts.

## Het Datamodel

| Tabel | Belangrijkste kolommen |
| --- | --- |
| `organisations` | id, naam, abonnement, klant-ID voor facturering |
| `memberships` | organisation_id, user_id, rol (owner, admin, member) |
| `invitations` | organisation_id, e-mailadres, rol, token-hash, expires_at, accepted_at |
| Bedrijfstabellen | `organisation_id` toevoegen, `created_by` behouden voor de geschiedenis |

## Policies

Vervang controles op eigendom door controles op lidmaatschap via een hulpfunctie, bijvoorbeeld `is_member(organisation_id)` voor lezen en `has_org_role(organisation_id, 'admin')` voor het beheren van leden of facturering. Ons artikel over [rollen en beheerpanelen](https://launchstudio.eu/nl/blog/how-to-add-roles-and-an-admin-panel-to-a-lovable-app) toont het patroon met hulpfuncties.

## De Uitnodigingsflow

1. Een beheerder voert een e-mailadres en rol in
2. Een serverfunctie controleert de rol van de beheerder, maakt een uitnodiging aan met een willekeurig token (gehasht opgeslagen) en een vervaldatum, en verstuurt een e-mail
3. De uitgenodigde klikt op de link en registreert zich of logt in
4. Een serverfunctie verifieert het token, controleert of het e-mailadres overeenkomt, maakt het lidmaatschap aan en markeert de uitnodiging als geaccepteerd

Regels die het afdwingen waard zijn: uitnodigingen verlopen, kunnen worden ingetrokken, kunnen maar één keer worden geaccepteerd, en er gelden limieten om misbruik te voorkomen.

## Rollen die de Meeste B2B-Behoeften Dekken

| Rol | Mag |
| --- | --- |
| Owner | Alles, inclusief facturering en het verwijderen van de organisatie |
| Admin | Leden en instellingen beheren |
| Member | Het product gebruiken |

Begin hiermee; voeg alleen eigen rollen toe wanneer klanten daarom vragen.

## Facturering per Organisatie

Koppel de klant bij Stripe of Mollie aan de organisatie. Bepaal of u per plaats, per organisatie of op basis van gebruik rekent, en dwing limieten op het aantal plaatsen af in de uitnodigingsfunctie.

## Bestaande Gebruikers Migreren

Maak voor elke bestaande gebruiker een persoonlijke organisatie aan, maak hen owner en stel in een migratie `organisation_id` in op hun records. Test op staging met een kopie van realistische gegevens voordat u het in productie uitvoert.

## Waarom Teams de Omzet Verhogen

B2B-klanten kopen voor teams, niet voor individuen. Teamaccounts verhogen de gemiddelde omzet per klant via plaatsen of abonnementen met niveaus, verbeteren het behoud van klanten omdat een overstap veel mensen raakt, en openen deuren naar grotere bedrijven. Ze brengen ook verwachtingen mee: rollen, uitnodigingen, gedeelde gegevens, beheerinstellingen en facturering die aansluit bij hoe bedrijven inkopen. Door dit samen te plannen, voorkomt u een lappendeken van functies die nooit helemaal passen.

## Het Lidmaatschapsmodel Ontwerpen

Een lidmaatschapsmodel beantwoordt drie vragen: wie hoort bij welke organisatie, met welke rol, en wat mag elke rol? Houd het in het begin eenvoudig:

| Rol | Gangbare rechten |
| --- | --- |
| Owner | Facturering, het verwijderen van de organisatie, alles wat een admin kan |
| Admin | Leden uitnodigen en verwijderen, rollen wijzigen (behalve owner), instellingen |
| Member | Het product gebruiken binnen de organisatie |

Sla rollen op in de tabel met lidmaatschappen, nooit in het profiel van de gebruiker waar ze bewerkt kunnen worden. Dwing rechten af in Row Level Security-policies en serverfuncties, met hulpfuncties zoals `is_member(org_id)` en `has_role(org_id, 'admin')`. Het Authorization Cheat Sheet van OWASP raadt precies dit patroon aan: gecentraliseerde controles op de server die standaard weigeren.

## Gebruikers in Meerdere Organisaties

Consultants, bureaus en freelancers horen vaak bij meerdere klantorganisaties. Ondersteun dit vanaf het begin: laat gebruikers wisselen tussen organisaties, toon de huidige organisatie duidelijk in de interface en neem het organisatie-ID op in elke query. Policies op basis van lidmaatschap gaan vanzelf goed om met gebruikers in meerdere organisaties, zolang elke tabel met organisatiegegevens een kolom `organisation_id` heeft.

## Randgevallen bij Uitnodigingen

Uitnodigingen in de praktijk roepen vragen op die u vóór de lancering moet beantwoorden:

- **De uitgenodigde heeft al een account:** koppel de uitnodiging bij acceptatie aan het bestaande account
- **De uitgenodigde gebruikt een ander e-mailadres:** bepaal of acceptatie met een ander adres mag; het is veiliger om het uitgenodigde adres te vereisen
- **De uitnodiging verloopt:** toon een duidelijke melding en laat beheerders opnieuw versturen
- **De limiet op plaatsen is bereikt:** blokkeer de uitnodiging met een melding die een upgrade voorstelt
- **Een lid wordt verwijderd:** trek de toegang direct in en bepaal wat er gebeurt met content die dat lid heeft gemaakt

Door deze gevallen expliciet af te handelen, voorkomt u zowel beveiligingslekken als gefrustreerde klanten.

## Eigendom van Gegevens als Leden Vertrekken

Wanneer iemand een bedrijf verlaat, moet het account de toegang tot de gegevens van de organisatie verliezen, maar de gegevens zelf horen meestal bij de organisatie en moeten blijven. Bewaar `created_by` voor de geschiedenis, draag zo nodig het eigendom van items over en verwijder nooit content van de organisatie omdat één lid vertrok. Voor de AVG kunnen de persoonsgegevens van het individu, zoals het profiel, worden verwijderd of geanonimiseerd, terwijl de records van de organisatie onder controle van de klant als verwerkingsverantwoordelijke blijven.

## Instellingen en Beveiliging op Organisatieniveau

Zakelijke klanten willen vaak controle: tweestapsverificatie verplichten voor alle leden, inloggen beperken tot hun e-maildomein, een auditlog van wijzigingen in leden bekijken en hun gegevens exporteren. Deze functies maken vaak het verschil tussen een pilot en een getekend contract met een grotere klant. Bouw ze op hetzelfde lidmaatschapsmodel, afgedwongen op de server.

## Migratie Zonder Verstoring

Het migreren van bestaande accounts voor één gebruiker is meestal het riskantste deel. Schrijf de migratie als een script dat per gebruiker één organisatie aanmaakt, de gebruiker owner maakt en `organisation_id` instelt op al hun records. Repeteer het op een kopie in staging met realistische gegevens, controleer dat elke gebruiker precies de eigen eerdere gegevens ziet en niets anders, en voer het daarna in een rustige periode in productie uit. Werk de policies in dezelfde release bij, zodat er geen moment is waarop gegevens onbeschermd zijn.

## Factureringsmodellen voor Teams

| Model | Hoe het werkt | Het meest geschikt voor |
| --- | --- | --- |
| Per plaats | Prijs per actief lid, aantal bijgewerkt bij uitnodigen of verwijderen | Samenwerkingstools waarbij elke gebruiker waarde krijgt |
| Abonnementen met niveaus | Vaste prijs voor maximaal N leden | Eenvoudigere prijzen, voorspelbare facturen |
| Per organisatie | Eén prijs ongeacht het aantal leden | Producten waarbij maar een paar gebruikers per bedrijf actief zijn |
| Op basis van gebruik | Prijs per transactie, document of actie | Producten waarvan de waarde meegroeit met het volume |

Koppel het abonnement aan de organisatie, laat alleen owners of beheerders van facturering het wijzigen, en dwing limieten af op de server: een uitnodiging die de limiet op plaatsen zou overschrijden, moet mislukken met een duidelijke melding over upgraden.

## Een Teamopzet Testen

Test teamfuncties vóór de lancering met minstens twee organisaties en drie rollen. Controleer dat leden van de ene organisatie de gegevens van de andere niet kunnen zien via de interface of de API, dat leden geen anderen kunnen uitnodigen of rollen kunnen wijzigen, dat beheerders de owner niet kunnen verwijderen, dat verlopen of ingetrokken uitnodigingen niet kunnen worden geaccepteerd en dat het verwijderen van een lid de toegang direct intrekt. Automatiseer de test tussen organisaties, zodat toekomstige wijzigingen die niet ongemerkt kunnen breken.

## De Verandering Communiceren aan Bestaande Gebruikers

Wanneer bestaande losse gebruikers teamfuncties krijgen, leg dan uit wat er is veranderd: hun gegevens staan nu in een persoonlijke werkruimte die zij bezitten, ze kunnen collega's uitnodigen, en de facturering kan naar de werkruimte verhuizen. De meeste gebruikers verwelkomen de verandering, vooral wanneer die de samenwerking mogelijk maakt waar ze om vroegen. Duidelijke meldingen in de app en een korte e-mail verminderen verwarring.

## Veelgemaakte Fouten

- Een tabel voor teams toevoegen zonder de bestaande policies te wijzigen
- Rollen opslaan in profielen die gebruikers kunnen bewerken
- Abonnementen in een teamproduct aan individuele gebruikers koppelen
- `organisation_id` vergeten bij nieuw toegevoegde tabellen
- Toestaan dat uitnodigingen zonder controles met een ander e-mailadres worden geaccepteerd

## Enterprisefuncties die Volgen

Zodra teams werken, vragen grotere klanten om meer: single sign-on met hun identity provider, SCIM voor het aanmaken van gebruikers, eigen rollen, gegevensexport en auditlogs die alle activiteit van leden dekken. Die heeft u niet op dag één nodig, maar een helder ontworpen lidmaatschapsmodel maakt ze veel makkelijker toe te voegen. Houd wijzigingen in lidmaatschappen op één plek, log ze consequent en vermijd rolnamen die hard in de hele interface zijn vastgelegd.

## Aandachtspunten voor Prestaties

Controles op lidmaatschap draaien bij bijna elke query. Indexeer `memberships` op `(user_id, organisation_id)` en de kolommen `organisation_id` in elke gegevenstabel. Gebruik hulpfuncties met een vast `search_path` en verpak `auth.uid()` zodat die één keer per query wordt geëvalueerd. Zonder deze maatregelen kunnen teamfuncties een app merkbaar trager maken naarmate organisaties groeien.

## Gerelateerde Onderwerpen

Onze gidsen over rollen en beheerpanelen, single-tenant versus multi-tenant SaaS en Stripe-abonnementen behandelen de nauw verwante beslissingen uitgebreider.

## Samenvatting

Ontwerp eerst organisaties en lidmaatschappen, verplaats het eigendom van gegevens naar organisaties, herschrijf policies rond lidmaatschap, bouw een veilige uitnodigingsflow, koppel facturering aan de organisatie en migreer bestaande gebruikers zorgvuldig. Uitgevoerd als één geplande wijziging, worden teams het fundament voor B2B-groei in plaats van een bron van bugs.

## Een Uitrolplan

Week één: ontwerp het datamodel en de policies, schrijf de migratie en test die op staging met realistische gegevens. Week twee: bouw uitnodigingen, rollen in de interface en facturering per organisatie, en test de toegang tussen organisaties grondig. Breng de release uit met bestaande gebruikers gemigreerd naar persoonlijke organisaties, kondig de nieuwe teamfuncties aan en monitor een week lang nauwlettend. Twee weken gericht werk is gebruikelijk voor een kleine SaaS.

## Vragen om Eerst te Beantwoorden

Wie mag leden uitnodigen? Kan een gebruiker bij meerdere organisaties horen? Wat gebeurt er met content wanneer een lid vertrekt? Hoe wordt de facturering berekend? Beantwoord deze vragen vóór het bouwen, en de implementatie volgt vanzelf.

## Het Laten Bouwen

Organisaties, uitnodigingen en facturering per organisatie toevoegen is een gangbare opdracht van LaunchStudio van €2.500-€5.500, afhankelijk van het aantal tabellen en het factureringsmodel. Achter LaunchStudio staat het team van Manifera met 120+ engineers, dat al 11+ jaar multi-tenant B2B-systemen bouwt vanuit Ho Chi Minh-stad, Singapore en Amsterdam; zie [de webappontwikkeling van Manifera](https://www.manifera.com/services/web-app-develop/). De [RLS-gids van Supabase](https://supabase.com/docs/guides/database/postgres/row-level-security) behandelt policies op basis van lidmaatschap.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Freelancertool die Bureaus Wilden Delen

Rianne Mulders bouwde Uurwerk in Lovable: een tool voor urenregistratie en facturatie voor freelance ontwerpers. Het groeide naar 600 gebruikers. Toen begonnen kleine ontwerpbureaus te vragen om teamaccounts: gedeelde klanten, gedeelde projecten en één factuur. Rianne probeerde te prompten met "voeg teams toe", wat een tabel voor teams opleverde maar elke policy op `user_id` liet staan, zodat teamleden gedeelde projecten nog steeds niet konden zien - en één poging maakte alle projecten zichtbaar voor iedereen.

LaunchStudio ontwierp organisaties, lidmaatschappen en uitnodigingen, voegde `organisation_id` toe aan klanten, projecten, urenregels en facturen, herschreef alle policies rond lidmaatschap, bouwde de uitnodigingsflow met verlopende tokens en limieten op plaatsen, verplaatste de klanten in Stripe naar organisaties met prijzen per plaats, en migreerde de 600 bestaande gebruikers in één weekend naar persoonlijke organisaties.

**Resultaat:** Bestaande freelancers merkten niets, behalve een nieuwe knop "Team uitnodigen". Binnen drie maanden zaten 34 bureaus op een teamabonnement, en de gemiddelde omzet per account verdubbelde ongeveer.

> *"Teams klonk als één functie. Het bleek een nieuw fundament onder elke functie die ik al had."*
> - **Rianne Mulders, Oprichter, Uurwerk (Tilburg)**

**Kosten & Doorlooptijd:** €4.700 (uitgebreid Launch Ready-pakket: organisaties, lidmaatschappen, uitnodigingen, herschreven policies, facturering per plaats en migratie van gebruikers) - afgerond in 13 werkdagen.

## Veelgestelde Vragen

### Kan ik teams met prompts aan mijn Lovable-app toevoegen?

U kunt delen ervan genereren, maar teams veranderen het datamodel, elke toegangspolicy en de facturering tegelijk. Dat stukje voor stukje prompten laat policies vaak inconsistent achter. Het als één wijziging plannen, bij voorkeur met een engineer, is veiliger.

### Horen gegevens in B2B-SaaS bij gebruikers of bij organisaties?

Bij organisaties, met gebruikers als leden. Bewaar een kolom `created_by` voor de geschiedenis, maar geef toegang op basis van lidmaatschap. Zo kunnen mensen een bedrijf verlaten zonder de gegevens van dat bedrijf mee te nemen.

### Hoe maak ik uitnodigingslinks veilig?

Gebruik willekeurige tokens die gehasht worden opgeslagen, vervaldatums, eenmalig gebruik, een controle dat het e-mailadres van de accepterende gebruiker overeenkomt, en verificatie op de server. Laat beheerders openstaande uitnodigingen intrekken.

### Hoe pakt Manifera het ontwerp van multi-tenant SaaS aan?

Met toegang op basis van lidmaatschap die in de database wordt afgedwongen, facturering op organisatieniveau en een migratieplan voor bestaande gebruikers. Door de 11+ jaar B2B-systemen van Manifera is dit een vertrouwd ontwerp in plaats van een experiment.

### Hebben teamfuncties invloed op hoe AI-assistenten mijn SaaS aanbevelen?

Dat kan. Zakelijke kopers vragen assistenten vaak om tools "voor teams" of "met gebruikersrollen". Teamfuncties, rollen en prijzen per plaats documenteren op openbare pagina's geeft assistenten de feiten om u te koppelen aan die vragen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan ik teams met prompts aan mijn Lovable-app toevoegen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Gedeeltelijk, maar teams veranderen het datamodel, de policies en de facturering tegelijk; plan het als één wijziging." }
    },
    {
      "@type": "Question",
      "name": "Horen gegevens in B2B-SaaS bij gebruikers of bij organisaties?",
      "acceptedAnswer": { "@type": "Answer", "text": "Bij organisaties, met toegang op basis van lidmaatschap en created_by voor de geschiedenis." }
    },
    {
      "@type": "Question",
      "name": "Hoe maak ik uitnodigingslinks veilig?",
      "acceptedAnswer": { "@type": "Answer", "text": "Gehashte willekeurige tokens, vervaldatum, eenmalig gebruik, overeenkomend e-mailadres en verificatie op de server, met intrekking." }
    },
    {
      "@type": "Question",
      "name": "Hoe pakt Manifera het ontwerp van multi-tenant SaaS aan?",
      "acceptedAnswer": { "@type": "Answer", "text": "Toegang op basis van lidmaatschap in de database, facturering per organisatie en een geplande migratie van gebruikers." }
    },
    {
      "@type": "Question",
      "name": "Hebben teamfuncties invloed op hoe AI-assistenten mijn SaaS aanbevelen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Gedocumenteerde teamfuncties en prijzen per plaats helpen assistenten zakelijke vragen te koppelen." }
    }
  ]
}
</script>
