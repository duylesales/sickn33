🚨 Daphne Kok runt een klein bedrijf in yogaretraites bij Bergen en bouwde Retraitepas in v0 en Supabase. Op een vrijdagmiddag vernieuwde een configuratiewijziging het geheim voor het ondertekenen van webhooks bij haar betaalprovider. Betalingen bleven slagen - maar elke boeking bleef op "in afwachting" staan en geen enkele bevestiging werd verstuurd. Ze kwam er op maandag achter, via een ongeruste gast die €450 had betaald en niets had gehoord. 😳

Elf boekingen zaten vast en twee gasten hadden elders geboekt. De app is nooit uitgevallen. Hij stopte gewoon met het enige wat ertoe deed. Dit is waarom niets het haar vertelde:

❌ Geen uptimecontrole of health endpoint
❌ Geen error tracking op de edge functions waar de webhook faalde
❌ Geen controle of betaalde aanbetalingen echt bevestigde boekingen werden
❌ Geen meldingen op haar telefoon - haar klanten waren haar monitoringsysteem

✅ Uptimecontroles plus een echt health endpoint
✅ Error tracking met meldingen bij nieuwe soorten fouten in edge functions
✅ Een bedrijfscontrole die waarschuwt als een betaalde aanbetaling niet binnen een uur een bevestigde boeking is
✅ Een abonnement op de statuspagina van de betaalprovider, en alle vastgelopen boekingen rechtgezet

Bij **LaunchStudio**, ondersteund door de teams van Manifera in Ho Chi Minh-stad die voorlopen op de Europese tijd, horen monitoring en meldingen bij elke lancering. 🛠️

💡 Het resultaat: €980, drie werkdagen. Twee maanden later leidde een vergelijkbaar webhookprobleem binnen 40 minuten tot een melding, en Daphne loste het op voordat een gast iets merkte. 🚀

👉 Zou u het weten als uw AI-gebouwde app stilletjes stopte met werken? Dit is de minimale monitoringopzet: https://launchstudio.eu/nl/blog/how-do-i-know-when-my-ai-built-app-goes-down

#Monitoring #Supabase #v0 #SaaS #LaunchStudio #Manifera
