🚗 Pim Hendriks runt vanuit Apeldoorn een SaaS voor rijinstructeurs, in tien maanden gebouwd met Lovable en Supabase en gebruikt door zo'n 150 instructeurs voor lesplanning, de voortgang van leerlingen en betalingen via Mollie. Na een reeks bugs beoordeelde een bureau de app en stelde een volledige herbouw in een ander framework voor: zo'n €24.000 en vier maanden, met de code als "ononderhoudbare AI-output". Pim vroeg LaunchStudio om een second opinion. 🔍

De beoordeling vond dat het datamodel goed bij het bedrijf paste. De echte problemen: 🧠

❌ Losse policies waardoor instructeurs elkaars leerlingen konden zien
❌ Betalingen bevestigd bij de doorverwijzing
❌ Drie gedupliceerde versies van de lesagenda
❌ Ontbrekende indexen, geen staging en een rapportagemodule die alles in de browser berekende

Geen van deze vroeg om een herbouw: ✅

✅ Policies herschreven met tests
✅ Betalingen overgezet op geverifieerde webhooks met afstemming
✅ De agenda samengevoegd tot één component, plus indexen, staging en monitoring
✅ Alleen de rapportagemodule opnieuw gebouwd met query's aan de serverkant, met een ongewijzigde interface voor instructeurs

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met zowel het bouwen van nieuwe software als het verbeteren van bestaande systemen voor klanten zoals Vodafone en TNO, vertellen we u eerlijk of uw app opnieuw moet worden gebouwd. 🛠️

💡 Het resultaat: €3.300, negen werkdagen. Het aantal bugmeldingen daalde sterk, rapportages werden direct en Pim bleef bouwen in Lovable, met een geschatte besparing van €20.000 en vier maanden. 🚀

👉 Moet mijn app gebouwd met AI opnieuw worden gebouwd? Een eerlijke beoordeling: https://launchstudio.eu/nl/blog/does-my-ai-built-app-need-a-rebuild-an-honest-assessment

#Herbouw #Refactoren #Lovable #VibeCoding #AIFounder #LaunchStudio #Manifera
