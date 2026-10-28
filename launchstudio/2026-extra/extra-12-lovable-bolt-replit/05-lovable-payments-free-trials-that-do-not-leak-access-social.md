🚨 Lotte van Bemmel's Wachtkamer runs patient check-in for GP practices at €59/month after a 21-day trial. Usage was growing faster than revenue. When she compared active accounts against paying ones, the gap was 40 practices - some running daily check-ins for five months on an expired trial. 😳

On her screen the trial had ended. On the server, nothing had changed. Here's how trials leak access: 🧠

❌ Trial expiry handled only in the frontend - an upgrade screen, but every request still worked
❌ 19 of 34 endpoints with no authorisation check at all
❌ Duplicate trials via plus-addressed emails
❌ No reminders before expiry

✅ One server-side entitlement function, called by every endpoint
✅ The interface driven by the same function, so display and permission can't drift apart
✅ Email normalisation, plus reminders at day 14, day 20 and expiry
✅ Read-only access and data export kept for 60 days, plus an admin action to extend a trial

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we test your expired trial the way your users will - with the developer tools open. 🔍

Her result: three business days and €2,400 later, 12 of the 40 practices converted within a month, infrastructure costs fell by a third, and trial-to-paid conversion on new signups rose from 18% to 29%. 🚀

👉 Free trials that don't leak access: https://launchstudio.eu/en/blog/lovable-payments-free-trials-that-do-not-leak-access

#SaaS #FreeTrial #AccessControl #Lovable #LaunchStudio #Manifera
