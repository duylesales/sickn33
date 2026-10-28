🚨 Rogier Slagter's Verhuurbeheer handles rental admin for 62 holiday-home owners and small property managers - 380 properties. A municipality changed its tourist tax rate. He updated it, deployed - and three days later a customer's invoices still showed the old amount. 😳

The rate lived in seven places: two components, an invoice generator, a quote preview, a PDF template, a summary and a database default. He'd changed four. Two of the copies had quietly disagreed by a cent since spring. Here's how to read what an AI agent actually produced: 🧠

❌ The same calculation copy-pasted seven times
❌ Five date-formatting implementations with three different midnight behaviours
❌ Dead code everywhere - including an unauthenticated export of all bookings, reachable for eight months
❌ 600+ line files and blank screens whenever something failed or was empty

✅ One tax configuration and one calculation function, plus one date formatter
✅ 14 dead components, 6 unused endpoints and 3 abandoned tables removed - after checking each for exposure
✅ One data-fetching approach, the four biggest files split, and loading and empty states on eleven screens
✅ Human error messages, a formatter, and a conventions file the next AI session reads

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we find the duplication in your repository - and the risks hiding in what nobody uses anymore. 🔍

His result: two business days and €2,700 later, a tax change takes one edit. The forgotten export endpoint was the most serious finding - discovered only because dead code was being cleaned up - and later AI sessions now produce noticeably more consistent code. 🚀

👉 Bolt code quality: reading what the agent actually produced: https://launchstudio.eu/en/blog/bolt-code-quality-reading-what-the-agent-actually-produced

#CodeQuality #Bolt #TechDebt #AIDevelopment #LaunchStudio #Manifera
