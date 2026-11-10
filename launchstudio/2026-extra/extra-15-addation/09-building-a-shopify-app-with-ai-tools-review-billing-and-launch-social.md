🚨 Lisa Brouwer runs a Shopify store for sustainable baby products in Haarlem. With Cursor she built Bundelbaas, an app for product bundles with automatic stock deduction. Ten merchants installed it. Then Shopify rejected her App Store submission - twice. 😳

First: charges ran through Stripe instead of the Billing API. Second: compliance webhooks did nothing and the install flow showed a blank page. A code review found more underneath. Here's what it takes to launch a Shopify app built with AI tools: 🧠

❌ Webhook verification removed after it kept failing
❌ Nine access scopes requested, four used
❌ Merchants' access tokens stored unencrypted
❌ Stock updates running twice on webhook retries

✅ Moved onto Shopify's official template with session token handling
✅ Webhook verification restored, duplicates skipped by webhook ID, heavy work queued
✅ Compliance webhooks that export and delete data, scopes cut to four, tokens encrypted
✅ Billing API with three plans and a usage charge, EU hosting and a staging app

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we turn the app merchants want into one Shopify is willing to list. 🛠️

Her result: €4,700, 14 business days. Bundelbaas passed review on the third submission, reached around 230 installs within four months, and duplicate stock deductions disappeared entirely. 🚀

👉 Building a Shopify app with AI? Here's how to pass review and launch: https://launchstudio.eu/en/blog/building-a-shopify-app-with-ai-tools-review-billing-and-launch

#Shopify #ShopifyApps #Cursor #Ecommerce #AIFounder #LaunchStudio #Manifera
