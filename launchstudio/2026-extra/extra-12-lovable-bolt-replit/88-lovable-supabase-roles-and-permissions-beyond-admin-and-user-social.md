🔐 Three roles, one workaround, and a problem nobody saw

THE OLD GRID
                    edit schedules   approve hours   see all wages
Owner               ✓                ✓               ✓
Admin               ✓                ✓ (incl. own)   ✓ (every location)
Member              ✗                ✗               ✗

Location managers needed the first two columns. Only Admin had them. So every location manager became an Admin, and got the third column too.

Marloes Teunissen built Horecarooster in Lovable: staff scheduling and hour registration for 27 hospitality groups, 140 locations, around 3,800 staff. 🍷

In one week:
• A group's finance director saw overtime rising at one location while revenue didn't. The manager had been approving his own extra hours.
• A 34-location group declined to sign, because managers would see wages across the whole group.

THE NEW GRID (excerpt; 24 permissions × 6 roles in full)
                    hours.approve        wages.read
Owner               ✓                    ✓
Location manager    ✓ own location,      ✗
                    never own hours
Staff               ✗                    ✗

Building it (LaunchStudio, 4 business days, €4,800):
✓ 24 permission codes taken from checks already scattered through the code
✓ Six roles (Owner, Administrator, Location manager, Planner, Staff, Read-only), first reproducing existing behaviour
✓ Role assignments with an optional location scope, backfilled from the old role column
✓ Row level security on 19 tables rewritten around an indexed has_permission helper
✓ Wages in a separate compensation table, readable only with wages.read
✓ Approvals checking hours.approve for the location, and refusing anyone approving hours they submitted
✓ No granting permissions you don't hold yourself
✓ The matrix kept as data, generating 288 tests in CI
✓ A role-change audit for each group's administrators

A review of past approvals found three managers in two groups who'd approved their own overtime, €4,100 in total, which the groups recovered. The 34-location group signed within the month, and a similar-sized group followed: 61 locations added between them.

"We made every location manager an admin because it was the only role that could approve hours. That also let them see everyone's wages and approve their own overtime." - Marloes Teunissen

https://launchstudio.eu/en/blog/lovable-supabase-roles-and-permissions-beyond-admin-and-user

#Supabase #AccessControl #SaaS #AppSecurity #LaunchStudio #Manifera
