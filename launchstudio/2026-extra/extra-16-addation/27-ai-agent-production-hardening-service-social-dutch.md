📬 Maarten Bos heeft vanuit Breda een boekhoud-SaaS voor kleine aannemers en bouwde Factuurmaat met Claude Code en Supabase. De agent las e-mails van leveranciers, haalde facturen eruit, koppelde ze aan inkooporders en kon via een bankintegratie betalingen inplannen. Klanten waren er dol op. Toen stuurde een bevriende security engineer één e-mail met verborgen tekst, en de agent plande zonder enige controle een betaling naar een nieuwe bankrekening in. 😨

De risicoreview vond meer: 🧠

❌ Een databasesleutel met toegang tot alle klanten
❌ Externe e-mails verwerkt met elke beschikbare tool, inclusief betalingen
❌ Geen limieten op stappen of uitgaven, en nieuwe pogingen die betalingen konden verdubbelen
❌ De enige vastlegging een chattranscript dat na een week verdween

✅ Een ontwerp in twee fasen: alleen-lezentools voor e-mails, acties pas na een duidelijke preview
✅ Tools afgebakend tot de organisatie van de klant en de rechten van de gebruiker
✅ Betalingen naar nieuwe of gewijzigde rekeningen geblokkeerd tot bevestiging buiten de agent, met idempotentiesleutels
✅ Limieten, een audittrail, een noodstop per klant en 80 evaluatiescenario's, waarvan 20 gemanipuleerd

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met software en security engineering, maken we AI-agents beheersbaar zonder ze minder nuttig te maken. 🛠️

💡 Het resultaat: €6.900, achttien werkdagen. Alle 20 gemanipuleerde e-mails werden geblokkeerd, en in drie maanden werden 11 echte verdachte facturen gemarkeerd. 🚀

👉 AI-agents productierijp maken: https://launchstudio.eu/nl/blog/ai-agent-production-hardening-service

#AIAgents #PromptInjection #Beveiliging #ClaudeCode #AIFounder #LaunchStudio #Manifera
