🚨 Vincent Bogaers's Taxatierapport produces property valuation reports for nineteen estate agents and four valuation firms around Bergen op Zoom and Roosendaal. He moved hosting and consolidated DNS on a Thursday afternoon. The site was up on the new host in twenty minutes. He considered it done. 😳

For three days, every email to his domain was rejected — including the address printed on every valuation report. Here's what a domain move can silently break: 🧠

❌ Mail exchange records never recreated
❌ Login callbacks still naming the old hosting address — nobody could sign in
❌ A payment webhook pointing at the old address: eleven days of subscription events lost
❌ Hosting move and registrar transfer planned together

✅ MX, SPF, DKIM and DMARC restored and delivery tested against four major providers
✅ Both addresses registered for login callbacks during the transition
✅ The webhook repointed with signature verification and deduplication, and eleven days reconciled
✅ Lower TTLs, a zone export, a full inventory of everything using the domain — and the registrar transfer done separately

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we migrate live domains without losing a single email. 🌐

His result: five business days and €2,800 later, the registrar transfer three weeks on was uneventful and the inventory now guides every DNS change. The rejected mail couldn't be recovered — he estimates it cost him one valuation firm's trust for most of a year. 🚀

👉 Migrating a live domain safely: https://launchstudio.eu/en/blog/lovable-custom-domain-migrating-a-live-domain-safely

#DNS #Lovable #CustomDomain #EmailDeliverability #LaunchStudio #Manifera
