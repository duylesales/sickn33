🚨 Pieter Blom's Huurbeheer manages about 2,300 rental units for nine letting agencies around Dordrecht. The property list was filtered correctly. But a dashboard figure - "total units under management" - counted the whole table. One agency saw a number far larger than its own portfolio and worked out what it meant. 😳

Arrears and average rent were unfiltered too, so every agency could see its competitors' figures. Here's where multi-tenancy actually leaks: 🧠

❌ Records owned by the user who created them, instead of by the organisation
❌ Shared logins between colleagues, because that was the only way to see each other's work
❌ Dashboard totals and reports with no tenant filter
❌ Privileged server-side queries that skip the tenant check

✅ An organisation model with roles for agent, manager and owner
✅ A required tenant column on every table, with policies per operation
✅ Every figure and report rewritten with an explicit tenant filter - and tested
✅ Proper invitation and ownership flows, so shared logins become individual accounts

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build tenancy you can prove to a buyer. 🏢

His result: twelve business days and €6,800 later, the shared logins became 31 individual accounts and three unfiltered server queries were fixed. Two agencies evaluating an alternative stayed - and Pieter now sends a one-page isolation description with every proposal. 🚀

👉 Multi-tenancy in Lovable and Supabase without leaking data: https://launchstudio.eu/en/blog/lovable-supabase-multi-tenancy-without-leaking-data

#Lovable #Supabase #MultiTenancy #PropTech #LaunchStudio #Manifera
