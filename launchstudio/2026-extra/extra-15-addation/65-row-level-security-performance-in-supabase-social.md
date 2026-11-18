Would you rather have a helpdesk that's secure, or one that's fast? 🤔

Trick question. Lars Willemsen got both, but only after almost giving up the first one.

Lars built Servicedesk Lite with Lovable and Supabase: a helpdesk for small IT service providers whose engineers handle tickets for many client organisations. He followed security advice carefully and put policies on every table. Then one customer grew to around 400,000 tickets, and the ticket list took over six seconds to load, sometimes timing out.

The tempting answer came from a freelancer: switch the list to the service role key. Fast, yes. But it would have removed tenant isolation entirely.

The real reasons it was slow:
• The ticket policy joined tickets to client organisations, teams and team memberships to decide visibility
• auth.uid() was called inside that join without a subselect
• No indexes on the columns used in the join
• The memberships table had its own policy that queried memberships again, causing heavy recursive evaluation
• The frontend fetched tickets with no filters, sorted on an unindexed column

The "both" answer (LaunchStudio, 8 business days, €3,000):
1. Access tests for every role and table, first
2. organisation_id and team_id added directly to tickets and backfilled
3. Membership checked through a small security definer function in a private schema with a fixed search path
4. auth.uid() wrapped in subselects, and policies limited to the authenticated role
5. Composite indexes for team, status and update time
6. Matching filters and keyset pagination in the frontend
7. A simpler memberships policy, without recursion
8. The access tests run before and after every change

The result: the ticket list loads in about 200 milliseconds for the largest customer, with identical access rules proven by tests. Database CPU during office hours down around 60%. The service role shortcut was never needed.

"I thought I had to choose between secure and fast. It turned out my policies were secure and badly written, and they could be both." - Lars Willemsen

https://launchstudio.eu/en/blog/row-level-security-performance-in-supabase

#Supabase #RLS #Postgres #Performance #AIFounder #LaunchStudio #Manifera
