🚨 Ilona Peters bouwde Circuo, een IoT-bewakingsdashboard voor kleine productievloeren, met Lovable — gepolijst genoeg dat twee fabrikanten uit de Brainport-regio vroegen om het te mogen pilotten. Tijdens de onboarding bleek de database helemaal geen row-level security te hebben: elke ingelogde gebruiker kon de sensordata van een ander bedrijf opvragen door simpelweg een ID in de URL te wijzigen. 😳

Het werkte feilloos in de demo omdat er nooit meer dan één account was geweest. 🧠

❌ Row-level security was nooit geconfigureerd — een standaard Supabase-gat dat onzichtbaar blijft totdat er een tweede echte tenant bijkomt
❌ API-sleutels stonden blootgesteld in client-side code
❌ De authenticatiestroom liet sessies tussen bedrijven lekken zodra er meer dan één account bestond
❌ Niets daarvan was zichtbaar in de demo

✅ Doorlicht het schema en implementeer correct row-level-securitybeleid, afgebakend per bedrijfsaccount
✅ Herbouw de authenticatiestroom zodat sessies niet tussen tenants kunnen overlopen
✅ Haal blootgestelde API-sleutels uit de frontend en breng ze onder in een beveiligde backendlaag

Bij **LaunchStudio** behandelen we precies dit gat — de onzichtbare laag onder een gepolijste, door AI gebouwde frontend — als een vast controlepunt, gesteund door de 11+ jaar productie-ervaring van Manifera voor klanten zoals Vodafone en TNO. 🛡️

Het resultaat voor Circuo: het ging binnen dezelfde maand live bij beide pilotfabrikanten, en Ilona tekende een derde klant nadat ze diens beveiligingsvragenlijst probleemloos doorstond. 🚀

👉 Een IoT- of SaaS-dashboard gebouwd met een AI-tool? Laat het vooraf checken met een vaste scope: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #RowLevelSecurity #Eindhoven
