🚨 Lotte Brouwer heeft twee fietsenwerkplaatsen in Zwolle en bouwde Fietsdepot in Lovable: klanten boeken een reparatie, betalen € 15 boekingskosten en krijgen updates. Een bureau offreerde € 32.000 en vier maanden om het "op een degelijke stack opnieuw te bouwen" — inclusief een herontwerp dat ze niet wilde. 😳

De echte problemen zaten elders: klanten konden reparatienotities van anderen lezen door een ID in de URL te veranderen, boekingskosten werden als betaald gemarkeerd zodra de browser terugkwam van Mollie, en de database stond in een Amerikaanse regio zonder geteste back-ups. Zo maakt u een AI-app productieklaar zonder hem te herschrijven:

❌ Geen row level security — reparatienotities zichtbaar voor andere klanten
❌ Betaalstatus vertrouwd op de terugkeer van de browser
❌ Een database in de VS zonder geteste back-ups
❌ Statusmails vanaf een gedeeld domein, een derde in de spam

✅ Row level security op elke tabel
✅ Betalingen bevestigd via geverifieerde Mollie-webhooks
✅ Database verhuisd naar een EU-regio met dagelijkse back-ups en een getest herstel
✅ Een eigen verzenddomein met SPF, DKIM en DMARC — en geen enkel scherm opnieuw ontworpen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, repareren we wat eronder zit en houden we de app die u bouwde. ⚙️

💡 Het resultaat: € 2.600, elf werkdagen. 1.340 boekingen in drie maanden, afwijkingen in boekingskosten van één per dag naar nul, en "uw fiets is klaar"-mails uit de spam — klanten belden niet meer om te vragen. 🚀

👉 Een AI-applicatie productieklaar maken zonder te herschrijven: https://launchstudio.eu/nl/blog/productionize-an-ai-application-without-rewriting-it

#Lovable #Supabase #NoCode #Startups #LaunchStudio #Manifera
