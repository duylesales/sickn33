🗺️ Where does a claim email travel? Follow the route.

Nadia Bouzid built Claimhulp with Cursor and Supabase: a tool for small insurance intermediaries that reads incoming claim emails and attachments, extracts the key facts and drafts a first response for the claims handler. In the pilot, it worked impressively.

THE ORIGINAL ROUTE
📧 A claim email with names, addresses, policy numbers, bank details and sometimes medical details about injuries
➜ sent in full, attachments included, as a prompt
➜ to a US AI API, on a plan whose data terms Nadia hadn't reviewed
➜ retention terms never checked
➜ the full prompt and response stored indefinitely in a logging tool

When a mid-sized Rotterdam intermediary wanted to roll it out, its compliance officer asked: where is this processed, is it used for training, how long is it kept, and which transfer mechanism applies? Nadia couldn't answer.

THE NEW ROUTE (LaunchStudio, 10 business days, €3,900)
📧 The claim email
➜ a preprocessing step swaps bank account numbers, policy numbers and contact details for placeholders, restored later in the draft
➜ medical attachments processed only with explicit opt-in per customer
➜ a European region of a cloud platform offering the same model family, under a processing agreement with no training use
➜ logs reduced to metadata, 30-day retention
➜ a provider abstraction, so the model can be swapped
➜ one page documenting data flow, location, retention and agreement

ARRIVAL
The compliance officer approved after one follow-up call, and Claimhulp went to 14 claims handlers. Draft quality stayed essentially the same. The one-page statement has since shortened sales talks with three more intermediaries.

"The model was never the problem. The problem was that I couldn't answer where my customers' claims data went. Now I can, in one page." - Nadia Bouzid

https://launchstudio.eu/en/blog/us-ai-apis-and-eu-data-transfers-what-founders-need-to-know

#AI #GDPR #DataTransfers #InsurTech #AIFounder #LaunchStudio #Manifera
