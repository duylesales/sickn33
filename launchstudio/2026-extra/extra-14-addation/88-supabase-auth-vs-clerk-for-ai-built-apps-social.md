🔀 A fork in the road for a B2B quote tool

Tim Schouten built Offertetracker in v0 with Supabase: a quote pipeline for sales teams at installation companies. Customers asked for three things: team invitations, roles, and Microsoft login for their staff.

ROAD A: Add Clerk
Its organisation features looked complete. Tim started integrating it, and got stuck. Every RLS policy used Supabase user IDs. Half his tables referenced auth.users. Road A meant migrating users, rewriting policies and adding a vendor.

ROAD B: Stay with Supabase Auth
His policies already understood it. And his customers, Dutch companies, preferred fewer processors.

LaunchStudio compared both with Tim. Road B won.

What Road B looked like (10 business days, €3,800):
✓ Microsoft (Azure) login
✓ Organisations, memberships and invitations with expiring tokens
✓ Owner, manager and sales roles, enforced in RLS
✓ MFA for managers

THE DESTINATION
Team features delivered in two weeks. No user migration. No extra vendor. And the processor list Tim shares with customers stayed short.

"Clerk looked like the fast route. Staying with what my database already understood turned out to be faster." - Tim Schouten

https://launchstudio.eu/en/blog/supabase-auth-vs-clerk-for-ai-built-apps

#Supabase #Clerk #Authentication #B2B #LaunchStudio #Manifera
