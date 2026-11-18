🧮 A little Postgres logic

Policy A: technicians see work orders of their own company
OR
Policy B: all authenticated users can read all work orders
= everyone sees everything

Permissive policies combine with OR. Add one generous policy, and it outranks every careful one. 🔓

Joost Hermsen built Montagebon in Lovable: digital work orders for installation companies, where technicians record jobs, materials and customer signatures. After an audit, everything was fixed: Row Level Security, keys moved server-side, payments handled by webhooks.

One week later, a customer reported seeing another company's work orders.

Joost had asked Lovable to "make sure technicians can see work orders assigned by any planner." Lovable added Policy B, right next to the correct ones. One innocent prompt, and the audit was undone.

The guardrails LaunchStudio added (4 business days, €1,300):
✓ Policy B removed
✓ Project rules forbidding policy changes through prompts
✓ The technician assignment logic moved into a database function
✓ A Playwright test that checks cross-company visibility on every deployment
✓ A GitHub notification for any change in supabase/migrations

Joost kept building in Lovable. In the following months, the automated test blocked one similar regression before it was deployed. And the migration notifications let him catch two more risky suggestions before accepting them.

"The audit fixed my app. One innocent prompt broke it again. The guardrails are what made the fix last." - Joost Hermsen

https://launchstudio.eu/en/blog/how-do-i-stop-lovable-prompts-from-breaking-security

#Lovable #Supabase #RLS #AppSecurity #LaunchStudio #Manifera
