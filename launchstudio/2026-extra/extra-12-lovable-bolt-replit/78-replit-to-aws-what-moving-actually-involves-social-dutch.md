🚨 Dossierbeheer van Maarten Kolff beheert zo'n 2.800 dossiers voor negen jeugdzorgorganisaties en draait op Replit. Een regionaal zorgsamenwerkingsverband bood een contract voor nog vier organisaties — op voorwaarde dat persoonsgegevens in Nederland werden opgeslagen, onder een specifieke overeenkomst, met een genoemde certificering. Zijn bestuur en twee adviseurs waren het eens: alles migreren naar AWS. 😳

Geschat: zeven weken werk en ongeveer € 900 per maand om te draaien. Maar de voorwaarde in het contract ging over waar persoonsgegevens worden opgeslagen — niet over waar de applicatie draait. Dit houdt overstappen van Replit naar AWS werkelijk in, en zo herkent u wanneer het niet nodig is:

❌ "Data moet in Nederland staan" lezen als "alles moet naar AWS"
❌ De migratie begroten maar niet het permanente beheerwerk erna
❌ Niet nagaan of een kleinere wijziging aan dezelfde eis voldoet
❌ Vergeten wat het platform impliciet deed: netwerk, certificaten, logging, alerting, back-ups, geheimen

✅ De database verhuisd naar een beheerde Postgres-instance in een Nederlandse regio onder een passende overeenkomst — gerepeteerd, daarna een overschakeling van 35 minuten op zondag
✅ Dossierdocumenten naar object storage in dezelfde regio, met URL's die bij het lezen worden gegenereerd
✅ De applicatie op Replit gelaten, simpelweg gekoppeld aan de nieuwe database en opslag
✅ Een gepubliceerde verklaring over datalocatie en een pagina met subverwerkers, plus back-ups in de regio met een getest herstel

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, voeren we volledige migraties uit — en vinden we vaker de kleinste stap die aan dezelfde eis voldoet. ⚙️

💡 Het resultaat: € 8.900, negen werkdagen in plaats van een kwartaal. Het contract werd getekend, en de infrastructuur ging van € 95 naar € 340 per maand — niet € 900. 🚀

👉 Van Replit naar AWS: wat overstappen werkelijk inhoudt: https://launchstudio.eu/nl/blog/replit-to-aws-what-moving-actually-involves

#Replit #AWS #Cloudmigratie #Dataresidentie #LaunchStudio #Manifera
