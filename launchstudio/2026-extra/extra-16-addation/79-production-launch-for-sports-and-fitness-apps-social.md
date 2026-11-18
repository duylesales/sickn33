Imagine it's January, and you've just joined a boutique gym in Breda. 🏋️

Your direct debit went through. You walk up to the entrance, scan the QR code in your app, and the door says no.

The member behind you, whose payment failed, keeps booking classes without a problem. Your favourite spinning class is overbooked. Every evening at 21:00, when tomorrow's classes open, the app slows to a crawl. And your heart rate data, from the watch you connected, is visible to every personal trainer in the building.

That was January at Bas Timmermans's gyms.

Bas runs two boutique gyms in Breda and built Sportpas with Cursor and Supabase for memberships, class bookings and QR check-in at the entrance. With lots of new members, everything that could lag, did.

Why:
• Membership status was updated by a nightly job, not by payment webhooks, so it was always a day behind
• QR codes were static member IDs, easy to share
• Class capacity was checked in the browser
• The schedule query loaded every booking ever made
• Wearable data was imported at full resolution and shown to every trainer

What LaunchStudio changed (8 business days, €3,200):
✓ Membership status driven by verified, idempotent Mollie webhooks, with a grace period and payment reminders for failed debits
✓ Short-lived QR codes generated in the app and validated against live status, with a cached list of valid members at each entrance for brief connection losses
✓ Class capacity enforced in a database transaction, with a waitlist
✓ The schedule query indexed and cached, and the 21:00 release load-tested
✓ Wearable imports limited to the workout summaries members choose, with explicit consent, and trainers seeing data only for clients connected to them

Within a week, check-in problems disappeared. Overbooking stopped, and the 21:00 release ran smoothly. Several members told Bas they appreciated choosing which trainer sees their workout data.

"In January, every new member's first experience is the door. Now the door knows who has paid, and the trainers only see what members choose to share." - Bas Timmermans

https://launchstudio.eu/en/blog/production-launch-for-sports-and-fitness-apps

#Fitness #GymSoftware #Wearables #Cursor #AIFounder #LaunchStudio #Manifera
