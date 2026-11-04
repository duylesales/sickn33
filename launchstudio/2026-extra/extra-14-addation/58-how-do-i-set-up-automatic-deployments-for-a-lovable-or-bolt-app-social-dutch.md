🚨 Wouter van Rossum runt een keuringsbedrijf in Den Helder en bouwde Keuringsapp met Bolt: inspecteurs vullen op tablets checklists voor brandveiligheid in en genereren rapporten voor klanten. Op een avond deployde hij vanaf zijn laptop een nieuwe versie van een checklist - zonder de bijbehorende databasekolom, die alleen in zijn lokale aantekeningen bestond. De volgende ochtend konden inspecteurs drie uur lang geen rapporten insturen. 😳

Elke release hing ervan af dat hij vijf handmatige stappen onthield. Zo werkte deployen eerst:

❌ Builds gemaakt op zijn laptop en met de hand naar Netlify geüpload
❌ Databasewijzigingen met de hand in het Supabase-dashboard, niet in git
❌ Geen controles voordat een release de inspecteurs bereikte
❌ Eén keer een deployment vanaf een branch met onafgemaakte wijzigingen

✅ De repository gekoppeld aan Netlify met staging- en productiebranches
✅ Elke schemawijziging omgezet in migraties
✅ Een GitHub Actions-workflow met linting, build, migraties en twee end-to-end-tests
✅ Edge functions gedeployd via de CLI, en de stappen voor terugdraaien gedocumenteerd

Bij **LaunchStudio**, ondersteund door Manifera's 160+ enterpriseprojecten met GitHub Actions en cloudpipelines als standaard, maken we de snelheid van AI veilig: controles, staging, bewuste promotie en terugdraaien met één klik. 🛠️

💡 Het resultaat: €1.500, vier werkdagen. In het kwartaal daarna bracht Wouter 22 updates uit zonder één mislukte deployment - en één kapotte build door een wijziging in Bolt werd automatisch tegengehouden voordat die de inspecteurs bereikte. 🚀

👉 Deployt u uw Lovable- of Bolt-app nog met de hand? Dit is een praktische CI/CD-opzet: https://launchstudio.eu/nl/blog/how-do-i-set-up-automatic-deployments-for-a-lovable-or-bolt-app

#CICD #GitHubActions #Bolt #Supabase #LaunchStudio #Manifera
