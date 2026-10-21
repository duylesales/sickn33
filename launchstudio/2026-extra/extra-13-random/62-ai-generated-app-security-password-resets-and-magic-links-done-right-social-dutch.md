🚨 Tijmen Boersma heeft een schoonmaakbedrijf voor bedrijfspanden in Almelo en bouwde Poetsplan met Cursor: planners wijzen schoonmakers toe aan kantoorgebouwen, en klanten zien voltooide rondes en toegangsnotities — inclusief alarmcodes. 22 schoonmaakbedrijven in Twente gebruikten het. Toen raadde een klant met oog voor beveiliging zich met een eenvoudig script in één middag een testaccount binnen. 😳

Tijmen had Cursor gevraagd om "inloggen zonder wachtwoord met een code per e-mail". Hij kreeg een code van zes cijfers, 24 uur geldig, met onbeperkt aantal pogingen. De aparte herstelflow bouwde zijn link op uit de host-header van het verzoek, tokens stonden als platte tekst opgeslagen, een herstel beëindigde geen andere sessies, en het inlogformulier meldde niet-klanten "onbekend e-mailadres". Zo regelt u wachtwoordherstel en magic links goed in een AI-gebouwde app:

❌ Codes van zes cijfers met onbeperkt raden
❌ Herstellinks opgebouwd uit de host van het verzoek
❌ Tokens als platte tekst opgeslagen en nooit ongeldig gemaakt
❌ Sessies die een wachtwoordwijziging overleven

✅ Eigen login en herstel vervangen door de ingebouwde flows van Supabase Auth
✅ Vervaltijd van tien minuten, gehashte tokens voor eenmalig gebruik en een bevestigingsstap die e-mailscanners overleeft
✅ Rate limits per e-mailadres en IP met blokkades, en herstel-URL's vast op een geconfigureerde basis-URL
✅ Alle sessies ingetrokken bij wachtwoordwijziging met een meldingsmail, gelijke meldingen, een geauthenticeerd verzenddomein — en alarmcodes alleen voor planners

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering en zijn wortels in cybersecurity, controleren we de tweede deur naar elk account — niet alleen de voordeur. ⚙️

💡 Het resultaat: € 1.150, vier werkdagen. De vervolgtest van de klant vond geen weg naar binnen, Poetsplan doorstond de beveiligingscontrole voor leveranciers van die klant, en het groeide sindsdien naar 35 schoonmaakbedrijven. 🚀

👉 Beveiliging van AI-Apps: Wachtwoordherstel en Magic Links Goed Inrichten: https://launchstudio.eu/nl/blog/ai-generated-app-security-password-resets-and-magic-links-done-right

#Authenticatie #AppSecurity #Supabase #Cursor #LaunchStudio #Manifera
