🚨 Nadia El Amrani runs a small accounting practice in Rotterdam and built Boekhoudportaal in Lovable: clients upload receipts and bank statements, see their quarterly VAT overview and message the practice. Forty clients were invited to a soft launch. A friend who works in IT ran a 30-minute security test with her first. 😳

Test one passed: two client accounts didn't see each other's data on screen. Test two failed - badly. Here's what the 30 minutes uncovered: 🧠

❌ Changing a document ID in the URL opened another client's bank statement
❌ A Supabase policy on documents letting any logged-in user read any row
❌ File links that never expired
❌ An email provider's secret key sitting in the JavaScript bundle

✅ RLS rewritten: clients see only their own documents, accountants only their assigned clients
✅ Files moved to a private bucket with short-lived signed URLs
✅ Email sending moved into an edge function, key rotated
✅ An audit log of document access for the practice's own records

At **LaunchStudio**, backed by Manifera and its founder's cybersecurity roots at CFLW, security is the first thing we check in any Lovable project. 🛠️

💡 Her result: €2,400, seven business days. She re-ran all six tests and passed, the full launch went ahead three weeks later, and the portal now serves around 120 clients. 🚀

👉 Is your Lovable app secure? Run the 30-minute self-test before your customers do: https://launchstudio.eu/en/blog/is-my-lovable-app-secure

#Lovable #AppSecurity #Supabase #FinTech #LaunchStudio #Manifera
