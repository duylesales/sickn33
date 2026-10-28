🚨 Tim de Graaf, a software tester in Breda, built Gereedschapdelen on Replit: neighbours rent each other hedge trimmers, tile cutters and carpet cleaners by the day, with a deposit. Three neighbourhoods, 600 users, about 150 rentals a month. And at any moment, Tim was holding around €2,000 of other people's money in his personal Stripe account. 😳

He paid lenders weekly from a spreadsheet. Deposits were charged in full and refunded by hand, sometimes days late. Two renters regularly booked the same tool for the same day. Anyone could leave reviews - one lender was flooded with fake ones by a disgruntled neighbour - and suspended users could still book. Here's what breaks when an AI marketplace meets real buyers and sellers: 🧠

❌ Marketplace money flowing through the founder's own account
❌ Full deposit charges with manual refunds
❌ Availability checked in code, not enforced in the database
❌ Open reviews and suspensions that only hid a profile

✅ Stripe Connect with lender onboarding and automatic payouts after the return date
✅ Card authorisations instead of deposit charges, released on return
✅ An exclusion constraint on tool and date range, with a 15-minute checkout hold
✅ Reviews only after completed rentals, suspension that blocks transactions, server-side PostGIS search, fee invoices and seller reporting data

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we turn a marketplace demo into a platform strangers can trust. ⚙️

His result: €5,200, sixteen business days. Gereedschapdelen went citywide and passed 400 rentals a month. Double bookings stopped, Tim no longer holds lender funds, and he saves about six hours a week on payouts and refunds. 🚀

👉 AI marketplace app to production: what breaks with real buyers and sellers: https://launchstudio.eu/en/blog/ai-marketplace-app-to-production-what-breaks-with-real-buyers-and-sellers

#Marketplace #StripeConnect #Replit #Breda #LaunchStudio #Manifera
