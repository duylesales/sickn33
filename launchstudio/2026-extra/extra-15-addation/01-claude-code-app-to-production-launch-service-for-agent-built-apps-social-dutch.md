🚨 Joost Vermeulen werkte vijftien jaar in de expeditie in Venlo. In twee maanden avondwerk bouwde Claude Code voor hem Vrachtbod: verladers plaatsen ladingen, kleine transportbedrijven brengen een prijsofferte uit. Zes verladers en twintig vervoerders deden mee aan de pilot. Toen meldde een vervoerder, behulpzaam, dat hij concurrerende biedingen kon zien door een getal in de URL te veranderen. 😳

Joost vroeg Claude Code het te repareren. De agent voegde een controle toe aan de detailpagina, maar het API-endpoint erachter, en twee andere, gaven nog steeds elk bod aan elke ingelogde gebruiker. Dit komt er echt kijken bij het naar productie brengen van een door een agent gebouwde app: 🧠

❌ Endpoints die elk bod aan elke ingelogde gebruiker teruggaven
❌ Een Mollie API-sleutel in een gecommit seed-script
❌ Tests die de database volledig nabootsten
❌ Productiedeploys vanaf Joosts laptop

✅ Eigenaarschapscontroles op alle elf endpoints met bedrijfsdata, plus Row Level Security
✅ De gelekte sleutel geroteerd en de git-geschiedenis opgeschoond
✅ Negatieve autorisatietests voor elke rol
✅ Een geautomatiseerde pipeline met staging, en een CLAUDE.md met beveiligingsafspraken

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, vertellen we u welke beslissingen van uw agent u kunt vertrouwen, en repareren we de rest. 🛠️

💡 Het resultaat: €3.200, 9 werkdagen. Vrachtbod ging opnieuw live en verwerkte het kwartaal daarna zo'n 2.300 offertes zonder één toegangsincident - en de nieuwe tests blokkeerden twee keer een deploy die de biedingen weer zichtbaar had gemaakt. 🚀

👉 Uw app gebouwd met Claude Code? Zo maakt u hem productieklaar: https://launchstudio.eu/nl/blog/claude-code-app-to-production-launch-service-for-agent-built-apps

#ClaudeCode #AIAgents #Logistics #AIFounder #LaunchStudio #Manifera
