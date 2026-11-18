1 garden centre.
1 Lovable project.
7 copies, one for each new customer.
7 places to make every fix.
7 imports for every supplier price update.
Some copies weeks behind. 🌱

Koen Janssen managed a garden centre in Venlo and built Plantvoorraad with Lovable and Supabase to track stock, plant care schedules and supplier orders. Other garden centres saw it at a trade fair and wanted it. So Koen copied the project for each one, with a new Supabase project every time. By copy seven, that approach had stopped working.

The original app had no idea of tenants at all. Every table was shared by the users of one single garden centre.

The conversion (LaunchStudio, 18 business days, €6,800, plus €49/month):
1 organisation model, with owner, manager and staff roles
23 tables given an organisation column, each with its own RLS policy
Shared supplier catalogues, kept in shared tables with read-only access
Invitations, plus an organisation switcher for regional managers working across locations
1 Stripe subscription per organisation, priced by number of locations
7 databases merged into 1
4 rehearsals of the migration scripts, on copies, with a report of every record moved
1 isolation test suite checking every table and storage path
1 cutover, on a Sunday night

The new numbers:
7 garden centres logging in on Monday, all data intact
1 app to maintain
30 garden centres six months later, each onboarded in minutes with an invitation
1 supplier price import for all of them

"Copying the app felt like the quick solution. It was quick for one customer and impossible for thirty. Now a new customer is just a new organisation." - Koen Janssen

https://launchstudio.eu/en/blog/multi-tenant-saas-conversion-service

#SaaS #MultiTenant #Supabase #Lovable #AIFounder #LaunchStudio #Manifera
