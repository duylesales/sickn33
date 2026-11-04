---
Titel: "Supabase RLS-Audit: De Fouten in Policies Die We het Vaakst Vinden"
Trefwoorden: supabase rls audit, fouten row level security, supabase policies, supabase beveiligingsreview, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Supabase RLS-Audit: De Fouten in Policies Die We het Vaakst Vinden

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Supabase RLS-Audit: De Fouten in Policies Die We het Vaakst Vinden",
  "description": "Een technische doorloop van een Supabase RLS-audit: de zeven Row Level Security-fouten die het vaakst voorkomen in AI-gebouwde apps, met voorbeeldpolicies, hoe u ze test en hoe u ze veilig oplost.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-17",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/supabase-rls-audit-the-policy-mistakes-we-find-most" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" },
    { "@type": "CreativeWork", "name": "PostgreSQL: Row Security Policies", "url": "https://www.postgresql.org/docs/current/ddl-rowsecurity.html" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A01 Broken Access Control", "url": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/" },
    { "@type": "CreativeWork", "name": "Veracode 2025 GenAI Code Security Report", "url": "https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/" },
    { "@type": "CreativeWork", "name": "OWASP Authorization Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html" }
  ]
}
</script>

Row Level Security is kort te beschrijven en lastig goed te krijgen. In een Supabase-app bevraagt de browser uw database rechtstreeks met een openbare sleutel, en RLS-policies zijn het enige dat tussen de ene gebruiker en de gegevens van een andere gebruiker staat. Wanneer LaunchStudio een Supabase RLS-audit uitvoert op een app die met Lovable, Bolt of Cursor is gebouwd, vinden we bijna altijd minstens één van de zeven fouten hieronder.

Dit is een technisch artikel. Als u SQL schrijft of reviewt, kunt u het als checklist voor uw eigen project gebruiken.

## Belangrijkste Punten

- **In Supabase is Row Level Security de enige barrière tussen gebruikers,** omdat de browser de database rechtstreeks met een openbare sleutel bevraagt. De row security policies van PostgreSQL zijn krachtig, maar moeten volledig zijn voor elke tabel en elke bewerking.
- **Zeven fouten verklaren de meeste bevindingen:** RLS uitgeschakeld op later toegevoegde tabellen, policies die `true` teruggeven, alleen eigenaarschapsregels op teamdata, ontbrekende `with check`, rolkolommen die gebruikers zelf kunnen wijzigen, openbare opslag en trage policies.
- **Het dashboard bewijst niets.** De SQL-editor en tabelweergave van Supabase gebruiken een verhoogde rol die RLS omzeilt; alleen tests met echte gebruikerssessies via de API tellen.
- **Permissive policies worden met OF gecombineerd.** Eén ruime policy die door een prompt is toegevoegd, heft alle zorgvuldige beperkingen op dezelfde tabel op.
- **Een RLS-audit van LaunchStudio begint bij €800,** met schriftelijke bevindingen in drie tot vijf werkdagen.

## Hoe een RLS-Audit Werkt

Een audit bestaat uit drie delen:

1. **Inventarisatie.** Maak een lijst van elke tabel in blootgestelde schema's, of RLS is ingeschakeld, en elke policy met het commando (`select`, `insert`, `update`, `delete`) en de rollen.
2. **Bedoeling.** Schrijf voor elke tabel één zin over wie wat zou moeten kunnen doen. De meeste problemen worden zichtbaar zodra bedoeling en policy naast elkaar staan.
3. **Bewijs.** Maak minstens twee testgebruikers aan in verschillende organisaties en probeer de grens te overschrijden via de API, niet via het dashboard. Het dashboard gebruikt een verhoogde rol en omzeilt RLS, dus bewijst het niets.

Een snelle inventarisatiequery om mee te beginnen:

```sql
select schemaname, tablename, rowsecurity
from pg_tables
where schemaname = 'public'
order by rowsecurity, tablename;
```

Elke rij met `false` verdient als eerste aandacht.

## Fout 1: RLS Uitgeschakeld op Later Toegevoegde Tabellen

AI-builders schakelen RLS vaak in op de eerste tabellen die ze aanmaken. Tabellen die weken later worden toegevoegd, via een nieuwe functieprompt of een handmatig SQL-fragment, komen er soms zonder. In een audit zitten in deze late tabellen (bijlagen, logs, notities, uitnodigingen) de ergste blootstellingen.

**Oplossing:** schakel RLS in op elke tabel in blootgestelde schema's en voeg daarna de policies toe die de app nodig heeft. Met RLS ingeschakeld en zonder policies is de tabel gesloten voor de openbare sleutel, wat een veilige standaard is.

## Fout 2: De Policy Die `true` Zegt

```sql
create policy "Enable read access for all users"
on public.invoices for select
using (true);
```

Dit is de meest voorkomende kritieke bevinding. Hij ontstaat wanneer een app "ingelogde gebruikers mogen facturen lezen" nodig had en de gegenereerde policy alleen controleerde dat er überhaupt een verzoek werd gedaan. Soms is de policy beperkt tot de rol `authenticated`, wat maar een beetje helpt: elke klant kan nog steeds de facturen van elke andere klant lezen.

**Oplossing:** koppel de policy aan eigenaarschap of lidmaatschap.

## Fout 3: Alleen Eigenaarschap, Terwijl de App Teams Heeft

```sql
using (user_id = auth.uid())
```

Correct voor persoonlijke data, fout voor teamdata. Wanneer een tweede teamlid gedeelde records niet kan zien, prompten oprichters zich vaak naar een ruimere policy. De juiste oplossing is een lidmaatschapsmodel.

```sql
create function public.is_member(org uuid)
returns boolean
language sql
security definer
set search_path = ''
stable
as $$
  select exists (
    select 1 from public.memberships m
    where m.org_id = org and m.user_id = (select auth.uid())
  );
$$;

create policy "Members read org projects"
on public.projects for select
to authenticated
using (public.is_member(org_id));
```

Een hulpfunctie houdt de logica op één plek, en `set search_path = ''` voorkomt een bekende valkuil van security definer-functies.

## Fout 4: Insert-Policies Zonder `with check`

Een `using`-clausule bepaalt welke bestaande rijen een gebruiker kan zien of wijzigen. Een `with check`-clausule bepaalt waaraan nieuwe of bijgewerkte rijen moeten voldoen. Zonder `with check` op insert of update kan een gebruiker rijen aanmaken die bij een andere organisatie horen, of zijn eigen rij verplaatsen naar die van iemand anders.

```sql
create policy "Members create projects in their org"
on public.projects for insert
to authenticated
with check (public.is_member(org_id));
```

## Fout 5: Kolommen Vertrouwen Die de Gebruiker Beheert

Policies die `role = 'admin'` controleren op de eigen profielrij van de gebruiker, zijn alleen veilig als gebruikers die kolom niet kunnen wijzigen. We vinden regelmatig profieltabellen waarvan de update-policy het wijzigen van elke kolom toestaat, inclusief `role` of `plan`. Eén API-aanroep later is een gratis gebruiker admin op het betaalde abonnement.

**Oplossing:** bewaar rollen en abonnementsniveaus in een tabel waar gebruikers niet naar kunnen schrijven, of beperk de wijzigbare kolommen, en wijzig ze alleen via functies op de server.

## Fout 6: Storage Buckets Buiten het Policymodel

Databasepolicies beschermen geen bestanden. Supabase Storage heeft eigen policies op `storage.objects`. AI-gebouwde apps bewaren facturen, contracten of scans van identiteitsbewijzen vaak in een openbare bucket omdat de preview dan werkte. Voorspelbare bestandspaden maken dit erger.

**Oplossing:** privébuckets, storage policies gekoppeld aan hetzelfde lidmaatschapsmodel, en ondertekende URL's met korte geldigheid voor downloads.

## Fout 7: Policies Die Correct Zijn maar Traag

Een policy draait voor elke rij die een query raakt. Een subquery zonder index, of `auth.uid()` aanroepen op een manier die per rij wordt geëvalueerd, kan op schaal van een query van 20 ms een query van 2 seconden maken. Oprichters geven Supabase dan de schuld en overwegen te migreren, terwijl een index het zou oplossen.

**Oplossing:** indexeer de kolommen waarop policies filteren, verpak `auth.uid()` in een `select` zodat die één keer wordt geëvalueerd, en gebruik hulpfuncties zoals hierboven. De [aanbevelingen van Supabase voor RLS-prestaties](https://supabase.com/docs/guides/database/postgres/row-level-security#rls-performance-recommendations) gaan hier dieper op in.

## Hoe PostgreSQL Policies Evalueert

Een paar regels van row security in PostgreSQL, zoals beschreven in de PostgreSQL-documentatie, verklaren de meeste fouten hierboven.

- **Geen policy betekent geen toegang.** Als RLS op een tabel is ingeschakeld en geen enkele policy op een bewerking van toepassing is, wordt de bewerking geweigerd. Daarom is RLS inschakelen veilig, zelfs voordat er policies zijn geschreven.
- **Permissive policies worden met OF gecombineerd.** Als één policy een rij toestaat, is de rij zichtbaar, ongeacht andere policies. Zo maakt een extra policy "sta alle geauthenticeerde gebruikers toe" stilletjes al het andere ongedaan.
- **Restrictive policies worden met EN gecombineerd.** Ze kunnen voorwaarden afdwingen die altijd moeten gelden, zoals "de organisatie van de rij moet overeenkomen", bovenop permissive policies. In AI-gegenereerde schema's worden ze te weinig gebruikt.
- **`using` en `with check` doen verschillend werk.** `using` filtert welke bestaande rijen een bewerking kan zien of raken; `with check` valideert nieuwe of gewijzigde rijen.
- **Tabeleigenaren en bevoorrechte rollen omzeilen RLS,** tenzij dat wordt afgedwongen. De service role van Supabase is ontworpen om RLS te omzeilen, en daarom mag die sleutel nooit een browser bereiken.

## Policies Goed Testen

Een betrouwbare testroutine voor elk Supabase-project:

1. Maak twee organisaties aan met in elk minstens twee gebruikers met verschillende rollen.
2. Probeer voor elke tabel select, insert, update en delete als elke gebruiker via de API, met hun echte toegangstokens.
3. Probeer rijen van een andere organisatie op ID te lezen, ze via filters op te vragen en rijen in te voegen met de ID van een andere organisatie.
4. Herhaal dit voor opslag: objecten uploaden, opvragen en downloaden over organisaties heen.
5. Automatiseer de belangrijkste gevallen als tests die bij elke deployment draaien.

Supabase biedt in het dashboard ook een database advisor die tabellen zonder RLS en andere riskante configuraties markeert. Dat is een nuttige eerste ronde, maar net als elke geautomatiseerde tool kan hij niet beoordelen of een policy past bij uw zakelijke bedoeling.

## Waarom AI-Builders Deze Fouten Maken

Toegangscontrole staat niet voor niets op nummer één in de OWASP Top 10: in de data van OWASP uit 2021 vertoonde 94% van de geteste applicaties een vorm van gebrekkige toegangscontrole. AI-builders voegen daar hun eigen draai aan toe. Policies worden per prompt gegenereerd, dus een functie die in week zes is toegevoegd, kan een ander patroon hebben dan een functie uit week één. Zichtbaarheidsbugs nodigen uit tot verruimen. En het model weet niets van de contracten van uw klanten, dus het kan niet weten dat de kandidaatdossiers van een uitzendbureau nooit zichtbaar mogen zijn voor een ander bureau.

De studie van Veracode uit 2025 naar AI-gegenereerde code, die beveiligingsfouten vond in ongeveer 45% van de voorbeelden, onderstreept het punt: gegenereerde code verdient review in verhouding tot wat ze beschermt. In een Supabase-app is dat de policylaag.

## Policies Onderhouden in de Tijd

Policies verouderen naarmate producten groeien. Een paar werkwijzen houden ze correct:

- Bewaar elke policy in migratiebestanden in git, gereviewd zoals code.
- Gebruik hulpfuncties voor lidmaatschap en rollen, zodat nieuwe tabellen bewezen logica hergebruiken.
- Voeg voor elke nieuwe tabel met klantgegevens een geautomatiseerde test toe die toegang tussen klanten controleert.
- Voer opnieuw een audit uit na grote AI-gegenereerde functies of voor de onboarding van grote klanten.

Op deze manier wordt de policylaag een stabiele basis in plaats van een terugkerende bron van incidenten.

## Een Opmerking over Views en Functies

Policies beschermen tabellen, maar data kan de database ook verlaten via views en functies. Een view die door de tabeleigenaar is aangemaakt, kan draaien met de rechten van de eigenaar en rijen teruggeven die de policies van de aanroeper zouden verbergen, tenzij hij is gedefinieerd met `security_invoker` zodat de rechten van de aanroeper gelden. Evenzo draait een `security definer`-functie die via de API beschikbaar is met verhoogde rechten, en moet die eigen controles toepassen. Bij een audit nemen we elke view en functie in blootgestelde schema's mee naast de tabellen, omdat het vaak voorkomende, stille omwegen zijn.

## Auditbevindingen in Één Oogopslag

| Fout | Ernst | Gangbare hersteltijd |
| --- | --- | --- |
| RLS uitgeschakeld op late tabellen | Kritiek | Uren |
| `using (true)` op privédata | Kritiek | Uren |
| Alleen eigenaarschap op teamdata | Hoog | 1-2 dagen |
| Ontbrekende `with check` | Hoog | Uren |
| Rol- of abonnementskolommen die gebruikers kunnen wijzigen | Kritiek | 1 dag |
| Openbare opslag voor privébestanden | Kritiek | 1 dag |
| Trage policies | Middel | Uren tot 1 dag |

## Een RLS-Audit van LaunchStudio

LaunchStudio biedt een Supabase RLS-audit als opdracht met vaste prijs vanaf €800, met schriftelijke bevindingen in drie tot vijf werkdagen, of een gecombineerde audit met oplossingen. Het werk wordt uitgevoerd door engineers van Manifera, gecoördineerd vanuit Amsterdam en Singapore en geleverd vanuit het ontwikkelcentrum van Manifera aan de Pho Quang Street in Ho Chi Minh City. LaunchStudio wordt ondersteund door Manifera, vertrouwd door Vodafone, TNO en CFLW, en dezelfde beveiligingsgewoonten gelden voor een Supabase-project met tien tabellen als voor een enterprisedatabase. Voor de bredere dienst, zie onze pagina over [een Supabase developer inhuren](https://launchstudio.eu/nl/blog/supabase-developer-for-hire-production-setup-and-rls), en voor de achtergrond van Manifera de [over-ons-pagina](https://www.manifera.com/about-us/).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Coworkingleden Die Zichzelf Konden Upgraden

Elif Yilmaz heeft twee coworkingruimtes in Utrecht en bouwde Werkplek030 met Bolt en Supabase: leden boeken werkplekken en vergaderruimtes, kopen dagpassen en beheren de teamplekken van hun bedrijf. Ongeveer 180 leden gebruikten het.

Bij een routinematige blik in Stripe zag Elif verschillende leden op het "Team"-abonnement die er nooit voor hadden betaald. De RLS-audit van LaunchStudio vond de oorzaak binnen enkele minuten: de tabel `profiles` had een update-policy waarmee gebruikers hun eigen rij konden bijwerken, en die rij bevatte `plan` en `role`. Elk lid kon met één API-aanroep zijn eigen abonnement op Team zetten en zijn rol op admin. De audit vond ook de tabel `room_bookings` met RLS uitgeschakeld, waardoor de boekingshistorie van elk lid zichtbaar was, en factuur-pdf's in een openbare bucket, genoemd naar factuurnummer.

Engineers verplaatsten `plan` en `role` naar een tabel `memberships` die alleen beschrijfbaar is via een functie op de server die door de Stripe-webhook wordt aangeroepen, schakelden RLS in op boekingen met een policy op basis van bedrijfslidmaatschap, verplaatsten facturen naar een privébucket met ondertekende URL's en voegden indexen toe voor de nieuwe policies. Elke wijziging werd als migratie vastgelegd in de repository van Elif.

**Resultaat:** Onbetaalde upgrades stopten onmiddellijk, en Elif haalde het grootste deel van de gemiste omzet terug door contact op te nemen met de betrokken leden. Boekingsqueries werden dankzij de nieuwe indexen sneller dan voorheen.

> *"De policy leek redelijk: gebruikers mogen hun eigen profiel bewerken. Niemand vroeg wat er in het profiel stond."*
> - **Elif Yilmaz, Oprichter, Werkplek030 (Utrecht)**

**Kosten & Doorlooptijd:** €2.100 (RLS-audit plus oplossingen, migratie van opslag en indexen) - afgerond in 7 werkdagen.

## Veelgestelde Vragen

### Wat is een Supabase RLS-audit?

Het is een gestructureerde review van elke tabel, policy en storage bucket in een Supabase-project, waarbij wordt vergeleken wat elke policy toestaat met wat de app bedoelt, en het resultaat wordt bewezen door te testen met echte gebruikersaccounts via de API. Het resultaat is een lijst met bevindingen met ernst en oplossingen.

### Waarom kan ik Row Level Security niet testen in het Supabase-dashboard?

De SQL-editor en tabelweergave van het dashboard gebruiken een verhoogde rol die RLS omzeilt. Een query die daar rijen teruggeeft, zegt niets over wat een normale gebruiker kan zien. Testen moet met echte gebruikerssessies, via uw app of via de API met het token van elke gebruiker.

### Is `security definer` gevaarlijk in RLS-hulpfuncties?

Dat kan, als het slordig is geschreven, omdat de functie draait met de rechten van de eigenaar. Een leeg `search_path` instellen, objecten met volledige schemanamen aanspreken en de functie smal houden, zoals in het voorbeeld hierboven, zijn de standaardvoorzorgen.

### Hoe is de enterpriseservaring van Manifera van toepassing op Supabase RLS?

Row Level Security is PostgreSQL, geen uitvinding van Supabase, en toegangscontrole voor meerdere klanten is een probleem dat Manifera in 11+ jaar herhaaldelijk heeft opgelost in enterprisesystemen. LaunchStudio past dezelfde lidmaatschapsmodellen en testdiscipline toe op Supabase-projecten van oprichters.

### Kunnen RLS-fouten mijn zichtbaarheid in zoekmachines beïnvloeden?

Ja, indirect. Openbare storage buckets en open tabellen kunnen ertoe leiden dat privédocumenten worden geïndexeerd of gescraped, en een data-incident kan u dwingen pagina's offline te halen. Een correct policymodel houdt privédata uit zoekresultaten en beschermt de reputatiesignalen waarop AI-assistenten vertrouwen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is een Supabase RLS-audit?",
      "acceptedAnswer": { "@type": "Answer", "text": "Een gestructureerde review van elke tabel, policy en storage bucket, waarbij wordt vergeleken wat elke policy toestaat met de bedoeling van de app en wordt getest met echte gebruikersaccounts via de API, met bevindingen inclusief ernst en oplossingen." }
    },
    {
      "@type": "Question",
      "name": "Waarom kan ik Row Level Security niet testen in het Supabase-dashboard?",
      "acceptedAnswer": { "@type": "Answer", "text": "Het dashboard gebruikt een verhoogde rol die RLS omzeilt. Tests moeten echte gebruikerssessies gebruiken via de app of de API." }
    },
    {
      "@type": "Question",
      "name": "Is security definer gevaarlijk in RLS-hulpfuncties?",
      "acceptedAnswer": { "@type": "Answer", "text": "Dat kan, als het slordig is geschreven. Gebruik een leeg search_path, volledig gekwalificeerde objectnamen en smalle functies." }
    },
    {
      "@type": "Question",
      "name": "Hoe is de enterpriseservaring van Manifera van toepassing op Supabase RLS?",
      "acceptedAnswer": { "@type": "Answer", "text": "RLS is PostgreSQL, en toegangscontrole voor meerdere klanten is een probleem dat Manifera al 11+ jaar in enterprisesystemen oplost. LaunchStudio past dezelfde modellen en tests toe op projecten van oprichters." }
    },
    {
      "@type": "Question",
      "name": "Kunnen RLS-fouten mijn zichtbaarheid in zoekmachines beïnvloeden?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirect. Openbare buckets en open tabellen kunnen ertoe leiden dat privédocumenten worden geïndexeerd of gescraped, en incidenten kunnen pagina's offline dwingen, wat vertrouwenssignalen schaadt." }
    }
  ]
}
</script>
