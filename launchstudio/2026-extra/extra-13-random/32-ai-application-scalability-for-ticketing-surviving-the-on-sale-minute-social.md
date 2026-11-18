🎸 THE ON-SALE MINUTE (before)

10:00 · A well-known Dutch band's intimate show goes on sale. 450 seats. About 6,000 people try to buy.
10:00 + seconds · Every visitor's page load queries the database. The site crawls.
Moments later · Buyers who get through see seats as available that are already sold. 38 seats are sold twice.
Meanwhile · Buyers who pay in their banking app and never return to the site get no tickets at all.
Meanwhile · With no holds, seats in unfinished checkouts are sold to others while the first buyers are still paying.
Meanwhile · A handful of accounts buy 40 tickets each.

Kevin Oosterhuis, a sound engineer and promoter in Amsterdam Noord, built Zaalkaart on Replit: ticketing for small music venues and theatres, with seated and standing events, Mollie payments and QR-code tickets. Eighteen venues, typically 150 to 600 people per event. In ticketing, your worst day and your best day are the same minute.

What LaunchStudio rebuilt for that minute (Launch & Grow, 14 business days, €4,800, plus €49/month):
✓ Every seat a row, with a unique hold and order constraint
✓ 10-minute holds with automatic release, and a rule for late payments
✓ Mollie webhooks through a verified, idempotent queue
✓ Cached event pages, with a lightweight availability endpoint
✓ A waiting room for events flagged as high demand
✓ Per-account and per-card limits, plus rate limiting
✓ A load test of 10,000 buyers against staging before the venue's next big on-sale

🎸 THE ON-SALE MINUTE (after)
The venue's next sold-out show: 450 seats, around 7,500 buyers in the first minute. Sold out in four minutes. Oversold: zero. Unissued tickets: zero. Most tickets for one account: four.

Zaalkaart has since added nine venues, several of them citing that on-sale.

"Ticketing is the only business where your worst day and your best day are the same minute. The app has to be built for that minute." - Kevin Oosterhuis

https://launchstudio.eu/en/blog/ai-application-scalability-for-ticketing-surviving-the-on-sale-minute

#Ticketing #Scalability #Replit #LiveMusic #LaunchStudio #Manifera
