🚨 Ruben Dekker organiseert kaasboerderijtours rond Alkmaar en bouwde Kaasroute in Bolt: toeristen boeken, betalen en krijgen een QR-ticket; partnerboerderijen zien komende bezoekers. In de tweede zomer mailde een gast die in de IT werkte hem beleefd. Ze had het boekingsnummer in haar ticket-URL veranderd — en de namen, het telefoonnummer en het hotel van een ander gezin gezien. 😳

Ook had ze gemerkt dat /admin elke boeking van het seizoen toonde. De beheerlink stond nergens in de app, dus Ruben ging ervan uit dat niemand hem zou vinden. Dit probeert een aanvaller in de eerste tien minuten bij een AI-gebouwde app:

❌ Minuut 1: sleutels in de paginabron (er stond een betaal-API-sleutel)
❌ Minuut 3: voorspelbare adressen als /admin zonder rolcontrole op de server
❌ Minuut 5: een nummer in de URL veranderen en het record van een ander lezen
❌ Minuut 7: inlogformulieren zonder rate limit en met verraderlijke foutmeldingen

✅ Beheergedeelte en de bijbehorende API op dag één achter rolcontroles op de server
✅ Controles op eigenaarschap van tickets, met onvoorspelbare codes in plaats van oplopende nummers
✅ De betaalsleutel geroteerd en naar de server verplaatst; login met rate limiting en uniforme foutmeldingen
✅ Partnerportaal beperkt per boerderij, logs gecontroleerd en beoordeling van een datalekmelding gedaan

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering — en een oprichter met een achtergrond in cybersecurity — sluiten we de deuren in dezelfde volgorde waarin aanvallers ze proberen. ⚙️

💡 Het resultaat: € 1.100, vier werkdagen. Geen bewijs van bredere toegang, het seizoen werd veilig afgerond, de gast kreeg een gratis tour voor twee — en de site heeft nu een adres om beveiligingsproblemen te melden. 🚀

👉 Beveiliging van AI-gegenereerde apps: wat een aanvaller als eerste probeert: https://launchstudio.eu/nl/blog/ai-generated-app-security-what-an-attacker-tries-first

#AppSecurity #Bolt #OWASP #Startups #LaunchStudio #Manifera
