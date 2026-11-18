🧮 The math that didn't work

€79 per month
− 200+ hours of meetings transcribed and summarised per month
= a customer who costs several times what they pay

Julia van Leeuwen built Notulist with Cursor and Supabase: it transcribes and summarises meetings for municipalities, housing associations and consultancies, on one flat €79 plan. Customers loved it. Three of them, a large municipality and two consultancies, each used it for over 200 hours a month. Her AI provider's invoice told the rest of the story.

Capping usage would have risked losing her best customers. Usage-based pricing made more sense, but there was no reliable usage data to price on:
• Transcription jobs weren't recorded consistently
• Failed jobs were sometimes retried and processed twice
• Customers couldn't see how much they had used

The new math (LaunchStudio, 13 business days, €5,400):

base subscription with included hours
+ metered overage per extra hour, through a Stripe meter
+ a usage ledger recording each completed transcription with duration, customer and job ID
+ usage events sent from a backend queue, with the job ID as identifier, so retries never count twice
+ a usage page with a monthly projection
+ email alerts at 80% and 100% of included hours
+ an optional spending cap
+ monthly reconciliation of the ledger, Stripe invoices and AI provider costs
= fair pricing customers can check for themselves

THE RESULT
All three heavy users accepted the new pricing after seeing their usage pages. Two moved to bigger plans. Gross margin on AI features went from negative for heavy users to healthy on every plan. Disputed usage charges: none.

"My best customers were my most expensive ones. Showing them exactly what they used made the conversation about fair pricing easy." - Julia van Leeuwen

https://launchstudio.eu/en/blog/usage-based-billing-for-ai-features-with-stripe-meters

#Stripe #UsageBasedPricing #AISaaS #GovTech #AIFounder #LaunchStudio #Manifera
