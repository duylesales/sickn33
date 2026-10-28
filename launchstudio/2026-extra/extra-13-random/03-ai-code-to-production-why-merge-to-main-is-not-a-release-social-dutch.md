🚨 Daan Visser bouwde PlankPal met Cursor: lidmaatschappen en QR-check-in voor twee boulderhallen in Delft. Elke push naar main werd automatisch gedeployd. Op een donderdagavond vroeg hij Cursor een status "bevroren lidmaatschap" toe te voegen. De gegenereerde migratie herschreef elke bestaande rij - en zette onbekende statussen op null. 😳

Twee uur lang werden leden met een geldig abonnement bij de deur geweigerd. Code terugdraaien hielp niet: de data was al veranderd. Daarom is "mergen naar main" geen releaseproces:

❌ Elke push binnen veertig seconden direct naar productie
❌ Een migratie die stil bestaande data herschreef
❌ Geen stagingdatabase, geen tests op de check-in
❌ Alleen een terugdraaiplan voor code, niet voor data

✅ De getroffen rijen hersteld uit een point-in-time-back-up
✅ GitHub Actions met typecontroles en check-intests op elke branch
✅ Een apart Supabase-stagingproject met testdata, en migraties in eigen gereviewde PR's
✅ Een vastgelegde terugdraaistap in elk PR-sjabloon, plus foutregistratie op Daans telefoon

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, bouwen we releaseprocessen rond de manier waarop u al met AI-tools werkt. ⚙️

💡 Het resultaat: € 1.600, zes werkdagen. 212 releases in vier maanden - CI hield er negen tegen, waaronder twee migraties die data zouden herschrijven - en sindsdien geen enkele check-instoring. 🚀

👉 Van AI-code naar productie: waarom mergen naar main geen release is: https://launchstudio.eu/nl/blog/ai-code-to-production-why-merge-to-main-is-not-a-release

#Cursor #DevOps #CI #Supabase #LaunchStudio #Manifera
