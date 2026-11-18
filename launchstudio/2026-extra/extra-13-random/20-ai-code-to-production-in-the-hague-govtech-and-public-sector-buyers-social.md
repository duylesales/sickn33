🏛️ A pilot proves residents want it. A contract needs proof the municipality can trust it.

Hugo Verbeek spent eleven years as a policy adviser before founding BuurtSignaal in The Hague: residents report broken streetlights, illegal dumping or unsafe crossings, and municipal teams triage and respond. He built it in Windsurf with a Next.js frontend and Postgres, and ran a pilot in one city district. Residents liked it. District staff liked it more.

Then came the formal contract, and procurement's 90-question security and privacy questionnaire. Hugo could answer about a third.

THE PROCUREMENT CHECKLIST
☐ Staff roles enforced in the database (there were only "user" and "admin," with restrictions in the interface)
☐ An audit log (none)
☐ Staff login through the municipality's identity provider (passwords instead)
☐ Retention rules for residents' reports, including photos with location data (kept forever)
☐ EU hosting (a US region)
☐ An accessible resident form (missing labels and keyboard traps)
☐ Security documentation

TICKED OFF (LaunchStudio, Launch & Grow, 21 business days, €6,900, plus €49/month)
☑ Four staff roles, enforced in the database
☑ An append-only audit log for access to resident data
☑ SSO via the municipality's OpenID Connect provider, with MFA for administrators
☑ Location metadata removed from photos automatically
☑ Retention rules agreed with the municipality
☑ EU hosting, with tested backups
☑ Accessibility fixes in the existing interface
☑ A BIO-mapped security overview, processor list, recovery description, incident procedure and exit plan

THEN, AN INDEPENDENT PENETRATION TEST
Commissioned by the municipality. Two low-severity findings, fixed the same week.

BuurtSignaal signed a three-year contract, and two neighbouring municipalities have since piloted it, both accepting the existing documentation with minor additions.

"The pilot proved residents wanted it. The contract depended on proving the municipality could trust it. Those were two different projects, and I'd only done the first one." - Hugo Verbeek

https://launchstudio.eu/en/blog/ai-code-to-production-in-the-hague-govtech-and-public-sector-buyers

#GovTech #TheHague #BIO #Accessibility #LaunchStudio #Manifera
