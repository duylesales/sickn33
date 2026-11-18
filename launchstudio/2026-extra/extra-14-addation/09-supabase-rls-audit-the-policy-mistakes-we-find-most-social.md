🎉 HOW TO UPGRADE YOURSELF TO THE TEAM PLAN FOR FREE (a guide nobody should be able to follow)

Step 1: Log in as a regular member.
Step 2: Send one API call updating your own profile: plan = "Team", role = "admin".
Step 3: Enjoy.

(This no longer works. But until LaunchStudio's audit, it did.)

Elif Yilmaz runs two coworking spaces in Utrecht and built Werkplek030 with Bolt and Supabase: members book desks and meeting rooms, buy day passes and manage their company's team seats. Around 180 members.

During a routine look at Stripe, Elif spotted several members on the Team plan who had never paid for it. The RLS audit found why in minutes. The profiles table had a perfectly reasonable-sounding policy: users can update their own row. But that row included plan and role.

The audit found two more things:
• room_bookings with RLS disabled, exposing every member's booking history
• Invoice PDFs in a public bucket, named by invoice number

The fix (LaunchStudio, 7 business days, €2,100):
✓ plan and role moved into a memberships table, writable only through a server-side function called by the Stripe webhook
✓ RLS enabled on bookings, with a company-membership policy
✓ Invoices moved to a private bucket with signed URLs
✓ Indexes added for the new policies
✓ Every change written as a migration in Elif's repository

Unpaid upgrades stopped immediately, and Elif recovered most of the lost revenue by contacting the members involved. Bonus: thanks to the new indexes, booking queries are faster than before.

"The policy looked reasonable: users can edit their own profile. Nobody asked what was in the profile." - Elif Yilmaz

https://launchstudio.eu/en/blog/supabase-rls-audit-the-policy-mistakes-we-find-most

#Supabase #PostgreSQL #RowLevelSecurity #Bolt #LaunchStudio #Manifera
