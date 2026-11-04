🚨 Sevda Arslan built Buurtruil in Lovable: a free swap marketplace for her neighbourhood in Arnhem. A local newspaper wrote about it on a Thursday. By Monday, Buurtruil had 4,300 new accounts - about 3,900 of them fake - and hundreds of listings advertising dubious crypto schemes. 😳

The newspaper article brought her neighbours and bots. The bots were much faster. Here's why: 🧠

❌ No CAPTCHA on the sign-up form
❌ Email confirmation switched off
❌ Listings that could contain any link
❌ The built-in email sender exhausted by fake sign-ups, so real neighbours never got their confirmation emails

✅ Cloudflare Turnstile enabled on Supabase Auth
✅ Email confirmation turned on, with custom SMTP
✅ Rate limits on sign-ups and listings per IP and per account, and links blocked in listings from new accounts
✅ Fake accounts and listings removed with a server-side script, plus a daily sign-up chart with alerts

At **LaunchStudio**, backed by Manifera and its founder's cybersecurity background at CFLW, bot protection is layered and monitored - not just a CAPTCHA added once. 🛠️

💡 Her result: €1,050, three business days. Fake sign-ups dropped to a handful per week, real membership grew to about 900 households, and the marketplace was usable again within two days. 🚀

👉 Protecting your Lovable app from spam sign-ups and bots? Here's the layered defence: https://launchstudio.eu/en/blog/how-do-i-protect-my-lovable-app-from-spam-and-bots

#Lovable #Supabase #BotProtection #AppSecurity #LaunchStudio #Manifera
