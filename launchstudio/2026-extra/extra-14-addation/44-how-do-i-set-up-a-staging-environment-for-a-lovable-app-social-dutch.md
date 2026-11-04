🚨 Wessel Jansen heeft een padel- en squashcentrum in Hoorn en bouwde Baanboeker in Lovable: leden boeken banen, betalen per sessie en schrijven zich in op wachtlijsten. Op een vrijdagavond vroeg hij Lovable een optie "neem een gast mee" toe te voegen en drukte op publiceren. Op zaterdagochtend - het drukste moment voor boekingen - kon niemand boeken. 😳

Op vrijdagavond publiceren voelde efficiënt. Een verloren zaterdagochtend liet hem zien wat efficiënt echt kost. Dit ging er mis:

❌ Een nieuw veld voor gasten dat in de database verplicht was, maar nooit werd meegestuurd door het oudere mobiele boekingsformulier
❌ Geen stagingomgeving om de wijziging eerst te testen
❌ Geen vorige versie om naar terug te gaan
❌ Vier uur aan gemiste boekingen terwijl hij met prompts terugdraaide

✅ Een staging-project in Supabase met testleden en -banen
✅ Vercel-deployments voor main (staging) en productie
✅ Mollie op staging in testmodus en schemawijzigingen ondergebracht in migraties
✅ Een releaseroutine van één pagina en terugdraaien met één klik via de host

Bij **LaunchStudio**, ondersteund door Manifera's 160+ projecten waarin gescheiden omgevingen standaard zijn, geven we elke wijziging een veilige plek om te landen voordat uw klanten haar zien. 🛠️

💡 Het resultaat: €1.250, vier werkdagen. In de drie maanden daarna bracht Wessel 14 wijzigingen via staging uit - twee zouden boekingen hebben gebroken, en beide werden opgemerkt voordat leden iets merkten. 🚀

👉 Staging inrichten voor een Lovable-app? Dit is de praktische opzet en de releaseroutine van 15 minuten: https://launchstudio.eu/nl/blog/how-do-i-set-up-a-staging-environment-for-a-lovable-app

#Lovable #Staging #Supabase #DevOps #LaunchStudio #Manifera
