🔔 Friday 16:00: "Webhook verification failing since this afternoon."
🔔 Friday 17:00: "Paid deposits not turning into confirmed bookings."
🔔 Saturday: "11 bookings stuck in pending."

None of these alerts existed. Daphne Kok found out on Monday, from an anxious guest. (Alert times are illustrative.)

Daphne runs a small yoga retreat business near Bergen and built Retraitepas in v0 and Supabase: guests book retreats, pay a deposit and get packing lists. One Friday afternoon, a configuration change she made caused her payment provider to rotate a webhook signing secret. From that moment, every webhook failed verification. Payments went through. Bookings stayed "pending." Confirmations never went out.

The app never went down. It just stopped doing the one thing that mattered.

By Monday: eleven bookings stuck, one guest who'd paid €450 and heard nothing, and two guests who had booked elsewhere.

What LaunchStudio set up (3 business days, €980):
✓ Uptime checks and a health endpoint
✓ Error tracking, with alerts on new error types in edge functions
✓ A business check that alerts if paid deposits don't become confirmed bookings within an hour
✓ A subscription to the payment provider's status page
✓ The stuck bookings reconciled and confirmed

🔔 Two months later, for real: a similar webhook problem after an email provider change. The alert fired within 40 minutes, and Daphne fixed it before any guest noticed.

"The app never went down. It just stopped doing the one thing that mattered, and nothing told me." - Daphne Kok

https://launchstudio.eu/en/blog/how-do-i-know-when-my-ai-built-app-goes-down

#Monitoring #Supabase #v0 #SaaS #LaunchStudio #Manifera
