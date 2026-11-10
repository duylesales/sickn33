🚨 Ahmed Benali bouwde Factuurportaal met v0, Next.js en Supabase: freelancers sturen facturen, klanten bekijken en betalen ze online. Hij had zorgvuldig Row Level Security-policies geschreven. Toen installeerde de agent, bij het toevoegen van rapportages met Cursor, Prisma. 😳

Een klant veranderde het factuurnummer in een URL en zag de factuur van een andere freelancer. Prisma verbond met de postgres-rol - en omzeilde elke policy die Ahmed had geschreven. Dit moet u weten over Prisma of Drizzle in een door AI geschreven Next.js-app: 🧠

❌ Een ORM-verbinding die RLS ongemerkt omzeilde
❌ 14 van de 23 server actions die records op ID laadden zonder eigenaarschapscheck
❌ Schemawijzigingen zowel in het dashboard als via Prisma-migraties
❌ Directe verbindingen die faalden bij de facturatiepiek aan het eind van de maand

✅ Eén helder patroon: Prisma serverside met afgebakende helpers, de Supabase-client voor door RLS beschermde reads
✅ Alle 23 server actions herschreven met verplichte organisatiescope, en negatieve tests
✅ Eén migratiegeschiedenis met RLS als tweede laag
✅ Prisma via de Supabase-pooler, en projectinstructies voor Cursor

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zorgen we dat de code die het meeste werk doet uw beveiligingsregels ook echt respecteert. 🛠️

💡 Het resultaat: €3.500, 9 werkdagen, met het lek binnen een dag gedicht. Verbindingsfouten aan het eind van de maand verdwenen, en de nieuwe tests vingen twee latere AI-wijzigingen die weer onafgebakende queries hadden geïntroduceerd. 🚀

👉 Gebruikt u Prisma of Drizzle met Supabase? Hier moet u op letten: https://launchstudio.eu/nl/blog/prisma-or-drizzle-in-an-ai-written-nextjs-app

#Prisma #Drizzle #NextJS #Supabase #AIFounder #LaunchStudio #Manifera
