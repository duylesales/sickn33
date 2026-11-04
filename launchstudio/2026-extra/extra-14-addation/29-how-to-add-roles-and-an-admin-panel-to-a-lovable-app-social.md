🚨 Roos van Dam coordinates a neighbourhood help network in Zaandam and built Buurthulp in Lovable: residents post requests like groceries or a lift to the doctor, volunteers accept them, coordinators check sensitive requests. About 140 volunteers and 300 residents joined. Then a volunteer found something by accident. 😳

The admin page was hidden. That's all it was: hidden. Anyone who knew how to look could promote themselves. Here's how: 🧠

❌ Coordinator status stored as a role column on the profiles table
❌ A profile edit page that saved the whole row - including role
❌ One edit in the browser's developer tools turned a volunteer into a coordinator
❌ That revealed residents' addresses and medical notes; the admin check lived only in React

✅ A user_roles table with no write policies, existing coordinators migrated into it
✅ The role column removed from profiles, plus a has_role helper for policies
✅ RLS rewritten: medical notes and addresses visible only to coordinators and the assigned volunteer
✅ Volunteer approval and coordinator assignment moved into edge functions with an audit log

At **LaunchStudio**, backed by Manifera's 11+ years of enterprise access control, we enforce roles in the database - where regenerated components can't undo them. 🛠️

💡 Her result: €1,750, six business days. The privilege escalation was closed within four days, Roos reviews the audit log monthly, and Buurthulp has since handled around 2,000 requests. 🚀

👉 Adding roles and an admin panel to a Lovable app? Here's the secure pattern step by step: https://launchstudio.eu/en/blog/how-to-add-roles-and-an-admin-panel-to-a-lovable-app

#Lovable #Supabase #AccessControl #Community #LaunchStudio #Manifera
