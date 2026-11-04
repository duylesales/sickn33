🚨 Elif Yilmaz runs two coworking spaces in Utrecht and built Werkplek030 with Bolt and Supabase: desk bookings, meeting rooms, day passes and team seats for about 180 members. Then she spotted something odd in Stripe: members on the "Team" plan who had never paid for it. 😳

The cause took minutes to find. The policy looked reasonable: users can edit their own profile. Nobody asked what was in the profile. 🧠

❌ An update policy on profiles - and the row contained plan and role
❌ Any member could set themselves to Team plan and admin with one API call
❌ RLS disabled on room_bookings, exposing every member's booking history
❌ Invoice PDFs in a public bucket, named by invoice number

✅ plan and role moved to a memberships table, writable only via a server function called by the Stripe webhook
✅ RLS on bookings with a company-membership policy
✅ Invoices in a private bucket with signed URLs
✅ Indexes for the new policies, every change written as a migration

At **LaunchStudio**, backed by Manifera's 11+ years of multi-tenant PostgreSQL work, an RLS audit compares what each policy allows with what your app intends - and proves it with real user accounts. 🛠️

💡 Her result: €2,100, seven business days. Unpaid upgrades stopped immediately, most lost revenue was recovered, and booking queries got faster than before. 🚀

👉 Using Supabase? Check your project against the seven RLS mistakes we find most: https://launchstudio.eu/en/blog/supabase-rls-audit-the-policy-mistakes-we-find-most

#Supabase #PostgreSQL #RowLevelSecurity #Bolt #LaunchStudio #Manifera
