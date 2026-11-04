🚨 Victor Hamers built Inspectieloket in Bolt and Supabase: an inspection and compliance tool for property maintenance companies, multi-tenant, with 25 customers. Then a national housing corporation wanted to sign - but required a dedicated database in an EU region of its choice, with its own backup schedule. His first instinct: copy the whole project by hand. 😳

He almost created a second product by copying the first. One codebase deployed twice was the answer. Here's what copying would have caused: 🧠

❌ Two codebases drifting apart with every change
❌ Migrations run by hand on separate databases
❌ The dedicated customer falling behind on features and fixes
❌ An enterprise deal priced without the real cost of running a second instance

✅ The multi-tenant setup hardened first, with organisation-based RLS and automated isolation tests
✅ A dedicated Supabase project for the housing corporation, deployed from the same codebase
✅ A GitHub Actions workflow applying migrations and edge functions to both projects in sequence
✅ Enterprise pricing that covers the extra instance, plus documentation

At **LaunchStudio**, backed by Manifera's 11+ years building both multi-tenant and dedicated B2B systems, we keep multi-tenant as the default and automate dedicated instances only when a contract truly requires one. 🛠️

💡 His result: €5,200, fourteen business days. The housing corporation signed at an enterprise price, and every feature released since has reached both environments on the same day. 🚀

👉 Single-tenant or multi-tenant for your B2B SaaS? Here's how to decide: https://launchstudio.eu/en/blog/single-tenant-vs-multi-tenant-for-b2b-saas

#SaaS #MultiTenant #Supabase #B2B #LaunchStudio #Manifera
