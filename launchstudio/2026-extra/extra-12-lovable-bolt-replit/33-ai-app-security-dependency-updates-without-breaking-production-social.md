🚨 Menno Zwartjes's Werkbonnen handles digital work orders and signatures for 47 installation firms — about 400 field engineers. In fourteen months he had never updated a dependency. Then he ran an audit: 63 advisories, 11 in packages handling incoming requests. 😳

One was a request-parsing flaw letting a crafted payload eat unbounded memory — on exactly the public endpoints his engineers' phones used. It had been published nine months earlier. Here's how to update dependencies without breaking production: 🧠

❌ No lockfile in the repository — every build resolved versions fresh
❌ Never running an audit, so nobody knew what was vulnerable
❌ Treating every advisory the same, or ignoring the list because it was long
❌ Packages installed for a single date format and a single button

✅ Lockfile committed, and the 63 advisories triaged by reachability: 11 urgent, 34 dev-only
✅ The 11 applied immediately against a written test list, with major versions upgraded one at a time
✅ Automated scanning on every build, alerts to his phone, and pull requests for new advisories
✅ 9 unused direct dependencies removed (190 packages gone), install scripts disabled, and a three-speed update routine written down

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we keep your dependencies current so nothing piles up into a week-long upgrade. 📦

His result: three business days and €2,600 later, the memory flaw was closed with no sign of exploitation. Packages went from 1,340 to 1,150 — and Menno now spends about 40 minutes a month on updates. 🚀

👉 Dependency updates without breaking production: https://launchstudio.eu/en/blog/ai-app-security-dependency-updates-without-breaking-production

#SupplyChain #AppSecurity #npm #Lovable #LaunchStudio #Manifera
