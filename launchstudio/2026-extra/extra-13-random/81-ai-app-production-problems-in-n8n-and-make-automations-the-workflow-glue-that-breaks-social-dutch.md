🚨 Sabine Kroes, mede-eigenaar van een schildersbedrijf in Heerhugowaard met veertien schilders, bouwde Schildersplanner in Lovable: klanten vragen offertes aan, kantoor plant klussen en schilders registreren uren op hun telefoon. Daarachter draaiden elf n8n-workflows — bevestigingen, facturen, een Google Sheet, betalingsherinneringen. Drie andere schildersbedrijven namen een licentie. Toen ontving één klant drie identieke facturen, en een ander geen enkele voor een klus die zes weken eerder af was. 😳

De factuurworkflow probeerde het bij time-outs opnieuw zonder te controleren of de factuur al bestond. De herinneringsworkflow werd vanuit de browser gestart via een openbare webhook zonder authenticatie. Meer dan 200 mislukte runs in twee maanden waarschuwden niemand. Elke workflow gebruikte de persoonlijke inloggegevens van Sabine, logs bewaarden klantadressen voor altijd op een abonnement met hosting in de VS, en de data van twee licentienemers liep door dezelfde workflows. Hier breken AI-apps in de lijm van n8n en Make:

❌ Herhaalde pogingen die dubbele facturen maken
❌ Openbare webhooktriggers die vanuit de browser worden aangeroepen
❌ Mislukte runs die niemand waarschuwen
❌ Persoonlijke inloggegevens en geen scheiding tussen klanten

✅ Het aanmaken van facturen verplaatst naar de backend met idempotentiesleutels en een registratie van uitgereikte facturen
✅ Alle webhooktriggers geauthenticeerd en vanaf de server aangeroepen, plus een foutworkflow die kantoor per e-mail en Slack waarschuwt
✅ Serviceaccounts van het bedrijf per licentienemer, n8n op een instance in de EU met logs die 14 dagen worden bewaard
✅ Workflows geëxporteerd naar Git met aparte testkopieën — en ontbrekende en dubbele facturen rechtgezet

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, beoordelen we het onzichtbare deel achter uw app voordat uw klanten het merken. ⚙️

💡 Het resultaat: € 1.900, zeven werkdagen. Dubbele en ontbrekende facturen stopten, storingen bereiken kantoor nu binnen minuten, en Sabine heeft er nog twee licentienemers bij. 🚀

👉 AI-App Productieproblemen in n8n en Make Automatiseringen: De Workflow-Lijm die Onzichtbaar Breekt: https://launchstudio.eu/nl/blog/ai-app-production-problems-in-n8n-and-make-automations-the-workflow-glue-that-breaks

#n8n #Make #Automatisering #Lovable #LaunchStudio #Manifera
