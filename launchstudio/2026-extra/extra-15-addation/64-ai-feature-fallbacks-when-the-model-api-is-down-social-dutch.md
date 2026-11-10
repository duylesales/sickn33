🚨 Maarten Oosterhuis bouwde Bonnetjesbot met Bolt en Supabase: medewerkers fotograferen bonnetjes en AI haalt leverancier, datum, bedrag en btw eruit. Het gebruik piekte op maandagochtend. Op meerdere maandagen beperkte de provider het account - en één keer was er een gedeeltelijke storing van twee uur. 😳

Elke keer faalden uploads, moesten medewerkers later opnieuw foto's maken en haakten sommigen af. Support hoorde het van klanten. Zo bouwt u fallbacks voor AI-functies voor als de model-API plat ligt: 🧠

❌ Het model synchroon aangeroepen tijdens de upload, zonder timeout
❌ Geen retries en geen alternatieve provider
❌ Mislukte extracties die de geüploade afbeelding weggooiden
❌ Geen overzicht van wachtende bonnetjes, en geen meldingen

✅ Bonnetjes direct opgeslagen in privé-opslag, extractie via een wachtrij
✅ Timeouts, exponential backoff met jitter en respect voor rate-limitheaders
✅ Een circuit breaker die overschakelt naar een tweede model met verwerking in de EU, en taken die wachten op herstel
✅ Schemavalidatie, vooraf ingevulde handmatige invoer, status per bonnetje en monitoringmeldingen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, laten we de wachtrij de pieken opvangen en de fallback de storingen. 🛠️

💡 Het resultaat: €3.500, 9 werkdagen. Bij de volgende rate-limitpiek op maandag merkten medewerkers niets behalve een minuut vertraging. Het kwartaal daarna ging geen enkel bonnetje verloren en tickets over uploads daalden naar nul. 🚀

👉 Wat gebeurt er als uw AI-provider uitvalt? Zo bouwt u fallbacks: https://launchstudio.eu/nl/blog/ai-feature-fallbacks-when-the-model-api-is-down

#AIReliability #LLM #Resilience #FinTech #AIFounder #LaunchStudio #Manifera
