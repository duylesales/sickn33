🔍 Nadia bouwde ClauseBank, een SaaS voor contractzoeken voor advocatenkantoren, met **Bolt** — en voegde semantisch zoeken toe met pgvector via een tutorial die het binnen een dag werkend kreeg. Acht maanden en 40 kantoren later stelde een enterprise-beveiligingsbeoordeling één vraag die ze niet met vertrouwen kon beantwoorden.

Als u vectorzoeken toevoegt zonder dezelfde Row Level Security-scrutiny die u op elke andere tabel zou toepassen, wordt "gewoon zoeken" een cross-tenant datalek dat wacht om ontdekt te worden.

❌ Row Level Security nooit ingeschakeld op de embeddingstabel
❌ De zoekopdracht van elke geauthenticeerde gebruiker kon technisch gezien vertrouwelijke contractfragmenten van een ander kantoor opvragen
❌ De lacune bleef acht maanden onzichtbaar omdat de frontend het nooit toonde

✅ RLS-beleid ingeschakeld en gescoped naar `auth.uid()` en kantoor-ID op de embeddingstabel
✅ Een re-ranking-stap toegevoegd om de relevantie van resultaten te verbeteren
✅ Adversariële testquery's die bevestigen dat cross-tenant-opvraging nu wiskundig onmogelijk is

Bij **LaunchStudio** lossen wij dit type productie-engineeringprobleem al sinds 2014 op via Manifera, over 160+ opgeleverde projecten. 🛡️

ClauseBank slaagde voor de beveiligingsbeoordeling van de enterprise-klant met de kwetsbaarheid volledig gedocumenteerd als verholpen, en Nadia sloot het grootste contract van het kantoor tot nu toe — een enterprise-implementatie met 200 zetels. (€ 1.700 (Launch & Grow Pakket) — beveiligd en geverifieerd in 6 werkdagen.) 🚀

👉 Bekijk hoe wij het oplosten: [Link naar artikel]

#LaunchStudio #Manifera #AISaaS #VectorDatabase #RAGSecurity
