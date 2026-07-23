🚨 Ze had het "opgelost" zodra ze de sleutel naar een omgevingsvariabele verplaatste. Ze had geen idee dat de oude versie nog in 3 openbare commits stond die iedereen kon zien. 😱

Hardgecodeerde API-sleutels zijn het #1 beveiligingsgat in AI-gegenereerde code. Dit is het mechanisme dat niemand uitlegt: 🧠

❌ Git verwijdert nooit — elke commit is een permanente momentopname, voor altijd
❌ "Ik heb het verwijderd" verwijdert het alleen uit het HUIDIGE bestand, niet de geschiedenis
❌ Geautomatiseerde bots scannen openbare repo's specifiek op zoek naar dit patroon
❌ Visuele inspectie van huidige bestanden mist blootstellingen in oude commits

✅ Scan de VOLLEDIGE git-geschiedenis, niet alleen de huidige code (git-secrets, trufflehog)
✅ Roteer de credential bij de bron — maakt oude blootstelling onschadelijk
✅ Automatiseer geheimenscanning in CI zodat het wordt opgevangen vóór het ooit wordt vastgelegd

Bij **LaunchStudio** is een volledige geheimenaudit — codebase + complete git-geschiedenis — stap één van elke Launch Ready-opdracht. Gesteund door Manifera's beveiligingscultuur gevormd door klanten zoals TNO. 🛡️

Haar resultaat: blootgestelde sleutel dezelfde dag geroteerd, nul ongeautoriseerd gebruik, CI-scanning voorkomt nu dat dit ooit weer gebeurt. 🚀

👉 Laat je repogeschiedenis auditen voordat je spijt krijgt dat je niet hebt gecontroleerd: [Link naar artikel]

#AISecure #LaunchStudio #Manifera #IndieHacker #GitBeveiliging
