👀 What Lotte's screen said vs. what her server did

THE SCREEN SAID
"Your trial has ended. Upgrade to continue." Navigation disabled.

THE SERVER DID
Answer every authenticated request anyway, as if nothing had changed.

Lotte van Bemmel built Wachtkamer in Lovable: patient check-in and waiting-room display software for general practices, €59 a month after a 21-day trial with no card. The trial logic lived entirely in the frontend.

She found out from her own hosting bill. Usage was growing faster than revenue. When she counted active accounts against paying ones, the gap was 40 practices. Some had been running daily check-ins for five months on an expired trial. Several thought the product was free. Two had told colleagues so. 🏥

The interface was lying to her as much as to them.

Making the screen and the server agree (LaunchStudio, 3 business days, €2,400):
✓ One server-side entitlement function reading plan and trial state from the database, called by every endpoint, including the display-screen API that had never checked anything
✓ The frontend rewired to ask the same function what to show
✓ All 34 endpoints audited: 19 had no authorisation check at all
✓ Email normalisation, collapsing plus-addressed duplicate trials
✓ Reminders at day 14, day 20 and expiry
✓ Read-only access, with data export kept for 60 days after expiry
✓ An admin action to extend a trial by a set number of days

What happened once access really stopped:
• 12 of the 40 practices converted to paid plans within a month
• 6 asked for a short extension, and half of those converted too
• Infrastructure costs fell by a third
• Trial-to-paid conversion on new sign-ups rose from 18% to 29%, which Lotte credits mostly to the day-14 reminder

"Forty practices were using it daily and I had no idea, because on my screen the trial had ended. The interface was lying to me as much as it was to them." - Lotte van Bemmel

https://launchstudio.eu/en/blog/lovable-payments-free-trials-that-do-not-leak-access

#SaaS #FreeTrial #AccessControl #Lovable #LaunchStudio #Manifera
