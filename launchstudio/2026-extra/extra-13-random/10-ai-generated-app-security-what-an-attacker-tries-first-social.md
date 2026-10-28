🚨 Ruben Dekker runs cheese-farm tours around Alkmaar and built Kaasroute in Bolt: tourists book, pay and get a QR ticket; partner farms see upcoming visitors. In its second summer, a guest who worked in IT emailed him politely. She'd changed the booking number in her ticket URL - and seen another family's names, phone number and hotel. 😳

She'd also noticed that /admin loaded every booking of the season. The admin link wasn't shown anywhere in the app, so Ruben assumed nobody would find it. Here's what an attacker tries in the first ten minutes against an AI-built app: 🧠

❌ Minute 1: keys in the page source (a payment API key was there)
❌ Minute 3: predictable addresses like /admin with no server-side role check
❌ Minute 5: change a number in the URL and read someone else's record
❌ Minute 7: login forms with no rate limit and revealing error messages

✅ Admin area and its API locked behind server-side role checks on day one
✅ Ownership checks on tickets, with unguessable codes instead of sequential numbers
✅ The payment key rotated and moved server-side; login rate-limited with uniform errors
✅ Partner portal restricted per farm, logs reviewed, and breach-notification assessment done

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering - and a founder with a cybersecurity background - we close the doors in the same order attackers try them. ⚙️

His result: €1,100, four business days. No evidence of wider access, the season finished safely, the guest got a free tour for two - and the site now has a "report a security issue" address. 🚀

👉 AI-generated app security: what an attacker tries first: https://launchstudio.eu/en/blog/ai-generated-app-security-what-an-attacker-tries-first

#AppSecurity #Bolt #OWASP #Startups #LaunchStudio #Manifera
