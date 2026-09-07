🕵️‍♂️ Een sollicitant uploadt een CV met onzichtbare witte tekst... en uw AI-tool zet hem direct op de shortlist voor de directie.

Dit heet **Indirect Prompt Injection**, en het is het gevaarlijkste beveiligingslek in moderne AI-applicaties.

Waarom?
Omdat een taalmodel instructies en gebruikersdata **niet** van elkaar kan onderscheiden:
Voor het model is álles platte tekst.

De 4 gevaarlijkste misvattingen over AI-security:
❌ **"We filteren foute woorden":** Aanvallers omzeilen trefwoordfilters moeiteloos via synoniemen of base64
❌ **"We instrueren het model om niet te luisteren":** Een model strikt toespreken verlaagt het risico, maar biedt 0% garantie
❌ **Het model schrijfbevoegdheden geven:** Een gekaapt model dat zelfstandig de database aanpast of e-mails verstuurt
❌ **Geheimen in de systeemprompt:** API-keys of regels in de prompt zetten ➔ ze liggen binnen 5 minuten op straat

Hoe u uw software wél beschermt tegen prompt injection:
✅ **Geef het model minimale rechten:** Nooit meer database-toegang dan de ingelogde gebruiker zélf heeft
✅ **Dwing menselijke bevestiging af:** Laat het model een concept maken, maar laat de mens klikken
✅ **Isoleer externe documenten:** Markeer PDF's en mails expliciet als `<untrusted_data>`
✅ **Strikte JSON-schema validatie:** Laat gemanipuleerde antwoorden direct stuklopen op de server

Bij **LaunchStudio**, ondersteund door Manifera (11+ jaar ervaring), voeren we AI-security audits uit en ontwerpen we veilige RAG-architecturen.

💡 Zo ontdekte Pim de Rooij van Sollicitatiebox dat kandidaten hun eigen sollicitatie manipuleerden via witte tekst in PDF-cv's. Binnen 4 dagen isoleerden we de prompt-pijplijn en elimineerden we automatische schrijfbevoegdheden.

👉 Weet u 100% zeker dat een kwaadaardige PDF uw AI-model morgen niet kaapt? [Link naar artikel]

#AISecurity #PromptInjection #CyberSecurity #SaaS #GenerativeAI #LaunchStudio #Manifera
