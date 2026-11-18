🏛️ What a gemeente's contract asks for, clause by clause

Martijn Koster, a former municipal civil servant, built Buitenmelder with Bolt and Supabase. Residents report problems in public space, like broken streetlights, litter or damaged pavement, and municipal teams plan and track repairs. A Noord-Holland municipality liked the pilot and wanted a contract, after its information security officer's assessment and under its standard IT purchasing conditions.

CLAUSE: Single sign-on through our identity provider
Found: separate passwords, no MFA
Now: SAML SSO, with MFA enforced by the municipality's own identity provider

CLAUSE: Personal data only for those who need it
Found: every team could see every report, including residents' names, addresses and photos
Now: Row Level Security isolating each municipality, and personal details limited to the teams handling those reports

CLAUSE: Secure storage of uploads
Found: photos in a public bucket
Now: private storage with signed links, and location metadata stripped from resident uploads automatically

CLAUSE: Traceability
Found: no audit logs
Now: logins, report views, changes and exports all logged

CLAUSE: Data location and processing
Found: US hosting, no processing agreement
Now: EU hosting with tested backups, and a processing agreement drafted with a lawyer

CLAUSE: Exit arrangement with full data return
Found: not possible
Now: a full data export in documented formats

LaunchStudio also prepared the technical sections of a BIO-mapped security overview (18 business days, €6,900).

The result: approved after the security officer's second review, signed with the exit arrangement included. Within a year, two neighbouring municipalities adopted it, reusing most of the documentation.

"I used to work inside a municipality, so I knew they were careful. I hadn't realised how much of that care would need to be visible in my own product." - Martijn Koster

https://launchstudio.eu/en/blog/selling-saas-to-dutch-municipalities-bio-and-security-requirements

#GovTech #BIO #Municipalities #B2GSaaS #AIFounder #LaunchStudio #Manifera
