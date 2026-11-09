🔓 Sanne Bakker heeft een administratiekantoor in Apeldoorn en bouwde Boekdeel met Lovable en Supabase: een portaal waar klanten bonnetjes uploaden, opdrachtbevestigingen ondertekenen en jaarrapporten downloaden. Een maand voordat ze haar 60 klanten zou uitnodigen, logde een vriend uit de IT in met een testaccount en veranderde één getal in de adresbalk. Hij zag het jaarrapport van een andere klant. 😱

De beveiligingsreview vond meer dan één open deur: 🧠

❌ Policies waarmee elke ingelogde gebruiker elke rij kon lezen
❌ Een openbare storagebucket, dus links naar rapporten werkten zonder in te loggen
❌ De service role key gebruikt in een functie aan de clientkant
❌ Beheercontroles alleen in de browser en herstellinks die overal naartoe konden verwijzen

✅ Databasepolicies per klant en toegewezen medewerker, met geautomatiseerde tests voor elke tabel
✅ Rapporten in een privébucket met kortlevende signed links
✅ De sleutel geroteerd, e-mail naar de server en beheerdersrollen aan de serverkant gecontroleerd
✅ Rate limits, security headers, beperkte redirects en een getest herstel van back-ups

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met software voor klanten zoals Vodafone en TNO, harden we apps gebouwd met AI vóór de lancering, tegen een vaste prijs en zonder uw interface te veranderen. 🛠️

💡 Het resultaat: €2.650, zeven werkdagen. Sanne lanceerde volgens planning voor alle 60 klanten, en twee grotere klanten kregen hun beveiligingsvragen beantwoord met één rapport. 🚀

👉 Security hardening voor uw AI-app vóór de lancering: https://launchstudio.eu/nl/blog/ai-app-security-hardening-service-before-launch

#Beveiliging #Lovable #Supabase #Lancering #AIFounder #LaunchStudio #Manifera
