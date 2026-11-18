🚩 RED FLAG COUNT: a clothing repair studio's app

🚩 1. Changing a number in the order address showed another customer's photos and address
🚩 2. The page source contained a key beginning with sk_
🚩 3. The admin page opened in a private browser window, without logging in
🚩 4. A backup had never been restored
🚩 5. She once learned about an outage from a customer's Instagram comment

Five out of eight. Noortje couldn't read the code, but she could count the flags. And five was enough. 🧵

Noortje Vermeer runs a clothing alteration and repair studio in Naarden and built Naaiwerk in Bolt: customers book a fitting, describe repairs with photos, get a price and pay a deposit, and are notified when garments are ready. About 500 customers had used it. After reading about AI app security, she went through the red flags herself, and booked a review.

LaunchStudio confirmed all five, and found a sixth:
🚩 6. Deposits confirmed by the browser redirect

Taking the flags down (5 business days, €1,300):
✓ Customer-level access enforced in the database
✓ The Mollie secret key rotated, with payment creation moved server-side
✓ The admin area protected with roles
✓ Deposit confirmation moved to webhooks
✓ Backups enabled, with a tested restore
✓ A staging environment
✓ Uptime and error alerts on Noortje's phone

RED FLAG COUNT, after Noortje re-ran the checks herself: 0

Naaiwerk now handles around 120 bookings a month, and Noortje repeats the checks after every major change.

"I couldn't read the code, but I could count the flags. Five was enough to know I needed help." - Noortje Vermeer

https://launchstudio.eu/en/blog/ai-development-red-flags-eight-things-in-your-codebase-that-mean-get-a-review

#RedFlags #CodeReview #Bolt #SmallBusiness #LaunchStudio #Manifera
