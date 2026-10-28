🚨 Tim de Graaf, softwaretester in Breda, bouwde Gereedschapdelen op Replit: buren verhuren elkaar heggenscharen, tegelsnijders en tapijtreinigers per dag, met een borg. Drie wijken, 600 gebruikers, zo'n 150 verhuringen per maand. En op elk moment had Tim ongeveer € 2.000 van anderen op zijn persoonlijke Stripe-account staan. 😳

Hij betaalde uitleners wekelijks uit vanuit een spreadsheet. Borgsommen werden volledig afgeschreven en met de hand teruggestort, soms dagen te laat. Twee huurders boekten regelmatig hetzelfde gereedschap voor dezelfde dag. Iedereen kon reviews plaatsen - één uitlener werd door een ontevreden buurman overspoeld met nepreviews - en geschorste gebruikers konden nog boeken. Dit gaat er mis als een AI-marktplaats echte kopers en verkopers ontmoet:

❌ Geld van de marktplaats via de eigen rekening van de oprichter
❌ Volledige borgafschrijvingen met handmatige terugbetalingen
❌ Beschikbaarheid gecontroleerd in code, niet afgedwongen in de database
❌ Open reviews en schorsingen die alleen een profiel verborgen

✅ Stripe Connect met onboarding van uitleners en automatische uitbetalingen na de retourdatum
✅ Kaartautorisaties in plaats van borgafschrijvingen, vrijgegeven bij terugbrengen
✅ Een exclusion constraint op gereedschap en datumbereik, met een reservering van 15 minuten bij de checkout
✅ Reviews alleen na voltooide verhuur, schorsing die transacties blokkeert, zoeken op de server met PostGIS, commissiefacturen en rapportagedata over verkopers

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, maken we van een marktplaatsdemo een platform dat vreemden kunnen vertrouwen. ⚙️

💡 Het resultaat: € 5.200, zestien werkdagen. Gereedschapdelen breidde uit over de hele stad en ging voorbij de 400 verhuringen per maand. Dubbele boekingen stopten, Tim beheert geen geld van uitleners meer, en hij bespaart zo'n zes uur per week op uitbetalingen en terugbetalingen. 🚀

👉 AI-Marktplaats-App naar Productie: Wat Er Misgaat met Echte Kopers en Verkopers: https://launchstudio.eu/nl/blog/ai-marketplace-app-to-production-what-breaks-with-real-buyers-and-sellers

#Marktplaats #StripeConnect #Replit #Breda #LaunchStudio #Manifera
