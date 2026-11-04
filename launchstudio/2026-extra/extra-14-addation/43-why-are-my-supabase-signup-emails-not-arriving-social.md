🚨 Mirjam Dekkers coordinates a food bank in Helmond and built Voedselhulp in Lovable: volunteers sign up for distribution shifts and get reminders. On launch evening, the first 30 or so volunteers received their confirmation emails. After that - nothing. Volunteers tried again, created duplicate accounts and gave up. 😳

Thirty people got in and then the door quietly closed. Nobody saw an error, including her. Here's what happened: 🧠

❌ Supabase's built-in email service hit its sending limit
❌ The emails that did go out came from a generic address, several straight into spam
❌ Password reset links pointing to the Lovable preview domain
❌ Duplicate accounts piling up from repeated sign-up attempts

✅ Custom SMTP through an EU-region transactional email provider
✅ SPF, DKIM and DMARC records added to the food bank's own domain
✅ Production redirect URLs and Dutch templates with the food bank's name
✅ One-time codes instead of magic links for volunteers on work email, and duplicate accounts merged

At **LaunchStudio**, backed by Manifera's 11+ years of transactional email at scale, we treat email as infrastructure - not an afterthought. 🛠️

💡 Her result: €850, three business days. Every waiting volunteer was confirmed the next morning, 210 volunteers registered within a month, and reminders now land in inboxes instead of spam. 🚀

👉 Supabase sign-up emails not arriving? Here are the four usual causes and the fix: https://launchstudio.eu/en/blog/why-are-my-supabase-signup-emails-not-arriving

#Supabase #Lovable #EmailDeliverability #NonProfit #LaunchStudio #Manifera
