🚨 Stijn Koster runs yoga studios in Deventer and built Lesrooster in Lovable: members book classes, teachers see attendance, members track their credits. It ran smoothly for a year with about 900 members. Then a partnership added two studios and 1,400 members - and Monday mornings became painful. 😳

Booking took eight to twelve seconds, some requests timed out, and Stijn was about to rebuild everything because "Lovable doesn't scale". It turned out to be three queries and one policy: 🧠

❌ A schedule page loading all classes, all bookings and every member's credits into the browser
❌ Filtering done locally instead of in the database
❌ No indexes on the bookings table beyond the primary key
❌ An RLS policy running a studio-membership subquery for every single row

✅ A database function returning only this week's classes and the member's own bookings
✅ Indexes on class date, studio and member
✅ The RLS policy rewritten with an indexed helper function
✅ Paginated class history and a load test simulating 300 members booking in five minutes

At **LaunchStudio**, backed by Manifera's 11+ years of optimising enterprise databases, we fix how your app queries data before anyone suggests a rebuild or a bigger plan. 🛠️

💡 His result: €1,900, six business days. Monday booking time dropped to under half a second, the Supabase plan stayed the same, and Lesrooster has since grown to six studios. 🚀

👉 Can a Lovable app handle real users? Here's where it scales and where it strains: https://launchstudio.eu/en/blog/can-a-lovable-app-handle-real-users

#Lovable #Supabase #Performance #Scaling #LaunchStudio #Manifera
