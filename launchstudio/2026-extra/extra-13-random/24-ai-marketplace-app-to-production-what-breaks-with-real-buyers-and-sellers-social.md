In Tim's tests, he was the renter and the lender. In real life, they were two neighbours in Breda who'd never met. 🔨

Tim de Graaf, a software tester, built Gereedschapdelen on Replit: neighbours list tools they rarely use, like hedge trimmers, tile cutters and carpet cleaners, and rent them to each other by the day, with a deposit. It launched in three Breda neighbourhoods and reached 600 users and about 150 rentals a month.

And then the two neighbours who'd never met started to need something the demo never had: an app that acted like the adult in the room.

All the money went into Tim's personal Stripe account. Every week, he paid lenders by bank transfer, from a spreadsheet. At any moment, he was holding around €2,000 of other people's money.

Deposits were charged in full and refunded by hand, sometimes days late. Two renters regularly booked the same tool for the same day. Anyone could leave a review, and one lender was flooded with fake negative reviews by a disgruntled neighbour. And suspending a user only hid their profile. They could still book.

So LaunchStudio's engineers made the app grow up (Launch & Grow, 16 business days, €5,200, plus €49/month):
✓ Payments on Stripe Connect, with lender onboarding and automatic payouts after the return date
✓ Deposits as card authorisations, released on return, instead of full charges
✓ An exclusion constraint on tool and date range, with a 15-minute hold during checkout
✓ Reviews only after a completed rental
✓ Suspension that blocks every transaction
✓ Search on the server, with PostGIS for distance filtering
✓ Fee invoices and seller reporting data in the data model

Gereedschapdelen expanded citywide and passed 400 rentals a month. Double bookings stopped. Tim no longer holds anyone's money, and he spends about six fewer hours a week on payouts and refunds.

"In my tests I was the renter and the lender. In reality they were two neighbours who'd never met, and the app had to be the adult in the room." - Tim de Graaf

https://launchstudio.eu/en/blog/ai-marketplace-app-to-production-what-breaks-with-real-buyers-and-sellers

#Marketplace #StripeConnect #Replit #Breda #LaunchStudio #Manifera
