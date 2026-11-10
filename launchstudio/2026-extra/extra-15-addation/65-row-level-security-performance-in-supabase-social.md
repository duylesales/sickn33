🚨 Lars Willemsen built Servicedesk Lite with Lovable and Supabase: a helpdesk for small IT service providers. He followed security advice carefully, with policies on every table. Then one customer reached around 400,000 tickets - and the ticket list took over six seconds and sometimes timed out. 😳

Under pressure, a freelancer suggested switching the list to the service role key. That would have removed tenant isolation entirely. Here's how to make Row Level Security fast in Supabase: 🧠

❌ A policy joining tickets, organisations, teams and memberships per row
❌ auth.uid() called inside the join without a subselect
❌ No indexes on joined columns, and a recursive memberships policy
❌ Unfiltered queries sorted on an unindexed column

✅ Access tests for every role and table first, before and after each change
✅ organisation_id and team_id added directly to tickets and backfilled
✅ A security definer helper in a private schema, auth.uid() in subselects
✅ Composite indexes, matching filters and keyset pagination

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we prove you don't have to choose between secure and fast. 🛠️

His result: €3,000, 8 business days. The ticket list loads in about 200 milliseconds with identical, tested access rules, and database CPU dropped by around 60% - no service role shortcut needed. 🚀

👉 Is RLS slowing down your Supabase app? Here's how to fix it: https://launchstudio.eu/en/blog/row-level-security-performance-in-supabase

#Supabase #RLS #Postgres #Performance #AIFounder #LaunchStudio #Manifera
