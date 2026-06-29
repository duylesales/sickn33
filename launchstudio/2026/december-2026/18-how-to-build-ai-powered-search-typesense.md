---
Title: How to Build AI-Powered Search with Typesense and Next.js
Keywords: AI, Search, Typesense, Next.js, Vector, Semantic
Buyer Stage: Awareness
---

# How to Build AI-Powered Search with Typesense and Next.js

Traditional keyword search is dead. When a user searches an enterprise knowledge base for "How do I request time off?", a traditional SQL `LIKE '%time off%'` query will fail to return the HR document titled "Vacation and PTO Policy." For decades, developers patched this with complex full-text search engines like Elasticsearch, spending months tuning synonyms and weights. Today, AI has completely revolutionized search via **Vector Embeddings and Semantic Search**. But relying purely on vector databases like pgvector can sometimes fall short when users want exact keyword matches. The ultimate solution for a production Next.js AI application is **Typesense**—a blazing-fast search engine that seamlessly blends traditional keyword search with modern AI semantic search.

## The Limits of Pure Vector Search

Vector search (RAG) is magical because it understands meaning. It knows that "time off" and "vacation" are semantically similar. However, vector search struggles with strict constraints:

1. **Exact Matches:** If a user searches for an exact product SKU like "AX-775B", vector search might return "AX-775C" because their meanings are mathematically adjacent. The user wants the exact match.
2. **Filtering:** "Find all PTO policies updated in the last 30 days." Vector search handles the semantic part ("PTO policies"), but struggles with the metadata filtering ("last 30 days").
3. **Typo Tolerance:** Vector embeddings are sensitive to extreme spelling errors that traditional fuzzy search handles elegantly.

This is why production AI SaaS products use **Hybrid Search**: combining the precise filtering of keyword search with the conceptual understanding of vector search.

## Why Typesense is the Ultimate Hybrid Engine

Elasticsearch is the legacy giant, but it is incredibly heavy, requires massive RAM, and relies on the complex Java Virtual Machine (JVM). Typesense is an open-source, typo-tolerant search engine written in C++. It is insanely fast (sub-50ms latency), runs on minimal memory, and most importantly, it has built-in, native support for Vector Search.

Typesense allows you to store both structured metadata (Titles, Dates, Categories) and unstructured vector embeddings in the same document schema, and query them simultaneously.

## Architecture of a Next.js + Typesense App

Building this with Next.js involves three distinct pipelines:

### 1. The Indexing Pipeline (Data Ingestion)

When a new document is added to your Postgres/Supabase database, you must sync it to Typesense.

1. A Supabase webhook triggers a background job (or Edge Function).
2. The job calls the OpenAI API (`text-embedding-3-small`) to generate a vector embedding of the document content.
3. The job pushes a JSON document to Typesense containing the metadata and the vector array:

```json
{
  "id": "doc_123",
  "title": "PTO Policy 2026",
  "department": "HR",
  "timestamp": 1700000000,
  "content_embedding": [0.012, -0.045, 0.088, ...] 
}
```

### 2. The Next.js Search UI

Typesense maintains an official React library (`react-instantsearch-hooks-web`) that provides out-of-the-box UI components for search boxes, facets (checkbox filters), and pagination. It handles the state management of complex search queries seamlessly. 

The beauty of Typesense is that the search executes directly from the client's browser to the Typesense API (using a restricted search-only API key), resulting in ultra-low latency, "search-as-you-type" experiences.

### 3. The Hybrid Search Query

When the user types a query, the Typesense client executes a hybrid search. Typesense can automatically handle the embedding generation on the fly (if configured with your OpenAI key), or your Next.js backend can generate the embedding of the user's query and pass it to Typesense.

The Typesense query looks like this:

```javascript
const searchParameters = {
  q: 'vacation policy',
  query_by: 'title,content_embedding', // Search keyword in title, semantic in embedding
  filter_by: 'department:HR',          // Strict metadata filtering
  vector_query: 'content_embedding:([0.012, ...], k: 10)'
};
```

This query tells Typesense: "Find the 10 closest semantic matches to the query vector, but also score documents where the exact word 'vacation policy' appears in the title, and strictly filter out anything not in the HR department."

## Securing Typesense for SaaS

In a multi-tenant AI SaaS, you cannot allow User A to search User B's documents. 

Typesense solves this brilliantly with **Scoped API Keys**. When User A logs into your Next.js app, your backend generates a temporary Typesense API key that contains an embedded filter (e.g., `filter_by: organization_id:=org_123`). When the React frontend uses this key to query Typesense, the engine completely isolates the search to that specific organization's data.

## The LaunchStudio Approach

At LaunchStudio, we know that users judge the quality of an AI product heavily by the speed and accuracy of its search bar. Relying purely on Postgres `LIKE` queries is obsolete, and pure vector databases often fail at exact keyword matches. We architect hybrid search engines using Typesense and Next.js, delivering blazing-fast, typo-tolerant, semantically aware search experiences that make enterprise knowledge bases feel magical.

---

*Frustrated by poor search results in your AI product? LaunchStudio implements lightning-fast hybrid search architectures using Next.js and Typesense. [Talk to us today](https://launchstudio.eu/en/).*
