A restaurant owner mentioned it casually: he'd noticed a competitor got a better price on cod. 🐟

In fish wholesale, that's not small talk. That's the business.

Thijs Visser runs sales for a family fish wholesaler in IJmuiden that supplies around 300 restaurants and fishmongers. He built Visbestel with Lovable and Supabase so customers could order online instead of calling the order desk before dawn. Within two months, a third of orders came through the portal.

Three lessons from what happened next.

LESSON 1: Hiding data in the interface doesn't hide it.
Prices sat in one table with customer IDs, readable by any logged-in customer through the API. Only the interface filtered them.
➜ Prices now come from a server-side function that calculates each customer's effective prices from price lists, agreements and daily market prices. Row Level Security blocks direct access to the tables. This was closed the same day.

LESSON 2: A nightly export is too slow for a 04:00 picking run.
Late corrections got lost, and some orders reached the warehouse too late.
➜ Orders now go to the ERP immediately, through a queue with retries and idempotent submission, with alerts if the ERP doesn't acknowledge.

LESSON 3: Rules on screen aren't rules.
Cut-off times were displayed but not enforced. Credit limits weren't checked. Chain restaurants shared one login, so the desk still retyped orders.
➜ Cut-off times and delivery days per route enforced, credit limits checked against balances synced from the ERP, users per location for chains with approval above a threshold, plus reorder lists from the last eight weeks and quick ordering by article number.

The full rebuild: 19 business days, €7,400. Next quarter, portal orders rose to around 70% of volume, retyping almost vanished, and late orders missing the picking run dropped to nearly zero.

"In fish wholesale, your price agreements are your business. Customers seeing each other's prices could have cost us more than any software ever saves." - Thijs Visser

https://launchstudio.eu/en/blog/b2b-wholesale-ordering-portal-built-with-ai

#B2BEcommerce #Wholesale #ERP #FoodIndustry #AIFounder #LaunchStudio #Manifera
