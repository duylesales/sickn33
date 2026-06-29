---
Title: Hoe bouw je een White-Label AI Product met Next.js
Keywords: White-Label, AI, Product, Next.js, Multi-Tenant, Branding, SaaS
Buyer Stage: Overweging
---

# Hoe bouw je een White-Label AI Product met Next.js

Er is een lucratief, maar vaak over het hoofd gezien bedrijfsmodel in de B2B AI-ruimte: **White-Labeling**. Bepaalde grote traditionele bedrijven (denk aan advocatenkantoren, makelaardijen of zorgverleners) willen uw specifieke AI-oplossing (zoals uw geavanceerde documentanalysator) aan *hun eigen klanten* aanbieden. Ze willen echter niet dat hun klanten zien dat het wordt aangedreven door "StartupXYZ". Ze eisen dat de app op hun eigen domein draait (`ai.megacorp.com`), met hun eigen bedrijfslogo, hun eigen kleurenpalet en hun eigen welkomst-e-mails. Dit is een B2B2C (Business-to-Business-to-Consumer) model. Het vereist een robuuste **Multi-Tenant White-Label Architectuur** in Next.js.

## De Uitdagingen van White-Labeling

Het handmatig klonen en implementeren van 50 afzonderlijke Vercel-projecten voor 50 verschillende klanten is operationele zelfmoord. U kunt de code niet onderhouden en CI/CD wordt onmogelijk. 

De moderne aanpak is **één enkele codebase (Single Codebase)** die dynamisch de branding, het domein en de database-isolatie aanpast op basis van de URL die wordt bezocht.

## Architectuur: Next.js Middleware & Supabase

### 1. Domein Routering met Middleware
De kern van de oplossing ligt in **Next.js Edge Middleware**. Wanneer een verzoek binnenkomt op uw Vercel-app, onderschept de middleware de URL (bijv. `ai.megacorp.com`).

```typescript
// middleware.ts
import { NextResponse } from 'next/server';

export default async function middleware(req) {
  const url = req.nextUrl.clone();
  // Krijg de host (bijv. 'ai.megacorp.com')
  const hostname = req.headers.get('host');

  // Herschrijf het verzoek naar een dynamische route, met behoud van de originele URL
  url.pathname = `/_sites/${hostname}${url.pathname}`;
  return NextResponse.rewrite(url);
}
```

Met behulp van Vercel's *Custom Domains API* kunnen uw klanten hun domein naar uw Vercel-project verwijzen via een CNAME-record. De middleware vertaalt dit vervolgens stilzwijgend, zodat uw Next.js-app weet welke klant dit domein opvraagt.

### 2. Dynamische Branding Ophalen
In uw Next.js dynamische route (`app/_sites/[domain]/page.tsx`), haalt u de branding-instellingen op uit Supabase:

```typescript
// Haal de configuratie op uit de database op basis van het domein
const { data: tenantConfig } = await supabase
  .from('tenants')
  .select('company_name, logo_url, primary_color')
  .eq('custom_domain', params.domain)
  .single();

// Pas dynamisch CSS-variabelen toe voor Tailwind
return (
  <div style={{ '--primary': tenantConfig.primary_color } as React.CSSProperties}>
    <img src={tenantConfig.logo_url} alt={tenantConfig.company_name} />
    <AIInterface />
  </div>
);
```
Door CSS-variabelen te injecteren, kan uw Tailwind CSS-systeem direct de primaire knopkleuren veranderen van het paars van uw startup naar het bedrijfsrood van de klant.

### 3. Data Isolatie (Row-Level Security)
Dit is het meest kritieke punt. Als een gebruiker inlogt via `ai.megacorp.com`, mogen de AI en het RAG-systeem uitsluitend toegang hebben tot de documenten van MegaCorp.

Gebruik Supabase Auth en Row-Level Security (RLS). Bij het aanmaken van gebruikers via een white-label domein, wijst u het betreffende `tenant_id` toe aan hun metadata.

```sql
-- Postgres RLS Beleid voor White-Label AI Documenten
CREATE POLICY "Users access their tenant's documents only"
ON documents FOR SELECT
USING (tenant_id = (auth.jwt() -> 'app_metadata' ->> 'tenant_id')::uuid);
```

### 4. White-Label E-mails verzenden
U kunt geen bevestigingsmail sturen vanaf `support@startupxyz.com` als de app white-labeled is.

Met behulp van **Resend** kunt u dynamisch het `from`-adres in uw backend wijzigen. U moet API's implementeren zodat uw zakelijke klanten hun eigen domeinen in Resend kunnen verifiëren (via DNS-records), zodat uw systeem namens hen geautoriseerde e-mails kan verzenden:

```typescript
await resend.emails.send({
  from: `${tenantConfig.company_name} AI <ai@${tenantConfig.custom_domain}>`,
  to: user.email,
  subject: "Uw AI-analyse is voltooid",
  // ...
});
```

## De LaunchStudio-aanpak

Bij LaunchStudio bouwen we niet zomaar B2B apps; we bouwen schaalbare platformen. We ontwerpen de complexe Next.js Middleware-structuren die honderden custom domeinen routeren naar één enkele, robuuste Vercel-implementatie. We zetten de tenant-configuratietabellen en ondoordringbare RLS-beleidsregels op in Supabase om absolute gegevensisolatie te garanderen, en we implementeren dynamische Tailwind-theming. Uw startup kan zo met vertrouwen $10k/maand white-label licenties verkopen aan Enterprises, in de wetenschap dat de infrastructuur moeiteloos schaalt.

---

*Willen Enterprises uw AI-product white-labelen, maar laat uw architectuur dit niet toe? LaunchStudio bouwt schaalbare, multi-tenant white-label architecturen in Next.js. [Maak uw platform enterprise-ready](https://launchstudio.eu/en/).*
