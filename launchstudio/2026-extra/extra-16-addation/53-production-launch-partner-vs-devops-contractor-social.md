🍽️ Martijn Koster runs a SaaS for event caterers from Den Bosch, built with Bolt and Supabase: caterers manage menus, quotes and staff schedules. Before launching with a national catering association, he hired a DevOps contractor for a week. The work was excellent: a GitHub pipeline, separate staging and production, uptime monitoring and structured logs. 👌

Two weeks before launch, a pilot caterer filtered the quote list and saw another company's quotes. The review found the application had never been checked: 🧠

❌ Quotes and menus tables readable by any logged-in user
❌ Staff phone numbers exposed through a view without policies
❌ Mollie deposits marked as paid on the redirect page
❌ Quote PDFs in a public bucket, and no email authentication

✅ Policies rewritten per caterer and role, with tests running in the contractor's pipeline
✅ The view secured
✅ Deposits moved to verified webhooks, with reconciliation
✅ PDFs in private storage and email authentication added

At **LaunchStudio**, backed by Manifera's 11+ years of DevOps and application engineering for clients such as Vodafone and TNO, we cover the application and the delivery around it, and work alongside DevOps specialists when you need custom infrastructure. 🛠️

His result: €2,400, six business days. The association launched on schedule with about 60 caterers, and the pipeline now runs the access tests on every change. 🚀

👉 Production launch partner vs DevOps contractor: https://launchstudio.eu/en/blog/production-launch-partner-vs-devops-contractor

#DevOps #Security #Bolt #Supabase #AIFounder #LaunchStudio #Manifera
