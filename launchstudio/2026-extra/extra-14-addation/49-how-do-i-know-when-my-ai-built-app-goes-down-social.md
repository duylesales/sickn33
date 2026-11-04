🚨 Daphne Kok runs a small yoga retreat business near Bergen and built Retraitepas in v0 and Supabase. One Friday afternoon, a configuration change rotated her payment provider's webhook signing secret. Payments kept succeeding - but every booking stayed "pending" and no confirmation went out. She found out on Monday, from an anxious guest who had paid €450 and heard nothing. 😳

Eleven bookings were stuck and two guests had booked elsewhere. The app never went down. It just stopped doing the one thing that mattered. Here's why nothing told her: 🧠

❌ No uptime check or health endpoint
❌ No error tracking on the edge functions where the webhook failed
❌ No check that paid deposits actually became confirmed bookings
❌ No alerts reaching her phone - her customers were her monitoring system

✅ Uptime checks plus a real health endpoint
✅ Error tracking with alerts on new error types in edge functions
✅ A business check that alerts if a paid deposit isn't a confirmed booking within an hour
✅ A payment provider status page subscription, and all stuck bookings reconciled

At **LaunchStudio**, backed by Manifera's teams in Ho Chi Minh City working ahead of European time, monitoring and alerting are part of every launch. 🛠️

💡 Her result: €980, three business days. Two months later, a similar webhook problem triggered an alert within 40 minutes, and Daphne fixed it before any guest noticed. 🚀

👉 Would you know if your AI-built app silently stopped working? Here's the minimal monitoring stack: https://launchstudio.eu/en/blog/how-do-i-know-when-my-ai-built-app-goes-down

#Monitoring #Supabase #v0 #SaaS #LaunchStudio #Manifera
