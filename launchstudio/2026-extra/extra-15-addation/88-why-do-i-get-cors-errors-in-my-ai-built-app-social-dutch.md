🚨 Mila Verbeek bouwde Plantwijzer met Bolt en Supabase: klanten fotograferen een kamerplant, krijgen een AI-diagnose van de gezondheid en ontvangen verzorgingsherinneringen. Op de lanceringsdag koppelde ze plantwijzer.nl en kondigde het aan bij haar 9.000 nieuwsbriefabonnees. Elke diagnose faalde: "blocked by CORS policy". 😳

Een tip van internet om alle origins toe te staan, loste sommige requests op, maar niet alle. Achter één foutmelding zaten vier afzonderlijke problemen. Waarom door AI gebouwde apps CORS-fouten krijgen: 🧠

❌ De toegestane origin hardgecodeerd op het previewdomein
❌ Geen afhandeling van OPTIONS-preflightrequests
❌ Grote afbeeldingen die de functie lieten crashen met een 500 zonder headers - wat op CORS leek
❌ Het herinneringsscherm dat de AI-API vanuit de browser aanriep, met de sleutel zichtbaar in de bundle

✅ Een gedeelde CORS-helper die productie, staging en lokaal toestaat, inclusief www
✅ Elke functie beantwoordt preflight en geeft headers terug bij fouten
✅ Afbeeldingsgrootte gecontroleerd vóór upload, met een duidelijke melding
✅ De AI-call naar een edge function verplaatst, de blootgestelde sleutel geroteerd en fouten naar monitoring

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, vinden we het echte probleem achter verwarrende foutmeldingen en lossen we het veilig op. 🛠️

💡 Het resultaat: €1.400, 3 werkdagen. Diagnoses werkten dezelfde avond weer, en in de eerste week deden zo'n 1.100 klanten een diagnose zonder één CORS-fout. 🚀

👉 Ziet u "blocked by CORS policy"? Dit zijn de oorzaken en veilige oplossingen: https://launchstudio.eu/nl/blog/why-do-i-get-cors-errors-in-my-ai-built-app

#CORS #Bolt #Supabase #WebDevelopment #AIFounder #LaunchStudio #Manifera
