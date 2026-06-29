# Social Media Post: How to Build AI-Powered Search with Typesense and Next.js

If your AI app relies entirely on vector embeddings for search, your users are frustrated.

Vectors are amazing at understanding semantic concepts, but they fail completely at exact-match keyword searches (like searching for an exact order ID or acronym).

You need Hybrid Search. And the fastest way to build it is with Typesense.

1️⃣ Typesense is an open-source, typo-tolerant search engine.
2️⃣ It handles vector generation *internally* using local ML models (saving you OpenAI API costs).
3️⃣ You query `query_by: 'title,content,embedding'`. It simultaneously runs an exact keyword search AND a semantic vector search, intelligently merging the results in milliseconds.

Use Supabase Postgres as your source of truth, but sync your data to Typesense for the frontend search bar.

Read our implementation guide on the LaunchStudio blog.

#LaunchStudio #Typesense #HybridSearch #AISaaS #Nextjs #Supabase #RAG
