🧪 LAB NOTEBOOK: LabAgenda, from one department to a spin-off

ENTRY 1: THE INSTRUMENT
Pieter-Jan Maes, a postdoctoral researcher in Leuven, built LabAgenda with Cursor: booking and usage tracking for shared lab equipment like microscopes and sequencers, with automated cost allocation to research grants. His own department used it for two years.

ENTRY 2: THE NEW EXPERIMENT
Three other research institutes in Belgium and the Netherlands asked to use it. Pieter-Jan founded a spin-off, with support from the university's tech transfer office.

ENTRY 3: THE QUESTIONNAIRE
The first institute's data protection officer sent questions. The answers were uncomfortable:
• All institutions' bookings, grant numbers and usage notes in one table, visible to every logged-in user
• Login by email and password, not the institution's own credentials
• The database in a US region
• No access log
• Grant data never deleted
• Deployment by pushing from Pieter-Jan's laptop

OBSERVATION
In the lab, trust had been implicit: everyone knew each other. Selling it meant writing that trust down, and enforcing it in code.

ENTRY 4: THE METHOD (LaunchStudio, 11 business days, €3,200)
• Institution and facility tenancy, with Row Level Security and per-facility roles
• SSO via OpenID Connect for institutional logins, with a fallback for external users
• Database migrated to an EU region, with backups and a tested restore
• Access logging, and configurable retention per institution
• Versioned releases through a CI pipeline with staging
Meanwhile, the tech transfer office finalised the licence to the spin-off.

ENTRY 5: RESULTS
All three institutes signed within two months. LabAgenda now manages bookings for 41 facilities, and its data-handling description has been reused in every procurement since.

"In the lab, trust was implicit because we all knew each other. Selling it meant writing that trust down and enforcing it in the code." - Pieter-Jan Maes

https://launchstudio.eu/en/blog/ai-prototype-to-production-in-leuven-university-spin-offs-and-research-data

#Leuven #SpinOff #ResearchData #SSO #LaunchStudio #Manifera
