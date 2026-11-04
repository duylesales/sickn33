🚨 Ruud Koopman bouwde Klantbezoek in Lovable: een lichte CRM voor buitendienstmedewerkers van een groothandel in bouwmaterialen, gebruikt op telefoons tussen klantbezoeken door. Vertegenwoordigers klaagden dat ze voortdurend werden uitgelogd - vaak tijdens het typen van bezoeknotities, die daarna verloren gingen. Sommigen werden twintig keer per dag uitgelogd. 😳

Elke uitlog kostte een vertegenwoordiger zijn notities en zijn geduld. De oorzaak bleek vier kopieën van dezelfde inlogcode die met elkaar ruzieden. Dit speelde er:

❌ Een Supabase-client aangemaakt in vier verschillende componenten, die elk volgens een eigen schema tokens vernieuwden
❌ De app bereikbaar op zowel klantbezoek.nl als www.klantbezoek.nl
❌ E-mails met meldingen die naar de versie met www linkten, een andere sessie
❌ Het vernieuwen van tokens dat mislukte op zwakke mobiele verbindingen nadat telefoons op slot gingen, met uitloggen in plaats van een nieuwe poging

✅ Eén gedeelde module met de Supabase-client, overal geïmporteerd
✅ www doorgestuurd naar het canonieke domein, met bijgewerkte redirectinstellingen
✅ Afhandeling die het vernieuwen opnieuw probeert zodra de verbinding terug is, in plaats van uit te loggen
✅ Concepten van bezoeknotities lokaal opgeslagen, zodat er niets verloren gaat als een sessie toch verloopt

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar werk aan authenticatie, volgen we de volledige levenscyclus van de sessie - omdat de meeste "willekeurige" uitlogs een of twee oorzaken hebben die te verhelpen zijn. 🛠️

💡 Het resultaat: €1.200, vier werkdagen. Onverwachte uitlogs gingen van een dagelijkse klacht naar vrijwel nul, en het aantal vastgelegde bezoeknotities per vertegenwoordiger steeg merkbaar zodra ze de app vertrouwden. 🚀

👉 Logt uw Lovable-app gebruikers willekeurig uit? Dit zijn de zes gebruikelijke oorzaken en hoe u ze oplost: https://launchstudio.eu/nl/blog/why-does-my-lovable-app-log-users-out

#Lovable #Supabase #Authenticatie #UX #LaunchStudio #Manifera
