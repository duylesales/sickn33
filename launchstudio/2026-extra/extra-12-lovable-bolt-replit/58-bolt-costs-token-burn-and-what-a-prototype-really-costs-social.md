💳 STATEMENT: AI tool spend, Inruilwaarde

Month 1 ............................ €48
Month 4 ............................ €740
Was the product four times better? Not obviously.

WHERE MONTH 4 WENT
• No version control: two sessions that went wrong were rebuilt by hand, over several days
• Broad prompts ("make the valuation page better"), then six or seven turns correcting the result
• Labels and colours changed by prompting
• One mileage adjustment bug: three separate sessions across two weeks, never fixed

Lucas Verdonschot built Inruilwaarde with Bolt: used-car dealers estimate trade-in values from vehicle data and their own sales history. 14 dealers in Noord-Brabant use it. 🚙

That bug, once a person read it: twenty minutes. A rounding was applied twice, in two places. The tool kept fixing it in one file while reintroducing it in the other, because it only ever looked at one of them.

THE CORRECTION (LaunchStudio, 2 business days, €1,600)
✓ The project in a repository with history, so a bad session is reverted in seconds
✓ The mileage bug fixed
✓ 11 abandoned files and a half-built feature deleted, cutting the context carried on every request
✓ Data access gathered into one place, not spread across nineteen components
✓ A working agreement with himself: one specific request at a time, small edits by hand, a new session per area

NEW BALANCE
Monthly spend ...................... about €60
Held for ........................... four more months of development
Biggest saving, by Lucas's account ... version control
The real cost ...................... the three weeks lost to the mileage bug, more than the credits

"I spent three weeks and a lot of money asking a tool to fix a bug it could not see, because it was two lines in two different files and it only ever looked at one of them." - Lucas Verdonschot

https://launchstudio.eu/en/blog/bolt-costs-token-burn-and-what-a-prototype-really-costs

#Bolt #AIDevelopment #Startup #Budgeting #LaunchStudio #Manifera
