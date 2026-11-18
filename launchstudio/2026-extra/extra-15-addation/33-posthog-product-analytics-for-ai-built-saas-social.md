GROUP A: companies that uploaded their own materials price list in the first session.
GROUP B: companies that didn't.

Group A converted to paid at about four times the rate of Group B. 📈

That one insight took Offertemaker's trial-to-paid conversion from around 9% to 17%. But first, Bram Willems had to be able to see it.

Bram built Offertemaker with Lovable and Supabase: installers and contractors create professional quotes with materials, labour and photos, then send them for digital approval. Sign-ups grew through LinkedIn, but most trial users never paid, and website page views couldn't tell him why.

Lovable had added PostHog with autocapture when he asked. The result:
• Thousands of events named after CSS classes
• No way to look at companies instead of individual users
• Session replays showing clients' names, addresses and prices unmasked
• No payment events, because payments happened in a Mollie webhook
• The US cloud with cookie persistence, and no consent banner

What LaunchStudio set up (6 business days, €1,950):
→ An event plan of nine events, with one activation definition: "first quote sent to a client"
→ Autocapture off, explicit events in the frontend
→ Payment and subscription events sent from the Mollie webhook handler
→ Users identified by internal ID and grouped by company
→ PostHog EU cloud with memory persistence
→ Replays masking all inputs and skipping quote detail pages, plus inputs for the privacy policy

Within a month, the Group A vs Group B pattern was obvious. Bram rebuilt onboarding around a price list import, and conversion nearly doubled over the next quarter.

"I had analytics, but I didn't have answers. Once we tracked the right nine things, the answer was obvious within weeks." - Bram Willems

What does your Group A do differently? https://launchstudio.eu/en/blog/posthog-product-analytics-for-ai-built-saas

#PostHog #ProductAnalytics #SaaS #Growth #AIFounder #LaunchStudio #Manifera
