🚨 Lisa Brouwer runt een Shopify-winkel in duurzame babyproducten in Haarlem. Met Cursor bouwde zij Bundelbaas, een app voor productbundels met automatische voorraadafboeking. Tien winkeliers installeerden hem. Toen wees Shopify haar App Store-aanvraag af - twee keer. 😳

Eerst: betalingen liepen via Stripe in plaats van de Billing API. Daarna: compliance-webhooks deden niets en de installatieflow toonde een lege pagina. Een codereview vond meer. Dit is er nodig om een met AI gebouwde Shopify-app te lanceren: 🧠

❌ Webhookverificatie verwijderd nadat die bleef falen
❌ Negen toegangsscopes aangevraagd, vier gebruikt
❌ Toegangstokens van winkeliers onversleuteld opgeslagen
❌ Voorraadupdates die dubbel liepen bij webhook-retries

✅ Overgezet naar Shopify's officiële template met sessietokens
✅ Webhookverificatie hersteld, dubbele leveringen overgeslagen op webhook-ID, zwaar werk in een wachtrij
✅ Compliance-webhooks die data exporteren en verwijderen, scopes teruggebracht naar vier, tokens versleuteld
✅ Billing API met drie plannen en een gebruiksheffing, EU-hosting en een staging-app

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, maken we van de app die winkeliers willen een app die Shopify wil vermelden. 🛠️

💡 Het resultaat: €4.700, 14 werkdagen. Bundelbaas werd bij de derde aanvraag goedgekeurd, had binnen vier maanden zo'n 230 installaties en dubbele voorraadafboekingen verdwenen volledig. 🚀

👉 Een Shopify-app bouwen met AI? Zo komt u door de review en lanceert u: https://launchstudio.eu/nl/blog/building-a-shopify-app-with-ai-tools-review-billing-and-launch

#Shopify #ShopifyApps #Cursor #Ecommerce #AIFounder #LaunchStudio #Manifera
