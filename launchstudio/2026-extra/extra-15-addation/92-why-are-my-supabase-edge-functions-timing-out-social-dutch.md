🚨 Joost van Leeuwen bouwde Huurcheck met Lovable en Supabase: vastgoedbeheerders uploaden bedrijfshuurcontracten, en een AI-model signaleert ongebruikelijke bepalingen, indexatie en opzegtermijnen. Pilots met korte contracten gingen goed. Toen uploadde één bedrijf 60 lange huurcontracten voor een jaarlijkse review. Bijna elke analyse gaf een timeout. 😳

Eén functie probeerde een dag werk in één adem te doen. Waarom Supabase Edge Functions een timeout geven: 🧠

❌ Hele contracten in één request naar de AI, plus een tweede samenvattingscall, terwijl de gebruiker wachtte
❌ Lange contracten die de wall-clock-limiet overschreden
❌ Gescande pdf's die de tekstextractie over de CPU-limiet duwden
❌ Alle 60 bestanden in één functieaanroep doorlopen, zodat één fout de rest stopte

✅ Eén taak per contract, met uploads die direct antwoorden
✅ Een wachtrij met extractie als aparte stap
✅ Contracten opgesplitst in secties die parallel worden geanalyseerd met timeouts en retries, daarna samengevoegd
✅ Een aparte OCR-dienst, voortgang per contract, e-mail bij afronding en handmatige review na twee retries

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, geven we zwaar werk de juiste vorm - zodat het saai en betrouwbaar wordt. 🛠️

💡 Het resultaat: €3.200, 9 werkdagen. De batch van 60 contracten was in zo'n 25 minuten klaar zonder één timeout, batches tot 300 draaien betrouwbaar, en twee pilotbedrijven werden betalende klanten op jaarbasis. 🚀

👉 Geven uw Edge Functions een timeout? Dit zijn de limieten en oplossingen: https://launchstudio.eu/nl/blog/why-are-my-supabase-edge-functions-timing-out

#Supabase #EdgeFunctions #AIEngineering #PropTech #AIFounder #LaunchStudio #Manifera
