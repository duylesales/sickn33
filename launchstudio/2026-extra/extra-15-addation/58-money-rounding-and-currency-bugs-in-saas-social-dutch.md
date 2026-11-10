🚨 Esther Bakker bouwde Cateringbestel met Lovable, Supabase en Mollie: bedrijven bestellen lunch en catering bij lokale cateraars, met maandfacturen. Financiële afdelingen begonnen facturen af te wijzen omdat het btw-totaal niet klopte met de regels - en een cateraar kreeg maar een fractie van een grote bestelling betaald. 😳

De beheerder van een cateraar had een prijs ingevoerd als "1.250,00" - en parseFloat las 1.25. Dit zijn de afrondings- en valutabugs die SaaS-facturen breken: 🧠

❌ Prijzen als floating point-getallen, totalen berekend in de browser
❌ Btw per regel afgerond op het scherm, maar per totaal in de pdf
❌ Gemengde btw-tarieven verkeerd samengevoegd
❌ Nederlandse getalnotatie verkeerd gelezen, en terugbetalingen met drie decimalen afgewezen door Mollie

✅ Alle bedragen gemigreerd naar gehele centen met expliciete valuta
✅ Eén berekening aan de serverkant voor afrekenen, facturen en exports
✅ Btw per tariefgroep met één afrondingsstap, afgestemd met de accountant
✅ Invoer die de notatie herkent, bedragen in Mollie-formaat, idempotente terugbetalingen met creditnota's, en tests

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, laten we elke cent kloppen - zodat financiële afdelingen uw facturen blijven vertrouwen. 🛠️

💡 Het resultaat: €3.200, 9 werkdagen. Afgewezen facturen stopten binnen de eerste factuurcyclus, en de accountant krijgt nu exports die exact aansluiten op de Mollie-uitbetalingen. 🚀

👉 Kloppen uw facturen altijd? Dit zijn de geldbugs om te repareren: https://launchstudio.eu/nl/blog/money-rounding-and-currency-bugs-in-saas

#Invoicing #VAT #Mollie #FoodTech #AIFounder #LaunchStudio #Manifera
