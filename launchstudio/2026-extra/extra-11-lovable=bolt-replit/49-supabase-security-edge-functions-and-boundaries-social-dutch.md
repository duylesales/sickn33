🛡️ Bram Osinga bouwde Declaratie in Lovable voor onkostendeclaraties bij 7 accountantskantoren in Hilversum. Werknemers dienden declaraties in, kantooreigenaren keurden goed. Een audit wees echter uit dat de Supabase Edge Functions goedkeuringen verwerkten zonder verificatie van de afzender: medewerkers konden hun eigen declaraties goedkeuren door simpelweg een payload-parameter aan te passen. 😳

Code verplaatsen naar een Edge Function maakt het pas veilig als u de server-side vertrouwensgrenzen strikt controleert. Waar het misgaat:

❌ Denken dat Edge Functions automatisch veilig zijn zonder het inlogtoken (JWT) van de gebruiker te valideren
❌ De almachtige `service_role` key gebruiken in functies zonder autorisatiechecks per organisatie
❌ Ongevalideerde JSON-payloads van de browser klakkeloos vertrouwen en wegschrijven
❌ Geen rate limiting toepassen waardoor gevoelige functies vatbaar zijn voor brute-force misbruik

Wat u wél moet inrichten vóór gebruikers ongeoorloofd data manipuleren via de backend:

✅ Bij elke functie-aanroep cryptografisch verifiëren wie de ingelogde gebruiker is via het JWT-token
✅ Database-acties strikt beperken tot de specifieke organisatie en rol van de geverifieerde gebruiker
✅ Inkomende request-data strikt valideren via Zod-schema's vóór verwerking in de database
✅ Strikte rate limiting en gestructureerde auditlogging activeren op alle publieke endpoints

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in enterprise engineering, controleren en beveiligen we server-side Edge Functions zodat uw zakelijke logica 100% fraudebestendig is.

💡 Het resultaat: Bram Osinga liet 6 Edge Functions binnen 5 werkdagen beveiligen voor € 2.300 (caller-verificatie, inputvalidatie, key scoping, rate limiting, logging). Het lek werd vóór de lancering gedicht en de controlerend accountant ontving een sluitende security-verklaring. 🚀

👉 Lees hoe u Supabase Edge Functions waterdicht beveiligt tegen manipulatie: https://launchstudio.eu/nl/blog/supabase-security-edge-functions-and-boundaries

#Supabase #EdgeFunctions #Beveiliging #WebApps #LaunchStudio #Manifera
