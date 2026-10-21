---
Titel: "Lovable Supabase: Teamuitnodigingen en Lidmaatschap van Organisaties"
Trefwoorden: lovable supabase, teamuitnodigingen, lidmaatschap organisaties, accounts met meerdere gebruikers, uitnodigingslinks, row level security, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Lovable Supabase: Teamuitnodigingen en Lidmaatschap van Organisaties

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Teamuitnodigingen en Lidmaatschap van Organisaties",
  "description": "Zodra een klant een collega wil toevoegen, heeft een app voor één gebruiker organisaties, lidmaatschappen en uitnodigingen nodig. Het datamodel, veilige uitnodigingstokens, de randgevallen die AI-gegenereerde flows missen, en wat iemand verwijderen werkelijk moet doen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-05",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-supabase-team-invitations-and-organisation-membership" }
}
</script>

De meeste AI-gebouwde producten beginnen met één persoon per account. De oprichter meldt zich aan, het product werkt, de eerste klanten melden zich op dezelfde manier aan. Dan stelt een klant de vraag die elk B2B-product uiteindelijk hoort: "Kan mijn collega het ook gebruiken?"

Wat er als antwoord wordt gebouwd, is meestal een knop "uitnodigen" die een link verstuurt, en een kolom `organisation_id` op het profiel van de gebruiker. Voor de demonstratie werkt het. Het levert ook vaak uitnodigingslinks op die nooit verlopen, links die werken voor wie een doorgestuurde e-mail ontvangt, mensen die niet bij twee bedrijven kunnen horen, en oud-medewerkers die hun toegang houden omdat "verwijderen" ze alleen uit een lijst haalde.

Lidmaatschap is het fundament waarop rechten, facturatie, audit en datascheiding allemaal rusten. Het is de moeite waard het model goed te hebben voordat de tweede klant vijf gebruikers heeft, omdat het later veranderen betekent dat elke policy die ervan afhangt moet worden gemigreerd.

## Het Datamodel: Drie Tabellen, Niet Eén Kolom

De kortere weg is één kolom: `profiles.organisation_id`. Die beantwoordt "bij welk bedrijf hoort deze persoon" — en verder niets.

Ze kan geen persoon weergeven die bij twee organisaties hoort, en dat komt vaak voor: accountants die meerdere klanten bedienen, onderaannemers die voor meerdere installateurs werken, adviseurs, en iedereen die van werkgever wisselt maar zijn e-mailadres houdt. Ze kan geen rol per organisatie bevatten. En ze kan geen uitnodiging weergeven die nog niet is geaccepteerd.

Het model dat standhoudt, gebruikt drie tabellen.

```sql
create table organisations (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  created_at timestamptz not null default now()
);

create table memberships (
  organisation_id uuid not null references organisations(id) on delete cascade,
  user_id uuid not null references auth.users(id) on delete cascade,
  role text not null check (role in ('owner', 'admin', 'member')),
  created_at timestamptz not null default now(),
  primary key (organisation_id, user_id)
);

create table invitations (
  id uuid primary key default gen_random_uuid(),
  organisation_id uuid not null references organisations(id) on delete cascade,
  email text not null,
  role text not null check (role in ('admin', 'member')),
  token_hash text not null unique,
  invited_by uuid not null references auth.users(id),
  expires_at timestamptz not null,
  accepted_at timestamptz,
  revoked_at timestamptz,
  created_at timestamptz not null default now()
);
```

Een lidmaatschap is de relatie tussen een persoon en een organisatie, waarbij de rol bij die relatie hoort in plaats van bij de persoon. Een uitnodiging is een lidmaatschap in afwachting, met een vervaldatum. Geen van beide vervangt de ander: de uitnodiging legt vast wie werd gevraagd, door wie en wanneer; het lidmaatschap legt vast wie werkelijk toegang heeft.

De samengestelde primaire sleutel op `memberships` dwingt af dat iemand maar één keer lid kan zijn van een organisatie. De cascades zorgen ervoor dat het verwijderen van een organisatie haar lidmaatschappen en uitnodigingen verwijdert, en dat het verwijderen van een gebruiker zijn lidmaatschappen verwijdert — wat de AVG bij wissing vereist, zoals het verwijderartikel in extra-11 beschrijft.

## Policies Volgen het Lidmaatschap

Zodra lidmaatschap een tabel is, stellen row level security policies één vraag: is de huidige gebruiker lid van de organisatie die eigenaar is van deze rij?

```sql
create function is_member(org uuid) returns boolean
language sql security definer stable set search_path = public as $$
  select exists (
    select 1 from memberships
    where organisation_id = org and user_id = auth.uid()
  );
$$;

create policy "members read invoices" on invoices
  for select using (is_member(organisation_id));
```

De hulpfunctie doet er om twee redenen toe. Ze houdt policies kort en gelijk over alle tabellen, wat ze reviewbaar maakt. En omdat ze `security definer` is, leest ze `memberships` zonder dat de eigen policies van die tabel naar zichzelf terugverwijzen — de fout van oneindige recursie die AI-gegenereerde policies verrassend vaak opleveren wanneer een lidmaatschapspolicy het lidmaatschap probeert te controleren.

Indexeer `memberships (user_id, organisation_id)`. Elke policy-evaluatie op elke tabel roept deze functie aan, en zonder de index is elke aanroep een scan.

Rollen voegen een tweede hulpfunctie toe — `has_role(org, 'admin')` — gebruikt voor schrijfacties die niet elk lid mag uitvoeren: mensen uitnodigen, facturatie wijzigen, records verwijderen. Het artikel over rollen en rechten in deze reeks behandelt wanneer drie rollen niet meer volstaan.

## Uitnodigingstokens Goed Gedaan

De uitnodigingslink is een inloggegeven. Wie hem heeft, kan lid worden van een organisatie en haar data zien. Hij verdient dezelfde zorg als een link om een wachtwoord te herstellen, en het artikel over wachtwoordherstel in deze reeks beschrijft het meeste van wat er misgaat.

**Willekeurig, lang en onvoorspelbaar.** Minstens 32 bytes uit een cryptografische randomgenerator. Niet het database-ID van de uitnodiging, niet het gebruikers-ID van de uitnodiger, geen oplopend getal — die komen allemaal voor in AI-gegenereerde uitnodigingsflows.

**Opgeslagen als hash.** De database bevat `sha256(token)`, de e-mail bevat het token. Wie de uitnodigingstabel leest — via een back-up, een gelekte service key, een te ruime policy — kan niet gebruiken wat hij vindt.

**Met een vervaldatum.** Zeven dagen is een verstandige standaard voor B2B-producten. Lang genoeg voor iemand op vakantie; kort genoeg dat een oude e-mail in een gecompromitteerde mailbox waardeloos is.

**Eenmalig.** Accepteren zet `accepted_at`, en een token waarbij `accepted_at` is gezet, wordt geweigerd.

**Intrekbaar.** Een beheerder die het verkeerde adres uitnodigde, kan de uitnodiging intrekken voordat ze wordt gebruikt, wat `revoked_at` zet.

**Gekoppeld aan een e-mailadres.** Dit is de eigenschap die het vaakst ontbreekt, en die het meest uitmaakt.

```ts
// Edge function: uitnodiging accepteren
const tokenHash = await sha256(token);
const { data: inv } = await admin.from('invitations')
  .select('*').eq('token_hash', tokenHash)
  .is('accepted_at', null).is('revoked_at', null)
  .gt('expires_at', new Date().toISOString())
  .single();
if (!inv) return error(410, 'invitation_invalid');
if (inv.email.toLowerCase() !== user.email.toLowerCase())
  return error(403, 'invitation_email_mismatch');
// lidmaatschap aanmaken en als geaccepteerd markeren in één transactie
```

Zonder de e-mailcontrole is een uitnodiging een toegangsbewijs voor wie hem vasthoudt: één keer doorgestuurd laat hij binnen wie erop klikt. Met de controle is een doorgestuurde link nutteloos voor iedereen behalve de bedoelde ontvanger.

Doe het accepteren in één transactie — lidmaatschap aanmaken, `accepted_at` zetten — zodat twee gelijktijdige klikken geen duplicaat kunnen maken of een ingetrokken uitnodiging kunnen accepteren.

## De Flows Die AI-Gegenereerde Code Mist

Het gelukkige pad — een beheerder nodigt een nieuw adres uit, de ontvanger meldt zich aan en wordt lid — is wat wordt gebouwd en getest. Echt gebruik raakt binnen de eerste maand aan verschillende andere.

**De ontvanger heeft al een account.** Die moet inloggen en worden toegevoegd, niet worden gevraagd zich opnieuw aan te melden en te horen dat het e-mailadres al bestaat.

**De ontvanger meldt zich aan met een ander adres.** Iemand die is uitgenodigd op `j.devries@bedrijf.nl` meldt zich aan met een persoonlijk Gmail-adres. De koppeling aan het e-mailadres weigert dat, terecht, en de foutmelding moet zeggen waarom en wat te doen — inloggen met het uitgenodigde adres, of om een nieuwe uitnodiging vragen.

**De ontvanger wordt twee keer uitgenodigd.** Een tweede uitnodiging aan hetzelfde adres voor dezelfde organisatie moet de eerste vervangen, niet een parallelle aanmaken. Een gedeeltelijke unieke index op `(organisation_id, lower(email))` voor uitnodigingen die nog openstaan, dwingt dat af.

**De ontvanger is al lid.** Een bestaand lid uitnodigen moet dat melden, niet een e-mail versturen.

**De uitnodiging is verlopen.** De link moet uitleggen dat ze is verlopen en dat de beheerder een nieuwe kan sturen — geen algemene fout tonen, wat elke keer een supportticket oplevert.

**De organisatie heeft haar limiet aan gebruikers bereikt.** Hieronder besproken; de controle hoort bij het uitnodigen en opnieuw bij het accepteren.

Elk hiervan is een paar regels. Samen zijn ze het verschil tussen een functie die support-e-mail oplevert en een die dat niet doet.

## Iemand Verwijderen Moet Hem Echt Verwijderen

Het gat met de meeste gevolgen in AI-gebouwde teamfuncties: verwijderen dat verbergt in plaats van intrekt.

Een knop "lid verwijderen" die `active = false` zet, of iemand van een lijst op het scherm haalt terwijl zijn `organisation_id` intact blijft, laat hem volledige toegang houden via de API. Zoals het sessie-artikel in deze reeks beschrijft, loopt een bestaande sessie ook door totdat ze verloopt, tenzij iets haar beëindigt.

Verwijderen moet vier dingen doen:

1. **De lidmaatschapsrij verwijderen.** Elke policy die het lidmaatschap controleert, weigert dan bij het volgende verzoek de toegang.
2. **Zijn sessie voor die organisatie beëindigen**, of alle sessies als hij nergens anders bij hoort. Supabase staat toe een gebruiker vanaf de server uit te loggen; gebruik dat.
3. **Alles intrekken wat persoonlijk van hem was** — API-sleutels die hij aanmaakte, integraties die hij koppelde, agendafeeds met zijn token in de URL.
4. **Het vastleggen** — wie wie verwijderde, wanneer — in het auditlog.

En één ding mag verwijderen niet doen: het werk wissen dat hij maakte. Facturen die een oud-medewerker uitschreef, horen nog steeds bij de organisatie. Verwijs naar de gebruiker via zijn ID, houd de rij, en toon "voormalig lid" waar zijn naam zou staan. Iemands bijdragen wissen omdat hij is vertrokken, is een dataverliesincident dat op zijn beurt wacht.

## Bescherm de Laatste Eigenaar

Een organisatie zonder eigenaar kan door niemand behalve u worden beheerd, gefactureerd of verwijderd. Het gebeurt wanneer de enige eigenaar vertrekt, zichzelf verwijdert, of zijn eigen rol verandert naar lid om iets te testen.

Dwing het af in de database in plaats van de interface:

```sql
create function prevent_ownerless_org() returns trigger language plpgsql as $$
begin
  if (select count(*) from memberships
      where organisation_id = old.organisation_id and role = 'owner'
      and not (organisation_id = old.organisation_id and user_id = old.user_id)) = 0
     and (tg_op = 'DELETE' or new.role <> 'owner') then
    raise exception 'organisation_must_keep_an_owner';
  end if;
  return coalesce(new, old);
end $$;
```

Geef eigenaren daarna een bewuste manier om over te dragen: eerst iemand anders promoveren, dan aftreden. Dat is een proces in twee stappen dat klanten begrijpen, en het neemt een categorie supportverzoeken weg die anders binnenkomt als een urgente e-mail van een bedrijf waarvan de eigenaar is vertrokken.

## Wisselen Tussen Organisaties

Zodra één persoon bij twee organisaties kan horen, moet elk scherm weten in welke hij werkt.

De veelgemaakte fout is de actieve organisatie alleen in de browser bij te houden — in `localStorage` of een React-context — en haar bij elk verzoek mee te sturen als parameter die de server vertrouwt. Een gebruiker die die parameter aanpast, vraagt om de data van een andere organisatie, en het enige wat tussen hem en die data staat, is de policy. Kloppen de policies, dan krijgt hij niets; maar "de policies kloppen" is precies de aanname waar het IDOR-artikel in deze reeks over gaat.

De robuuste opzet:

- De actieve organisatie wordt gekozen in de interface en meegestuurd met verzoeken.
- De server, of de policy, controleert bij elk verzoek het lidmaatschap van die organisatie — en vertrouwt nooit alleen op de parameter.
- De organisatiewisselaar toont alleen organisaties waarvan de gebruiker lid is, gelezen uit `memberships`, niet uit een gecachete lijst.
- URL's bevatten de organisatie waar dat helpt — `/app/org/{id}/invoices` — zodat een link die collega's delen de juiste context opent, en een link die wordt geopend door iemand zonder lidmaatschap duidelijk "geen toegang" toont in plaats van een lege pagina.

## Gebruikerslimieten, Facturatie en Domeinen

Lidmaatschap is waar prijzen per gebruiker de database raken.

**Gebruikerslimieten** worden op de server op twee momenten afgedwongen: wanneer een uitnodiging wordt aangemaakt, en wanneer ze wordt geaccepteerd. Alleen bij het uitnodigen controleren laat een organisatie twintig uitnodigingen aanmaken terwijl ze onder de limiet zit, en alle twintig accepteren. Tel openstaande uitnodigingen mee voor de limiet, of controleer opnieuw bij het accepteren.

**Facturatiewijzigingen** volgen lidmaatschapswijzigingen. Rekent u per gebruiker, dan moet het toevoegen of verwijderen van een lid de hoeveelheid in het abonnement bijwerken — via de API van de aanbieder, met pro rata zoals beschreven in het artikel over terugbetalingen en pro rata in deze reeks — in plaats van te wachten tot iemand het bij de verlenging opmerkt.

**Lid worden op basis van domein** — iedereen met een adres op `@bedrijf.nl` mag zonder uitnodiging lid worden — is handig voor grotere klanten en standaard gevaarlijk. Bied het alleen aan wanneer de organisatie het eigendom van het domein heeft geverifieerd, nooit voor gratis e-mailaanbieders, en laat gebruikers die zo binnenkomen als lid binnenkomen, niet als beheerder.

## Leg Vast Wat Lidmaatschap Verandert

Wie wie uitnodigde, wie accepteerde, wie een rol wijzigde, wie iemand verwijderde. Deze gebeurtenissen zijn waar de beheerder van een klant naar vraagt wanneer er iets misgaat, en waarvan een beveiligingsvragenlijst vraagt of u ze vastlegt.

Eén tabel `audit_events` met de actor, de organisatie, de actie, het doel en een tijdstip dekt het, zoals het artikel over audittrails in extra-11 beschrijft. Schrijf de gebeurtenis in dezelfde transactie als de wijziging, zodat het log het nooit oneens kan zijn met de data.

Toon de eigen gebeurtenissen van een organisatie aan haar beheerders. Een pagina "Leden" met een tabblad geschiedenis beantwoordt een groot deel van de vragen die anders in uw supportinbox belanden.

## Migreren Vanaf Eén Kolom

Voor een product dat al in productie draait met `profiles.organisation_id`, is de migratie mechanisch als ze in de juiste volgorde gebeurt.

1. Maak `organisations`, `memberships` en `invitations` aan naast de bestaande kolom.
2. Vul aan: één lidmaatschap per bestaand profiel, met de rol die het feitelijk had — meestal eigenaar voor degene die zich aanmeldde, lid voor iedereen die later werd toegevoegd.
3. Herschrijf elke policy zodat ze `is_member()` gebruikt in plaats van te vergelijken met de profielkolom. Dit is de grootste stap; maak eerst een lijst van elke tabel.
4. Pas de frontend aan zodat die de actieve organisatie uit de lidmaatschappen leest.
5. Laat beide een periode naast elkaar draaien, en verwijder de kolom zodra niets haar nog leest.

Test het herschrijven van de policies met twee accounts in twee organisaties, waarbij elke lees- en schrijfactie over de grens heen wordt geprobeerd — de test tussen accounts die het IDOR-artikel in deze reeks aanbeveelt. Het is de enige betrouwbare manier om te weten dat de nieuwe policies standhouden.

## Dit Inrichten

Voor een Lovable-product dat teams toevoegt, is dit doorgaans twee tot vier dagen: aparte tabellen voor organisaties, lidmaatschappen en uitnodigingen met de rol op het lidmaatschap, row level security herschreven rond een `security definer`-functie voor lidmaatschap met de bijbehorende index, uitnodigingstokens die willekeurig, gehasht, verlopend, eenmalig, intrekbaar en gekoppeld aan het uitgenodigde e-mailadres zijn, accepteren in één transactie, de randgevallen afgehandeld — bestaande accounts, afwijkende adressen, duplicaten, verlopen — verwijderen dat het lidmaatschap wist, sessies beëindigt en persoonlijke inloggegevens intrekt terwijl het werk van de persoon behouden blijft, een databasebewaking tegen organisaties zonder eigenaar, door de server gecontroleerd wisselen van organisatie, gebruikerslimieten afgedwongen bij uitnodigen en accepteren, de hoeveelheid in de facturatie gelijk gehouden, en lidmaatschapsgebeurtenissen weggeschreven naar een auditlog.

LaunchStudio bouwt dit wanneer een product voor één gebruiker zijn eerste teamklant krijgt. De engineers zijn van Manifera — elf jaar, 120+ engineers, 160+ projecten, vanuit Amsterdam en Ho Chi Minh-stad.

[Vraag ons wat het verwijderen van een gebruiker in uw product werkelijk doet](https://launchstudio.eu/nl/#contact).

## Echt voorbeeld

### Zevenendertig Mensen Die Waren Vertrokken

Joost Verhagen bouwde Werkbonapp in Lovable: digitale werkbonnen voor installatiebedrijven, gebruikt door 48 bedrijven met zo'n 600 monteurs.

Teamondersteuning was toegevoegd met een uitnodigingsknop en een kolom `organisation_id` op elk profiel. De uitnodigingslink bevatte het ID van de organisatie en verliep nooit; iedereen die hem opende en zich aanmeldde, werd lid van dat bedrijf. Een monteur verwijderen haalde hem uit de teamlijst en zette een vlag, maar liet de kolom — en zijn toegang via de API — onaangeroerd.

Twee dingen brachten het probleem in dezelfde maand aan het licht. Een onderaannemer die voor twee installateurs werkte, kon niet aan de tweede worden toegevoegd omdat een profiel maar één organisatie kon bevatten, en had als omweg een tweede e-mailadres gekregen. En een installateur merkte dat werkbonnen werden bekeken door een account dat ze vier maanden eerder hadden verwijderd.

Drie werkdagen: tabellen voor lidmaatschappen en uitnodigingen aangemaakt, met alle 600 profielen overgezet naar lidmaatschappen; row level security herschreven over 17 tabellen rond een lidmaatschapsfunctie, gecontroleerd met een testsuite tussen organisaties; uitnodigingstokens vervangen door willekeurige, gehashte tokens die na zeven dagen verlopen, eenmalig zijn en gekoppeld aan het uitgenodigde e-mailadres; elke openstaande uitnodigingslink van de oude soort ongeldig gemaakt; verwijderen opnieuw gebouwd zodat het lidmaatschap wordt gewist, de sessies van de gebruiker worden uitgelogd en de tokens van zijn agendafeed worden ingetrokken, terwijl zijn werkbonnen toegeschreven blijven aan "voormalig lid"; een bewaking van de laatste eigenaar in de database; gebruikersaantallen gecontroleerd bij uitnodigen en accepteren; en lidmaatschapsgebeurtenissen weggeschreven naar een auditlog dat zichtbaar is voor de beheerders van elk bedrijf.

**Resultaat:** bij het overzetten werden 37 verwijderde monteurs bij 11 bedrijven gevonden die nog werkende toegang hadden, allemaal op de eerste dag ingetrokken; de logs toonden dat vier van hen de toegang na hun verwijdering hadden gebruikt. Onderaannemers kunnen nu met één login bij meerdere installateurs horen, en twee installateurs stapten binnen de maand over op grotere abonnementen omdat onderaannemers toevoegen mogelijk was geworden.

> *"Iemand verwijderen haalde hem van het scherm en verder niets. Zevenendertig mensen die waren vertrokken, hadden nog toegang, en vier van hen hadden die gebruikt."*
> — **Joost Verhagen, Oprichter, Werkbonapp (Hengelo)**

**Kosten & Doorlooptijd:** €3.400 (model voor lidmaatschappen en uitnodigingen met overzetting, herschreven policies over 17 tabellen met tests tussen organisaties, veilige uitnodigingstokens, verwijderen met intrekking van sessies, bewaking van de laatste eigenaar, afdwingen van gebruikerslimieten, auditlog voor lidmaatschap) — afgerond in 3 werkdagen.

## Veelgestelde vragen

### Waarom niet gewoon een organisatie-ID op het gebruikersprofiel?

Omdat mensen bij meer dan één organisatie horen, rollen bij de relatie horen in plaats van bij de persoon, en openstaande uitnodigingen ergens moeten staan. Een tabel met lidmaatschappen regelt alle drie; een kolom geen enkele.

### Wat maakt een uitnodigingslink veilig?

Een lang willekeurig token dat alleen als hash wordt opgeslagen, een geldigheid van ongeveer zeven dagen, eenmalig gebruik, intrekbaarheid, en een controle dat degene die accepteert inlogt met het e-mailadres dat werd uitgenodigd.

### Wat moet het verwijderen van een teamlid doen?

Het lidmaatschap wissen, zijn sessies beëindigen, persoonlijke inloggegevens zoals API-sleutels en agendatokens intrekken, en de wijziging vastleggen — terwijl het werk dat hij maakte aan hem toegeschreven blijft.

### Hoe voorkom ik de fout van oneindige recursie in lidmaatschapspolicies?

Zet de lidmaatschapscontrole in een `security definer`-functie en roep die aan vanuit uw policies, in plaats van een policy op `memberships` direct `memberships` te laten bevragen.

### Hoe moeten gebruikerslimieten worden afgedwongen?

Op de server, zowel bij het aanmaken als bij het accepteren van een uitnodiging, met openstaande uitnodigingen meegeteld — en met de hoeveelheid in de facturatie bijgewerkt bij elke wijziging in het lidmaatschap.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom een tabel met lidmaatschappen in plaats van een organisatiekolom op profielen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Mensen horen bij meerdere organisaties, rollen horen bij de relatie, en openstaande uitnodigingen hebben een eigen record nodig — een kolom ondersteunt geen van deze."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe maak ik uitnodigingslinks voor teams veilig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Gebruik lange willekeurige tokens opgeslagen als hash, zeven dagen geldigheid, eenmalig gebruik, intrekbaarheid, en vereis acceptatie vanaf het uitgenodigde e-mailadres."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet het verwijderen van een teamlid doen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het lidmaatschap wissen, sessies beëindigen, persoonlijke inloggegevens intrekken en het vastleggen, terwijl eerder werk toegeschreven blijft."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom ik oneindige recursie in Supabase-lidmaatschapspolicies?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Verplaats de lidmaatschapscontrole naar een security definer-functie en roep die aan vanuit policies, in plaats van memberships binnen de eigen policy te bevragen."
      }
    },
    {
      "@type": "Question",
      "name": "Waar moeten gebruikerslimieten worden afgedwongen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Op de server bij zowel uitnodigen als accepteren, met openstaande uitnodigingen meegeteld, en met de facturatie bijgewerkt bij elke wijziging in het lidmaatschap."
      }
    }
  ]
}
</script>
