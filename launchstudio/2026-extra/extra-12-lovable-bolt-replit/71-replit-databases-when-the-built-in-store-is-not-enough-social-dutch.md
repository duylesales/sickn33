🚨 Materieelverhuur van Vera Slothouber regelt de verhuur voor negen materieelverhuurders in de bouw - zo'n 1.400 machines. Alles stond in de ingebouwde key-value store van Replit. Toen braken twee dingen tegelijk: het maandelijkse bezettingsrapport - de meestgebruikte functie van elke klant - gaf time-outs, en een naamswijziging van een klant miste 60 records, waardoor facturen twee namen voor hetzelfde bedrijf toonden. 😳

Ze hield handmatig sleutellijsten bij en werkte namen bij in honderden kopieën. Zonder het te merken had ze een database geschreven - een zonder constraints. Zo herkent u dat u de ingebouwde opslag bent ontgroeid:

❌ Eigen sleutellijsten bijhouden alleen om records te vinden
❌ Rapportages die elk ooit aangemaakt record lezen en in code tellen
❌ Klantnamen gekopieerd in elke verhuring in plaats van ernaar te verwijzen
❌ Niets dat verweesde verwijzingen of duplicaten voorkomt

✅ Vijf entiteiten gemodelleerd vanuit het bedrijf; een Postgres-schema met foreign keys en een organisatie-ID op elke tabel
✅ Een migratiescript zes keer tegen een kopie gedraaid - met 140 verweesde verhuringen en 31 dubbele klanten blootgelegd, elk opgelost met een beslissing
✅ Vier dagen dubbel schrijven met dagelijkse vergelijking, wat twee gemiste schrijfpaden opving
✅ Lezen per deel omgeschakeld, de oude opslag drie weken bewaard, back-ups ingericht met een getest herstel

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, brengen we Replit-producten naar productie - inclusief de databasemigratie, zonder downtime. ⚙️

💡 Het resultaat: € 3.800, drie werkdagen. Het bezettingsrapport ging van een time-out naar 400 milliseconden, en het probleem met naamswijzigingen werd structureel onmogelijk. 🚀

👉 Replit-databases: wanneer de ingebouwde opslag niet meer volstaat: https://launchstudio.eu/nl/blog/replit-databases-when-the-built-in-store-is-not-enough

#Replit #Postgres #Database #Datamodellering #LaunchStudio #Manifera
