🚨 Erik Boersma runt een schildersbedrijf in Hengelo en bouwde Verfofferte in Bolt: schilders meten ruimtes op met een tablet, de app berekent verf, uren en prijs, en klanten accepteren online een PDF-offerte. Toen verhoogde hij zijn prijzen - en klanten die een al geaccepteerde offerte opnieuw openden, zagen ineens de nieuwe prijzen. Eén factuur kwam niet overeen met de offerte die de klant had ondertekend. 😳

De klant tekende voor de ene prijs en kreeg een andere. Beide kwamen uit zijn app, en beide waren "correct" op het moment dat ze werden gegenereerd. Dit is waarom:

❌ PDF's die elke keer bij het downloaden opnieuw werden gegenereerd uit de actuele prijstabellen
❌ Factuurnummers uit een teller in de browser - twee facturen deelden een nummer
❌ Geaccepteerde offertes en uitgegeven facturen nooit bevroren als records
❌ Elke PDF opgeslagen in een openbare bucket

✅ Geaccepteerde offertes en uitgegeven facturen bevroren als onveranderlijke records
✅ Het genereren van PDF's verplaatst naar een edge function die elk document één keer rendert
✅ Factuurnummers toegekend via een sequence in de database
✅ Documenten verplaatst naar privéopslag met ondertekende links, plus creditnota's voor correcties

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar document- en factureersystemen, behandelen we facturen als records, niet als weergaven - genummerd in de database en alleen gecorrigeerd via creditnota's. 🛠️

💡 Het resultaat: €2.150, zeven werkdagen. Geschillen over veranderende prijzen stopten, de dubbele factuur werd gecorrigeerd met een creditnota, en zijn accountant accepteerde de nieuwe factuurreeks zonder opmerkingen. 🚀

👉 Genereert u facturen en offertes in uw AI-gebouwde app? Zo maakt u ze onveranderlijk, privé en conform: https://launchstudio.eu/nl/blog/how-do-i-generate-pdf-invoices-in-my-ai-built-app

#Facturatie #Bolt #Supabase #BTW #LaunchStudio #Manifera
