🚨 Thijs Hendriks bouwde Dossierdesk met Lovable en Supabase: een portaal waar cliënten van een immigratieadvocatenkantoor documenten uploaden, hun aanvraag volgen en hun advocaat berichten sturen. Zo'n 220 cliënten gebruikten het. Toen begonnen nieuwe cliënten te bellen: na het inloggen zagen ze een wit scherm. 😳

Bestaande cliënten hadden nergens last van, en Thijs kon het niet reproduceren. Eén screenshot van de console vertelde het verhaal: Cannot read properties of null (reading 'case_number'). Waarom apps een leeg wit scherm tonen: 🧠

❌ Een dashboard dat ervan uitging dat elke cliënt al een dossier had
❌ Herladen van een subpagina gaf een 404 op de live host
❌ Lege pagina's na elke deploy, als oude JavaScript-chunks verdwenen
❌ Geen error boundaries en geen monitoring

✅ Lege toestanden, met een welkomstpagina voor nieuwe cliënten die op hun dossier wachten
✅ Een rewrite-regel zodat subpagina's goed herladen
✅ Eén automatische herlaadactie bij mislukte chunks
✅ Error boundaries en Sentry - dat in de eerste week nog twee crashes vond

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, maken we van totale uitval een afgebakende, gemelde fout. 🛠️

💡 Het resultaat: €1.900, 5 werkdagen. Sindsdien geen meldingen meer van lege schermen, supportgesprekken over het portaal daalden van meerdere per week naar bijna nul, en nieuwe cliënten ronden hun uploads nu af in de eerste sessie. 🚀

👉 Toont uw app een wit scherm? Zo vindt u de echte fout: https://launchstudio.eu/nl/blog/why-does-my-app-show-a-blank-white-screen

#React #Lovable #ErrorMonitoring #LegalTech #AIFounder #LaunchStudio #Manifera
