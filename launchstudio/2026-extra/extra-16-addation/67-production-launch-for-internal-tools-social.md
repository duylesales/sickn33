✉️ AUTO-REPLY (dramatized): "I'm on holiday for three weeks."

What the auto-reply didn't say:
"Meanwhile, the planning board twelve planners use every day runs in my personal Supabase and Bolt accounts, paid with my own credit card. Everyone shares one login. And the connection to our transport system uses an administrator API key in a client-side function."

The IT manager found that out on their own. 🚚

Johan Vermeer is operations manager at a mid-sized transport company in Tiel. Fed up with spreadsheets, he built Ritbord with Bolt and Supabase in an evening: a planning board showing trucks, drivers and deliveries, pulling orders from the company's transport management system, with deliveries dragged between routes. Within two months, twelve planners used it daily, and the managing director called it indispensable.

What else the IT manager found:
• Drivers' phone numbers and home addresses, visible to anyone with the shared login
• No backups beyond the default
• No documentation

What LaunchStudio did (8 business days, €3,100):
✓ Everything moved into company accounts with company billing, and Johan kept on as collaborator
✓ Login through the company's Microsoft accounts, limited to the planning and management groups
✓ Roles for planners, managers and drivers, with drivers seeing only their own routes on their phones
✓ The transport system connection moved to a scheduled server function, with a dedicated account limited to reading and a small set of writes, and the admin key rotated
✓ Drivers' home addresses removed from the board
✓ Backups tested, staging set up, and documentation explaining how the tool works

The IT manager approved Ritbord as an official company tool. Johan still improves it with Bolt, through staging. And the next time he took leave, a colleague made a small change confidently, using the documentation.

"I built the tool in an evening. It took a holiday to realise the company depended on my personal credit card and one shared password." - Johan Vermeer

https://launchstudio.eu/en/blog/production-launch-for-internal-tools

#InternalTools #SSO #Bolt #Supabase #AIFounder #LaunchStudio #Manifera
