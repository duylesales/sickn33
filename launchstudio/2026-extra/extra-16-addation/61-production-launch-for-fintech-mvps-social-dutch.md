🐷 Mehmet Yildiz heeft in Rotterdam een start-up die Spaarpot bouwde met Cursor en Supabase: gezinnen en vriendengroepen sparen samen voor reizen en evenementen. Het geld loopt via een betaalinstelling met een vergunning, zodat Spaarpot zelf nooit gelden aanhoudt. Maar een pilot met 40 groepen liet kleine verschillen zien tussen de saldi in de app en de overzichten van de partner. Hier een cent, daar een cent. 🪙

Vóór de livetoegang stuurde de partner een technische vragenlijst. De beoordeling vond: 🧠

❌ Saldi opgeslagen als decimalen en direct bijgewerkt, met afronding in de browser
❌ Opnieuw verstuurde webhooks die een inleg soms twee keer crediteerden
❌ De API-sleutel van de partner gebruikt in een functie aan de clientkant
❌ Groepsleden konden de inleg van andere groepen zien, en er was geen auditlog

✅ Bedragen in gehele centen met expliciete valuta, en een grootboek waaraan alleen kan worden toegevoegd, met afgeleide saldi
✅ Geverifieerde, idempotente webhooks gekoppeld aan de event-ID's van de partner, plus een dagelijkse afstemming met meldingen
✅ De sleutel naar de serverkant verplaatst en geroteerd, en groepen gescheiden met Row Level Security en tests
✅ MFA, een extra bevestiging bij uitbetalingen, een auditlog en documentatie voor de due diligence

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met software met betaal- en financiële integraties voor organisaties zoals Vodafone en TNO, bouwen we financiële MVP's die tot op de cent kloppen. 🛠️

💡 Het resultaat: €5.800, vijftien werkdagen. Livetoegang drie weken na de documentatie, en sinds de lancering komen de saldi tot op de cent overeen met de overzichten van de partner. 🚀

👉 Productielancering voor fintech-MVP's: https://launchstudio.eu/nl/blog/production-launch-for-fintech-mvps

#Fintech #PSD2 #DORA #Supabase #AIFounder #LaunchStudio #Manifera
