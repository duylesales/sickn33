🚨 Iris Molenaar's Vakantieverhuur handles bookings and revenue for 210 holiday-rental owners on the Zeeland and South Holland coast. The owner dashboard was slow, so an AI session created a view to aggregate it. The page became instant. 😳

It also switched off the security on the table underneath. Any owner querying the view directly got occupancy and revenue for all 500 properties - including the competitors they priced against. Here's what to expose to the frontend in Supabase: 🧠

❌ A view created without security invoker - running past row-level security entirely
❌ Three of four client-facing views with the same defect
❌ Underlying tables still directly reachable from the API
❌ Tables from an abandoned experiment left exposed

✅ Every client-facing view redefined with security invoker and tested as three different owners
✅ Client access revoked on six tables now reachable only through views
✅ The expensive year comparison moved to a materialized view, refreshed every 15 minutes with an "updated at" line
✅ An automated test that queries every view as a second organisation and fails if any row comes back

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we query your API as another customer - a ten-minute test with an occasionally uncomfortable result. 🔍

Her result: two business days and €2,200 later, the exposure was closed within a day of being reported. The cross-tenant test has since caught two more faulty views from later AI sessions before production - and the dashboard still loads in under 200 ms. 🚀

👉 Views and what to expose to the frontend: https://launchstudio.eu/en/blog/lovable-supabase-views-and-what-to-expose-to-the-frontend

#Supabase #RowLevelSecurity #DataSecurity #Lovable #LaunchStudio #Manifera
