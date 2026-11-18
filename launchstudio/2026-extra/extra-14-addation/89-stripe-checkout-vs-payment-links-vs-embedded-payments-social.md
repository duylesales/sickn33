🧩 TONIGHT'S PUZZLE: match the payments to the bookings

Stripe: €45 · €45 · €45 · €60 · €45
Bookings: Anna · Bram · Chris · Dewi · Eva · Femke · Gijs

Which five paid? And which two are holding places they never paid for? (Illustrative, but the puzzle was real.)

Sophie Mertens solved a puzzle like this every evening. She runs pottery workshops in Mechelen and built Kleiatelier in Lovable: people book a workshop, pay and get preparation emails. Lovable connected one Stripe Payment Link per workshop. Payments came in. The app just had no idea who had paid. And twice, a workshop got overbooked, because unpaid reservations kept holding places.

How LaunchStudio retired the puzzle (5 business days, €1,450):
✓ Payment Links replaced with Stripe Checkout sessions created server-side for each booking
✓ The booking ID stored in the session metadata
✓ Bancontact and iDEAL enabled
✓ A webhook that confirms a booking only after payment
✓ Unpaid reservations released automatically after 30 minutes
✓ Preparation emails sent on confirmation

No more evening matching. No more overbooking. And with places now released reliably, Sophie added a waiting list that offers each freed place to the next person automatically.

"Payment Links got me paid. They just didn't tell my app who had paid for what." - Sophie Mertens

https://launchstudio.eu/en/blog/stripe-checkout-vs-payment-links-vs-embedded-payments

#Stripe #Payments #Bancontact #iDEAL #LaunchStudio #Manifera
