---
Titel: "Gebruikersrollen en een Beheerpaneel Toevoegen aan een Lovable-App"
Trefwoorden: lovable beheerpaneel, lovable gebruikersrollen, lovable authenticatierollen, supabase rollen lovable, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Gebruikersrollen en een Beheerpaneel Toevoegen aan een Lovable-App

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Gebruikersrollen en een Beheerpaneel Toevoegen aan een Lovable-App",
  "description": "Rollen en een beheerpaneel toevoegen aan een Lovable-app vraagt meer dan een verborgen menu. Deze gids toont een veilig patroon: een rollentabel die gebruikers niet kunnen bewerken, RLS-policies die rollen controleren, beheeracties in edge functions en testen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-06",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-to-add-roles-and-an-admin-panel-to-a-lovable-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A01 Broken Access Control", "url": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/" },
    { "@type": "CreativeWork", "name": "OWASP Authorization Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html" },
    { "@type": "CreativeWork", "name": "OWASP Logging Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html" },
    { "@type": "CreativeWork", "name": "Supabase: Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" },
    { "@type": "CreativeWork", "name": "Verizon Data Breach Investigations Report", "url": "https://www.verizon.com/business/resources/reports/dbir/" }
  ]
}
</script>

**Kort antwoord:** bewaar rollen in een aparte tabel waar gebruikers niet naar kunnen schrijven, controleer die rollen in Row Level Security-policies van Supabase, en voer beheeracties uit via edge functions die de rol van de aanroeper op de server controleren. Het beheerpaneel zelf kan een gewone Lovable-pagina zijn, maar het verbergen voor niet-beheerders is alleen cosmetisch. Echte bescherming gebeurt in de database en op de server.

Dit is het patroon stap voor stap.

## Belangrijkste Punten

- **Een beheerpagina verbergen is geen beveiliging.** Iedereen kan de URL intypen of dezelfde queries aanroepen; bescherming moet in de database en op de server zitten.
- **Bewaar rollen in een speciale tabel waar gebruikers niet naar kunnen schrijven,** en controleer ze in Row Level Security-policies via een hulpfunctie.
- **Voer bevoorrechte acties uit in edge functions** die de rol van de aanroeper controleren en een regel in een auditlog schrijven.
- **B2B-apps hebben meestal rollen per organisatie nodig** (eigenaar, beheerder, lid per organisatie) in plaats van alleen globale rollen.
- **Gebrekkige toegangscontrole is het grootste risico in de OWASP Top 10,** en het verhogen van rechten via rolkolommen die gebruikers zelf kunnen wijzigen, is een van de meest voorkomende vormen ervan in AI-gebouwde apps.

## Het Onveilige Patroon dat Lovable Vaak Genereert

Vraag Lovable om "een beheerpaneel alleen voor admins" en u krijgt mogelijk:

- Een kolom `is_admin` of `role` in de tabel `profiles`
- Een controle in React: als de gebruiker admin is, toon dan het beheermenu
- Beheerpagina's die tabellen rechtstreeks bevragen met de anon key

Drie problemen: gebruikers kunnen hun eigen profielrij vaak bijwerken, inclusief de kolom `role`; iedereen kan de beheer-URL openen en dezelfde queries aanroepen; en RLS-policies maken mogelijk helemaal geen onderscheid voor admins. Het beheerpaneel wordt alleen beschermd door het feit dat gewone gebruikers de knop niet zien.

## Stap 1: Een Rollentabel die Gebruikers Niet Kunnen Bewerken

```sql
create type public.app_role as enum ('admin', 'staff', 'member');

create table public.user_roles (
  user_id uuid references auth.users on delete cascade,
  role public.app_role not null,
  primary key (user_id, role)
);

alter table public.user_roles enable row level security;

create policy "Users read own roles"
on public.user_roles for select
to authenticated
using (user_id = (select auth.uid()));
```

Er zijn bewust geen policies voor insert, update of delete. Gebruikers kunnen hun eigen rollen lezen; niemand kan rollen via de openbare API veranderen. Rolwijzigingen gebeuren alleen via code op de server.

## Stap 2: Een Hulpfunctie voor Policies

```sql
create function public.has_role(_role public.app_role)
returns boolean
language sql
stable
security definer
set search_path = ''
as $$
  select exists (
    select 1 from public.user_roles
    where user_id = (select auth.uid()) and role = _role
  );
$$;
```

## Stap 3: Gebruik Rollen in Row Level Security

```sql
create policy "Admins read all orders"
on public.orders for select
to authenticated
using (public.has_role('admin') or customer_id = (select auth.uid()));
```

Nu dwingt de database af wat de interface toont. Een niet-admin die de API rechtstreeks aanroept, ziet nog steeds alleen zijn eigen bestellingen.

## Stap 4: Beheeracties in Edge Functions

Acties zoals een betaling terugstorten, iemands rol wijzigen of een account verwijderen, horen niet met de anon key vanuit de browser te gebeuren. Maak een edge function die:

1. De JWT van de aanroeper leest en verifieert
2. In `user_roles` controleert of de aanroeper de rol admin heeft
3. De actie uitvoert met inloggegevens op de server
4. Een regel in het auditlog schrijft: wie deed wat, bij wie, wanneer

## Stap 5: Het Beheerpaneel in Lovable

Nu kan Lovable vrij de beheerinterface bouwen. Die leest de data die de policies toestaan en roept voor bevoorrechte acties de edge functions aan. Tip voor het prompten: vertel Lovable uitdrukkelijk dat beheeracties specifieke edge functions moeten aanroepen en dat het de RLS-policies en de tabel `user_roles` niet mag veranderen.

## Stap 6: Test Zoals een Aanvaller

- Log in als lid, open de beheer-URL en probeer elke actie
- Roep de edge functions voor beheer aan met het token van een lid
- Probeer via de API een rij in `user_roles` toe te voegen
- Probeer uw eigen rij in `profiles` bij te werken met een rolveld, als dat nog bestaat

Elke poging hoort te mislukken.

## Het Principe van Minimale Rechten

De beveiligingskunde kent een oud principe: elke gebruiker en elk onderdeel hoort alleen de toegang te hebben die nodig is om zijn werk te doen. Het Authorization Cheat Sheet van OWASP vertaalt dit naar praktische regels voor webapplicaties: standaard weigeren, autorisatie bij elk verzoek op de server afdwingen, rechten controleren op specifieke objecten in plaats van alleen op pagina's, en autorisatielogica centraliseren zodat die consistent is. Een rollensysteem op basis van deze regels is saai in de beste zin van het woord: voorspelbaar, testbaar en moeilijk te omzeilen.

AI-gegenereerde beheerpanelen overtreden vaak meerdere van deze regels tegelijk. Toegang is standaard toegestaan en wordt in de interface beperkt, controles zitten in componenten in plaats van op de server, en elke nieuwe pagina implementeert zijn eigen versie van de regel.

## Uw Rolmodel Ontwerpen Voordat U Bouwt

Besteed dertig minuten op papier voordat u een policy schrijft:

1. **Maak een lijst van soorten gebruikers:** bijvoorbeeld klant, medewerker, manager, beheerder.
2. **Maak een lijst van onderdelen:** bestellingen, facturen, gebruikers, instellingen, rapportages.
3. **Schrijf voor elke combinatie de toegestane acties op:** lezen, aanmaken, wijzigen, verwijderen, exporteren, goedkeuren.
4. **Markeer gevoelige acties:** terugbetalingen, rolwijzigingen, verwijderingen, data-exports.
5. **Bepaal de reikwijdte:** eigen records, teamrecords, organisatierecords of alles.

Deze matrix wordt de specificatie voor uw policies en functies, en de checklist voor uw tests. Hij maakt ook gesprekken met klanten makkelijker wanneer ze vragen: "wie aan uw kant kan onze data zien?"

## Auditlogging Goed Gedaan

Elke gevoelige beheeractie hoort een spoor achter te laten: wie het deed, bij welk record, wanneer, vanaf waar en met welk resultaat. Bewaar regels van het auditlog in een tabel die gewone gebruikers niet kunnen lezen of wijzigen, en die beheerders kunnen lezen maar niet bewerken. Het Logging Cheat Sheet van OWASP raadt aan beveiligingsrelevante gebeurtenissen zoals mislukte autorisaties en beheeracties te loggen, de integriteit van logs te beschermen en gevoelige data zoals wachtwoorden of volledige betaalgegevens buiten logs te houden. Voor B2B-klanten is een leesbaar auditlog ook een verkoopargument; veel beveiligingsvragenlijsten vragen er uitdrukkelijk naar.

## Veelvoorkomende Fouten met Rollen in AI-Gebouwde Apps

| Fout | Gevolg | Oplossing |
| --- | --- | --- |
| Rol opgeslagen in het profiel, profiel volledig bewerkbaar | Elke gebruiker kan zichzelf promoveren | Aparte rollentabel zonder schrijfpolicies |
| Admincontrole alleen in React | Beheer-URL en -acties bereikbaar voor iedereen | Controles op de server in policies en functies |
| Eén policy per pagina, telkens net iets anders | Inconsistente en moeilijk te testen regels | Centrale hulpfuncties die door alle policies worden hergebruikt |
| Beheeracties met de service role key in de browser | Volledige databasetoegang voor iedereen | Edge functions met rolverificatie |
| Geen audittrail | Geschillen en incidenten kunnen niet worden onderzocht | Auditlogtabel en een overzichtsscherm |

## Tweestapsverificatie voor Beheerders

Beheerdersaccounts zijn in elke app de waardevolste doelwitten, omdat ze de data van iedereen kunnen zien en wijzigen. Vereis meerstapsverificatie voor alle beheerders en accounts van medewerkers. Supabase Auth ondersteunt TOTP-authenticatorapps en maakt het zekerheidsniveau van de sessie beschikbaar, dat u in policies kunt controleren, zodat data die alleen voor beheerders is een sessie vereist die met een tweede factor is geverifieerd. Het Data Breach Investigations Report van Verizon vindt gestolen of misbruikte inloggegevens consequent onder de meest voorkomende patronen bij datalekken; MFA maakt die aanval stomp voor de accounts die er het meest toe doen.

## Toegang voor Support Zonder Gedeelde Logins

Oprichters geven supportmedewerkers vaak een gedeelde beheerlogin. Dan is onmogelijk te weten wie wat heeft gedaan, en is toegang moeilijk in te trekken als iemand vertrekt. Geef elke medewerker een eigen account met de smalste rol die bij zijn werk past, en als support de app af en toe moet zien zoals een klant hem ziet, bouw dan een expliciete, gelogde functie "bekijken als" in plaats van inloggegevens van klanten te delen.

## Uw Rollen Testen

Maak van uw rolmatrix tests: log in als elke rol en probeer via de API elke toegestane en niet-toegestane actie. Automatiseer de belangrijkste, vooral "een lid kan geen beheerfuncties aanroepen" en "een gebruiker kan zijn eigen rol niet veranderen", zodat toekomstige prompts ze niet stilletjes kunnen verzwakken.

## Beheerpanelen en het Vertrouwen van Klanten

Zakelijke klanten vragen steeds vaker wie aan de kant van de leverancier toegang heeft tot hun data en hoe die toegang wordt gecontroleerd. Een rolmodel met minimale rechten, MFA voor medewerkers en een auditlog van gevoelige acties geeft een concreet, geloofwaardig antwoord. Het beschermt u ook intern: wanneer een klant een terugbetaling of verwijdering betwist, laat het auditlog precies zien wat er is gebeurd en wie het deed. Dit één keer vroeg bouwen, kost veel minder dan gebeurtenissen tijdens een geschil uit het geheugen reconstrueren.

## Veilig Prompten in Lovable Nadat Rollen Bestaan

Zodra rollen zijn ingericht, vertel Lovable dan in de projectkennis uitdrukkelijk dat de rollentabel, de hulpfuncties en de edge functions voor beheer niet mogen worden veranderd, en dat nieuwe beheerfuncties de bestaande functies moeten aanroepen. Bekijk elke wijziging in `supabase/migrations` voordat die productie bereikt. Deze twee gewoonten voorkomen dat een zorgvuldig ontworpen rolmodel prompt voor prompt afbrokkelt.

## Begin Eenvoudig, Groei Bewust

De meeste apps lanceren goed met drie rollen: admin, medewerker en lid. Voeg alleen rollen toe wanneer een echte klantbehoefte opduikt, en voeg elke rol tegelijk toe aan uw rolmatrix, policies en tests. Een klein, goed getest rolmodel is veel veiliger dan een groot model dat niemand volledig begrijpt.

## Rollen Naast Admin en Lid

| Patroon | Wanneer te gebruiken |
| --- | --- |
| Globale rollen (admin, medewerker, lid) | Eén organisatie, interne medewerkers en klanten |
| Rollen per organisatie (eigenaar, beheerder, lid per organisatie) | B2B SaaS waarin klanten hun eigen teams beheren |
| Rechten per onderdeel (bewerker, kijker per project) | Samenwerkingstools met gedeelde items |

B2B-producten hebben meestal rollen per organisatie nodig: een tabel `memberships` met `org_id`, `user_id` en `role`, en policies die het lidmaatschap controleren. Dezelfde principes gelden: gebruikers kunnen hun eigen rol niet veranderen, policies dwingen toegang af, bevoorrechte acties gaan via de server.

## Het Laten Bouwen

Rollen en een beheerpaneel horen bij de meest voorkomende toevoegingen van LaunchStudio aan Lovable-apps, meestal binnen een Launch Ready-opdracht van €1.200-€3.500. Achter LaunchStudio staat het team van Manifera met 120+ ervaren engineers, die in 11+ jaar rolgebaseerde systemen hebben gebouwd voor enterpriseklanten, gecoördineerd vanuit Amsterdam en geleverd vanuit Ho Chi Minh City. Zie [de ontwikkeling van webapplicaties door Manifera](https://www.manifera.com/services/web-app-develop/) voor de enterprisekant, en de [gids van Supabase over custom claims en RBAC](https://supabase.com/docs/guides/database/postgres/custom-claims-and-role-based-access-control-rbac) voor een alternatieve aanpak met JWT-claims. Als u ook de rest van uw app wilt controleren, probeer dan onze [zelftest voor de beveiliging van Lovable](https://launchstudio.eu/nl/blog/is-my-lovable-app-secure).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Het Vrijwilligersplatform Waar Iedereen Coördinator Kon Worden

Roos van Dam coördineert een burenhulpnetwerk in Zaandam en bouwde Buurthulp in Lovable: bewoners plaatsen verzoeken zoals boodschappen of een lift naar de dokter, vrijwilligers nemen ze aan, en coördinatoren beheren vrijwilligers en controleren gevoelige verzoeken. Ongeveer 140 vrijwilligers en 300 bewoners sloten zich aan.

Lovable had coördinatoren geïmplementeerd met een kolom `role` in `profiles`, en een pagina voor het bewerken van het profiel die de hele rij opsloeg. Een vrijwilliger ontdekte, zonder het te willen, dat het profiel bewerken via de ontwikkelaarstools van de browser `role` op `coordinator` kon zetten, waardoor adressen en medische notities van bewoners bij gevoelige verzoeken zichtbaar werden. De beheerpagina zelf controleerde de rol alleen in het React-component.

LaunchStudio maakte een tabel `user_roles` zonder schrijfpolicies, migreerde de bestaande coördinatoren ernaartoe, verwijderde de kolom `role` uit `profiles`, voegde een hulpfunctie `has_role` toe en herschreef RLS zodat medische notities en adressen alleen zichtbaar waren voor coördinatoren en de toegewezen vrijwilliger. Het goedkeuren van vrijwilligers en het aanwijzen van coördinatoren verhuisde naar edge functions met een auditlog.

**Resultaat:** Het verhogen van rechten was binnen vier werkdagen onmogelijk gemaakt. Roos informeerde het bestuur van het netwerk, documenteerde het incident en bekijkt nu maandelijks het auditlog. Buurthulp heeft sindsdien ongeveer 2.000 verzoeken verwerkt.

> *"De beheerpagina was verborgen. Dat was alles: verborgen. Iedereen die wist waar hij moest kijken, kon zichzelf promoveren."*
> - **Roos van Dam, Oprichter, Buurthulp (Zaandam)**

**Kosten & Doorlooptijd:** €1.750 (Launch Ready-pakket: rollentabel, migratie, herschreven RLS, edge functions voor beheer en auditlog) - afgerond in 6 werkdagen.

## Veelgestelde Vragen

### Kan ik de beheerpagina niet gewoon verbergen voor gebruikers die geen admin zijn?

Verbergen verbetert de interface, maar biedt geen beveiliging. Iedereen kan de URL intypen of dezelfde databasequeries rechtstreeks aanroepen. Bescherming moet komen van Row Level Security en controles op de server in edge functions.

### Moeten rollen in de tabel profiles worden opgeslagen?

Liever niet, tenzij gebruikers die kolom niet kunnen bijwerken. Een aparte rollentabel zonder schrijfpolicies is eenvoudiger en veiliger, omdat die het risico wegneemt dat het bewerken van een profiel een verhoging van rechten wordt.

### Hoe voeg ik rollen op organisatieniveau toe voor een B2B-app in Lovable?

Gebruik een tabel met lidmaatschappen die gebruikers aan organisaties koppelt met een rol per lidmaatschap. Policies controleren het lidmaatschap via een hulpfunctie, en alleen eigenaren of beheerders van een organisatie kunnen, via functies op de server, gebruikers uitnodigen of rollen wijzigen.

### Waarom geven de engineers van Manifera de voorkeur aan rollen die de database afdwingt?

Omdat interfaces voortdurend veranderen, zeker als AI-tools componenten opnieuw genereren, terwijl databasepolicies blijven staan. De 11+ jaar werk van Manifera aan toegangscontrole voor enterpriseklanten laat zien dat regels die op databaseniveau worden afgedwongen, herontwerpen en nieuwe functies overleven.

### Hebben beheerpanelen invloed op SEO?

Ze horen helemaal niet te worden geïndexeerd. Zorg dat beheerroutes op de server authenticatie vereisen en uit sitemaps worden weggelaten. Een blootgestelde beheerpagina die in zoekresultaten verschijnt, is zowel een beveiligings- als een reputatieprobleem.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan ik de beheerpagina niet gewoon verbergen voor gebruikers die geen admin zijn?",
      "acceptedAnswer": { "@type": "Answer", "text": "Verbergen biedt geen beveiliging. Bescherming moet komen van Row Level Security en controles op de server in edge functions." }
    },
    {
      "@type": "Question",
      "name": "Moeten rollen in de tabel profiles worden opgeslagen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Liever niet. Een aparte rollentabel zonder schrijfpolicies voorkomt dat het bewerken van een profiel een verhoging van rechten wordt." }
    },
    {
      "@type": "Question",
      "name": "Hoe voeg ik rollen op organisatieniveau toe voor een B2B-app in Lovable?",
      "acceptedAnswer": { "@type": "Answer", "text": "Gebruik een tabel met lidmaatschappen met een rol per organisatie, hulpfuncties in policies, en functies op de server voor uitnodigingen en rolwijzigingen." }
    },
    {
      "@type": "Question",
      "name": "Waarom geven de engineers van Manifera de voorkeur aan rollen die de database afdwingt?",
      "acceptedAnswer": { "@type": "Answer", "text": "Interfaces veranderen, zeker met AI-tools, terwijl databasepolicies blijven. De 11+ jaar werk van Manifera aan toegangscontrole geeft de voorkeur aan regels op databaseniveau." }
    },
    {
      "@type": "Question",
      "name": "Hebben beheerpanelen invloed op SEO?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ze horen niet te worden geïndexeerd. Vereis authenticatie op de server en laat beheerroutes weg uit sitemaps." }
    }
  ]
}
</script>
