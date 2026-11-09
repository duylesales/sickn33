---
Titel: "Conversieservice naar Multi-Tenant SaaS"
Trefwoorden: multi-tenant saas conversie, organisaties toevoegen aan saas, app voor één gebruiker naar teams, supabase multi tenant rls, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Conversieservice naar Multi-Tenant SaaS

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Conversieservice naar Multi-Tenant SaaS",
  "description": "Een dienst tegen een vaste prijs die apps gebouwd met Lovable, Bolt, v0, Cursor of Claude Code omzet van een opzet voor één gebruiker of één klant naar multi-tenant SaaS. De dienst omvat modellen voor organisaties en teams, uitnodigingen, rollen, scheiding van gegevens met Row Level Security, migratie van bestaande gebruikers en gegevens, facturatie per organisatie, beheertools en tests die bewijzen dat de ene klant nooit de gegevens van een andere kan zien.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-08-24",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/multi-tenant-saas-conversion-service" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" },
    { "@type": "CreativeWork", "name": "PostgreSQL: Row Security Policies", "url": "https://www.postgresql.org/docs/current/ddl-rowsecurity.html" },
    { "@type": "CreativeWork", "name": "AWS: SaaS tenant isolation strategies", "url": "https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/saas-tenant-isolation-strategies.html" },
    { "@type": "CreativeWork", "name": "Stripe: Subscriptions", "url": "https://docs.stripe.com/billing/subscriptions/overview" }
  ]
}
</script>

Veel apps die met AI zijn gebouwd, beginnen als tool voor één persoon of één bedrijf. De oprichter bouwt hem voor zijn eigen bedrijf, of voor een eerste klant, en hij werkt. Dan wil een tweede klant hem, en een derde, en opeens moet de app veel bedrijven tegelijk bedienen, elk met eigen gebruikers, gegevens, rollen en facturatie, zonder dat ze elkaars informatie zien. Dat is wat multi-tenancy betekent.

Het later toevoegen is een van de meest voorkomende structurele wijzigingen waar een groeiende SaaS voor staat. Goed gedaan weet elke tabel bij welke organisatie de gegevens horen, weigert de database zelf om gegevens over organisaties heen te tonen en kunnen klanten collega's uitnodigen, rollen toekennen en per team betalen. Slecht gedaan legt een ontbrekend filter in één query de gegevens van de ene klant bloot aan een andere, en zo'n incident kan het einde betekenen van een jong SaaS-bedrijf.

De conversieservice naar multi-tenant van LaunchStudio maakt deze wijziging in uw bestaande app tegen een vaste prijs, migreert uw huidige gebruikers en gegevens en bewijst de scheiding met tests.

## Belangrijkste Punten

- **Multi-tenancy is een wijziging in het datamodel,** niet alleen een nieuwe instellingenpagina.
- **Scheiding moet in de database worden afgedwongen,** niet alleen in de interface.
- **Bestaande gebruikers en gegevens worden gemigreerd** naar organisaties zonder dat er iets verloren gaat.
- **Uitnodigingen, rollen en facturatie per organisatie** maken de app verkoopbaar aan teams.
- **Gebruikelijke prijs: €3.000-€7.500 binnen Launch & Grow,** opgeleverd in twee tot vier weken.

## Signalen Dat U Deze Dienst Nodig Heeft

- Uw app is voor één bedrijf gebouwd en nu willen andere bedrijven hem gebruiken.
- Klanten vragen om collega's uit te nodigen en gegevens binnen hun team te delen.
- U draait voor elke klant een aparte kopie van de app of database.
- Gegevens van verschillende klanten staan in dezelfde tabellen zonder betrouwbare koppeling aan een organisatie.
- U wilt per team of per gebruiker in een team factureren in plaats van per losse gebruiker.
- Een enterpriseprospect vraagt hoe klantgegevens worden gescheiden.
- U bent bang dat een ontbrekend filter de gegevens van de ene klant aan een andere kan tonen.

## Wat de Dienst Omvat

| Gebied | Wat we implementeren |
| --- | --- |
| Tenantmodel | Organisaties, leden en rollen, met een koppeling aan een organisatie op elke tabel met tenantgegevens |
| Scheiding van gegevens | Row Level Security-policies die elke query beperken tot de organisaties van de gebruiker |
| Scheiding van opslag | Bestandspaden en storagepolicies per organisatie |
| Uitnodigingen | Uitnodigen via e-mail, accepteren, opnieuw versturen, intrekken, met beperking op domein indien nodig |
| Rollen en rechten | Eigenaar, beheerder, lid en eigen rollen, afgedwongen op de server en in de database |
| Wisselen van organisatie | Gebruikers die bij meerdere organisaties horen, kunnen tussen die organisaties wisselen |
| Facturatie per organisatie | Abonnementen, gebruikersplaatsen en plannen per organisatie, gekoppeld aan Stripe of Mollie |
| Beheertools | Interne tools waarmee supportmedewerkers organisaties veilig kunnen bekijken |
| Gegevensmigratie | Bestaande gebruikers en records toegewezen aan organisaties, zonder gegevensverlies |
| Tests op scheiding | Geautomatiseerde tests die proberen bij gegevens van andere organisaties te komen en moeten falen |
| Prestaties | Indexen op organisatiekolommen zodat de scheiding de app niet vertraagt |

## Hoe het Werk Wordt Gedaan

1. **Kennismakingsgesprek** om uw klanten te begrijpen, hoe ze in teams werken en hoe u wilt factureren.
2. **Beoordeling** van uw datamodel, query's, policies, opslag en facturatie.
3. **Ontwerp van het tenantmodel** samen met u: welke tabellen bij organisaties horen, welke gedeeld zijn en hoe rollen werken.
4. **Plan en offerte** inclusief de migratieaanpak voor bestaande gegevens.
5. **Schemawijzigingen en policies** geïmplementeerd op staging met migraties.
6. **Wijzigingen in de app** voor uitnodigingen, rollen, wisselen, facturatie en query's.
7. **Gegevensmigratie** geoefend op kopieën van productiegegevens tot de resultaten kloppen.
8. **Tests op scheiding** geschreven en gedraaid voor elke tabel met tenantgegevens en elk opslagpad.
9. **Overstap** in een gepland venster, met terugvalplan.
10. **Overdracht** met documentatie en richtlijnen om veilig nieuwe tabellen toe te voegen.

## Wat U Ontvangt

- Een model voor organisaties, leden en rollen in uw database
- Row Level Security-policies op elke tabel met tenantgegevens en elke storagebucket
- Uitnodigingen, rolbeheer en wisselen van organisatie in uw app
- Facturatie per organisatie, met gebruikersplaatsen of plannen zoals afgesproken
- Gemigreerde gebruikers en gegevens, met een migratierapport
- Geautomatiseerde tests op scheiding die bij elke wijziging draaien
- Indexen en aanpassingen aan query's voor goede prestaties
- Documentatie van het tenantmodel en projectinstructies voor uw AI-tool
- Doorlopende ondersteuning via Launch & Grow voor €49 per maand

## Veelvoorkomende Uitgangssituaties

| Uitgangssituatie | Wat we meestal aantreffen | Aanpak |
| --- | --- | --- |
| Eén gebruiker per account | Gegevens alleen gekoppeld aan een gebruikers-ID | Een organisatie per gebruiker aanmaken, daarna uitnodigingen toestaan |
| Eén bedrijf, veel gebruikers | Geen tenantconcept; alle gebruikers zien alles | Bestaande gebruikers toewijzen aan de eerste organisatie, scheiding toevoegen |
| Aparte database per klant | Meerdere kopieën om te onderhouden en bij te werken | Samenvoegen tot één multi-tenant database, of scheiding behouden waar vereist |
| Gedeeltelijke organisatiekolom | Sommige tabellen hebben hem, andere niet; filters in de frontend | Het model afmaken, afdwinging naar de database verplaatsen |
| Gekopieerde app per klant | Meerdere codebases die uit elkaar groeien | Samenvoegen tot één codebase met configuratie per organisatie |

## Gedeelde Database, Aparte Databases of Iets Daartussen

Er zijn meerdere manieren om klanten te scheiden. De meest gebruikelijke voor SaaS in een vroege fase is een gedeelde database met een organisatiekolom op elke tabel met tenantgegevens en policies die de scheiding afdwingen. Dat is kostenefficiënt en eenvoudig te beheren. Aparte schema's of databases per klant bieden sterkere scheiding en kunnen door sommige enterprise- of overheidsklanten worden vereist, maar ze verhogen de beheerinspanning en de kosten.

Voor de meeste SaaS-apps gebouwd met AI op Supabase is de gedeelde aanpak met Row Level Security de juiste standaard, en die kan worden gecombineerd met aparte projecten voor een paar klanten die dat eisen. We adviseren een aanpak op basis van de eisen van uw klanten en uw verwachte groei, niet op basis van mode.

## Waarom Scheiding in de Database Hoort

Door AI gegenereerde code filtert gegevens vaak in de frontend of in afzonderlijke query's: "toon projecten waar organisation_id gelijk is aan de huidige organisatie". Dat werkt tot één query het filter vergeet, er een nieuwe functie zonder filter wordt toegevoegd of iemand de API direct aanroept. In een multi-tenant app is elk van die fouten een mogelijk datalek tussen klanten.

Row Level Security verplaatst de regel naar de database. Elke query, of die nu uit uw app komt, uit een door AI gegenereerde functie of uit een directe API-aanroep, wordt door de policies gefilterd. Een vergeten filter in de code lekt geen gegevens meer; het levert simpelweg niets op. Geautomatiseerde tests op scheiding controleren vervolgens voor elke tabel dat een gebruiker van de ene organisatie geen gegevens van een andere kan lezen, bijwerken of verwijderen. Dankzij die tests kunt u de enterprisevraag "hoe scheidt u klantgegevens?" met vertrouwen beantwoorden.

## Bestaande Gebruikers en Gegevens Migreren

De meeste oprichters hebben al echte gebruikers en gegevens voordat ze converteren. De migratie moet alles behouden, het aan de juiste organisaties toewijzen en gebruikers niet storen. We leggen met u regels vast, bijvoorbeeld: elke bestaande gebruiker wordt eigenaar van een nieuwe organisatie met zijn gegevens, of alle gebruikers met een e-maildomein van een bedrijf worden lid van de organisatie van dat bedrijf. Migratiescripts draaien herhaaldelijk op kopieën van productiegegevens, en een rapport toont hoeveel records waar terechtkwamen, met uitzonderingen waarover u beslist.

Op de dag van de overstap loggen gebruikers zoals gewoonlijk in en vinden ze hun gegevens in hun organisatie. Wie bij meerdere organisaties hoort, ziet een schakelaar. Uitnodigingen zijn direct beschikbaar.

## Facturatie per Organisatie

De overstap naar teams verandert meestal de prijsstelling. Gebruikelijke modellen zijn een prijs per organisatie per plan, een prijs per gebruikersplaats, of een basisprijs met inbegrepen plaatsen en extra plaatsen tegen betaling. We koppelen het organisatiemodel aan abonnementen in Stripe of Mollie, verwerken het aantal plaatsen als leden worden toegevoegd of verwijderd, dwingen de limieten van plannen af en migreren bestaande abonnementen. Als u niet zeker weet welk model past, laten we u de afwegingen zien, maar de beslissing over prijzen is aan u.

## Wat We van U Nodig Hebben

- Een kennismakingsgesprek van 15 minuten en een beschrijving van hoe klanten in teams werken
- Toegang tot uw repository, database, opslag, hosting en betaalprovider
- Beslissingen over rollen, regels voor uitnodigingen, prijsmodel en migratieregels
- Tijd om uitnodigingen, rollen en facturatie op staging te testen
- Overeenstemming over een overstapvenster en de communicatie naar bestaande gebruikers

## Prijs en Doorlooptijd

| Scope | Gebruikelijke app | Indicatieve prijs | Duur |
| --- | --- | --- | --- |
| Basisconversie | Weinig tabellen, eenvoudige rollen, geen wijzigingen in facturatie | €3.000-€4.000 | 2 weken |
| Standaardconversie | Veel tabellen, opslag, uitnodigingen, rollen, facturatie per organisatie | €4.000-€6.000 | 2-3 weken |
| Complexe conversie | Aparte databases of codebases samenvoegen, eigen rollen, enterprise-eisen | €6.000-€7.500 | 3-4 weken |

Conversies worden geleverd binnen Launch & Grow, met doorlopende ondersteuning voor €49 per maand. De offerte staat vast na de beoordeling. Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een indicatie.

## Niet Inbegrepen

De dienst zet het datamodel en de toegangscontrole van uw bestaande app om. Een herontwerp, nieuwe productfuncties die niets met teams te maken hebben, single sign-on of auditlogs vallen er niet onder; die worden gedekt door ons enterprise-gereedheidspakket en kunnen met de conversie worden gecombineerd. Kosten van betaalproviders worden door de provider gefactureerd.

## Veilig Bouwen na de Conversie

Na de conversie moet elke nieuwe tabel met klantgegevens het tenantmodel volgen. AI-tools weten dat niet tenzij u het ze vertelt. We voegen projectinstructies toe die voor elke nieuwe tabel met tenantgegevens een organisatiekolom, een Row Level Security-policy en een test op scheiding vereisen. De testsuite voor scheiding draait bij elke wijziging en faalt als een nieuwe tabel geen bescherming heeft. Zo wordt een regel die mensen kunnen vergeten een controle die niet kan worden overgeslagen.

## Toegang voor Beheer en Support

Zodra veel klanten de app delen, heeft uw supportteam een veilige manier nodig om hen te helpen. Inloggen met het wachtwoord van een klant of een databasesleutel met volledige toegang gebruiken zijn gebruikelijke shortcuts, en beide zijn riskant. We bouwen interne beheerweergaven die organisaties, leden en abonnementen tonen, met acties die beperkt zijn tot wat support nodig heeft, en waarbij elke toegang wordt gelogd. Als u de app als een specifieke gebruiker moet zien om een probleem na te bootsen, kunnen we een gecontroleerde functie implementeren om als die gebruiker mee te kijken, met toestemming van de klant en een duidelijke vastlegging.

## Waarom Oprichters voor LaunchStudio Kiezen

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, 160+ opgeleverde projecten en 120+ engineers, dat platforms voor meerdere klanten bouwt voor klanten zoals Vodafone en TNO, waar scheiding van gegevens een basiseis is. Oprichters ontmoeten het team aan de Herengracht 420 in Amsterdam; de engineering gebeurt in het ontwikkelcentrum van Manifera aan de Pho Quang Street in Ho Chi Minh City, met een hub aan de Tras Street in Singapore. We veranderen de structuur onder uw app, houden de interface die uw klanten kennen en laten de code compatibel met uw AI-tools.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Van Eén Tuincentrum naar Dertig

Koen Janssen leidde een tuincentrum in Venlo en bouwde Plantvoorraad met Lovable en Supabase om voorraad, verzorgingsschema's voor planten en bestellingen bij leveranciers bij te houden. Andere tuincentra zagen de app op een vakbeurs en wilden hem ook. De eerste aanpak van Koen was het Lovable-project te kopiëren en voor elke nieuwe klant een nieuw Supabase-project aan te maken. Bij de zevende kopie moest elke fix zeven keer worden gemaakt, liepen sommige kopieën weken achter en moest een prijsupdate van een leverancier in elke database apart worden geïmporteerd.

De beoordeling bevestigde dat de oorspronkelijke app helemaal geen tenantconcept had: elke tabel werd gedeeld door alle gebruikers van dat ene tuincentrum. LaunchStudio ontwierp een organisatiemodel met de rollen eigenaar, manager en medewerker, voegde een organisatiekolom toe aan 23 tabellen en maakte voor elke tabel Row Level Security-policies. Leverancierscatalogi, die tuincentra gemeenschappelijk gebruikten, bleven in gedeelde tabellen met alleen-lezentoegang. Er kwamen uitnodigingen en een schakelaar tussen organisaties bij voor regiomanagers die op meerdere locaties werkten. De facturatie ging over naar een Stripe-abonnement per organisatie, op basis van het aantal locaties.

De zeven aparte databases werden samengevoegd tot één, met migratiescripts die vier keer op kopieën werden geoefend en een rapport van elk verplaatst record. Een testsuite voor scheiding controleerde elke tabel en elk opslagpad. De overstap gebeurde op een zondagavond, en op maandag logden alle zeven tuincentra in en vonden ze hun gegevens intact.

**Resultaat:** Koen onderhoudt nu één app in plaats van zeven. In de zes maanden daarna groeide Plantvoorraad naar 30 tuincentra, elk in enkele minuten aangesloten met een uitnodiging. Prijsupdates van leveranciers worden één keer voor alle klanten geïmporteerd.

> *"De app kopiëren voelde als de snelle oplossing. Het was snel voor één klant en onmogelijk voor dertig. Nu is een nieuwe klant gewoon een nieuwe organisatie."*
> - **Koen Janssen, Oprichter, Plantvoorraad (Venlo)**

**Kosten & Doorlooptijd:** €6.800 (Launch & Grow-pakket: tenantmodel, policies op 23 tabellen, uitnodigingen en rollen, facturatie per organisatie, samenvoegen van zeven databases, tests op scheiding en overstap, plus €49 per maand) - afgerond in 18 werkdagen.

## Veelgestelde Vragen

### Wat kost het om een app om te zetten naar multi-tenant SaaS?

De meeste conversies kosten tussen €3.000 en €7.500 binnen Launch & Grow, afhankelijk van het aantal tabellen, opslag, rollen, wijzigingen in facturatie en of aparte databases of codebases moeten worden samengevoegd. U ontvangt een vaste offerte na een beoordeling van uw datamodel.

### Verliezen bestaande gebruikers gegevens of hebben ze nieuwe accounts nodig?

Nee. Bestaande gebruikers houden hun accounts en gegevens, die worden toegewezen aan organisaties volgens regels die u goedkeurt. Migratiescripts worden geoefend op kopieën van productiegegevens, en een rapport toont vóór de overstap waar elk record terechtkwam.

### Is een gedeelde database veilig voor meerdere klanten?

Ja, als de scheiding in de database wordt afgedwongen met Row Level Security en wordt gecontroleerd met geautomatiseerde tests. Dit is een veelgebruikte aanpak voor SaaS. Sommige klanten kunnen aparte databases eisen, die voor die specifieke organisaties kunnen worden aangeboden.

### Hoe helpt de ervaring van Manifera bij multi-tenant SaaS?

Manifera bouwt al 11+ jaar platforms voor meerdere klanten over 160+ projecten met 120+ engineers, voor klanten zoals Vodafone en TNO. LaunchStudio past die patronen toe om apps gebouwd met AI veilig om te zetten, met geteste scheiding en geplande migraties.

### Heeft multi-tenancy invloed op mijn SEO en zichtbaarheid in AI?

Indirect. Teamfuncties en heldere prijzen per organisatie maken het mogelijk pagina's te maken voor teamplannen, use cases en integraties waar kopers op zoeken. Sterke, gedocumenteerde scheiding van gegevens ondersteunt ook een beveiligingspagina die de vragen beantwoordt die kopers aan zoekmachines en AI-antwoordmachines stellen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat kost het om een app om te zetten naar multi-tenant SaaS?",
      "acceptedAnswer": { "@type": "Answer", "text": "De meeste conversies kosten tussen €3.000 en €7.500 binnen Launch & Grow, afhankelijk van het aantal tabellen, opslag, rollen, wijzigingen in facturatie en of aparte databases of codebases moeten worden samengevoegd. U ontvangt een vaste offerte na een beoordeling van uw datamodel." }
    },
    {
      "@type": "Question",
      "name": "Verliezen bestaande gebruikers gegevens of hebben ze nieuwe accounts nodig?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. Bestaande gebruikers houden hun accounts en gegevens, die worden toegewezen aan organisaties volgens regels die u goedkeurt." }
    },
    {
      "@type": "Question",
      "name": "Is een gedeelde database veilig voor meerdere klanten?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, als de scheiding in de database wordt afgedwongen met Row Level Security en wordt gecontroleerd met geautomatiseerde tests. Dit is een veelgebruikte aanpak voor SaaS." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij multi-tenant SaaS?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera bouwt al 11+ jaar platforms voor meerdere klanten over 160+ projecten met 120+ engineers, voor klanten zoals Vodafone en TNO. LaunchStudio past die patronen toe om apps gebouwd met AI veilig om te zetten, met geteste scheiding en geplande migraties." }
    },
    {
      "@type": "Question",
      "name": "Heeft multi-tenancy invloed op mijn SEO en zichtbaarheid in AI?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirect. Teamfuncties en heldere prijzen per organisatie maken het mogelijk pagina's te maken voor teamplannen, use cases en integraties waar kopers op zoeken." }
    }
  ]
}
</script>
