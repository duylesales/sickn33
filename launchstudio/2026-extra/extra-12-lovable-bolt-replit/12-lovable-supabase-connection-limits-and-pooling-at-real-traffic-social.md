MYTH: "The product breaks every Monday, so I need a bigger database."
FACT: Nine users and one line in the wrong place. 🏛️

Thijs Kranenburg built Zaalplanner in Lovable: booking software for community centres and village halls, 48 venues across Friesland and Groningen, each with a handful of staff. Every Monday morning, it broke completely. Database errors on every page, for ten to twenty minutes, then recovery on its own. Monday morning is when venue managers do the week's bookings. Two venues were already asking about alternatives. Thijs was about to upgrade his plan for €300 a month.

MYTH: "60 connections should be plenty for nine people."
FACT: The app created a new database client inside each serverless function call. Every request opened a connection and left it to expire. Nine or ten managers, each loading pages making four or five requests, used up the limit in minutes.

MYTH: "Waiting on an email inside a transaction is harmless."
FACT: During one email provider outage, two such transactions held connections open for ninety seconds each.

MYTH: "A realtime calendar subscribes once."
FACT: It subscribed again on every render.

What LaunchStudio changed (1 business day, €1,450):
✓ The database client moved to module scope, so each function instance reuses one connection
✓ Every application connection string on the pooled port, with the direct connection kept for migrations
✓ Pool size set explicitly, not left at the library default
✓ The email calls taken out of the two transactions
✓ The calendar subscription fixed to subscribe once
✓ A dashboard alert at 70% of the connection limit
✓ A load test at 120 concurrent users, to confirm the fix instead of assuming it

Monday mornings stopped failing. Peak connection use went from the 60-connection ceiling to a steady 7. And the load test cleared 120 concurrent users, more than double Thijs's realistic peak, on the plan he'd been about to upgrade.

"I was convinced I needed a bigger database. The whole problem was one line in the wrong place, creating a connection for every request and never giving it back." - Thijs Kranenburg

https://launchstudio.eu/en/blog/lovable-supabase-connection-limits-and-pooling-at-real-traffic

#Supabase #PostgreSQL #Serverless #Lovable #LaunchStudio #Manifera
