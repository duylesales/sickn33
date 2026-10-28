🚨 Marloes Teunissen's Horecarooster schedules around 3,800 staff across 140 locations for 27 hospitality groups. It had three roles: owner, admin, member. Location managers needed to approve hours - which only admins could do - so every manager became an admin. Then a finance director noticed one manager approving his own overtime. 😳

As admins, managers could also see every location's wages. The same week, a 34-location group declined to sign for exactly that reason. Here's how to build roles and permissions beyond "admin and user": 🧠

❌ One role field that couldn't express "only my location"
❌ Managers promoted to admin just to approve hours
❌ Hourly wages visible to anyone with the admin role
❌ Nothing stopping people from approving their own hours

✅ 24 permission codes defined from the checks already scattered through the code, bundled into six system roles
✅ Location-scoped role assignments; row level security rewritten across 19 tables around one indexed has_permission helper
✅ Wages moved to a separate table readable only with wages.read, and self-approval blocked in the database
✅ Escalation rules, a role-change audit, and a 24×6 permission matrix generating 288 tests in CI

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build this when a product starts selling to multi-location organisations. ⚙️

Her result: €4,800, four business days. A historical review found three managers who had approved €4,100 of their own overtime. The 34-location group signed within the month, and a second group followed - 61 new locations. 🚀

👉 Lovable Supabase: roles and permissions beyond admin and user: https://launchstudio.eu/en/blog/lovable-supabase-roles-and-permissions-beyond-admin-and-user

#Supabase #AccessControl #SaaS #AppSecurity #LaunchStudio #Manifera
