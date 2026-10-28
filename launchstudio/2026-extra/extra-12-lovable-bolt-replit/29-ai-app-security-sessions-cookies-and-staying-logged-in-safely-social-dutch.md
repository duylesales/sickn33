🚨 Zorgplanning van Roos Verhagen plant diensten en cliëntbezoeken voor 18 thuiszorgorganisaties - zo'n 900 zorgverleners. Een planner vertrok na een meningsverschil, en haar manager verwijderde haar account op haar laatste dag. Zaak gesloten. 😳

Drie weken later werden diensten 's nachts verschoven en cliëntbezoeken verwijderd. Haar tablet was nog ingelogd: een refresh token van 90 dagen dat het verwijderen van het account nooit ongeldig had gemaakt. Zo overleven sessies de mensen van wie ze zijn:

❌ Sessietokens in local storage, leesbaar voor elk script op de pagina
❌ Refresh tokens van 90 dagen, zonder registratie van actieve sessies op de server
❌ Een account verwijderen beëindigde de sessies niet
❌ Uitloggen dat heel even de cliëntenlijst van de vorige gebruiker toonde

✅ Tokens verplaatst naar httpOnly-, secure- en sameSite-cookies, met CSRF-tokens bij wijzigingen
✅ Een sessietabel - en deactivering of wachtwoordwijziging beëindigt nu direct elke sessie
✅ Overal uitloggen voor gebruikers, geforceerd uitloggen voor beheerders, en een scherm met actieve sessies
✅ Access tokens van 30 minuten, een refresh van 14 dagen afgestemd met klanten, een inactiviteitstime-out van 12 uur voor gedeelde tablets, en een nieuwe sessie bij inloggen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, controleren we waar uw app haar token bewaart - twee minuten die bepalen wat een toekomstige fout u kost. 🔐

💡 Het resultaat: na twee werkdagen en € 2.700 werden de ongeautoriseerde wijzigingen gereconstrueerd uit de audittrail en gecorrigeerd. Sindsdien hebben drie organisaties het scherm met actieve sessies gebruikt om tablets te vinden die ingelogd waren achtergelaten op cliëntlocaties. 🚀

👉 Sessies, cookies en veilig ingelogd blijven: https://launchstudio.eu/nl/blog/ai-app-security-sessions-cookies-and-staying-logged-in-safely

#Appbeveiliging #Authenticatie #Zorg #Lovable #LaunchStudio #Manifera
