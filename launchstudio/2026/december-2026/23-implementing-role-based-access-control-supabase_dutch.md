---
Title: Role-Based Access Control (RBAC) implementeren in Supabase voor AI
Keywords: RBAC, Role-Based Access Control, Supabase, AI, Rechten, Postgres
Buyer Stage: Overweging
---

# Role-Based Access Control (RBAC) implementeren in Supabase voor AI

Een prototype van een AI SaaS heeft meestal twee soorten gebruikers: de "gebruiker" en u (de oprichter). Maar in de echte B2B-wereld vereist software complexere hiërarchieën. Binnen één bedrijf heeft u een "Beheerder" (die creditcards kan beheren en alle geüploade documenten kan zien), een "Bewerker" (die de AI kan prompten en teamdocumenten kan aanpassen), en een "Kijker" (die alleen door de AI gegenereerde rapporten kan lezen, maar de AI niet mag aanspreken of API-credits mag verbruiken). Dit heet **Role-Based Access Control (RBAC)**. Als uw Next.js en Supabase AI-architectuur geen RBAC ondersteunt op het niveau van de database, bent u slechts één UI-bug verwijderd van een Junior medewerker die de creditcard van de CEO verwijdert.

## Het Probleem met RBAC op Applicatieniveau

Veel ontwikkelaars implementeren permissies op de verkeerde plek: de frontend of de Next.js API route.

```javascript
// FOUT: Permissies op applicatieniveau (kwetsbaar)
if (user.role === 'viewer') {
  return Response.json({ error: "Onvoldoende rechten" }, { status: 403 });
}
// Ga door en query de database...
```

Dit is gevaarlijk. Als u ooit een nieuwe API-route toevoegt en vergeet de `if (user.role === ...)` check toe te voegen, is uw beveiliging verdwenen.

In **Supabase**, dat direct Postgres blootstelt via een PostgREST API, moet de beveiliging worden ingebouwd in het fundament van de database. We gebruiken **Row-Level Security (RLS)** om RBAC waterdicht af te dwingen, onafhankelijk van hoe slordig uw frontend-code wordt.

## De RBAC Database Schema

Om RBAC te implementeren, heeft u twee nieuwe tabellen nodig in Supabase:

1. **`roles` Tabel (Optioneel maar aanbevolen voor uitbreidbaarheid):** Bevat rollen zoals `admin`, `editor`, `viewer`.
2. **`user_roles` Tabel (De Koppelingstabel):** Koppelt een `user_id` aan een `organization_id` en een `role`. 

*Let op: In B2B SaaS heeft een gebruiker geen rol over de hele wereld. Ze hebben een specifieke rol BINNEN een specifieke organisatie.*

```sql
CREATE TABLE user_roles (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES auth.users(id),
  organization_id UUID REFERENCES organizations(id),
  role TEXT CHECK (role IN ('admin', 'editor', 'viewer'))
);
```

## JWT Custom Claims: De Geheime Truc voor Prestaties

U *zou* complexe SQL-joins kunnen schrijven in uw RLS-beleidsregels om bij elke aanvraag de rol van de gebruiker op te zoeken in de `user_roles` tabel. Dit is echter verschrikkelijk traag en vertraagt uw AI-applicatie aanzienlijk bij elke databasetransactie.

De industriestandaard-oplossing is **JWT Custom Claims**.

Wanneer de gebruiker inlogt, vuurt u een database-trigger af (of een Supabase Auth Hook) die de rol en het organisatie-ID van de gebruiker rechtstreeks *in* hun JSON Web Token (JWT) injecteert.

Op deze manier reist het token van de gebruiker met hen mee. Wanneer de Next.js frontend Supabase opvraagt, bevat het token al het bewijs van hun rol. De database hoeft de `user_roles` tabel niet opnieuw te bevragen.

## RLS Beleidsregels Schrijven (Voorbeelden)

Zodra de rol in het token zit (bijv. in `app_metadata.role`), is het schrijven van RLS-beleidsregels eenvoudig en razendsnel.

### Beschermen van AI Generatie Acties
Een Kijker mag het AI-budget van het bedrijf niet opbranden door prompts te sturen.

```sql
-- Beleid voor het toevoegen van prompts aan de AI_history tabel
CREATE POLICY "Only admins and editors can prompt the AI"
ON ai_history FOR INSERT
WITH CHECK (
  auth.jwt() -> 'app_metadata' ->> 'role' IN ('admin', 'editor')
  AND organization_id = (auth.jwt() -> 'app_metadata' ->> 'organization_id')::uuid
);
```

### Beschermen van Facturering
Alleen Beheerders mogen de Stripe-abonnementsgegevens van het bedrijf bekijken of wijzigen.

```sql
CREATE POLICY "Only admins can view billing data"
ON billing_settings FOR SELECT
USING (
  auth.jwt() -> 'app_metadata' ->> 'role' = 'admin'
);
```

## UI/UX voor RBAC in Next.js

Hoewel beveiliging in Supabase leeft, leeft de gebruikerservaring (UX) in Next.js. Als een gebruiker een 'Kijker' is, mag de frontend de knop "Verwijder Document" niet eens renderen.

Omdat u de `role` via Supabase in het sessieobject heeft geïnjecteerd, heeft uw React-code er direct toegang toe zonder extra netwerkverzoeken:

```tsx
// Next.js (Client Component)
const { data: { session } } = await supabase.auth.getSession();
const userRole = session?.user.app_metadata.role;

return (
  <div>
    <DocumentViewer doc={document} />
    
    {/* Verberg de Delete-knop als ze geen Admin zijn */}
    {userRole === 'admin' && (
      <Button variant="destructive">Verwijder Project</Button>
    )}
  </div>
);
```

## De LaunchStudio-aanpak

Bij LaunchStudio beschouwen we de toevoeging van RBAC als de transformatie van een 'speelgoed-app' naar een B2B SaaS. We ontwerpen complexe databasearchitecturen en implementeren Supabase Custom JWT Claims om te zorgen voor snelle, schaalbare RLS-beleidsregels. We koppelen de backend-beveiliging feilloos aan uw Next.js frontend, zodat Beheerders de controle behouden en uw AI-API budget veilig is voor onbevoegde gebruikers. Uw startup is klaar om enterprise IT-beveiligingscontroles moeiteloos te doorstaan.

---

*Wilt u uw AI-product verkopen aan grote bedrijven, maar ontbreekt het u aan permissiebeheer? LaunchStudio implementeert geavanceerde Role-Based Access Control (RBAC) architecturen. [Laten we uw software beveiligen](https://launchstudio.eu/en/).*
