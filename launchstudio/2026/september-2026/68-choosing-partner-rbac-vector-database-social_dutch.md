⚖️ De met Lovable gebouwde juridische onderzoekstool van Femke had één `firm_id`-kolom op zijn vectortabel — waardoor elke medewerker bij een advocatenkantoor met meerdere praktijkgroepen dossiers uit elk praktijkgebied kon ophalen, ongeacht anciënniteit of rol. 🧠

Als uw vectordatabase geen role-based access control heeft die verder gaat dan één enkele eigenaarkolom, kan semantische gelijkenis de privégegevens van iemand anders naar voren brengen als het *meest* relevant ogende antwoord.

❌ Embeddings zonder eigendomsmetadata verder dan een platte team- of kantoor-ID
❌ Rolhiërarchieën die niet op één kolom passen — managers, leiders en partners hebben allemaal verschillende scopes nodig
❌ RBAC alleen getest op leesweigering, met schrijfpaden (`INSERT`, `UPDATE`, `DELETE`) op een standaard-toestaande status achtergelaten

✅ Metadataschema ontworpen rond de daadwerkelijke rolhiërarchie voordat er beleid wordt geschreven
✅ RLS-beleid gejoind tegen een rollentabel, dekkend alle vier databaseoperaties
✅ Adversariële tests gericht op cross-tenant-lekkage via semantische gelijkenis, niet alleen toestemmingscontroles

Bij **LaunchStudio** lossen wij dit type productie-engineeringprobleem al sinds 2014 op via Manifera, over 160+ opgeleverde projecten. 🛡️

Het kantoor van Femke kreeg aantoonbare tenant-isolatie: medewerkers en praktijkleiders zien nu alleen de dossiers van hun praktijkgebied, partners behouden kantoorbrede toegang precies zoals bedoeld, en adversariële tests bevestigden geen lekkage tussen praktijkgebieden, zelfs niet via randgeval-query's. (€4.600 (Enterprise Hardening Pakket) — RBAC-ontwerp, implementatie en testen voltooid in 14 werkdagen.). 🚀

👉 Bekijk hoe wij het oplosten: [Link naar artikel]

#LaunchStudio #Manifera #AISaaS #RBAC #VectorDatabase
