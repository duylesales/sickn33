✈️ Imagine an airport that builds a fast lane to cut the queues. It works. Passengers fly through. Then someone notices the fast lane skips the security checkpoint entirely.

Iris Molenaar's dashboard had a fast lane like that.

She built Vakantieverhuur in Lovable: booking and revenue administration for owners of holiday rentals on the Zeeland and Zuid-Holland coast, 210 owners with around 500 properties. The owner dashboard, with occupancy, revenue, average nightly rate and a year-on-year comparison, was slow. So an AI session created a view to aggregate it, and the page became instant.

The view was created without security invoker. Row Level Security on the bookings table was correct, and always had been. The view simply ran past it. Any logged-in owner who queried the view directly, instead of through the dashboard's filtered request, got the occupancy and revenue of all 500 properties. Including those of the competitors they were pricing against.

An owner found it while building a spreadsheet against the API, and reported it the same day.

Putting the checkpoint back in the fast lane (LaunchStudio, 2 business days, €2,200):
✓ The aggregation view redefined with security invoker, and verified by querying as three different owners
✓ All nine views audited: four were client-facing, and three of those had the same defect
✓ Client access revoked on six underlying tables, now reachable only through views
✓ The expensive year-comparison turned into a materialized view refreshed every fifteen minutes, with a unique index for concurrent refresh, and an "updated at" line on the dashboard
✓ Two tables from an abandoned pricing experiment removed from the API entirely
✓ A test that queries every client-facing view as a second-organisation user, and fails if any row comes back

The exposure closed within a day of the report. The dashboard still loads in under 200 milliseconds. And the cross-tenant test has since caught two more views, created in later AI sessions, before they reached production.

"The view was created to make a page fast, and it worked. Nobody mentioned that it also switched off the security on the table underneath it." - Iris Molenaar

https://launchstudio.eu/en/blog/lovable-supabase-views-and-what-to-expose-to-the-frontend

#Supabase #RowLevelSecurity #DataSecurity #Lovable #LaunchStudio #Manifera
