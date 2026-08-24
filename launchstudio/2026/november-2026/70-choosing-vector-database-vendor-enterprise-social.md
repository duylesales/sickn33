🔍 Nadia built ClauseBank, a contract-search SaaS for law firms, with **Bolt** — and added semantic search with pgvector using a tutorial that got it working in a day. Eight months and 40 firms later, an enterprise security review asked one question she couldn't confidently answer.

If you add vector search without the same Row Level Security scrutiny you'd apply to any other table, "just search" becomes a cross-tenant data leak waiting to be found.

❌ Row Level Security never enabled on the embeddings table
❌ Any authenticated user's query could technically retrieve another firm's confidential contract chunks
❌ The gap sat invisible for eight months because the frontend never surfaced it

✅ RLS policies enabled and scoped to `auth.uid()` and firm ID on the embeddings table
✅ A re-ranking step added to improve retrieval relevance
✅ Adversarial test queries confirming cross-tenant retrieval is now mathematically impossible

At **LaunchStudio**, we've been fixing exactly this class of production engineering problem since 2014 through Manifera, across 160+ delivered projects. 🛡️

ClauseBank passed the enterprise client's security review with the vulnerability fully documented as remediated, and Nadia closed the firm's largest contract to date — a 200-seat enterprise deployment. (€1,700 (Launch & Grow Package) — secured and verified in 6 business days.) 🚀

👉 See how we fixed it: [Link to article]

#LaunchStudio #Manifera #AISaaS #VectorDatabase #RAGSecurity
