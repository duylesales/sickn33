🚨 Jelmer Ottevanger's Inkoopportaal connects 19 wholesalers with about 300 retailers. Early in the build, an AI session hit a permissions error writing an admin report — and "fixed" it with the Supabase service role key, given a public prefix so it ran in the browser. 😳

That key — the one that can read every wholesaler's pricing — sat in a file anyone could download for six months. Here's how configuration leaks keys and breaks deploys: 🧠

❌ A server-only secret with a public VITE_ prefix, compiled into every bundle
❌ An email provider key that leaked the same way
❌ Staging sharing production's database and email credentials
❌ No list of required variables and no check that they're set

✅ The service role key rotated immediately — before anything else
✅ The admin report rewritten as a server-side function with proper authorisation
✅ Three fully separate environments, an example file and a startup check for eleven required variables
✅ Protected preview deployments and a build step that scans for secret patterns and fails the build

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we search your deployed bundle for secrets — it takes five minutes. 🔑

His result: one business day and €1,700 later, both keys were rotated with no evidence of misuse — "luck rather than a result". Six weeks later, the build scan blocked a new AI session making exactly the same mistake. 🚀

👉 Environment variables across three environments: https://launchstudio.eu/en/blog/lovable-hosting-environment-variables-across-three-environments

#Secrets #DevOps #Supabase #Lovable #LaunchStudio #Manifera
