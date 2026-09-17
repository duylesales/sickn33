🛡️ Kan een medewerker zijn eigen declaratie van € 800 goedkeuren door simpelweg `approved: true` mee te sturen naar uw Edge Function? Server-side code is niet automatisch veilig.

Een serverless functie aanmaken is niet genoeg. Als de functie niet als eerste stap verifieert wie de aanvrager is en welke rol die heeft, staat de achterdeur wagenwijd open.

Waar het vaak misgaat bij beveiliging van Supabase Edge Functions:

❌ Functies vertrouwen blind op parameters uit de HTTP-request payload zonder autorisatiecheck
❌ Nalaten om het JWT-sessietoken van de aanroeper te valideren via `supabase.auth.getUser()`
❌ De almachtige `service_role` key gebruiken in functies zonder te controleren of de gebruiker wel admin is
❌ Geen CORS-beperkingen of rate limiting instellen op openbaar bereikbare serverless endpoints

Wat u wél moet inrichten vóór onbevoegden zichzelf beheerdersrechten toekennen:

✅ Elke Edge Function laten starten met strikte cryptografische tokenvalidatie van de beller
✅ Server-side controleren of het geverifieerde account de benodigde rechten bezit in de rollentabel
✅ Het gebruik van de `service_role` key beperken tot strikt gevalideerde en gelogde handelingen
✅ Strikte CORS-headers en rate limiting configureren op alle publieke API-aanroepen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in enterprise engineering, trekken we harde server-side beveiligingsgrenzen rond uw Edge Functions.

💡 Zo dichtte declaratieplatform Declaratie in Hilversum een kritiek autorisatiegat vóór de officiële lancering en stelde accountants volledig gerust.

👉 Ontdek waar de beveiligingsgrens hoort te liggen bij Supabase Edge Functions: https://launchstudio.eu/nl/blog/supabase-security-edge-functions-and-boundaries

#Supabase #EdgeFunctions #Cybersecurity #Autorisatie #LaunchStudio #Manifera
