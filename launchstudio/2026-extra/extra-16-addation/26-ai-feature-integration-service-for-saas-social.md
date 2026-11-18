🧮 The math of a contract assistant everyone loved

BEFORE
every question
× the full text of every contract in the account
× no limit per user
× one test account asking again and again
= an AI bill bigger than the feature's revenue, after two months

Sven de Boer runs a small procurement consultancy in Eindhoven and built Contractwijzer with v0, Cursor and Supabase: supplier contract storage for mid-sized manufacturers, plus an assistant that answers questions like "Which contracts renew automatically next quarter?" It wowed customers in demos. Then the bill came. And there were worse problems:
• Answers sometimes mentioned contracts belonging to another customer
• The assistant often hung for half a minute
• The API key was in the frontend
• Retrieval searched every customer's embeddings, with no organisation filter

AFTER (LaunchStudio, 14 business days, €5,600, plus €49/month)
the assistant in a server function, with a rotated key
× retrieval with pgvector in Supabase, filtered by organisation before searching, returning only the most relevant clauses
× simple questions to a smaller model, complex ones to a larger model
− questions that became plain database queries, once renewal dates and notice periods were extracted per contract
+ source contracts shown with every answer
+ limits per plan, caching, timeouts, a fallback message and usage alerts
+ 60 real questions to compare versions
= AI cost per customer at a small fraction of before

On the evaluation set, correct answers rose from 41 to 55 out of 60. Answers got faster, the cross-customer leak was closed, and the assistant moved into Sven's paid plan with clear usage limits.

"Customers loved the assistant and I was quietly paying for every question. Now it is faster, safer and part of a plan people pay for." - Sven de Boer

https://launchstudio.eu/en/blog/ai-feature-integration-service-for-saas

#AI #LLM #SaaS #Supabase #AIFounder #LaunchStudio #Manifera
