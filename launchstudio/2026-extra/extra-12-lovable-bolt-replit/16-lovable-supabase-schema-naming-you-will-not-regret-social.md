🚨 Barend Kloosterman's Serviceplan manages maintenance contracts for 44 installation companies — about 9,000 service addresses. An installer updated a customer's address in the portal. That evening's invoice carried the old address. The engineer was sent to a third one. 😳

Customers lived in three tables — clients, customers and contacts — because every feature request had produced a new one. Here's what inconsistent schema naming really costs: 🧠

❌ Three tables for the same customer, each with a different answer
❌ A comma-separated text column instead of a proper table
❌ Nine missing foreign keys hiding 340 orphaned records
❌ Money stored as floating point — and a one-cent invoice discrepancy nobody could explain

✅ A full schema inventory and a conventions file committed to the repo, including the product's vocabulary
✅ Three customer tables merged into one, migrated with zero downtime (add, write both, switch reads, drop)
✅ Foreign keys declared, orphans resolved, timestamps made time zone aware
✅ Money columns renamed and stored as integer cents, with generated types regenerated

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we clean up AI-built schemas so every change afterwards goes faster. 🗂️

His result: four business days and €3,400 later, the three-address bug became structurally impossible. A contractor hired the next month was productive on day one — and his AI sessions stopped inventing new column names. 🚀

👉 Schema naming you won't regret: https://launchstudio.eu/en/blog/lovable-supabase-schema-naming-you-will-not-regret

#Supabase #DatabaseDesign #TechDebt #Lovable #LaunchStudio #Manifera
