---
Title: Hoe bouw je AI-Powered Search met Typesense en Next.js
Keywords: AI, Search, Typesense, Next.js, Vector, Hybrid, RAG
Buyer Stage: Overweging
---

# Hoe bouw je AI-Powered Search met Typesense en Next.js

Wanneer uw SaaS-product opschaalt naar duizenden documenten, projecten of chatgeschiedenissen, verwachten gebruikers een feilloze zoekervaring. Ze willen niet alleen zoeken op exacte zoekwoorden ("factuur Q3"); ze willen zoeken op betekenis ("recente financiële documenten over inkomsten"). Pure trefwoordzoekopdrachten (keyword search) via Postgres `LIKE` of `tsvector` schieten hierin tekort. Tegelijkertijd falen pure semantische vectorzoekopdrachten via `pgvector` vaak bij specifieke namen, ID's of acroniemen. De oplossing voor enterprise AI-applicaties is **Hybride Zoeken**, en het open-source zoekmechanisme dat deze revolutie leidt, is **Typesense**.

## De Beperkingen van Pure Vector Databases

Veel AI-oprichters stoppen al hun documenten in een vector-database zoals Pinecone of uitsluitend in Supabase met `pgvector`. Wanneer een gebruiker vervolgens zoekt naar "SKU-9982", vindt de vector-database geen overeenkomst. 

Waarom? Omdat vectorembeddings de *semantische betekenis* (concepten, synoniemen, sfeer) van tekst vastleggen, niet de exacte tekenreeks. "SKU-9982" heeft geen semantische betekenis in de taalruimte, het is gewoon een specifiek ID.

Voor een zoekbalk op consumentenniveau (zoals in e-commerce of SaaS-dashboards) heeft u de precisie van typos-tolerante trefwoordzoekopdrachten nodig, *gecombineerd* met de intelligentie van vectorzoekopdrachten. Dit heet Hybrid Search.

## Introductie van Typesense

Typesense is een extreem snelle, in-memory, open-source zoekmachine (een modern, gebruiksvriendelijker alternatief voor Elasticsearch of Algolia). Het heeft ingebouwde native ondersteuning voor Machine Learning-modellen, het genereren van vectoren en hybride zoeken.

U hoeft niet langer handmatig embeddings te genereren met OpenAI, deze op te slaan in uw Postgres-database en complexe zoeklogica te schrijven. Typesense kan het genereren en doorzoeken van vectoren zelfstandig afhandelen.

## Architectuur: Typesense integreren met Supabase en Next.js

Om een realtime AI-zoekervaring in uw Next.js-app te bouwen, volgt u dit architectuurpatroon:

### 1. Typesense Hosting
Implementeer een Typesense-cluster. U kunt Typesense Cloud gebruiken of het zelf hosten via Docker op Fly.io of AWS.

### 2. De Schema Definitie
Maak een "collectie" (collection) in Typesense die overeenkomt met uw Supabase-tabel. U definieert welke velden stringvelden zijn en u instrueert Typesense om automatisch een `embedding`-veld te maken op basis van de tekst.

```javascript
const schema = {
  name: 'documents',
  fields: [
    { name: 'title', type: 'string' },
    { name: 'content', type: 'string' },
    { name: 'org_id', type: 'string', facet: true },
    { 
      name: 'embedding', 
      type: 'float[]', 
      embed: { 
        from: ['title', 'content'], 
        model_config: { model_name: 'ts/all-MiniLM-L12-v2' } 
      } 
    }
  ]
};
```
*Merk op hoe we het ingebouwde model van Typesense (`all-MiniLM-L12-v2`) gebruiken. Typesense genereert de vectoren voor u op de achtergrond. U betaalt geen OpenAI API-kosten voor deze embeddings!*

### 3. Database Synchronisatie (Supabase Webhooks)
Uw Supabase Postgres-database blijft uw bron van waarheid. U moet Typesense synchroon houden.
Maak een database-webhook (of een Edge Function) in Supabase. Telkens wanneer een rij in de tabel `documents` wordt ingevoegd, bijgewerkt of verwijderd, stuurt de webhook de wijziging onmiddellijk naar uw Typesense API.

### 4. De Next.js Frontend (InstantSearch)
In uw Next.js React frontend, gebruikt u de open-source bibliotheek `react-instantsearch` of bouwt u een aangepast zoekveld aan de hand van de Typesense JavaScript-client.

Wanneer u de zoekopdracht uitvoert, voert u een **Hybride Query** uit:
```javascript
const searchParameters = {
  q: 'financiële risico\'s SKU-9982',
  query_by: 'title,content,embedding', // Doorzoek zowel tekst als vectoren
  filter_by: `org_id:=${userOrgId}`, // Row-Level Security!
  vector_query: 'embedding:([], k: 10)',
};
```

Typesense zoekt nu razendsnel met BM25 (voor trefwoorden zoals "SKU-9982") én vergelijkt vectoren (voor concepten als "financiële risico's"), en combineert de resultaten in één feilloze lijst. Bovendien handelt het typefouten af.

## Beveiliging (Tenancy Filtering)

Net als in Postgres RLS, moet u er absoluut voor zorgen dat gebruikers niet zoeken in documenten van andere bedrijven. Zoals in het bovenstaande codevoorbeeld getoond, filtert u in Typesense door uw `filter_by` parameter in te stellen op de `org_id` van de geauthenticeerde gebruiker. Genereer een "Scoped Search Key" op uw backend met dit filter voorgeprogrammeerd, zodat de client dit nooit kan manipuleren.

## De LaunchStudio-aanpak

Bij LaunchStudio geloven we niet in het forceren van Postgres om elke taak te doen. Terwijl we Supabase en `pgvector` gebruiken voor zware backend RAG-pijplijnen, implementeren we **Typesense** voor consumentgerichte, razendsnelle zoekbalken in de UI. Wij verzorgen de volledige integratie: het opzetten van het Typesense-cluster, het schrijven van de Supabase synchronisatie-webhooks, het configureren van hybride ML-schema's en het bouwen van de reactieve Next.js zoekcomponenten. Uw gebruikers ervaren het soort magische AI-zoekopdrachten dat normaal gesproken alleen grote technologiebedrijven kunnen leveren.

---

*Leveren de zoekopdrachten in uw SaaS-app slechte resultaten op, of zijn uw vectorzoekopdrachten te traag? LaunchStudio implementeert supersnelle Hybride AI Search met Typesense en Next.js. [Neem contact met ons op](https://launchstudio.eu/en/).*
