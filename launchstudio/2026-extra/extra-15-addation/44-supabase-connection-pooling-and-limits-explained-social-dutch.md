🚨 Mila Pauwels bouwde Urenregistratie Pro met Cursor, Next.js en Supabase: urenregistratie en salarisexports voor kleine uitzendbureaus. Elke vrijdagmiddag, als bureaus uren exporteerden voor de salarisadministratie, begon de app te falen met verbindingsfouten. 😳

Mila plande een grotere database. Het echte probleem: de code opende steeds een nieuwe deur zodra iemand aanklopte. Zo werken connection pooling en limieten in Supabase: 🧠

❌ Serverless functies op de directe connection string, opgeschaald op vrijdag
❌ Een nieuwe databaseclient in elke server action
❌ Een exportworker die per taak een pool opende en nooit sloot
❌ Lange transacties rond externe API-calls, en een BI-tool op productie

✅ De app op Supavisor transaction mode met Drizzle daarop ingesteld, één client per instantie
✅ Eén kleine pool in session mode voor de worker, met verbindingen netjes vrijgegeven
✅ Externe API-calls buiten transacties, plus statement timeouts
✅ Een alleen-lezen BI-rol en meldingen bij 75% van de verbindingslimiet

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, repareren we de oorzaak voordat u betaalt voor een grotere server. 🛠️

💡 Het resultaat: €2.600, 7 werkdagen. De vrijdag erna bleef het piekaantal verbindingen onder 40% terwijl bureaus zo'n 2.600 urenstaten exporteerden - en de geplande upgrade was niet nodig. 🚀

👉 Ziet u verbindingsfouten in Supabase? Zo werken pooling en limieten: https://launchstudio.eu/nl/blog/supabase-connection-pooling-and-limits-explained

#Supabase #Postgres #Serverless #Performance #AIFounder #LaunchStudio #Manifera
