🚨 Joost Hermsen built Montagebon in Lovable: digital work orders for installation companies. After an audit, his Row Level Security was fixed, keys were moved server-side and payments ran through webhooks. One week later, a customer reported seeing another company's work orders. 😳

The audit had fixed his app. One innocent prompt broke it again. Here's what happened: 🧠

❌ He asked Lovable to "make sure technicians can see work orders assigned by any planner"
❌ Lovable added a new policy giving every logged-in user read access to the work orders table
❌ Postgres combines permissive policies with OR - so that one policy overrode all the correct ones
❌ No rules, no review of migrations and no test to catch it before customers did

✅ The broad policy removed, and project rules added that forbid policy changes
✅ Technician assignment logic moved into a database function, out of reach of regenerated components
✅ A Playwright test checking cross-company visibility on every deployment
✅ A GitHub notification for any change in supabase/migrations

At **LaunchStudio**, backed by Manifera - whose founder Herre Roelevink comes from cybersecurity - we set up guardrails so you can keep prompting without undoing your security. 🛠️

💡 His result: €1,300, four business days. Joost kept building in Lovable; the automated test blocked one similar regression before deployment, and migration alerts flagged two more risky suggestions before he accepted them. 🚀

👉 Worried the next prompt will undo your security fixes? Here are the five guardrails that make them last: https://launchstudio.eu/en/blog/how-do-i-stop-lovable-prompts-from-breaking-security

#Lovable #Supabase #RLS #AppSecurity #LaunchStudio #Manifera
