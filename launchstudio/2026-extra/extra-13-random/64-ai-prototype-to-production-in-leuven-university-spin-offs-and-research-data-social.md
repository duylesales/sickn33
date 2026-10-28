🚨 Pieter-Jan Maes, a postdoc in Leuven, built LabAgenda with Cursor: booking and usage tracking for shared lab equipment like microscopes and sequencers, with automatic cost allocation to research grants. His department used it for two years. Then three institutes in Belgium and the Netherlands wanted it, and he founded a spin-off. The first data protection questionnaire made for uncomfortable reading. 😳

Every institution's bookings, grant numbers and usage notes sat in one table visible to any logged-in user. Logins were email and password, not institutional credentials. The database ran in a US region. There was no access log, grant data was never deleted, and deploying meant Pieter-Jan pushing from his laptop. Here's what taking a lab tool from AI prototype to production really involves: 🧠

❌ One shared table for every institution
❌ No institutional single sign-on
❌ Research data hosted outside the EU, kept forever
❌ Deployments from a laptop

✅ Institution and facility tenancy with row level security and per-facility roles
✅ SSO via OpenID Connect for institutional logins, plus a fallback for external users
✅ The database migrated to an EU region with backups and a tested restore
✅ Access logging, configurable retention per institution and versioned releases through CI with staging - while the tech transfer office finalised the licence

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering and work with research organisations like TNO, we turn trust that was implicit in the lab into rules enforced in code. ⚙️

His result: €3,200, eleven business days. All three institutes signed within two months, LabAgenda now runs bookings for 41 facilities, and its data-handling description is reused in every procurement. 🚀

👉 AI prototype to production in Leuven: university spin-offs and research data: https://launchstudio.eu/en/blog/ai-prototype-to-production-in-leuven-university-spin-offs-and-research-data

#Leuven #SpinOff #ResearchData #SSO #LaunchStudio #Manifera
