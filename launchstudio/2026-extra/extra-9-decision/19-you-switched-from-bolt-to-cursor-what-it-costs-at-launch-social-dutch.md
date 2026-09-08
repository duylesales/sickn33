🚨 Sem was twee weken lang bezig met het opsporen van een e-mailbezorgingsfout in Rittenboek. De export voor accountants werd in werkelijkheid überhaupt nooit gegenereerd. 😳

Tussentijds overstappen van Bolt naar Cursor is de juiste beslissing — maar het laat zeven soorten technisch puin achter waar geen van beide tools zich verantwoordelijk voor voelt: 🧠

❌ Een verouderde Netlify-deployment die nog altijd bouwde vanaf een oude branch, nog altijd verbonden met productie
❌ Twee RLS-policies verwezen naar een kolom die bij een latere refactor al van bereik was veranderd
❌ De exporttaak bevatte een unawaited async-aanroep, waardoor één op de vijftien exports nooit werd uitgevoerd
❌ Omgevingsvariabelen stonden verspreid over vier locaties, zonder enige overeenstemming

✅ Documenteer de herkomst van een geïmporteerde codebase — tool, datum, framework — als een papieren spoor
✅ Voer een audit uit bij elke hostingprovider op sites die nog aan uw repo gekoppeld zijn, verwijder ongebruikte
✅ Lees elke RLS-policy door tegen het huidige databaseschema in plaats van blind te vertrouwen op het bestaan ervan
✅ Een beknopt regelsbestand voorkomt dat het model twee tegenstrijdige conventies blijft combineren

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, ruimen we het puin van een tooloverstap grondig op zonder de onderliggende interface aan te raken. 🧹

Zijn resultaat: de verouderde deployment verwijderd, policies herschreven, de exporttaak verplaatst naar een echte wachtrij — vijf dagen werk, nul wijzigingen aan de interface, 240 betalende gebruikers. 🚀

👉 Ontdek hoe codebases met gemengde tools succesvol live gingen en stuur die van u door: https://launchstudio.eu/nl/blog/u-bent-tussentijds-overgestapt-van-bolt-naar-cursor-wat-dat-kost-bij-de-lancering

#IndieHacker #AICoding #LaunchStudio #Manifera #ProductionReady #StartupGrowth
