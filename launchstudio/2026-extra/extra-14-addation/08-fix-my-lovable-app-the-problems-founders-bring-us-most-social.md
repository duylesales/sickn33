🔍 CASE FILE: The Friday Vanishing

THE CLIENT
Tim Verbeek, Delft. Runs a cargo bike rental shop, and built Fietsdeel in Lovable so customers can reserve bikes online and staff can manage pickups. Two good months.

THE MYSTERY
Every Friday afternoon, the staff dashboard showed zero reservations. Customers kept getting confirmations.

THE WRONG LEADS
Tim prompted Lovable a dozen times. Each attempt changed the dashboard query. Twice, Lovable suggested making the reservations policy public "to fix the visibility issue." Three weeks went by.

THE CULPRIT
Not the dashboard at all. A scheduled cleanup function Lovable had added weeks earlier, which archived reservations once their pickup date had passed, using UTC instead of Dutch time. On Friday afternoons, the next day's early reservations landed on the wrong side of midnight and were archived before staff ever saw them.

AN ACCOMPLICE
The reservations table had a policy letting any logged-in customer list every reservation, names and phone numbers included.

THE RESOLUTION (LaunchStudio, 5 business days, €1,150)
• The cleanup function switched to the Europe/Amsterdam time zone, archiving only past pickups
• The archived reservations restored
• RLS rewritten: customers see only their own bookings, staff see all of them
• A staging project for testing prompts safely
• The Lovable frontend left untouched

CASE CLOSED
The Friday vanishings stopped that same week. Over the spring season, Fietsdeel handled about 900 reservations. Tim still builds in Lovable, testing in staging first.

"I spent three weeks asking Lovable to fix the dashboard. The bug wasn't in the dashboard at all." - Tim Verbeek

https://launchstudio.eu/en/blog/fix-my-lovable-app-the-problems-founders-bring-us-most

#Lovable #Supabase #NoCode #AIFounder #LaunchStudio #Manifera
