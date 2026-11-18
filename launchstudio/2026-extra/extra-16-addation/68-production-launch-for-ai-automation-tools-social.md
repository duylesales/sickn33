🏭 One worker doing everything, or an assembly line?

THE ONE-WORKER VERSION
Bonbot, built by Stijn Kuijpers in Venlo with Cursor and Supabase, reads purchase invoices from a customer's inbox, extracts supplier, amounts and VAT, and books them in Moneybird or Exact Online. Around 40 small bookkeeping firms signed up in the first months. Everything ran inside one web request, triggered by a scheduled call.

As volumes grew:
💥 Large batches timed out and started again, booking some invoices twice
💥 When Moneybird returned rate limit errors, the run just stopped, silently
💥 Expired Gmail tokens quietly stopped some customers' automations
💥 The AI step received full email threads, signatures and unrelated messages included
💥 One heavy customer drove a big share of AI costs
💥 Every customer's tokens sat unencrypted in one table

THE ASSEMBLY LINE (LaunchStudio, Launch & Grow, 16 business days, €6,200, plus €49/month)
STATION 1: A queue with workers, retries with backoff and a dead-letter list
STATION 2: A stable key per invoice, from the message and attachment, plus the external booking ID stored, so a retry never books twice
STATION 3: Throttling that respects each accounting system's limits
STATION 4: Tokens encrypted and refreshed automatically, with a reconnect prompt when access expires
STATION 5: The AI receives only the invoice attachment, a smaller model for simple invoices, a larger one for difficult ones
QUALITY CONTROL: Results below a confidence threshold go to a review queue
DISPATCH: A run history showing bookkeepers what happened to every invoice, and costs per customer tracked against plan limits

Duplicate bookings stopped completely. The review queue caught most extraction errors before they reached the books. AI cost per invoice fell substantially. And Bonbot grew to around 120 firms without new incidents.

"Booking an invoice once is a feature. Booking it twice is a reason to cancel. Now every invoice has a key, and every retry knows what already happened." - Stijn Kuijpers

https://launchstudio.eu/en/blog/production-launch-for-ai-automation-tools

#Automation #AI #Moneybird #Supabase #AIFounder #LaunchStudio #Manifera
