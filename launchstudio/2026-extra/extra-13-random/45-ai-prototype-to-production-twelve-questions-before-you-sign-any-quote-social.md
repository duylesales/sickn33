🧘 QUOTE #1: €2,400, already paid
"Making it production ready."
After: bookings still vanished sometimes, and passes were sometimes not deducted.

QUOTE #2: €4,000
"To finish the backend."
Asked how payments would be confirmed: couldn't say.
Hosting: on the provider's own servers.

QUOTE #3: a fixed price, with a written scope
The code reviewed during the intro call.

Esther van Leeuwen runs a yoga studio in Zeist and built Yogarooster in Lovable: students buy class passes, book classes, join waiting lists and get reminders, and teachers see attendance. Two other studios wanted to use it. The first time, she'd signed a quote she couldn't evaluate. This time, she asked twelve questions she could evaluate the answers to.

What the review behind quote #3 found, and why quote #1 hadn't worked:
• The freelancer had added a login, but pass balances were updated by the browser, so closing the tab after booking left a class booked without a deduction
• Mollie payments for passes were confirmed by redirect
• Students could see other students' booking histories through the API
• The "production" hosting was on the freelancer's personal Vercel account

What quote #3 delivered (LaunchStudio, 8 business days, €2,100):
✓ Pass deduction inside a database transaction, tied to the booking
✓ Payments confirmed by verified webhooks
✓ Student-level access enforced
✓ Hosting and every account transferred to Esther
✓ Staging and monitoring
✓ The changes documented

Yogarooster onboarded both new studios. Missing deductions and vanished bookings stopped entirely. And Esther now uses the twelve questions whenever she hires any supplier.

"The first time, I signed a quote I couldn't evaluate. The second time, I asked questions I could evaluate the answers to. That made all the difference." - Esther van Leeuwen

https://launchstudio.eu/en/blog/ai-prototype-to-production-twelve-questions-before-you-sign-any-quote

#Outsourcing #FixedPrice #Lovable #Founders #LaunchStudio #Manifera
