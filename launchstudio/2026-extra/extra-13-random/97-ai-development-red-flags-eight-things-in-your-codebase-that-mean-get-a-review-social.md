🚨 Noortje Vermeer runs a clothing alteration and repair studio in Naarden and built Naaiwerk in Bolt: customers book a fitting, describe repairs with photos, receive a price, pay a deposit and get notified when garments are ready. About 500 customers. After reading about AI app security, she went through the red flags herself - without reading a line of code. She counted five. 😳

Changing a number in the order address showed another customer's photos and home address. The page source held a key starting with sk_. The admin page opened in a private browser window. She had never restored a backup. And she'd once learned about an outage from a customer's Instagram comment. The review confirmed all five - and found a sixth: deposits confirmed by browser redirect. Here are the red flags in your codebase that mean: get a review: 🧠

❌ Another customer's data one number away
❌ A secret key visible in the page source
❌ An admin page that opens without logging in
❌ No tested backup and outages found by customers

✅ Customer-level access enforced in the database
✅ The Mollie secret key rotated and payment creation moved server-side, admin area protected with roles
✅ Deposit confirmation moved to webhooks
✅ Backups with a tested restore, a staging environment and uptime and error alerts on Noortje's phone

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we help non-technical founders count the flags - and clear them. ⚙️

Her result: €1,300, five business days. Noortje re-ran the checks herself and found none, Naaiwerk now handles about 120 bookings a month, and she repeats the checks after every major change. 🚀

👉 AI development red flags: eight things in your codebase that mean get a review: https://launchstudio.eu/en/blog/ai-development-red-flags-eight-things-in-your-codebase-that-mean-get-a-review

#RedFlags #CodeReview #Bolt #SmallBusiness #LaunchStudio #Manifera
