🚨 Sjoerd Wiersma, treasurer of a korfball club in Leeuwarden, built Contributieman with Bolt so members could pay their annual fees online through Mollie. After the first month, the app said 212 members had paid. Mollie said 174. 😳

The gap had one cause: the app trusted the return page. Anyone who landed on it was marked as paid - including members who cancelled in their banking app. Here's what was missing: 🧠

❌ No Mollie webhook at all
❌ Members marked paid on the redirect, even after cancelled or expired payments
❌ The Mollie live key in a frontend environment file
❌ Amounts sent from the browser

✅ Payment creation moved into a Supabase edge function, with amounts from the database
✅ A Mollie webhook that fetches the real status from Mollie's API and updates memberships idempotently
✅ Every status mapped to a clear message for members
✅ The exposed key rotated, plus a monthly reconciliation report

At **LaunchStudio**, backed by Manifera's 11+ years of payment integrations from Amsterdam, we build the parts of a Mollie integration that AI tools skip. 🛠️

💡 His result: €1,700, seven business days. The next reconciliation matched to the cent, the club collected 96% of annual fees online, and the 38 members wrongly marked as paid settled within two weeks. 🚀

👉 Using Mollie in a Lovable, Bolt or Cursor app? Here's the full integration step by step: https://launchstudio.eu/en/blog/mollie-integration-for-ai-built-apps-step-by-step

#Mollie #iDEAL #Supabase #Bolt #LaunchStudio #Manifera
