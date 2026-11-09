🏋️ Bas Timmermans runs two boutique gyms in Breda and built Sportpas with Cursor and Supabase: memberships, class bookings and QR check-in at the entrance. Then January arrived with a wave of new members. People whose direct debit had succeeded were refused at the door, others with failed payments kept booking, spinning classes were overbooked and the app slowed down every evening at 21:00 when the next day's classes opened. 🚪

The assessment found: 🧠

❌ Membership status updated by a nightly job, so it lagged a full day behind
❌ Static QR codes based on member IDs, easy to share
❌ Class capacity checked in the browser and a schedule query loading every booking ever made
❌ Full-resolution heart rate data from watches visible to every trainer

✅ Membership status driven by verified, idempotent Mollie webhooks, with a grace period and reminders
✅ Short-lived QR codes validated against live status, with a cached member list at each entrance
✅ Capacity enforced in a database transaction with a waitlist, plus an indexed, cached schedule and a load test of the 21:00 release
✅ Wearable imports limited to workout summaries members choose, with explicit consent and trainers seeing only their own clients

At **LaunchStudio**, backed by Manifera's 11+ years of building mobile, payment and data systems, we make memberships drive access and treat health data with care. 🛠️

His result: €3,200, eight business days. Check-in problems gone within a week, no more overbooking and a smooth 21:00 release. 🚀

👉 Production launch for sports and fitness apps: https://launchstudio.eu/en/blog/production-launch-for-sports-and-fitness-apps

#Fitness #GymSoftware #Wearables #Cursor #AIFounder #LaunchStudio #Manifera
