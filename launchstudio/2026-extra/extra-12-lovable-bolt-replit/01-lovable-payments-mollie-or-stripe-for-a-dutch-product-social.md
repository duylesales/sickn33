📊 ONE QUESTION IN AN ABANDONMENT EMAIL
"Was there anything missing at checkout?"

Replies: 46
"I don't use a credit card" (or similar): 38

Wouter Nagelkerke built Vaarschool Online with Lovable: €79 theory courses for consumers preparing for the Dutch boating licence exam. He integrated Stripe because that's what the tutorials used, and launched with card payments only. A Facebook group of sailing enthusiasts sent steady traffic. Checkout conversion sat at 31%, and he assumed that was normal. ⛵

It wasn't. He'd spent four months optimising a landing page for people who were never going to be able to pay him.

And while LaunchStudio was in the checkout, more turned up:
• The Stripe secret key, in the frontend bundle since launch
• Prices posted from the browser, and trusted by the server
• Unverified webhooks, so a retried event granted a second course enrolment
• Course access depending on a live API call, with no payment records of his own

What changed (4 business days, €2,150):
✓ iDEAL enabled, and placed as the default payment method instead of an option below the card fields
✓ Checkout sessions created server-side, with the price looked up from the database
✓ The secret key removed from the frontend
✓ Webhook signature verification, plus an idempotency key
✓ A payments table in his own database, recording every transaction with its provider reference
✓ Abandoned iDEAL payments leaving a pending record that expires cleanly, instead of a half-created enrolment

📊 THE NEXT MONTH, same traffic
Checkout conversion: from 31% to 68%
Duplicate-enrolment support emails (three or four a week, fixed by hand): zero

"I spent four months optimising a landing page for people who were never going to be able to pay me. The fix took less time than the landing page copy did." - Wouter Nagelkerke

👉 Mollie or Stripe for a Dutch product: https://launchstudio.eu/en/blog/lovable-payments-mollie-or-stripe-for-a-dutch-product

#iDEAL #Mollie #Stripe #Lovable #LaunchStudio #Manifera
