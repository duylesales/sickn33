🏃‍♀️ Fleur Jansen runs outdoor bootcamp classes in Haarlem and nearby towns, and built Buitensport with Bolt and Supabase. Every Sunday at 20:00, next week's classes opened, and twenty-spot morning classes filled within minutes. Within a month: classes with more than twenty participants, customers who paid but got no spot and, after the switch to winter time, reminders an hour late. ⏰

The assessment explained every one of them: 🧠

❌ Availability calculated in the browser, bookings inserted without any database check
❌ Spots held forever when customers abandoned payment, and confirmations relying on the Mollie redirect
❌ Times stored without time zone information and reminders scheduled in UTC
❌ An availability query loading every booking ever made, slowing down exactly at 20:00 on Sundays

✅ Capacity checked and reserved inside a database transaction, with a waitlist when full
✅ Holds expiring after ten minutes, bookings confirmed by idempotent webhooks and late payments refunded automatically
✅ Times migrated to Europe/Amsterdam timestamps, reminders in local time and clock-change weeks tested
✅ An indexed availability query with a short cache, plus a load test of 400 people booking at once

At **LaunchStudio**, backed by Manifera's 11+ years of building scheduling and payment systems for clients such as Vodafone and TNO, we make double bookings impossible and keep times right through every clock change. 🛠️

Her result: €2,600, seven business days. About 350 bookings in ten minutes the next Sunday, without one overbooked class. 🚀

👉 Production launch for booking platforms: https://launchstudio.eu/en/blog/production-launch-for-booking-platforms

#Booking #Bolt #Supabase #Mollie #AIFounder #LaunchStudio #Manifera
