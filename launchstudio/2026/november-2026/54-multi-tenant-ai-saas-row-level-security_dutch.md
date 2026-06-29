---
Title: Hoe bouw je een Multi-Tenant AI SaaS met Row-Level Security
Keywords: Multi-Tenant, AI, SaaS, Row-Level, Security, Supabase
Buyer Stage: Bewustzijn
---

# Hoe bouw je een Multi-Tenant AI SaaS met Row-Level Security

Op het moment dat uw AI SaaS-product zijn eerste zakelijke klant tekent, wordt u geconfronteerd met een niet-onderhandelbare vereiste: **data-isolatie**. Zakelijke juridische afdelingen zullen het contract niet ondertekenen als de vertrouwelijke documenten van Bedrijf A theoretisch toegankelijk zijn voor de gebruikers van Bedrijf B—zelfs niet per ongeluk, zelfs niet door een softwarebug. Dit is geen paranoia; het is een wettelijke verplichting onder de AVG (GDPR), SOC 2 en vrijwel elke zakelijke inkoopstandaard. De architectonische oplossing is **multi-tenancy met Row-Level Security (RLS)**, en als uw AI-prototype is gebouwd met Lovable of Bolt, heeft het dit vrijwel zeker niet.

## De Drie Multi-Tenancy Modellen

Er zijn drie benaderingen voor data-isolatie, elk met verschillende kosten- en beveiligingsprofielen:

**1. Database-per-tenant:** Elke klant krijgt zijn eigen Postgres-database. Maximale isolatie, maar operationeel een nachtmerrie op schaal. Als u 500 klanten heeft, beheert u 500 databases, 500 connection pools en 500 migratiescripts. Dit model is alleen haalbaar voor zeer grote enterprise-contracten ($100K+/jaar).

**2. Schema-per-tenant:** Elke klant krijgt zijn eigen schema binnen een gedeelde database. Beter dan database-per-tenant, maar creëert nog steeds operationele overhead met honderden schema's. Migratiebeheer wordt complex.

**3. Gedeelde tabel met RLS (Aanbevolen):** Alle klanten delen dezelfde tabellen, maar elke rij heeft een kolom `organization_id`, en Postgres Row-Level Security beleidsregels zorgen ervoor dat een gebruiker alleen rijen kan zien die behoren tot zijn organisatie. Dit is het model dat wij aanbevelen voor 95% van de AI SaaS-producten.

## RLS implementeren in Supabase

Supabase maakt RLS-implementatie opmerkelijk eenvoudig omdat het gebruikmaakt van native Postgres-beleidsregels. Hier is het patroon:

**Stap 1 — Voeg `organization_id` toe aan elke tabel:**

Elke tabel die klantgegevens bevat, moet een kolom `organization_id` hebben met een externe sleutel (foreign key) naar uw tabel `organizations`. Dit omvat: `documents`, `ai_conversations`, `embeddings`, `invoices`, `team_members` en `audit_logs`.

**Stap 2 — Maak een helperfunctie:**

Maak een Postgres-functie die de organisatie van de gebruiker extraheert uit het JWT-token:

```sql
CREATE OR REPLACE FUNCTION get_user_org_id()
RETURNS UUID AS $$
  SELECT (auth.jwt() -> 'app_metadata' ->> 'organization_id')::UUID;
$$ LANGUAGE sql SECURITY DEFINER;
```

**Stap 3 — Pas RLS-beleidsregels toe:**

```sql
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can only see their org's documents"
ON documents FOR SELECT
USING (organization_id = get_user_org_id());

CREATE POLICY "Users can only insert into their org"
ON documents FOR INSERT
WITH CHECK (organization_id = get_user_org_id());
```

Dit beleid wordt afgedwongen op databaseniveau. Zelfs als uw applicatiecode een bug heeft die vergeet te filteren op organisatie, zal de database stilletjes rijen uitsluiten die niet behoren tot de organisatie van de geauthenticeerde gebruiker. Dit is defense-in-depth.

## RLS voor AI-Specifieke Tabellen

AI SaaS-producten hebben unieke datatabellen die speciale RLS-aandacht vereisen:

**Vector Embeddings Tabel:** Uw RAG-pijplijn slaat document-embeddings op. Deze embeddings zijn wiskundige representaties van de bedrijfseigen inhoud van uw klant. Als een similariteitszoekopdracht embeddings retourneert van een andere tenant, heeft u een catastrofaal datalek. Pas RLS toe op uw tabel `embeddings` met hetzelfde `organization_id` patroon.

**AI Gespreksgeschiedenis:** LLM gesprekslogboeken bevatten gebruikersprompts, die vertrouwelijke bedrijfsinformatie kunnen bevatten. RLS moet worden toegepast om ervoor te zorgen dat de gespreksgeschiedenis strikt is geïsoleerd per tenant.

**Modelconfiguratie Tabel:** Als uw product klanten in staat stelt AI-gedrag aan te passen (aangepaste systeemprompts, temperatuurinstellingen, modelselectie), moeten deze configuraties ook tenant-geïsoleerd zijn.

## Het JWT Metadata Patroon

De sleutel om RLS naadloos te laten werken, is het inbedden van het `organization_id` in het JWT-token van de gebruiker op het moment van inloggen. Wanneer een gebruiker zich aanmeldt via Supabase Auth, gebruik dan een databasetrigger of Edge Function om automatisch `app_metadata.organization_id` in te stellen op de JWT. Op deze manier draagt elk volgend API-verzoek de tenant-context mee en kunnen RLS-beleidsregels deze extraheren zonder extra database-lookups.

## Prestatieoverwegingen

Een veelgehoorde zorg is dat RLS query-overhead toevoegt. In de praktijk is de impact op de prestaties verwaarloosbaar als u:

1. **De `organization_id` kolom indexeert** in elke tabel. Dit is niet onderhandelbaar.
2. **Samengestelde indexen gebruikt** voor veelgebruikte combinaties (bijv. `(organization_id, created_at)` voor op tijd gesorteerde queries).
3. **Grote tabellen partitioneert** op `organization_id` als een enkele tenant miljoenen rijen genereert (bijv. AI-inferentielogboeken met een hoog volume).

Met de juiste indexering voegt RLS minder dan 1ms overhead toe per query—onzichtbaar voor de eindgebruiker.

## Testen van Multi-Tenancy

Vertrouw er nooit op dat RLS werkt zonder expliciet te testen. Maak een testsuite die:

1. Twee testorganisaties met verschillende gebruikers aanmaakt
2. Data invoegt in beide organisaties
3. Authenticeert als Gebruiker A en verifieert dat zij alleen de data van Organisatie A kunnen zien
4. Authenticeert als Gebruiker B en verifieert dat zij alleen de data van Organisatie B kunnen zien
5. Toegang over de tenants heen probeert en bevestigt dat dit wordt geblokkeerd

Voer deze testsuite uit bij elke deployment. Eén enkele RLS-misconfiguratie kan leiden tot een datalek dat uw bedrijf vernietigt.

## De LaunchStudio-aanpak

Bij LaunchStudio implementeren we multi-tenancy met RLS als een standaardcomponent van elk AI SaaS-product dat we naar productie brengen. De meeste prototypes gebouwd met AI-builders missen elke vorm van data-isolatie—ze slaan alle data op in één enkele platte structuur zonder tenant-grenzen. We bouwen productieklare RLS in, voegen organisatiebeheer toe en implementeren het JWT-metadata-patroon zodat uw AI-product vanaf dag één enterprise-ready is.

---

*Wilt u uw AI-prototype enterprise-ready maken met goede data-isolatie? LaunchStudio implementeert productieklare multi-tenancy met Row-Level Security. [Laten we praten](https://launchstudio.eu/en/).*
