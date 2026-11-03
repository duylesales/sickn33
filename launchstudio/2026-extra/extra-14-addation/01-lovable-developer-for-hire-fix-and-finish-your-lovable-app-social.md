🚨 Lotte van Rijn, a former teacher in Groningen, built Bijlespunt in Lovable: parents book maths and language tutors, chat with them and pay per lesson. Twelve tutors, forty trial lessons booked. Then a parent emailed: she could read another family's messages with their tutor. 😳

Lotte asked Lovable to fix it three times. Each fix changed what appeared on screen, but the query underneath still returned every conversation. Here's what a Lovable developer actually fixes: 🧠

❌ Row Level Security that let every user read every chat
❌ A Stripe secret key sitting in a frontend file
❌ Double clicks that charged parents twice
❌ No staging, so every prompt went straight to live

✅ RLS policies so users only read their own conversations
✅ The Stripe key moved into a Supabase edge function
✅ An idempotency key on bookings: one click, one charge
✅ A staging project plus uptime and error alerts to Lotte's phone

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we keep your Lovable frontend and fix only what's underneath. 🛠️

Her result: €2,600, eleven business days. Bijlespunt handled ~1,400 lessons the next term with zero data exposure reports - and Lotte kept building in Lovable. 🚀

👉 Need a Lovable developer who won't rebuild your app? Here's what to expect: https://launchstudio.eu/en/blog/lovable-developer-for-hire-fix-and-finish-your-lovable-app

#Lovable #Supabase #EdTech #AIFounder #LaunchStudio #Manifera
