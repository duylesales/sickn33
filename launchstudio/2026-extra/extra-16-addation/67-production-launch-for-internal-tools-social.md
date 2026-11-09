🚚 Johan Vermeer is operations manager at a transport company in Tiel. Tired of spreadsheets, he built Ritbord with Bolt and Supabase: a planning board for trucks, drivers and deliveries, pulling orders from the transport management system. Within two months, twelve planners used it every day. Then Johan went on a three-week holiday, and the IT manager discovered the tool. 😳

What IT found: 🧠

❌ Everything running in Johan's personal accounts, paid with his own credit card
❌ One shared login for all planners
❌ An administrator API key for the transport system in a client-side function
❌ Drivers' phone numbers and home addresses visible to anyone with the login, and no backups or documentation

✅ All components moved into company accounts and billing, with Johan as collaborator
✅ Login through company Microsoft accounts, limited to planning and management groups
✅ Roles for planners, managers and drivers, with drivers seeing only their own routes
✅ The integration moved to a server function with a limited account, the key rotated, home addresses removed, plus tested backups, staging and documentation

At **LaunchStudio**, backed by Manifera's 11+ years of building internal systems and integrations for clients such as Vodafone and TNO, we move internal tools into company ownership and keep the builder's momentum going. 🛠️

The result: €3,100, eight business days. IT approved Ritbord as an official tool, and a colleague now confidently makes changes using the documentation. 🚀

👉 Production launch for internal tools: https://launchstudio.eu/en/blog/production-launch-for-internal-tools

#InternalTools #SSO #Bolt #Supabase #AIFounder #LaunchStudio #Manifera
