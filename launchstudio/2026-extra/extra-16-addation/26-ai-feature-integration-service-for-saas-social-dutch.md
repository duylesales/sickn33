📑 Sven de Boer heeft een inkoopadviesbureau in Eindhoven en bouwde Contractwijzer met v0, Cursor en Supabase: een SaaS die leverancierscontracten opslaat voor maakbedrijven. Hij voegde een AI-assistent toe: "Welke contracten worden volgend kwartaal automatisch verlengd?" Klanten waren er in demo's dol op. Twee maanden later was de AI-rekening hoger dan de omzet uit de functie. 💸

Erger nog, antwoorden noemden soms contracten van een andere klant. De review liet zien waarom: 🧠

❌ De API-sleutel in de frontend en geen limieten per gebruiker
❌ De volledige tekst van elk contract bij elke vraag meegestuurd
❌ Retrieval die de embeddings van alle klanten doorzocht zonder filter op organisatie
❌ Verzoeken die een halve minuut bleven hangen, zonder time-out

✅ De assistent naar de serverkant verplaatst, met een geroteerde sleutel
✅ Retrieval opnieuw gebouwd met pgvector, gefilterd op organisatie, met alleen relevante clausules
✅ Routering tussen modellen, plus verlengingsdata in velden zodat veel vragen gewone query's werden
✅ Limieten per abonnement, caching, time-outs, meldingen over gebruik en een evaluatieset van 60 vragen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met software en integraties voor klanten zoals Vodafone en TNO, maken we AI-functies nuttig, betaalbaar en veilig voor echte klanten. 🛠️

💡 Het resultaat: €5.600, veertien werkdagen. De AI-kosten per klant daalden tot een fractie, het lek werd gedicht en juiste antwoorden stegen van 41 naar 55 van de 60. 🚀

👉 Integratieservice voor AI-functies in SaaS: https://launchstudio.eu/nl/blog/ai-feature-integration-service-for-saas

#AI #LLM #SaaS #Supabase #AIFounder #LaunchStudio #Manifera
