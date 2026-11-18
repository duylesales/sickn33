Attempt #1: "Lovable, fix it." ➜ Different messages on screen. Same leak underneath.
Attempt #2: "Lovable, fix it." ➜ Different messages on screen. Same leak underneath.
Attempt #3: "Lovable, fix it." ➜ You can guess. 🔁

Lotte van Rijn, a former secondary school teacher in Groningen, built Bijlespunt in Lovable over five weeks of evenings: parents book maths and language tutors, chat with them and pay per lesson. Twelve tutors signed up, and about forty parents booked trial lessons.

Then a parent emailed. She could see messages between another family and their tutor.

Each prompt changed which messages appeared on screen. None changed the query underneath, which still returned every conversation in the database. And along the way Lotte found two more surprises:
• Her Stripe secret key in a frontend file
• Double clicks on "book" charging parents twice

Attempt #4, by LaunchStudio's engineers (11 business days, €2,600), with the Lovable frontend left untouched:
✓ Row Level Security, so users only read conversations they belong to
✓ The Stripe key moved into a Supabase edge function, and rotated
✓ An idempotency key on bookings: one click, one charge
✓ A staging project for testing Lovable changes before parents see them
✓ Uptime and error alerts to Lotte's phone, and the incident documented for her records

Bijlespunt reopened bookings eleven days after Lotte's first message. The following term: around 1,400 lessons, no data exposure reports. And Lotte is still building new features in Lovable, on top of a backend that now holds.

"I didn't need someone to rebuild my app. I needed someone who could look at what Lovable made and tell me exactly what was wrong underneath." - Lotte van Rijn

https://launchstudio.eu/en/blog/lovable-developer-for-hire-fix-and-finish-your-lovable-app

#Lovable #Supabase #EdTech #AIFounder #LaunchStudio #Manifera
