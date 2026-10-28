🚨 Noortje Vermeer heeft een kledingreparatie- en vermaakatelier in Naarden en bouwde Naaiwerk in Bolt: klanten boeken een pasafspraak, beschrijven reparaties met foto's, krijgen een prijs, betalen een aanbetaling en krijgen een melding als hun kleding klaar is. Zo'n 500 klanten. Na het lezen over de beveiliging van AI-apps liep ze de rode vlaggen zelf na - zonder één regel code te lezen. Ze telde er vijf. 😳

Een nummer in het adres van een bestelling veranderen toonde foto's en het huisadres van een andere klant. De broncode van de pagina bevatte een sleutel die begon met sk_. De beheerpagina opende in een privévenster van de browser. Ze had nooit een back-up teruggezet. En ze had een keer via een Instagram-reactie van een klant gehoord dat de app plat lag. De review bevestigde alle vijf - en vond een zesde: aanbetalingen bevestigd via de redirect in de browser. Dit zijn de rode vlaggen in uw codebase die betekenen: laat een review doen:

❌ De data van een andere klant op één nummer afstand
❌ Een geheime sleutel zichtbaar in de broncode
❌ Een beheerpagina die zonder inloggen opent
❌ Geen geteste back-up en storingen ontdekt door klanten

✅ Toegang per klant afgedwongen in de database
✅ De geheime Mollie-sleutel geroteerd en het aanmaken van betalingen naar de server verplaatst, beheergedeelte beschermd met rollen
✅ Bevestiging van aanbetalingen verplaatst naar webhooks
✅ Back-ups met een geteste restore, een stagingomgeving en meldingen voor uptime en fouten op Noortjes telefoon

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, helpen we niet-technische oprichters de vlaggen te tellen - en ze weg te werken. ⚙️

💡 Het resultaat: € 1.300, vijf werkdagen. Noortje voerde de controles daarna zelf opnieuw uit en vond er geen, Naaiwerk verwerkt nu zo'n 120 boekingen per maand, en ze herhaalt de controles na elke grote wijziging. 🚀

👉 Rode vlaggen in AI-ontwikkeling: Acht signalen in uw codebase die vragen om een code review: https://launchstudio.eu/nl/blog/ai-development-red-flags-eight-things-in-your-codebase-that-mean-get-a-review

#RodeVlaggen #CodeReview #Bolt #MKB #LaunchStudio #Manifera
