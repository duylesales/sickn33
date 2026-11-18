Submission #1: ❌ Rejected
Submission #2: ❌ Rejected
Submission #3: ✅ Approved

Here's what changed between them. 🛍️

Lisa Brouwer ran a Shopify store for sustainable baby products in Haarlem and wanted a better way to sell bundles, with stock deducted automatically for each component. She built Bundelbaas with Cursor, starting from a tutorial instead of the official template. Ten merchants she knew installed it as a custom app.

SUBMISSION #1
Rejected: charges ran through Stripe instead of Shopify's Billing API.

SUBMISSION #2
Rejected: the compliance webhooks returned success without doing anything, and the install flow showed a blank page for several seconds.

WHAT THE CODE REVIEW ADDED
• Webhook verification had been removed after it kept failing
• The app requested nine access scopes but used four
• Merchants' access tokens were stored unencrypted
• Stock updates sometimes ran twice when Shopify retried a webhook

BEFORE SUBMISSION #3 (LaunchStudio, 14 business days, €4,700)
→ Moved onto Shopify's official template, bundle logic carried across, session token handling instead of custom OAuth
→ Webhook verification restored on the raw body, duplicates skipped by webhook ID, heavy work in a background queue
→ Compliance webhooks that really export and delete data
→ Scopes cut to four, tokens encrypted at rest
→ Billing API with three plans and a usage charge for large catalogues
→ EU hosting, monitoring and a staging app

SUBMISSION #3
Approved, 14 business days after the first call. Within four months: around 230 installs, and no more duplicate stock deductions.

"Cursor helped me build the features merchants wanted. LaunchStudio made it the kind of app Shopify was willing to list." - Lisa Brouwer

https://launchstudio.eu/en/blog/building-a-shopify-app-with-ai-tools-review-billing-and-launch

#Shopify #ShopifyApps #Cursor #Ecommerce #AIFounder #LaunchStudio #Manifera
