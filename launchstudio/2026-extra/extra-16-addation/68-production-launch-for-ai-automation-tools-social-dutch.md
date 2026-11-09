🧾 Stijn Kuijpers heeft in Venlo een start-up die Bonbot bouwde met Cursor en Supabase: die leest inkoopfacturen uit de inbox van een klant, haalt leverancier, bedragen en btw eruit en boekt ze in Moneybird of Exact Online. In de eerste maanden meldden zich zo'n 40 boekhoudkantoren aan. Toen groeiden de volumes, en de problemen ook. 📈

Wat er in productie misging: 🧠

❌ Verwerking binnen een webverzoek, dus grote batches liepen in een time-out, begonnen opnieuw en boekten sommige facturen twee keer
❌ Fouten door rate limits die runs stopten zonder dat iemand het hoorde
❌ Verlopen Gmail-tokens die automatiseringen stilletjes stopten
❌ Volledige e-mailwisselingen naar het AI-model, en de tokens van alle klanten onversleuteld in één tabel

✅ Een wachtrij voor taken met workers, nieuwe pogingen met oplopende wachttijd en een lijst voor taken die blijven falen
✅ Een vaste sleutel per factuur en opgeslagen boekings-ID's, zodat nieuwe pogingen nooit twee keer boeken
✅ Afremming per boekhoudsysteem, versleutelde tokens met automatische vernieuwing en verzoeken om opnieuw te koppelen
✅ Alleen de factuurbijlage naar de AI, routering tussen modellen, een controlewachtrij voor onzekere resultaten en een runhistorie per factuur

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met integraties en verwerking op de achtergrond voor klanten zoals Vodafone en TNO, maken we automatiseringen veilig om opnieuw te proberen, zichtbaar voor klanten en betaalbaar in gebruik. 🛠️

💡 Het resultaat: €6.200, zestien werkdagen. Dubbele boekingen stopten volledig, de AI-kosten per factuur daalden aanzienlijk en Bonbot groeide naar zo'n 120 kantoren. 🚀

👉 Productielancering voor AI-automatiseringstools: https://launchstudio.eu/nl/blog/production-launch-for-ai-automation-tools

#Automatisering #AI #Moneybird #Supabase #AIFounder #LaunchStudio #Manifera
