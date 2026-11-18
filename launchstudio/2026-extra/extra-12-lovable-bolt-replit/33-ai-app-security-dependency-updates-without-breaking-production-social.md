14 months without a single dependency update.
63 advisories in the first audit.
11 in packages handling incoming requests.
1 that mattered immediately: a request parser where a crafted payload could eat unbounded memory.
9 months since that advisory was published.
0 lockfile in the repository. 📦

Menno Zwartjes built Werkbonnen in Lovable: digital work orders and signatures for installation and maintenance companies, 47 firms, around 400 field engineers. Engineers submit work orders from their phones, on public endpoints, which is exactly the exposure that advisory described. Nobody had ever told Menno that dependencies were something he owned. They arrived with the code, they worked, and he didn't know there was a list to look at.

The clean-up (LaunchStudio, 3 business days, €2,600):
1 lockfile committed, so builds stop resolving fresh versions every time
63 advisories triaged: 11 reachable from user input, 34 development-only, the rest needing configurations he didn't run
11 applied straight away, the parser included, with the product checked against a written test list
34 development-only fixes applied in one batch the following week
2 major version upgrades, done one at a time over two weeks
9 unused direct dependencies removed, including a date library used for one format string and a component library used for one button
190 transitive packages gone with them
Install scripts disabled by default
Automated scanning in the build, alerts to his phone, and pull requests opened for new advisories
1 written routine: security fixes within days, minor updates monthly, major ones deliberately

The new numbers:
0 evidence the memory issue was exploited, after nine months of exposure
1,340 ➜ 1,150 total packages
~40 minutes a month on updates
0 week-long upgrades piling up

"Nobody told me dependencies were a thing I owned. They arrived with the code, they worked, and for fourteen months I did not know there was a list to look at." - Menno Zwartjes

https://launchstudio.eu/en/blog/ai-app-security-dependency-updates-without-breaking-production

#SupplyChain #AppSecurity #npm #Lovable #LaunchStudio #Manifera
