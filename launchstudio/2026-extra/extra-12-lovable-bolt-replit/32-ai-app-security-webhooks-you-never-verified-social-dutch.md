🚨 Sportschoolbeheer van Lieke Ottenhof beheert lidmaatschappen voor 54 zelfstandige sportscholen en studio's — zo'n 8.000 leden. Lidmaatschappen werden geactiveerd door een betaalwebhook die nooit de handtekening controleerde. Het dashboard van de provider toonde dat elke levering slaagde, dus het leek in orde. 😳

De URL stond vier dagen in een publieke repository. Elf weken later begon iemand er valse "betaling geslaagd"-berichten naartoe te sturen — 23 lidmaatschappen bij negen sportscholen, elk € 240 tot € 580 per jaar waard, sommige doorverkocht. Dit is een niet-geverifieerde webhook werkelijk:

❌ Een publieke URL die toegang verleent wanneer hij wordt aangeroepen — zonder handtekeningcontrole
❌ Geen controle op tijdstempel, dus onderschepte berichten konden eeuwig opnieuw worden afgespeeld
❌ Geen registratie van verwerkte events, dus nieuwe pogingen konden dubbel toegang geven
❌ Lidmaatschap verleend op het woord van het bericht, zonder de provider te vragen

✅ Verificatie van de handtekening op de ruwe inhoud met een timing-veilige vergelijking — mislukkingen geweigerd en gemeld
✅ Berichten ouder dan vijf minuten geweigerd, en elk event-ID vastgelegd zodat replays en nieuwe pogingen onschadelijk zijn
✅ Verifiëren, vastleggen, bevestigen — met activering in een achtergrondtaak, pas na bevestiging van de betaling via de API van de provider
✅ De 23 valse lidmaatschappen gevonden door betalingen te vergelijken, plus een maandelijkse afstemming van lidmaatschappen tegen echte betalingen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, controleren we of uw webhook-URL iedereen gelooft die hem aanroept. 🔏

💡 Het resultaat: na twee werkdagen en € 2.500 werd ongeveer € 9.000 aan jaarlijkse lidmaatschapswaarde teruggewonnen — en de afstemmingstaak heeft sindsdien twee echte gaten door mislukte leveringen opgevangen. Vier regels code bewaken nu het hele verdienmodel. 🚀

👉 Webhooks die u nooit hebt geverifieerd: https://launchstudio.eu/nl/blog/ai-app-security-webhooks-you-never-verified

#Webhooks #Appbeveiliging #Betalingen #Lovable #LaunchStudio #Manifera
