---
Titel: "Soft Delete versus Hard Delete in SaaS"
Trefwoorden: soft delete vs hard delete, soft delete supabase rls, gdpr erasure soft delete, restore deleted records saas, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Soft Delete versus Hard Delete in SaaS

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Soft Delete versus Hard Delete in SaaS",
  "description": "Wanneer een gebruiker op 'Verwijderen' klikt, moet de data dan direct definitief verdwijnen of tijdelijk worden verborgen? Deze gids vergelijkt soft delete en hard delete voor met AI gebouwde SaaS-applicaties, legt uit hoe u soft delete implementeert met PostgreSQL Row Level Security (RLS) en partiële indexen, hoe u een prullenbak- en herstelfunctie bouwt, hoe cascading foreign keys zich gedragen en hoe u soft delete in overeenstemming brengt met AVG-verwijderingsverzoeken (GDPR erasure).",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-12",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/soft-delete-vs-hard-delete-in-saas" },
  "citation": [
    { "@type": "CreativeWork", "name": "GDPR Article 17: Right to erasure", "url": "https://gdpr-info.eu/art-17-gdpr/" },
    { "@type": "CreativeWork", "name": "PostgreSQL: Partial indexes", "url": "https://www.postgresql.org/docs/current/indexes-partial.html" },
    { "@type": "CreativeWork", "name": "PostgreSQL: Foreign keys", "url": "https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-FK" },
    { "@type": "CreativeWork", "name": "Supabase Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" }
  ]
}
</script>

Elke SaaS-applicatie beschikt over een verwijderknop. Achter die rode knop schuilt echter een fundamentele architectuurkeuze waar veel oprichters zelden bewust bij stilstaan. Wanneer een klant een project, een factuur, een klantrelatie of een dossier verwijdert, moet die datarij dan per direct fysiek uit de database worden gewist (hard delete), of moet de rij simpelweg worden gemarkeerd als inactief en worden verborgen voor de gebruikersinterface (soft delete), zodat deze bij een vergissing direct kan worden hersteld?

AI-ontwikkeltools zoals Lovable, Bolt en Cursor kiezen deze strategie standaard voor u - en zij kiezen vrijwel unaniem voor **hard delete**. De gegenereerde code vuurt een directe `DELETE`-query af, regelmatig gecombineerd met `ON DELETE CASCADE` op gerelateerde tabellen. In een vroege demo werkt dat prima. In een zakelijke productieomgeving leidt dit echter onvermijdelijk tot paniekerige supporttickets (*"Ik heb per ongeluk de verkeerde klant gewist, kunnen jullie dat alsjeblieft terugzetten?"*), onoplosbare aansprakelijkheidskwesties en soms zelfs catastrofale kettingreacties waarbij het wissen van één contactpersoon honderden gekoppelde facturen en projecten met terugwerkende kracht vernietigt.

Toch is soft delete niet automatisch de heilige graal. Het maakt databasequery's complexer, kan botsen met unieke constraints en leidt tot ophoping van data als er geen purge-beleid is. Deze handleiding legt uit wanneer u welke methode kiest en hoe u soft delete veilig en performant implementeert in Supabase.

## Belangrijkste Punten

- **Hard delete wist data definitief en onherroepelijk uit de database;** soft delete markeert een record met een `deleted_at`-tijdstempel en verbergt het voor reguliere gebruikers.
- **Soft delete maakt prullenbakken, ongedaan-maken (undo) en direct herstel mogelijk,** wat menselijke fouten opvangt en supportkosten minimaliseert.
- **Soft-deleted data telt juridisch niet als gewist:** onder de AVG (GDPR) heeft een betrokkene recht op vergetelheid, wat vereist dat soft-deleted persoonsgegevens na een bewaartermijn alsnog definitief worden gewist of geanonimiseerd.
- **Implementeer soft delete op databaseniveau** via PostgreSQL Row Level Security (RLS) of views, gecombineerd met partiële unieke indexen (`WHERE deleted_at IS NULL`).
- **Saniteer cascading deletes (`ON DELETE CASCADE`):** ongecontroleerde cascades zijn de voornaamste oorzaak van grootschalig onbedoeld dataverlies in AI-apps.

## Vergelijking: Hard Delete versus Soft Delete

| Eigenschap | Hard Delete (Fysiek wissen) | Soft Delete (Logisch markeren) |
| --- | --- | --- |
| Herstel na menselijke fout | Alleen via een tijdrovende database-restore | Met één muisklik vanuit een prullenbak |
| Spoorzoeking bij geschillen | Data is spoorloos verdwenen | Record blijft traceerbaar met `deleted_by` |
| Query-complexiteit | Laag en overzichtelijk | Vereist uitsluiting van gewiste rijen |
| Opslagruimte | Direct vrijgegeven | Data stapelt zich op tot de periodieke purge |
| AVG / GDPR Recht op Vergetelheid | Voldoet direct voor de actieve database | Vereist een harde purge na de bewaartermijn |
| Unieke constraints | Standaard indexen functioneren normaal | Vereist partiële indexen (`WHERE deleted_at IS NULL`) |

De meest volwassen softwareproducten combineren beide technieken: **soft delete** voor dagelijkse gebruikersacties met een herstelperiode van 30 tot 60 dagen, gevolgd door een geautomatiseerde **hard delete** (purge) of anonimisering zodra de bewaartermijn verstrijkt.

## Wanneer Kiest U voor Hard Delete?

Hard deletion is passend voor:

- **Echt vluchtige data:** tijdelijke concepten, verlopen sessietokens, wachtrij-items of cache-tabellen.
- **Officiële AVG-verwijderingsverzoeken (Recht op Vergetelheid):** persoonsgegevens die op expliciet verzoek van een burger definitief gewist moeten worden en waarvoor geen wettelijke bewaarplicht geldt.
- **Hoogvolume data zonder historische waarde:** gelezen pushnotificaties of tijdelijke upload-chunks.

## Wanneer Kiest U voor Soft Delete?

Soft deletion is onmisbaar voor:

- **Bedrijfskritische kernentiteiten:** klanten, dossiers, offertes, facturen, projecten en geüploade contracten.
- **Gedeelde teamdata:** omgevingen waarin meerdere collega's gelijktijdig in dezelfde dossiers werken en een vergissing van één medewerker grote gevolgen heeft.
- **Historische financiële data:** records waarnaar wordt verwezen door boekhoudkundige transacties (een gewiste debiteur mag niet leiden tot corrupte historische omzetstatistieken).

## Soft Delete Implementeren in Supabase met RLS

Het standaardpatroon voegt twee kolommen toe aan de tabel:

- `deleted_at timestamptz DEFAULT NULL`: bevat het tijdstip van verwijdering (null betekent actief).
- `deleted_by uuid REFERENCES auth.users(id)`: het gebruikers-ID van degene die de actie uitvoerde.

Het "verwijderen" van een record is functioneel een `UPDATE`-operatie die deze velden vult. Om te zorgen dat gewiste records automatisch onzichtbaar worden voor de frontend, configureert u **Row Level Security (RLS)**:

```sql
create policy "Gebruikers zien alleen actieve projecten"
  on projects for select
  using (deleted_at is null);
```

Een aparte beheerderspolicy of een specifieke databasefunctie stelt kantoorbeheerders in staat om rijen met `deleted_at IS NOT NULL` in te zien binnen een "Prullenbak"-weergave.

Trek daarnaast directe `DELETE`-permissies voor gewone gebruikers in op de tabel, zodat alle verwijderingen verplicht via een gecontroleerde databasefunctie verlopen.

## Voorkom Problemen met Unieke Indexen

Een veelvoorkomende bug bij soft delete ontstaat bij unieke constraints. Stel dat een klantentabel een unieke constraint heeft op het e-mailadres of de projectcode. Een gebruiker verwijdert een project met code `PROJ-2028-01` en probeert vervolgens een nieuw project met diezelfde code aan te maken. De database weigert het nieuwe record omdat de soft-deleted rij technisch nog steeds bestaat.

De oplossing is een **partiële unieke index** in PostgreSQL:

```sql
create unique index projects_unique_active_code
  on projects (organisation_id, code)
  where deleted_at is null;
```

Hierdoor dwingt PostgreSQL de uniekheid uitsluitend af over de *actieve* records. Zodra een record soft-deleted is, komt de unieke waarde direct vrij voor hergebruik.

## Het Gevaar van Cascading Deletes (`ON DELETE CASCADE`)

In relationele databases kunnen foreign keys worden ingesteld op cascade. Wist u een hoofdrecord, dan wist de database automatisch alle onderliggende rijen mee.

Bij hard deletes leidt dit regelmatig tot rampen. Het wissen van één debiteur kan geruisloos tientallen projecten, duizenden taken en jaren aan urenregistraties wegvagen.

Best practices voor relaties:

- Gebruik **restrictieve foreign keys** (`ON DELETE RESTRICT`) voor alle hoofdentiteiten: de database weigert verwijdering zolang er nog actieve projecten of facturen aan gekoppeld zijn.
- Pas cascading alleen toe op entiteiten die zonder hun ouder geen enkele zelfstandige betekenis hebben, zoals de afzonderlijke regels (`invoice_items`) van één factuur.
- Laat soft deletion van een ouder-record via een databasetransactie lopen die gekoppelde subrecords consistent van dezelfde `deleted_at`-tijdstempel voorziet, zodat ze bij een herstelactie ook gezamenlijk worden teruggezet.

## De Prullenbak en de 10-Seconden Undo

Soft delete maakt krachtige UX-features mogelijk die gebruikers enorm waarderen:

- **De directe Undo-toast:** toon na elke verwijdering gedurende tien seconden een melding onderin het scherm: *"Project verplaatst naar prullenbak [Ongedaan maken]"*.
- **De centrale Prullenbak:** een overzichtsscherm voor beheerders waarin gewiste items 30 of 60 dagen bewaard blijven, inclusief de naam van de collega die het item heeft gewist.
- **Herstelknop:** herstelt het record en alle gerelateerde subdata ogenblikkelijk naar de actieve toestand.
- **Definitieve purge-cronjob:** een geautomatiseerde achtergrondtaak (via pg_cron) die records waarvan de `deleted_at` ouder is dan 60 dagen definitief fysiek uit de database verwijdert.

## Soft Delete en AVG / GDPR

Let op: een soft-deleted record is juridisch **niet gewist**. Persoonsgegevens in soft-deleted tabellen vallen onverminderd onder de bescherming van de AVG en blijven kwetsbaar bij eventuele datalekken.

- **Actieve opschoning:** stel een harde bewaartermijn in waarna gegevens geautomatiseerd worden gewist (hard delete) of geanonimiseerd.
- **Recht op Vergetelheid:** dient een klant een formeel AVG-verwijderingsverzoek in, voer dan een echte fysieke verwijdering of grondige pseudonimisering uit, mits fiscale wetgeving (zoals de 7-jarige bewaarplicht voor facturen) dat toestaat.

## Veelvoorkomende Fouten

**Overal hard deletes toepassen.** Waardoor één verkeerde klik leidt tot onomkeerbaar dataverlies en dure herstelwerkzaamheden.

**Soft delete uitsluitend in frontend-JavaScript filteren.** Waardoor zoekfuncties, exports en totalenberekeningen per ongeluk 'gewiste' data blijven tonen.

**Reguliere unieke constraints behouden.** Waardoor gebruikers foutmeldingen krijgen als ze een gewiste gebruikersnaam of projectcode opnieuw willen gebruiken.

**Nooit een opschoontaak (purge) draaien.** Waardoor databases na jaren vollopen met miljoenen overbodige 'gewiste' rijen die de query-prestaties vertragen.

## Hoe LaunchStudio Helpt

LaunchStudio ontwerpt en realiseert betrouwbare data-lifecycle-architecturen voor met AI gebouwde SaaS-applicaties: we bepalen per entiteit de juiste balans tussen soft en hard delete, implementeren waterdichte Row Level Security policies en partiële indexen in PostgreSQL, saneren gevaarlijke cascading foreign keys, bouwen intuïtieve prullenbak- en herstelflows en automatiseren de periodieke AVG-opruimtaken.

Het **Launch Ready**-pakket (€800 - €3.500) omvat dataherstel, soft-delete architectuur en security hardening. **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) biedt daarnaast continue database-optimalisatie, managed hosting en actieve monitoring. Gebruik onze [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een helder inzicht in de kosten.

LaunchStudio is een initiatief van Manifera, een softwarebedrijf met 11+ jaar ervaring, 160+ succesvolle projecten en 120+ gespecialiseerde software engineers met diepgaande ervaring in enterprise database-architecturen. Oprichters ontmoeten ons aan de Herengracht 420 in Amsterdam; de softwareontwikkeling vindt plaats in ons gespecialiseerde ontwikkelcentrum aan Pho Quang Street in Ho Chi Minh City, ondersteund door onze hub aan Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Bouwplanningstool Waar Eén Verkeerde Klik Anderhalf Jaar Werk Wiste

Pieter Kuiper bouwde Bouwplanner met Bolt en Supabase: een intuïtief planningssysteem voor middelgrote bouw- en renovatiebedrijven, waarmee uitvoerders projectfasen inrichten, taken toewijzen, werf-foto's uploaden en chatten met onderaannemers. Op een ochtend wilde een projectleider bij een aangesloten aannemersbedrijf een dubbel aangemaakte klantrelatie opruimen. Omdat de door Bolt gegenereerde databaseschema's overal `ON DELETE CASCADE` bevatten, trad er een verwoestende kettingreactie op: het wissen van de klantrelatie wiste ogenblikkelijk vier actieve bouwprojecten, ruim 600 gekoppelde taken, circa 1.200 fotobijlagen en alle bijbehorende berichten - goed voor anderhalf jaar aan gedocumenteerde bouwgeschiedenis.

Het herstel vereiste een spoedprocedure: LaunchStudio voerde een point-in-time herstel van de gehele database uit naar een geïsoleerde kopie-omgeving, waarna engineers twee volle werkdagen bezig waren om de gewiste records handmatig te isoleren en terug te plaatsen in de live database. Een technische inspectie toonde aan dat dit gevaar in de gehele applicatie zat: elke verwijderknop voerde een directe harde delete uit, er was geen bevestigingsvenster bij acties met grote impact, geen auditspoor en geen mogelijkheid om fouten ongedaan te maken.

LaunchStudio verving de harde verwijderingen door een robuust soft-delete mechanisme voor klanten, projecten, taken, documenten en communicatie, aangedreven door `deleted_at`- en `deleted_by`-kolommen. PostgreSQL Row Level Security policies sluiten gewiste records automatisch uit van alle standaardquery's. De gevaarlijke cascades werden vervangen door restrictieve foreign keys, en partiële unieke indexen zorgen ervoor dat projectcodes na verwijdering direct hergebruikt kunnen worden. Beheerders kregen een centrale prullenbak waarin gewiste projecten met één muisklik inclusief alle onderliggende taken en foto's kunnen worden hersteld. Verwijderacties tonen nu een samenvatting van de impact met een 10-seconden undo-knop, een nachtelijke pg_cron taak wist records na 60 dagen definitief en elke actie wordt gelogd in het auditspoor.

**Resultaat:** In de daaropvolgende zes maanden herstelden gebruikers zelfstandig ruim 140 per ongeluk gewiste taken en documenten uit de prullenbak zonder de helpdesk te raadplegen. Er is sindsdien geen enkele nood-restore meer nodig geweest, en de getroffen hoofdaannemer trad zelfs op als enthousiaste referent voor Bouwplanner vanwege de professionele afhandeling.

> *"Eén onbedoelde muisklik mag nooit anderhalf jaar werk van een aannemer kunnen vernietigen. Nu is dat technisch onmogelijk, en lossen gebruikers eventuele foutjes binnen tien seconden zelfstandig op."*
> - **Pieter Kuiper, Oprichter, Bouwplanner (Zwolle)**

**Kosten & Doorlooptijd:** €3.300 (Launch Ready-pakket: dataherstel, soft delete met RLS, cascade-herontwerp, prullenbak en herstel, opschoontaak en auditlogging) - afgerond in 9 werkdagen.

## Veelgestelde Vragen

### Moet mijn SaaS kiezen voor soft delete of hard delete?

Voor waardevolle zakelijke kerngegevens (zoals klanten, projecten, dossiers en facturen) is soft delete met een bewaartermijn de beste keuze, omdat het herstel en compliance mogelijk maakt. Voor tijdelijke sessies, caches of na afloop van de bewaartermijn is hard delete passend. De meeste professionele applicaties combineren beide.

### Voldoet soft delete aan de AVG-eisen voor gegevensverwijdering?

Nee, niet op zichzelf. Omdat de persoonsgegevens in de database aanwezig blijven, is soft delete juridisch geen definitieve verwijdering. U voldoet aan de AVG door soft-deleted gegevens na een gedocumenteerde termijn (bijv. 30 of 60 dagen) via een geautomatiseerde purge definitief te wissen of te anonimiseren.

### Hoe verberg ik soft-deleted rijen het meest betrouwbaar in Supabase?

Via Row Level Security (RLS) policies met de voorwaarde `deleted_at IS NULL`, of via database views. Vertrouw niet op handmatige filters in frontend-code, omdat nieuwe functies of AI-gegenereerde query's deze filterconditie gegarandeerd een keer zullen vergeten.

### Hoe helpt de ervaring van Manifera bij data-lifecycle beheer?

Manifera ontwerpt al meer dan 11 jaar complexe datamodellen en lifecycles voor veeleisende enterprise-klanten. LaunchStudio benut deze ervaring om verwijderingsprocessen in te richten die gebruikers beschermen tegen dataverlies, prestaties waarborgen en voldoen aan privacywetgeving.

### Verhoogt een betrouwbaar dataherstelmechanisme het vertrouwen van kopers?

Zeker. Het voorkomen van dataverlies en het bieden van een duidelijke prullenbak- en herstelfunctie wekt enorm veel vertrouwen bij zakelijke beslissers. Bedrijven beoordelen software positiever wanneer een menselijke fout niet direct leidt tot een operationele crisis.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet mijn SaaS kiezen voor soft delete of hard delete?",
      "acceptedAnswer": { "@type": "Answer", "text": "Soft delete voor kernrecords met herstelbehoefte; hard delete voor tijdelijke data en na afloop van de bewaartermijn." }
    },
    {
      "@type": "Question",
      "name": "Voldoet soft delete aan de AVG-eisen voor gegevensverwijdering?",
      "acceptedAnswer": { "@type": "Answer", "text": "Niet vanzelf; er is een periodieke purge nodig die gegevens na de bewaartermijn alsnog definitief wist of anonimiseert." }
    },
    {
      "@type": "Question",
      "name": "Hoe verberg ik soft-deleted rijen het meest betrouwbaar in Supabase?",
      "acceptedAnswer": { "@type": "Answer", "text": "Gebruik PostgreSQL Row Level Security (RLS) policies met deleted_at IS NULL of views, nooit uitsluitend client-side filters." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij data-lifecycle beheer?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera bouwt al 11+ jaar robuuste enterprise data-architecturen die dataverlies voorkomen en prestaties waarborgen." }
    },
    {
      "@type": "Question",
      "name": "Verhoogt een betrouwbaar dataherstelmechanisme het vertrouwen van kopers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, het verlaagt operationele risico's voor zakelijke gebruikers en voorkomt kostbare reputatieschade door dataverlies." }
    }
  ]
}
</script>
