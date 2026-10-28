🚨 Noah Bos, zeilinstructeur in Den Helder, bouwde Getijdenwijzer in Bolt: getijden-, wind- en stromingsverwachtingen voor havens langs de Waddenzee en de Noordzeekust, met meldingen bij gunstige omstandigheden. Een vermelding in een zeilblad leverde in één voorjaarsmaand 6.000 gebruikers op. Dezelfde maand kwam zijn rekening voor de weer-API: ruim € 900. 😳

Elke keer dat iemand een havenpagina opende, riep de app direct de weer-API en de getijdendienst aan - dus een populaire haven die 20.000 keer per dag werd bekeken, veroorzaakte 20.000 identieke aanroepen voor data die elk uur veranderde. Op zonnige weekenden werd de rate limit van de getijdendienst bereikt. En een goedbedoelde versnelling had de persoonlijke pagina "mijn meldingen" op het CDN gecachet, waardoor sommige gebruikers kort de havens en het telefoonnummer van een andere zeiler zagen. Zo zit caching in elkaar, uitgelegd voor niet-technische oprichters:

❌ Twintigduizend keer per dag betalen voor dezelfde verwachting
❌ Rate-limitfouten op de drukste dagen
❌ Meldingsvoorwaarden bij elke paginaweergave opnieuw berekend
❌ Een persoonlijke pagina openbaar gecachet - een datalek

✅ Elk antwoord per gebruiker als privé gemarkeerd en het CDN gepurged - als eerste
✅ Havenverwachtingen op de server gecachet, met een vervaltijd passend bij het update-interval van elke bron
✅ Meldingsvoorwaarden vooraf berekend in een geplande taak
✅ CDN-caching met korte levensduur voor openbare havenpagina's, plus monitoring van API-gebruik en -kosten

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, cachen we wat gedeeld en duur is - en houden we wat persoonlijk is uit gedeelde caches. ⚙️

💡 Het resultaat: € 1.650, zes werkdagen. API-aanroepen daalden met zo'n 97%, de maandrekening zakte naar ongeveer € 40 terwijl het aantal gebruikers bleef groeien, en havenpagina's laden ruim binnen een seconde - ook op de eerste zonnige zaterdag van het seizoen. 🚀

👉 Schaalbaarheid van AI-Applicaties: Caching Uitgelegd voor Niet-Technische Oprichters: https://launchstudio.eu/nl/blog/ai-application-scalability-caching-explained-for-non-technical-founders

#Caching #Schaalbaarheid #APIkosten #Bolt #LaunchStudio #Manifera
