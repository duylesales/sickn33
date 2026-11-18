A hotel manager mentioned it, almost in passing: by changing a filter, he could see what another hotel chain paid. 🏨

Karin Wouters runs a family-owned wholesaler of hospitality supplies in Roosendaal. She built Bestelportaal with Lovable and Supabase, where around 300 restaurants and hotels reorder products, see their customer-specific prices and download invoices synced from Exact Online. Customers loved it so much that phone orders dropped within weeks.

Three lessons from what happened next.

LESSON 1: A filter in the interface is not a lock.
Prices and invoices were filtered by customer only on screen.
➜ Company separation enforced with Row Level Security on prices, orders and invoices, with isolation tests.

LESSON 2: Files and tokens need the same care as data.
Invoice PDFs sat in a public bucket with predictable names, and the Exact Online sync token was readable in a client-side function.
➜ Invoices in private storage, with signed links that expire after a few minutes and logged downloads. The sync moved to a scheduled server function, with a rotated, scoped token, the time of the last successful sync on screen, and alerts on failure.

LESSON 3: Not everyone at a customer needs everything.
Every user saw everything, including kitchen staff who only reorder.
➜ Customer roles for administrators, buyers and finance, with customer administrators managing their own staff.

Bonus fix: order submission made idempotent, so a double click no longer creates two orders.

All of it took 8 business days, for €3,200. After release, no customer could see another's prices or invoices, which Karin confirmed with the hotel manager who first noticed. Portal orders kept growing, and customer admins now add and remove their own staff without calling.

"The portal saved my sales team hours every day. It also very nearly told my customers what everyone else was paying. Now it does only the first." - Karin Wouters

https://launchstudio.eu/en/blog/production-launch-for-b2b-customer-portals

#CustomerPortal #B2B #ExactOnline #Lovable #AIFounder #LaunchStudio #Manifera
