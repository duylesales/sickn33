🚨 Bart Scholten bouwde Inkoopscan met Claude Code en Supabase: het leest inkoopfacturen uit e-mail en koppelt ze aan inkooporders. In maanden van agentsessies verzamelde het project 214 dependencies. Vóór de lancering vroeg de IT-afdeling van een klant om een review. Drie packages vielen op. 😳

Eén ervan, met een naam die suggereerde dat het Nederlandse facturen parste, was enkele weken oud, had één anonieme maintainer, geen broncode-repository - en een installatiescript dat een netwerkrequest deed. Dit betekenen slopsquatting en gehallucineerde packages voor door AI gegenereerde code: 🧠

❌ Een verdacht nieuw package met een installatiescript dat het netwerk opging
❌ Een verlaten package met bekende kwetsbaarheden
❌ Geen gecommit lockfile, dus elke build haalde opnieuw versies op
❌ De service role-sleutel van productie beschikbaar in de CI waar de agent draaide

✅ Verdachte en verlaten packages verwijderd, plus 37 ongebruikte dependencies
✅ Een gecommit lockfile en reproduceerbare builds
✅ Alle CI-secrets geroteerd en logs gecontroleerd - geen ongebruikelijke toegang gevonden
✅ Beschermde dependencybestanden, supply chain-scans, beperkte CI-credentials en goedgekeurde libraries voor Claude Code

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, controleren we wie de packages schreef die uw agent ongemerkt installeert. 🛠️

💡 Het resultaat: €2.800, 7 werkdagen. Inkoopscan doorstond de IT-review met een dependencybeleid en SBOM, en de scanner signaleerde later nog twee onbekende voorstellen van de agent, afgewezen vóór installatie. 🚀

👉 Installeert uw AI-agent packages waar u nog nooit van hoorde? Dit moet u controleren: https://launchstudio.eu/nl/blog/hallucinated-packages-slopsquatting-in-ai-generated-code

#SupplyChainSecurity #ClaudeCode #AppSecurity #AIAgents #LaunchStudio #Manifera
