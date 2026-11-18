⏰ SUNDAY, 19:59
Next week's outdoor bootcamp classes are about to open. Popular morning classes: twenty spots each.

20:00
Booking opens. Within minutes, a class has more than twenty confirmed participants. Some customers pay without getting a spot. And the availability page, loading every booking ever made, slows down exactly now.

That was every Sunday for Fleur Jansen, who runs bootcamp classes in Haarlem and the towns around it and built Buitensport with Bolt and Supabase. And after the switch to winter time, reminders arrived an hour late, and two classes showed at the wrong time for some users.

WHAT WAS HAPPENING AT 20:00
• Availability was calculated in the browser, and bookings were inserted without a database check, so simultaneous requests all succeeded
• Spots were held forever when customers abandoned payment
• Bookings were confirmed by the redirect after paying through Mollie
• Times were stored without time zone information, with reminders scheduled in UTC

THE NEW SUNDAY (LaunchStudio, 7 business days, €2,600)
✓ A database function that checks and reserves capacity inside a transaction, so overbooking is impossible, with a friendly message and a waitlist when a class is full
✓ Holds that expire after ten minutes, released by a scheduled job
✓ Bookings confirmed only by verified, idempotent Mollie webhooks
✓ Automatic refunds for late payments on expired holds
✓ Times migrated to Europe/Amsterdam timestamps, reminders in local time, and the clock-change weeks tested
✓ Availability as an indexed query with a short cache
✓ A load test: 400 people booking at 20:00

20:10, THE NEXT SUNDAY
Around 350 bookings in the first ten minutes. Overbooked classes: zero. Lost payments: zero. Reminders stayed on time through the next clock change, and the waitlist refilled cancelled spots by itself.

"Sunday at eight used to be the most stressful moment of my week. Now it is the moment I watch the classes fill up and do nothing." - Fleur Jansen

https://launchstudio.eu/en/blog/production-launch-for-booking-platforms

#Booking #Bolt #Supabase #Mollie #AIFounder #LaunchStudio #Manifera
