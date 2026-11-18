🧵 1/ Every Saturday, massage studios using Behandelagenda found two clients booked with the same therapist at overlapping times. Sometimes three or four times a weekend.

2/ Eva Hendriks built Behandelagenda with Lovable and Supabase: online booking for wellness studios and massage practices, with treatments of different lengths, therapists with their own schedules, and iDEAL payment at booking. Studios liked it. Until Saturdays.

3/ Bug one: availability was checked in the browser, then the booking inserted directly. And the check only compared start times. So a 60-minute booking at 10:00 and a 90-minute booking at 10:30 for the same therapist were both accepted.

4/ Bug two: iDEAL payment takes one to two minutes. During that time, the slot looked free to everyone else.

5/ Bug three: a double click on the pay button could create two bookings and two payments.

6/ Bug four: around the end of October, slots appeared twice. Daylight saving.

7/ The fix (LaunchStudio, 10 business days, €3,600): an exclusion constraint on therapist and time range, with a configurable buffer, so overlapping active bookings are impossible in the database itself.

8/ Booking creation moved into a database function, with direct inserts blocked by RLS. Bookings are "held" for ten minutes during payment, confirmed by the Mollie webhook, and released by a scheduled job. Rare late payments are refunded automatically.

9/ Client-generated IDs stop duplicate requests. Slots are generated in each studio's time zone, with daylight saving tests. Failed bookings show the next available times.

10/ Three months later: around 7,800 bookings, zero double bookings. Fifty simultaneous requests at one slot consistently produce exactly one booking.

11/ "My studios were apologising to clients every Saturday. Now the database simply refuses the second booking, and nobody has to apologise." - Eva Hendriks

https://launchstudio.eu/en/blog/preventing-double-bookings-in-a-booking-app

#BookingApp #Supabase #Postgres #Wellness #AIFounder #LaunchStudio #Manifera
