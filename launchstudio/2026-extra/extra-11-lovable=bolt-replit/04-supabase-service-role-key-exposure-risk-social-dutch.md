🔐 Thomas de Wit bouwde Factuurly in Cursor voor 180 zzp'ers in Utrecht. Tijdens een code-audit bleek zijn Supabase `service_role` key direct in de client-side JavaScript-bundle te staan — waarmee elke bezoeker volledige admin-rechten had om facturen van alle gebruikers in te zien of te wissen. 😳

De `service_role` key omzeilt alle Row Level Security. Waar het vaak misgaat bij API-sleutels in AI-code:

❌ `service_role` geheimen geplaatst in client-side omgevingsvariabelen (`NEXT_PUBLIC_` of `VITE_`)
❌ Frontend die rechtstreeks beheeracties uitvoert zonder tussenkomst van beveiligde backend functies
❌ Admin-sleutels die ongemerkt in versiebeheer (Git) terechtkomen
❌ Ontbreken van geautomatiseerde build-time checks tegen het uitlekken van privileged keys

Wat u wél moet inrichten vóór u opschaalt naar betalende gebruikers:

✅ Grondige audit van alle frontend bundles op gelekte beheerderstoegang
✅ Directe rotatie van gecompromitteerde `service_role` tokens in Supabase
✅ Verplaatsing van admin-queries naar strikt geauthenticeerde Edge Functions
✅ Implementatie van geautomatiseerde CI/CD-secret scanners om sleutellekken uit te sluiten

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in enterprise engineering, controleren en isoleren we uw API-credentials zodat beheerdersrechten altijd op de server blijven.

💡 Het resultaat: Thomas de Wit liet Factuurly binnen 5 werkdagen beveiligen voor € 1.900 (sleutelrotatie, Edge Functions, RLS en CI-checks). Het lek werd binnen een week gedicht en het platform draait veilig door voor 180 zzp'ers. 🚀

👉 Controleer direct of uw frontend bundle gevoelige admin-sleutels bevat: https://launchstudio.eu/nl/blog/supabase-service-role-key-exposure-risk

#Supabase #Beveiliging #VibeCoding #WebApps #LaunchStudio #Manifera
