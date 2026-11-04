🚨 Jeroen Vink verkoopt en installeert keukens in Ede. Hij bouwde Keukenofferte in Lovable: klanten stellen een keuken samen en krijgen een indicatieve offerte. Hij koppelde het aan GitHub en huurde een freelancer in om een afrondingsfout in de btw te repareren. De fix hield drie dagen stand. 😳

Toen vroeg Jeroen Lovable om een nieuw werkbladmateriaal, Lovable genereerde het offertecomponent opnieuw - en de afrondingsfout was terug. Het gebeurde nog twee keer. Dit ging er mis:

❌ Kritieke prijslogica in een component dat Lovable steeds opnieuw genereerde
❌ De repository onder het persoonlijke GitHub-account van Jeroen
❌ Een vastgelegd .env-bestand met de geheime sleutel van de e-mailprovider
❌ Geen werkwijze die de wijzigingen van Lovable scheidde van die van de freelancer

✅ Repository verplaatst naar een GitHub-organisatie van het bedrijf, blootgestelde sleutel vervangen en historie opgeschoond
✅ Prijsberekening verplaatst naar een Postgres-functie in Supabase, buiten het bereik van Lovable
✅ Een stagingdeployment vanuit main en een lijst met beschermde bestanden in de kennisinstellingen van Lovable
✅ Een werkwijze met featurebranches voor de freelancer

Bij **LaunchStudio**, ondersteund door Manifera's 160+ projecten met branches, reviews en staging als standaard, maken we uw Lovable-repository veilig voor meer dan één bouwer. 🛠️

💡 Het resultaat: €1.450, zes werkdagen. Jeroen bleef opties toevoegen in Lovable zonder de prijzen nog te breken, Keukenofferte maakte in vier maanden ongeveer 540 offertes, en fixes verdwenen niet meer. 🚀

👉 Lovable-code exporteren naar GitHub? Dit is de werkwijze die voorkomt dat fixes verdwijnen: https://launchstudio.eu/nl/blog/how-to-export-lovable-code-to-github-and-keep-building

#Lovable #GitHub #Supabase #AIFounder #LaunchStudio #Manifera
