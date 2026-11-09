🏃 Femke Smit leidt een netwerk van zelfstandige hardloopcoaches in Nijmegen en bouwde Looplijn met Cursor en Firebase. Coaches maken trainingsschema's, atleten leggen hun loopjes vast, beiden zien voortgangsgrafieken. Na twee jaar en zo'n 3.000 atleten had ze rapportages per coach nodig, een export voor een onderzoekspartner en gegevens gehost in de EU. En de Firebase-rekening was in zes maanden verdrievoudigd. 📈

De beoordeling liet zien waarom een zorgvuldige migratie telde: 🧠

❌ Schema's opgeslagen als geneste documenten, met namen van atleten op wel twaalf plekken
❌ Een voortgangsgrafiek die in realtime naar de hele loopgeschiedenis luisterde
❌ Security Rules waarmee elke coach de gegevens van elke atleet kon lezen
❌ Geen manier om over coaches heen te rapporteren zonder dure reads

✅ Een relationeel model voor coaches, atleten, schema's, trainingen, loopjes en reacties
✅ 400+ inconsistente kopieën van namen en e-mailadressen opgelost met goedkeuring van Femke
✅ Row Level Security zodat coaches alleen hun eigen atleten zien
✅ Gebruikers gemigreerd met wachtwoordhashes, getest met 50 echte accounts, en een overstap van 40 minuten op zondagavond

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met datamigraties waarbij het verliezen van records geen optie was, verhuizen we apps van Firebase naar Supabase tegen een vaste prijs, met een terugvalplan. 🛠️

💡 Het resultaat: €5.200, vijftien werkdagen. Geen enkele atleet hoefde een nieuw wachtwoord, rapportages per coach werden één query en de maandelijkse databasekosten daalden tot ongeveer een derde. 🚀

👉 Migratieservice van Firebase naar Supabase: https://launchstudio.eu/nl/blog/firebase-to-supabase-migration-service

#Firebase #Supabase #Migratie #Cursor #AIFounder #LaunchStudio #Manifera
