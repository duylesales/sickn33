🚨 Hugo Verheij bouwde Intakehulp met Lovable en Supabase: het verwerkt nieuwe aanvragen voor kleine advocatenkantoren, haalt de feiten eruit, bepaalt het rechtsgebied en stelt een Nederlands antwoord op. Elke stap gebruikte hetzelfde grote model via een Amerikaans endpoint, aangeroepen vanuit vier edge functions met net iets andere code. 😳

De kosten waren hoog, antwoorden duurden soms meer dan twintig seconden en de privacyfunctionaris van een kantoor vroeg waar aanvragen werden verwerkt. Toen werd aangekondigd dat de modelversie zou verdwijnen. Zo kiest u een LLM API voor een EU-SaaS: 🧠

❌ Eén groot model voor elke taak
❌ Vier net verschillende implementaties van AI-calls
❌ Geen helder antwoord over verwerkingslocatie, bewaartermijn of overeenkomsten
❌ Geen manier om te testen of een nieuwer model zich hetzelfde gedroeg

✅ Een evaluatieset van 120 geanonimiseerde aanvragen met verwachte uitkomsten
✅ Een kleiner model voor classificatie en extractie, een groter voor het opstellen
✅ Eén provider-abstractie met configuratie per taak, schemavalidatie, retries en kostenlogging
✅ Verwerking in EU-regio's zonder training op data, plus een fallbackmodel voor het opstellen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, maken we van de mogelijkheid om van model te wisselen uw echte troef. 🛠️

💡 Het resultaat: €4.800, 12 werkdagen. De AI-kosten per aanvraag daalden met zo'n 70%, de verwerkingstijd ging van ongeveer 18 naar 5 seconden en het uitfaseren van het model was in een middag geregeld. 🚀

👉 OpenAI, Anthropic of Mistral voor uw EU-SaaS? Zo kiest u: https://launchstudio.eu/nl/blog/choosing-an-llm-api-for-an-eu-saas-openai-anthropic-or-mistral

#LLM #AIEngineering #GDPR #LegalTech #AIFounder #LaunchStudio #Manifera
