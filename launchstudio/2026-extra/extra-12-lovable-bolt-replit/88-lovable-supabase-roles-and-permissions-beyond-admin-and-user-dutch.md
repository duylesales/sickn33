---
Titel: "Lovable Supabase: Rollen en Rechten Voorbij Beheerder en Gebruiker"
Trefwoorden: lovable supabase, rollen en rechten, RBAC, toegangsbeheer, row level security, eigen rollen, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: SaaS Scale-Up
---

# Lovable Supabase: Rollen en Rechten Voorbij Beheerder en Gebruiker

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Rollen en Rechten Voorbij Beheerder en Gebruiker",
  "description": "Beheerder en gebruiker volstaan niet meer zodra een grotere klant vraagt om een accountant die alleen mag lezen of managers die beperkt zijn tot één locatie. Hoe u rechten modelleert, afbakent, afdwingt in database en server, en test zonder combinatorische nachtmerrie.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-07",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-supabase-roles-and-permissions-beyond-admin-and-user" }
}
</script>

Elk AI-gebouwd product begint met twee soorten gebruikers: degene die het inrichtte en alle anderen. Soms drie — eigenaar, beheerder, lid. Voor een klant met vier medewerkers is dat genoeg.

Het volstaat niet meer op een herkenbaar moment. Een grotere klant vraagt om een externe accountant die facturen kan zien maar niets kan wijzigen. Of om locatiemanagers die hun eigen vestiging runnen en de andere niet mogen zien. Of om planners die personeel inroosteren maar niet mogen zien wat iemand verdient. De oprichter voegt een rol toe, dan nog een, en binnen een jaar staat er in de code op veertig plekken `if (role === 'admin' || role === 'manager' && location === user.location)`, elk net iets anders.

Rechten zijn waar beveiliging, product en verkoop samenkomen. Het model goed hebben laat u ja zeggen tegen grotere klanten; het verkeerd hebben levert de incidenten op die de artikelen over IDOR en beheerpanelen in deze reeks beschrijven. Dit artikel behandelt het model, de afbakening, het afdwingen, en hoe u het test.

## Waarom Drie Rollen Breken

Eigenaar, beheerder en lid beschrijven één dimensie: hoeveel iemand mag doen. Echte organisaties hebben er minstens drie nodig.

**Wat iemand mag doen** — facturen lezen, uren goedkeuren, prijzen wijzigen, mensen uitnodigen.

**Waar iemand het mag doen** — alle locaties, de eigen locatie, één project, één klant.

**Wat iemand mag zien** — elk veld, of elk veld behalve lonen, marges of medische notities.

Eén rolveld kan alleen de eerste weergeven, en dan nog grof. Elk verzoek van een klant dat de tweede of derde raakt, wordt beantwoord door een nieuwe rol te maken die een afbakening in de naam verpakt — "manager-amsterdam" — of met een uitzondering in de code. Beide schalen slecht, en bij beide drijft AI-gegenereerde rechtenlogica af, omdat elke nieuwe sessie haar eigen controle in haar eigen stijl toevoegt.

## Rechten als Codes, Rollen als Bundels

Het model dat standhoudt, scheidt drie dingen.

**Rechten** zijn de atomaire acties die uw product ondersteunt, benoemd als codes: `invoices.read`, `invoices.approve`, `hours.approve`, `wages.read`, `members.invite`, `billing.manage`. Ze worden door u gedefinieerd, in code, en veranderen alleen wanneer het product verandert.

**Rollen** zijn benoemde bundels rechten: een rol "Accountant" bevat `invoices.read` en `reports.read`. Rollen zijn wat klanten zien en toewijzen.

**Toewijzingen** verbinden een lid met een rol, optioneel binnen een afbakening.

```sql
create table roles (
  id uuid primary key default gen_random_uuid(),
  organisation_id uuid references organisations(id) on delete cascade, -- null = systeemrol
  name text not null,
  is_system boolean not null default false
);

create table role_permissions (
  role_id uuid not null references roles(id) on delete cascade,
  permission text not null,
  primary key (role_id, permission)
);

create table role_assignments (
  organisation_id uuid not null,
  user_id uuid not null,
  role_id uuid not null references roles(id) on delete cascade,
  location_id uuid references locations(id) on delete cascade, -- null = hele organisatie
  foreign key (organisation_id, user_id) references memberships(organisation_id, user_id) on delete cascade
);
```

Drie eigenschappen maken dit praktisch. Systeemrollen — Eigenaar, Beheerder, Manager, Lid, Alleen lezen — worden met het product meegeleverd en dekken de meeste klanten zonder configuratie. Eigen rollen per organisatie zijn later mogelijk zonder schemawijziging. En de foreign key naar `memberships` betekent dat iemand uit een organisatie verwijderen elke rol verwijdert die hij had, de garantie waarvoor het artikel over teamuitnodigingen in deze reeks pleit.

Houd de lijst met rechtencodes in één bestand in de codebase, met een beschrijving van één regel per code. Het is de referentie voor developers, de bron voor de rechtenmatrix die klanten zien, en de lijst die een AI-assistent leest voordat hij een nieuwe controle toevoegt.

## Afbakening: Waar een Recht Geldt

De meeste klanten met meerdere locaties of projecten hebben rechten nodig die voor een deel van de organisatie gelden. De `location_id` op de toewijzing drukt dat uit: een rol Manager die met een locatie is toegewezen, geldt alleen daar; zonder locatie geldt ze overal.

Kies één dimensie voor afbakening en modelleer haar expliciet — locaties, projecten, afdelingen, klanten — in plaats van een generieke hiërarchie te bouwen. Een generieke afbakening op "resource" met geneste ouders is verleidelijk en bijna altijd meer dan een product van deze omvang nodig heeft. Is later een tweede dimensie nodig, dan is dat een extra kolom die leeg mag zijn, geen herontwerp.

De regel voor het combineren van toewijzingen is optellen: iemand met Manager voor Amsterdam en Alleen lezen voor de hele organisatie, kan Amsterdam beheren en alles lezen. Bouw in deze fase nooit "weiger"-toewijzingen; die maken van elke vraag over toegang een redenering over voorrang, en ze zijn de bron van de meeste verwarring in grotere rechtensystemen.

## Afdwingen op Drie Plekken, Vertrouwen op Eén

Rechten worden in drie lagen gecontroleerd, en elke laag heeft een andere taak.

**De database beslist welke data zichtbaar is.** Row level security policies gebruiken een hulpfunctie die beantwoordt of de huidige gebruiker een recht heeft, in deze organisatie, voor deze locatie:

```sql
create function has_permission(org uuid, perm text, loc uuid default null)
returns boolean language sql security definer stable set search_path = public as $$
  select exists (
    select 1
    from role_assignments ra
    join role_permissions rp on rp.role_id = ra.role_id
    where ra.organisation_id = org
      and ra.user_id = auth.uid()
      and rp.permission = perm
      and (ra.location_id is null or ra.location_id = loc)
  );
$$;

create policy "read shifts" on shifts for select
  using (has_permission(organisation_id, 'shifts.read', location_id));
```

**De server beslist welke acties zijn toegestaan.** Edge functions en RPC's die goedkeuren, versturen, betalen of verwijderen, controleren het specifieke recht voordat ze handelen — `hours.approve`, niet alleen lidmaatschap. Policies beschermen rijen; acties beslaan vaak meerdere rijen, roepen externe diensten aan of hebben bijeffecten die een rijpolicy niet kan zien.

**De interface beslist wat wordt getoond.** Knoppen die een gebruiker niet kan gebruiken, worden verborgen of uitgeschakeld. Dat is alleen voor gebruiksgemak. Een verborgen knop is geen rechtencontrole, en AI-gegenereerde code behandelt hem vaak wel zo — het artikel over beheerpanelen in deze reeks beschrijft het resultaat.

De database is de laag om op te vertrouwen, omdat het de laag is waar elk pad doorheen gaat: de interface, de API, een integratie, een script dat iemand volgend jaar draait.

## Rechten op Veldniveau

Sommige rechten gaan over kolommen in plaats van rijen: een planner mag een dienst zien, maar niet het uurloon dat erbij hoort. Row level security kan geen kolom verbergen.

Twee opzetten werken in Supabase.

**Verplaats gevoelige velden naar een eigen tabel**, met een eigen policy. `staff_compensation` per medewerker, alleen leesbaar met `wages.read`. De hoofdtabel blijft leesbaar voor planners; de gevoelige is voor hen onzichtbaar. Dit is de schoonste optie en de optie om te verkiezen voor alles wat echt gevoelig is.

**Bied een view aan zonder de kolom** aan rollen die haar niet mogen zien, en trek directe toegang tot de onderliggende tabel in, zoals het views-artikel in deze reeks beschrijft. Werkbaar, maar makkelijker fout te doen wanneer iemand later een kolom aan de tabel toevoegt en de view vergeet.

Wat niet werkt, is de volledige rij ophalen en het veld in de interface weglaten. Het veld zit in het antwoord, zichtbaar voor iedereen die het netwerktabblad van de browser opent.

## Regels Tegen Rechtenescalatie

Een rechtensysteem moet ook zichzelf besturen, en daar zijn AI-gegenereerde implementaties het zwakst.

**Mensen kunnen geen rechten toekennen die ze zelf niet hebben.** Een beheerder zonder `billing.manage` kan geen rol maken die dat recht bevat, of er een toewijzen. Dwing dit af in de functie die rollen en toewijzingen aanmaakt, niet in de interface.

**Mensen kunnen hun eigen toegang niet verhogen.** Een rol aan uzelf toewijzen vereist een recht dat is voorbehouden aan eigenaren, of is volledig verboden.

**Sommige acties vragen scheiding.** Wie uren indient, hoort niet degene te zijn die ze goedkeurt; wie een betaling aanmaakt, hoort niet degene te zijn die haar vrijgeeft. Een eenvoudige controle — `approved_by <> submitted_by` — afgedwongen in de database, sluit het meest voorkomende fraudepatroon in kleine producten.

**Eigenaren zijn beschermd.** Niemand onder eigenaar mag een eigenaar verwijderen of de rol van een eigenaar wijzigen, en de laatste eigenaar kan helemaal niet worden verwijderd, zoals beschreven in het artikel over teamuitnodigingen.

## Prestaties en Actualiteit

`has_permission` draait op elke rij van elke query. Zonder zorg wordt het het traagste deel van het product.

Indexeer `role_assignments (user_id, organisation_id)` en `role_permissions (role_id, permission)`. Markeer de functie als `stable`, zodat Postgres haar voor constante argumenten één keer per statement kan evalueren. En houd het aantal joins klein — het model hierboven heeft er twee nodig.

Het vaak voorgestelde alternatief is rechten in de JWT te zetten via de custom access token hook van Supabase, zodat policies claims lezen in plaats van tabellen. Dat is sneller en het is verouderd: een recht dat om tien uur wordt ingetrokken, blijft in het token totdat het wordt vernieuwd. Voor de meeste B2B-producten is de databaseopzoeking met indexen snel genoeg en heeft ze de eigenschap die ertoe doet — intrekken werkt bij het volgende verzoek. Gebruik claims hooguit voor grove feiten die zelden veranderen, en houd intrekbare rechten in de database.

## Een Rechtenmatrix Testen

Rechten vermenigvuldigen zich. Zes rollen, vierentwintig rechten en twee afbakeningen leveren honderden combinaties op, en niemand test die door te klikken.

De aanpak die werkt, is de verwachte matrix als data op te schrijven en er tests uit te genereren:

```ts
const matrix = {
  'Manager (Amsterdam)': { 'shifts.read@amsterdam': true, 'shifts.read@utrecht': false, 'wages.read': false },
  'Accountant':          { 'invoices.read': true, 'invoices.approve': false, 'wages.read': false },
};
// Per regel: log in als een geseede gebruiker met die rol en controleer of de query slaagt of niets teruggeeft.
```

De matrix doet ook dienst als documentatie: het is wat u de IT-afdeling van een klant laat zien wanneer die vraagt wat elke rol kan, en de rechtenpagina voor klanten kan uit hetzelfde bestand worden gegenereerd. Wanneer een recht verandert, verandert de matrix in dezelfde commit, en de tests vertellen of de database het ermee eens is.

Voeg daar de test tussen organisaties uit het IDOR-artikel aan toe: een gebruiker met elk recht in organisatie A moet in organisatie B nog steeds niets zien.

## API-sleutels, Integraties en Toegang voor Support

Mensen zijn niet de enige actoren. Drie andere hebben ook rechten nodig, en AI-gebouwde producten geven ze meestal alles.

**API-sleutels die klanten aanmaken** moeten een rol dragen, precies zoals een persoon. Een sleutel die door een boekhoudintegratie wordt gebruikt, heeft `invoices.read` nodig, niet de volledige rechten van de beheerder die hem aanmaakte. Sla de rol op bij de sleutel, controleer haar op dezelfde manier, en toon haar op de instellingenpagina van de sleutel, zodat de klant kan zien wat elke integratie mag. Het artikel over integraties in extra-11 beschrijft wat er gebeurt wanneer één sleutel met volledige toegang lekt.

**Uw eigen achtergrondtaken** draaien met de service role en omzeilen row level security volledig. Dat is noodzakelijk, en het betekent dat elke taak expliciet op organisatie moet filteren en even zorgvuldig moet worden gereviewd als een policy — de service role is de ene actor die geen enkele rechtencontrole tegenhoudt.

**Toegang voor support** — u of een collega die in het account van een klant kijkt om te helpen — moet een bewuste, in tijd beperkte en vastgelegde actie zijn, idealiter toegekend door de klant: "sta toegang voor support toe gedurende 48 uur". Stilletjes als gebruikers meekijken, via de service role of door als hen in te loggen, is handig en is precies waar de beveiligingsvragenlijst van een zorgvuldige klant naar vraagt. Een korte tabel `support_grants` met een vervaldatum, gecontroleerd door dezelfde hulpfunctie, maakt er een mogelijkheid van die u eerlijk kunt beschrijven.

## Wat U Klanten Laat Zien

Grotere klanten beoordelen een product deels op hoe begrijpelijk de rechten zijn. Drie dingen helpen.

**Een rechtenmatrix in het product** — rollen aan de zijkant, mogelijkheden bovenaan — gegenereerd uit dezelfde definities die de code gebruikt, zodat ze niet uit de pas kan lopen.

**Verstandige standaardrollen**, benoemd in de taal van de klant: Eigenaar, Beheerder, Locatiemanager, Medewerker, Alleen lezen. De meeste klanten maken nooit een eigen rol; goede standaarden zijn wat ze echt gebruiken.

**Een audit van rolwijzigingen**, zichtbaar voor beheerders: wie gaf wie welke rol, wanneer. Het beantwoordt de vragen die anders supporttickets worden, en het is waar een beveiligingsvragenlijst naar vraagt.

## Wanneer U Nog Geen Eigen Rollen Bouwt

Eigen rollen per organisatie zijn een functie waar grotere klanten naar vragen en kleinere nooit gebruiken. De editor, de validatie en de regels tegen escalatie bouwen is een week werk.

De volgorde die werkt: eerst rechtencodes en systeemrollen, wat weinig meer kost dan drie vastgecodeerde rollen en al het andere mogelijk maakt. Afbakening wanneer de eerste klant met meerdere locaties haar nodig heeft. Een editor voor eigen rollen wanneer drie klanten erom hebben gevraagd — en tot dan richt u eigen rollen met de hand in voor de klanten die ze nodig hebben, wat het model zonder interface ondersteunt.

## Migreren Vanaf Eigenaar, Beheerder en Lid

Voor een product in productie met één rolkolom is de migratie veilig als ze in de juiste volgorde gebeurt:

1. Definieer de rechtencodes door elke controle die nu in de code staat op te sommen. De lijst is meestal langer dan verwacht, en haar maken is het nuttigste deel van de oefening.
2. Maak systeemrollen die het huidige gedrag precies nabootsen — de bestaande beheerdersrol wordt een bundel van de rechten die beheerders nu feitelijk hebben.
3. Vul toewijzingen aan vanuit de rolkolom.
4. Vervang controles onderdeel voor onderdeel — eerst policies, dan serverfuncties, dan de interface — en draai na elke stap de matrixtests.
5. Verwijder de oude kolom wanneer niets haar meer leest.

Pas wanneer de migratie het bestaande gedrag nabootst, moeten nieuwe rollen en afbakeningen worden toegevoegd. Model en gedrag in dezelfde stap veranderen maakt elk verschil dubbelzinnig.

## Dit Inrichten

Voor een Lovable-product met zijn eerste grotere klanten is dit doorgaans drie tot vijf dagen: rechtencodes in één bestand met beschrijvingen, systeemrollen als bundels rechten, toewijzingen gekoppeld aan lidmaatschappen met een optionele afbakening op locatie of project, row level security gebouwd op een geïndexeerde hulpfunctie `has_permission`, controles op actieniveau in serverfuncties, gevoelige velden naar apart beschermde tabellen, regels die zelfpromotie en toekenning boven eigen rechten voorkomen, functiescheiding bij goedkeuringen, een rechtenmatrix als data met gegenereerde tests, een matrix en audit van rolwijzigingen voor klanten, en een migratiepad dat het bestaande gedrag nabootst voordat er iets nieuws wordt toegevoegd.

LaunchStudio bouwt dit wanneer een product begint te verkopen aan organisaties met meer dan één locatie of afdeling. De engineers zijn van Manifera — elf jaar, 120+ engineers, 160+ projecten, klanten waaronder Vodafone, TNO en CFLW.

[Vraag ons in kaart te brengen wie wat kan zien in uw product](https://launchstudio.eu/nl/#contact). Die kaart is meestal de verrassing.

## Echt voorbeeld

### Managers Die Hun Eigen Overuren Goedkeurden

Marloes Teunissen bouwde Horecarooster in Lovable: personeelsplanning en urenregistratie voor horecagroepen, gebruikt door 27 groepen met 140 locaties en zo'n 3.800 medewerkers.

Het product had drie rollen: eigenaar, beheerder en lid. Locatiemanagers moesten hun eigen roosters bewerken en uren goedkeuren, wat alleen beheerders konden, dus werd elke locatiemanager beheerder. Beheerders konden elke locatie in de groep zien, inclusief de uurlonen van alle medewerkers, en konden alle uren goedkeuren — ook hun eigen.

De financieel directeur van een groep zag de overuren op één locatie stijgen terwijl de omzet van het restaurant dat niet deed, en ontdekte dat de manager zijn eigen extra uren had goedgekeurd. Dezelfde week weigerde een grotere groep met 34 locaties te tekenen, omdat managers de lonen van de hele groep zouden kunnen zien.

Vier werkdagen: 24 rechtencodes gedefinieerd op basis van de controles die al door de code verspreid stonden; zes systeemrollen — Eigenaar, Beheerder, Locatiemanager, Planner, Medewerker, Alleen lezen — die eerst het bestaande gedrag nabootsten; roltoewijzingen met een optionele afbakening op locatie, aangevuld vanuit de oude rolkolom; row level security herschreven rond een geïndexeerde hulpfunctie `has_permission` over 19 tabellen; lonen verplaatst naar een aparte tabel voor beloning die alleen met `wages.read` leesbaar is; goedkeuringsfuncties die `hours.approve` voor de locatie controleren en goedkeuring weigeren door degene die de uren indiende; regels die voorkomen dat iemand rechten toekent die hij zelf niet heeft; een rechtenmatrix van 24 rechten bij 6 rollen als data, die 288 tests genereert die in CI draaien; en een audit van rolwijzigingen zichtbaar voor de beheerders van elke groep.

**Resultaat:** de controle van historische goedkeuringen vond drie managers bij twee groepen die hun eigen overuren hadden goedgekeurd, samen €4.100, die de groepen terugvorderden. De groep met 34 locaties tekende binnen de maand, en een tweede groep van vergelijkbare omvang volgde, samen goed voor 61 locaties.

> *"We maakten elke locatiemanager beheerder omdat dat de enige rol was die uren kon goedkeuren. Daardoor konden ze ook ieders loon zien en hun eigen overuren goedkeuren."*
> — **Marloes Teunissen, Oprichter, Horecarooster (Haarlem)**

**Kosten & Doorlooptijd:** €4.800 (rechtenmodel en systeemrollen, toewijzingen per locatie met aanvulling, policies herschreven over 19 tabellen, gescheiden beloningsdata, scheiding bij goedkeuring, regels tegen escalatie, 288 gegenereerde matrixtests, audit van rolwijzigingen) — afgerond in 4 werkdagen.

## Veelgestelde vragen

### Wanneer volstaan eigenaar, beheerder en lid niet meer?

Wanneer klanten gebruikers nodig hebben die alleen mogen lezen, mensen die beperkt zijn tot één locatie of project, of mensen die mogen handelen zonder gevoelige velden zoals lonen te zien. Eén rolveld kan afbakening en zichtbaarheid van velden niet uitdrukken.

### Wat is het verschil tussen een rol en een recht?

Een recht is één actie die uw product ondersteunt, zoals `invoices.approve`. Een rol is een benoemde bundel rechten die klanten toewijzen. Code controleert rechten; klanten beheren rollen.

### Waar moeten rechten worden afgedwongen?

In de database voor zichtbaarheid van data, in serverfuncties voor acties, en in de interface alleen voor gebruiksgemak. De database is de laag om op te vertrouwen, omdat elk toegangspad erdoorheen gaat.

### Hoe verberg ik een veld zoals salaris voor sommige rollen?

Verplaats het naar een aparte tabel met een eigen policy, of bied een view aan zonder de kolom en trek de toegang tot de basistabel in. Haal het nooit op om het in de interface te verbergen.

### Moeten rechten in de JWT worden opgeslagen?

Zelden. Claims zijn snel maar verouderd totdat het token wordt vernieuwd, dus ingetrokken rechten blijven hangen. Een geïndexeerde databaseopzoeking is voor de meeste producten snel genoeg en werkt direct.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wanneer volstaan de rollen eigenaar, beheerder en lid niet meer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Wanneer klanten alleen-lezengebruikers, toegang per locatie of project, of toegang zonder zicht op gevoelige velden zoals lonen nodig hebben."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het verschil tussen rollen en rechten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een recht is één actiecode; een rol is een benoemde bundel rechten die klanten toewijzen. Code controleert rechten, klanten beheren rollen."
      }
    },
    {
      "@type": "Question",
      "name": "Waar moeten rechten worden afgedwongen in een Supabase-app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In row level security voor data, in serverfuncties voor acties, en in de interface alleen voor gebruiksgemak — de database is de vertrouwde laag."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe verberg ik salarisgegevens voor sommige rollen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sla ze op in een aparte tabel met een eigen policy, of gebruik een view zonder de kolom — haal ze nooit op om ze in de interface te verbergen."
      }
    },
    {
      "@type": "Question",
      "name": "Horen rechten in JWT-claims?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zelden, omdat claims geldig blijven tot de vernieuwing. Een geïndexeerde databaseopzoeking is snel genoeg en trekt toegang direct in."
      }
    }
  ]
}
</script>
