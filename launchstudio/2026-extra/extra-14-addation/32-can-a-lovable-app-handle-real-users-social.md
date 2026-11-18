MYTH: "Lovable doesn't scale. Time to rebuild."
FACT: It was three queries and one policy. 🧘

Stijn Koster runs three yoga studios in Deventer and built Lesrooster in Lovable: members book classes, teachers see attendance, members see their class history and remaining credits. It worked well for a year with about 900 members. Then a partnership added two studios and 1,400 members. Monday mornings, when everyone books the week's classes, became painful: eight to twelve seconds per booking, and some requests timing out.

Stijn was about to rebuild everything.

MYTH: "More members means a bigger database plan."
FACT: The schedule page fetched every class, every booking and every member's credits into the browser, then filtered there. The work was in the wrong place, not too big.

MYTH: "Databases are fast by default."
FACT: The bookings table had no indexes beyond its primary key.

MYTH: "Security policies don't affect speed."
FACT: The RLS policy on bookings checked studio membership with a subquery for every single row.

What LaunchStudio changed (6 business days, €1,900):
✓ A database function returning only the week's classes and the member's own bookings
✓ Indexes on class date, studio and member
✓ The RLS policy rewritten with an indexed helper function
✓ Paginated class history
✓ A load test simulating 300 members booking within five minutes

Booking on Monday mornings now takes under half a second. Same Supabase plan. Lesrooster has since grown to six studios without any further performance work.

"I was about to rebuild the whole thing because 'Lovable doesn't scale'. It was three queries and one policy." - Stijn Koster

https://launchstudio.eu/en/blog/can-a-lovable-app-handle-real-users

#Lovable #Supabase #Performance #Scaling #LaunchStudio #Manifera
